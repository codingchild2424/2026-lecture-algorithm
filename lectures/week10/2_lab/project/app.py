"""
Week 10 Project -- Hash Table Explorer
FastAPI backend with custom hash table implementations and API endpoints.
"""

import time
import random
from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI(title="Hash Table Explorer")


# ---------------------------------------------------------------------------
# Custom Hash Table Implementations
# ---------------------------------------------------------------------------

class ChainingHashTable:
    """Hash table using separate chaining for collision resolution."""

    def __init__(self, size: int = 11):
        self.size = size
        self.buckets: list[list[tuple]] = [[] for _ in range(size)]
        self.count = 0
        self.collisions = 0
        self.log: list[dict] = []

    def _hash(self, key) -> int:
        """Simple hash function: sum of character codes mod table size."""
        if isinstance(key, int):
            h = key % self.size
        else:
            h = sum(ord(c) for c in str(key)) % self.size
        return h

    def insert(self, key, value=None) -> dict:
        idx = self._hash(key)
        step = {
            "operation": "insert",
            "key": key,
            "hash_value": idx,
            "hash_computation": self._hash_detail(key),
            "collision": len(self.buckets[idx]) > 0,
            "chain_length_before": len(self.buckets[idx]),
        }
        # Update existing key if present
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx][i] = (key, value)
                step["action"] = "updated_existing"
                self.log.append(step)
                return step
        if len(self.buckets[idx]) > 0:
            self.collisions += 1
        self.buckets[idx].append((key, value))
        self.count += 1
        step["action"] = "inserted"
        step["chain_length_after"] = len(self.buckets[idx])
        self.log.append(step)
        return step

    def search(self, key) -> dict:
        idx = self._hash(key)
        probes = 0
        for k, v in self.buckets[idx]:
            probes += 1
            if k == key:
                return {
                    "operation": "search",
                    "key": key,
                    "hash_value": idx,
                    "hash_computation": self._hash_detail(key),
                    "found": True,
                    "value": v,
                    "probes": probes,
                }
        return {
            "operation": "search",
            "key": key,
            "hash_value": idx,
            "hash_computation": self._hash_detail(key),
            "found": False,
            "value": None,
            "probes": probes,
        }

    def delete(self, key) -> dict:
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.buckets[idx]):
            if k == key:
                self.buckets[idx].pop(i)
                self.count -= 1
                return {
                    "operation": "delete",
                    "key": key,
                    "hash_value": idx,
                    "found": True,
                    "chain_length_after": len(self.buckets[idx]),
                }
        return {
            "operation": "delete",
            "key": key,
            "hash_value": idx,
            "found": False,
        }

    def _hash_detail(self, key) -> str:
        if isinstance(key, int):
            return f"{key} mod {self.size} = {key % self.size}"
        codes = [ord(c) for c in str(key)]
        total = sum(codes)
        return f"sum(ord) of '{key}' = {total}, {total} mod {self.size} = {total % self.size}"

    def load_factor(self) -> float:
        return round(self.count / self.size, 4) if self.size > 0 else 0

    def avg_chain_length(self) -> float:
        non_empty = [len(b) for b in self.buckets if len(b) > 0]
        return round(sum(non_empty) / len(non_empty), 4) if non_empty else 0

    def snapshot(self) -> dict:
        return {
            "type": "chaining",
            "size": self.size,
            "count": self.count,
            "collisions": self.collisions,
            "load_factor": self.load_factor(),
            "avg_chain_length": self.avg_chain_length(),
            "buckets": [
                {
                    "index": i,
                    "entries": [{"key": k, "value": v} for k, v in bucket],
                }
                for i, bucket in enumerate(self.buckets)
            ],
            "log": self.log,
        }


class LinearProbingHashTable:
    """Hash table using open addressing with linear probing."""

    EMPTY = "__EMPTY__"
    DELETED = "__DELETED__"

    def __init__(self, size: int = 11):
        self.size = size
        self.keys = [self.EMPTY] * size
        self.values = [None] * size
        self.count = 0
        self.collisions = 0
        self.total_probes = 0
        self.log: list[dict] = []

    def _hash(self, key) -> int:
        if isinstance(key, int):
            return key % self.size
        return sum(ord(c) for c in str(key)) % self.size

    def insert(self, key, value=None) -> dict:
        if self.count >= self.size:
            step = {
                "operation": "insert",
                "key": key,
                "action": "table_full",
                "error": "Hash table is full",
            }
            self.log.append(step)
            return step

        idx = self._hash(key)
        original_idx = idx
        probes = 0
        probe_sequence = []

        while True:
            probe_sequence.append(idx)
            probes += 1
            if self.keys[idx] == self.EMPTY or self.keys[idx] == self.DELETED:
                # Empty slot found
                self.keys[idx] = key
                self.values[idx] = value
                self.count += 1
                if probes > 1:
                    self.collisions += 1
                self.total_probes += probes
                step = {
                    "operation": "insert",
                    "key": key,
                    "hash_value": original_idx,
                    "hash_computation": self._hash_detail(key),
                    "final_index": idx,
                    "probes": probes,
                    "probe_sequence": probe_sequence,
                    "collision": probes > 1,
                    "action": "inserted",
                }
                self.log.append(step)
                return step
            elif self.keys[idx] == key:
                # Update existing
                self.values[idx] = value
                self.total_probes += probes
                step = {
                    "operation": "insert",
                    "key": key,
                    "hash_value": original_idx,
                    "hash_computation": self._hash_detail(key),
                    "final_index": idx,
                    "probes": probes,
                    "probe_sequence": probe_sequence,
                    "collision": probes > 1,
                    "action": "updated_existing",
                }
                self.log.append(step)
                return step
            idx = (idx + 1) % self.size

    def search(self, key) -> dict:
        idx = self._hash(key)
        original_idx = idx
        probes = 0
        probe_sequence = []

        while True:
            probe_sequence.append(idx)
            probes += 1
            if self.keys[idx] == self.EMPTY:
                return {
                    "operation": "search",
                    "key": key,
                    "hash_value": original_idx,
                    "hash_computation": self._hash_detail(key),
                    "found": False,
                    "value": None,
                    "probes": probes,
                    "probe_sequence": probe_sequence,
                }
            if self.keys[idx] == key:
                return {
                    "operation": "search",
                    "key": key,
                    "hash_value": original_idx,
                    "hash_computation": self._hash_detail(key),
                    "found": True,
                    "value": self.values[idx],
                    "final_index": idx,
                    "probes": probes,
                    "probe_sequence": probe_sequence,
                }
            idx = (idx + 1) % self.size
            if idx == original_idx:
                return {
                    "operation": "search",
                    "key": key,
                    "hash_value": original_idx,
                    "found": False,
                    "value": None,
                    "probes": probes,
                    "probe_sequence": probe_sequence,
                }

    def delete(self, key) -> dict:
        idx = self._hash(key)
        original_idx = idx
        probes = 0

        while True:
            probes += 1
            if self.keys[idx] == self.EMPTY:
                return {
                    "operation": "delete",
                    "key": key,
                    "hash_value": original_idx,
                    "found": False,
                }
            if self.keys[idx] == key:
                self.keys[idx] = self.DELETED
                self.values[idx] = None
                self.count -= 1
                return {
                    "operation": "delete",
                    "key": key,
                    "hash_value": original_idx,
                    "found": True,
                    "deleted_from": idx,
                    "probes": probes,
                }
            idx = (idx + 1) % self.size
            if idx == original_idx:
                return {
                    "operation": "delete",
                    "key": key,
                    "hash_value": original_idx,
                    "found": False,
                }

    def _hash_detail(self, key) -> str:
        if isinstance(key, int):
            return f"{key} mod {self.size} = {key % self.size}"
        codes = [ord(c) for c in str(key)]
        total = sum(codes)
        return f"sum(ord) of '{key}' = {total}, {total} mod {self.size} = {total % self.size}"

    def load_factor(self) -> float:
        return round(self.count / self.size, 4) if self.size > 0 else 0

    def avg_probe_length(self) -> float:
        ops = len(self.log)
        return round(self.total_probes / ops, 4) if ops > 0 else 0

    def snapshot(self) -> dict:
        return {
            "type": "linear_probing",
            "size": self.size,
            "count": self.count,
            "collisions": self.collisions,
            "load_factor": self.load_factor(),
            "avg_probe_length": self.avg_probe_length(),
            "slots": [
                {
                    "index": i,
                    "key": None if self.keys[i] in (self.EMPTY, self.DELETED) else self.keys[i],
                    "value": self.values[i],
                    "state": (
                        "empty" if self.keys[i] == self.EMPTY
                        else "deleted" if self.keys[i] == self.DELETED
                        else "occupied"
                    ),
                }
                for i in range(self.size)
            ],
            "log": self.log,
        }


# ---------------------------------------------------------------------------
# Phone Book using custom hash table (chaining)
# ---------------------------------------------------------------------------

class PhoneBook:
    """A phone book backed by a chaining hash table."""

    def __init__(self, size: int = 17):
        self.table = ChainingHashTable(size)

    def add(self, name: str, phone: str) -> dict:
        step = self.table.insert(name, phone)
        return {
            "action": "add",
            "name": name,
            "phone": phone,
            "hash_info": step,
        }

    def lookup(self, name: str) -> dict:
        result = self.table.search(name)
        return {
            "action": "lookup",
            "name": name,
            "found": result["found"],
            "phone": result["value"] if result["found"] else None,
            "hash_info": result,
        }

    def remove(self, name: str) -> dict:
        result = self.table.delete(name)
        return {
            "action": "remove",
            "name": name,
            "found": result["found"],
            "hash_info": result,
        }

    def list_all(self) -> list[dict]:
        entries = []
        for bucket in self.table.buckets:
            for k, v in bucket:
                entries.append({"name": k, "phone": v})
        entries.sort(key=lambda e: e["name"])
        return entries

    def snapshot(self) -> dict:
        snap = self.table.snapshot()
        snap["entries"] = self.list_all()
        return snap


# ---------------------------------------------------------------------------
# In-memory state for interactive sessions
# ---------------------------------------------------------------------------

# Hash table visualization state (keyed by session type)
_chaining_table: Optional[ChainingHashTable] = None
_probing_table: Optional[LinearProbingHashTable] = None
_phone_book: Optional[PhoneBook] = None


# ---------------------------------------------------------------------------
# Pydantic request models
# ---------------------------------------------------------------------------

class HashTableInitRequest(BaseModel):
    size: int = 11
    method: str = "chaining"  # "chaining" or "linear_probing"


class HashTableOpRequest(BaseModel):
    method: str = "chaining"
    operation: str  # "insert", "search", "delete"
    key: str | int
    value: Optional[str] = None


class CollisionCompareRequest(BaseModel):
    n: int = 20
    table_size: int = 11
    key_range: int = 200


class PhoneBookOpRequest(BaseModel):
    operation: str  # "add", "lookup", "remove", "list"
    name: Optional[str] = None
    phone: Optional[str] = None


class PhoneBookInitRequest(BaseModel):
    size: int = 17


class PerformanceCompareRequest(BaseModel):
    sizes: list[int] = [100, 500, 1000, 5000, 10000]
    search_count: int = 100


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")


# --- Hash Table Visualization ---

@app.post("/api/hashtable/init")
async def api_hashtable_init(req: HashTableInitRequest):
    """Initialize a new hash table for visualization."""
    global _chaining_table, _probing_table
    size = max(2, min(req.size, 31))
    if req.method == "chaining":
        _chaining_table = ChainingHashTable(size)
        return _chaining_table.snapshot()
    else:
        _probing_table = LinearProbingHashTable(size)
        return _probing_table.snapshot()


@app.post("/api/hashtable/op")
async def api_hashtable_op(req: HashTableOpRequest):
    """Perform an operation on the visualization hash table."""
    global _chaining_table, _probing_table

    # Auto-init if needed
    if req.method == "chaining":
        if _chaining_table is None:
            _chaining_table = ChainingHashTable(11)
        table = _chaining_table
    else:
        if _probing_table is None:
            _probing_table = LinearProbingHashTable(11)
        table = _probing_table

    # Try to convert key to int if it looks like a number
    key = req.key
    if isinstance(key, str) and key.isdigit():
        key = int(key)

    if req.operation == "insert":
        step = table.insert(key, req.value)
    elif req.operation == "search":
        step = table.search(key)
    elif req.operation == "delete":
        step = table.delete(key)
    else:
        return {"error": f"Unknown operation: {req.operation}"}

    snapshot = table.snapshot()
    snapshot["last_operation"] = step
    return snapshot


# --- Collision Resolution Comparison ---

@app.post("/api/hashtable/compare")
async def api_hashtable_compare(req: CollisionCompareRequest):
    """Insert N random keys into both chaining and linear probing tables, compare."""
    n = max(1, min(req.n, 500))
    table_size = max(2, min(req.table_size, 101))
    key_range = max(n, min(req.key_range, 10000))

    keys = random.sample(range(key_range), min(n, key_range))

    chaining = ChainingHashTable(table_size)
    probing = LinearProbingHashTable(table_size)

    chaining_steps = []
    probing_steps = []

    for k in keys:
        cs = chaining.insert(k)
        chaining_steps.append(cs)
        if probing.count < probing.size:
            ps = probing.insert(k)
            probing_steps.append(ps)

    # Search performance
    search_keys = keys[:min(20, len(keys))]
    chaining_search_probes = []
    probing_search_probes = []

    for k in search_keys:
        cr = chaining.search(k)
        chaining_search_probes.append(cr["probes"])
        pr = probing.search(k)
        probing_search_probes.append(pr["probes"])

    return {
        "keys_inserted": keys,
        "n": len(keys),
        "table_size": table_size,
        "chaining": {
            "collisions": chaining.collisions,
            "load_factor": chaining.load_factor(),
            "avg_chain_length": chaining.avg_chain_length(),
            "snapshot": chaining.snapshot(),
            "insert_steps": chaining_steps[:30],
        },
        "probing": {
            "collisions": probing.collisions,
            "load_factor": probing.load_factor(),
            "avg_probe_length": probing.avg_probe_length(),
            "items_inserted": probing.count,
            "snapshot": probing.snapshot(),
            "insert_steps": probing_steps[:30],
        },
        "search_comparison": {
            "keys_searched": search_keys,
            "chaining_probes": chaining_search_probes,
            "probing_probes": probing_search_probes,
            "chaining_avg": round(
                sum(chaining_search_probes) / len(chaining_search_probes), 4
            ) if chaining_search_probes else 0,
            "probing_avg": round(
                sum(probing_search_probes) / len(probing_search_probes), 4
            ) if probing_search_probes else 0,
        },
    }


# --- Phone Book ---

@app.post("/api/phonebook/init")
async def api_phonebook_init(req: PhoneBookInitRequest):
    """Initialize a new phone book."""
    global _phone_book
    size = max(5, min(req.size, 53))
    _phone_book = PhoneBook(size)
    return _phone_book.snapshot()


@app.post("/api/phonebook/op")
async def api_phonebook_op(req: PhoneBookOpRequest):
    """Perform a phone book operation."""
    global _phone_book
    if _phone_book is None:
        _phone_book = PhoneBook(17)

    if req.operation == "add":
        if not req.name or not req.phone:
            return {"error": "Name and phone are required for add"}
        result = _phone_book.add(req.name.strip(), req.phone.strip())
    elif req.operation == "lookup":
        if not req.name:
            return {"error": "Name is required for lookup"}
        result = _phone_book.lookup(req.name.strip())
    elif req.operation == "remove":
        if not req.name:
            return {"error": "Name is required for remove"}
        result = _phone_book.remove(req.name.strip())
    elif req.operation == "list":
        result = {"action": "list"}
    else:
        return {"error": f"Unknown operation: {req.operation}"}

    snapshot = _phone_book.snapshot()
    snapshot["last_operation"] = result
    return snapshot


@app.post("/api/phonebook/preset")
async def api_phonebook_preset():
    """Load preset data into the phone book."""
    global _phone_book
    _phone_book = PhoneBook(17)
    presets = [
        ("Alice", "010-1234-5678"),
        ("Bob", "010-2345-6789"),
        ("Charlie", "010-3456-7890"),
        ("Diana", "010-4567-8901"),
        ("Eve", "010-5678-9012"),
        ("Frank", "010-6789-0123"),
        ("Grace", "010-7890-1234"),
        ("Hank", "010-8901-2345"),
        ("Ivy", "010-9012-3456"),
        ("Jack", "010-0123-4567"),
    ]
    results = []
    for name, phone in presets:
        r = _phone_book.add(name, phone)
        results.append(r)

    snapshot = _phone_book.snapshot()
    snapshot["preset_loaded"] = True
    snapshot["insert_results"] = results
    return snapshot


# --- Performance Comparison: Hash Table O(1) vs List O(n) ---

@app.post("/api/performance/compare")
async def api_performance_compare(req: PerformanceCompareRequest):
    """Compare hash table lookup vs list linear search at different N sizes."""
    sizes = [max(10, min(s, 100000)) for s in req.sizes[:8]]
    search_count = max(10, min(req.search_count, 1000))
    results = []

    for n in sizes:
        # Generate data
        data_keys = list(range(n))
        search_targets = [random.randint(0, n - 1) for _ in range(search_count)]

        # Build hash table (Python dict as baseline for hash performance)
        ht = {}
        for k in data_keys:
            ht[k] = f"value_{k}"

        # Build list of tuples
        lst = [(k, f"value_{k}") for k in data_keys]

        # Time hash table lookups
        start = time.perf_counter()
        ht_found = 0
        for t in search_targets:
            if t in ht:
                ht_found += 1
        ht_time = time.perf_counter() - start

        # Time list linear search
        start = time.perf_counter()
        list_found = 0
        for t in search_targets:
            for k, v in lst:
                if k == t:
                    list_found += 1
                    break
        list_time = time.perf_counter() - start

        # Also time our custom chaining hash table
        custom_ht = ChainingHashTable(max(n // 3, 11))
        for k in data_keys:
            custom_ht.insert(k, f"value_{k}")

        start = time.perf_counter()
        custom_found = 0
        for t in search_targets:
            r = custom_ht.search(t)
            if r["found"]:
                custom_found += 1
        custom_time = time.perf_counter() - start

        results.append({
            "n": n,
            "search_count": search_count,
            "hash_table_ms": round(ht_time * 1000, 4),
            "custom_hash_ms": round(custom_time * 1000, 4),
            "list_search_ms": round(list_time * 1000, 4),
            "speedup_builtin": round(list_time / ht_time, 1) if ht_time > 0 else "N/A",
            "speedup_custom": round(list_time / custom_time, 1) if custom_time > 0 else "N/A",
        })

    return {
        "search_count": search_count,
        "results": results,
        "note": (
            "Hash table provides O(1) average lookup regardless of N, "
            "while list linear search is O(n). The speedup grows with N."
        ),
    }


# --- Hash Function Demo ---

@app.post("/api/hashtable/hash")
async def api_hashtable_hash(key: str, table_size: int = 11):
    """Show how a key is hashed step by step."""
    size = max(2, min(table_size, 101))
    if key.isdigit():
        k = int(key)
        return {
            "key": key,
            "key_type": "integer",
            "table_size": size,
            "steps": [
                f"key = {k}",
                f"hash = {k} mod {size}",
                f"hash = {k % size}",
            ],
            "hash_value": k % size,
        }
    else:
        codes = [(c, ord(c)) for c in key]
        total = sum(ord(c) for c in key)
        return {
            "key": key,
            "key_type": "string",
            "table_size": size,
            "steps": [
                f"key = '{key}'",
                f"char codes: {', '.join(f'{c}={code}' for c, code in codes)}",
                f"sum of codes = {total}",
                f"hash = {total} mod {size}",
                f"hash = {total % size}",
            ],
            "hash_value": total % size,
        }


# Mount static files LAST so /api routes take priority
app.mount("/static", StaticFiles(directory="static"), name="static")
