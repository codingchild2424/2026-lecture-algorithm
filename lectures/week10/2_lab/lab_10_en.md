---
theme: default
title: "Week 10 Lab — Hash Tables + Project"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 10 Lab
## Hash Tables + Project

**Objectives**: Implement two collision resolution strategies; add hash-based features to the project

---
layout: section
---

# Algorithm Exercises
25 minutes

---

# Ex 1: Chaining Hash Table -- Problem

Implement a hash table that resolves collisions using **chaining** (linked lists at each bucket).

**Requirements**:
- `put(key, value)` -- insert or update
- `get(key)` -- retrieve value or `None`
- `delete(key)` -- remove entry
- `load_factor()` -- return `count / size`

**Example**:
```
Table size = 7
put("apple", 3) -> bucket[hash("apple") % 7]
put("banana", 5) -> same or different bucket?
```

Refer to `examples/ex1_hash_chaining.py` | **Time**: 15 min

---

# Ex 1: Chaining Hash Table -- Solution

```python
class HashTableChaining:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx][i] = (key, value)  # Update
                return
        self.table[idx].append((key, value))        # Insert
        self.count += 1

    def get(self, key):
        idx = self._hash(key)
        for k, v in self.table[idx]:
            if k == key:
                return v
        return None

    def delete(self, key):
        idx = self._hash(key)
        for i, (k, v) in enumerate(self.table[idx]):
            if k == key:
                self.table[idx].pop(i)
                self.count -= 1
                return True
        return False
```

---

# Ex 2: Open Addressing -- Problem

Implement a hash table that resolves collisions using **linear probing**.

**Requirements**:
- `put(key, value)` -- insert; probe linearly on collision
- `get(key)` -- retrieve value; follow probe sequence
- Raise exception when table is full

**Key idea**: If slot `h(key)` is occupied, try `h(key)+1`, `h(key)+2`, ...

```
Table size = 7
put("apple")  -> slot 3
put("banana") -> slot 3 occupied, try slot 4
```

Refer to `examples/ex2_hash_probing.py` | **Time**: 10 min

---

# Ex 2: Open Addressing -- Solution

```python
class HashTableProbing:
    def __init__(self, size=10):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size
        self.count = 0

    def _hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        if self.count >= self.size:
            raise Exception("Hash table is full")
        idx = self._hash(key)
        while self.keys[idx] is not None and self.keys[idx] != key:
            idx = (idx + 1) % self.size   # Linear probing
        if self.keys[idx] is None:
            self.count += 1
        self.keys[idx] = key
        self.values[idx] = value

    def get(self, key):
        idx = self._hash(key)
        start = idx
        while self.keys[idx] is not None:
            if self.keys[idx] == key:
                return self.values[idx]
            idx = (idx + 1) % self.size
            if idx == start:
                break
        return None
```

---

# Chaining vs. Open Addressing

| Aspect | Chaining | Open Addressing |
|--------|----------|-----------------|
| Collision handling | Linked list per bucket | Probe to next slot |
| Memory | Extra pointers | Compact array |
| Load factor | Can exceed 1.0 | Must stay < 1.0 |
| Clustering | No | Yes (primary clustering) |
| Cache performance | Poor (pointer chasing) | Good (contiguous memory) |
| Deletion | Simple | Needs tombstones |

---
layout: section
---

# Project Demo: Hash Table Explorer
10 minutes

---

# Run the Reference Project

```bash
cd project
pip install fastapi uvicorn
uvicorn app:app --reload
```

**Explore**:
- Hash table visualization -- see how keys map to buckets
- Collision resolution comparison -- chaining vs. probing side by side
- Phone book app -- practical hash table use case
- Performance benchmarks -- lookup time vs. load factor

---
layout: section
---

# Project Work
15 minutes

---

# Proj 1: Add Hash-Based Features

Add features to your project that utilize hash tables:

| Topic | Hash Table Feature Ideas |
|-------|-------------------------|
| Shopping Mall | Fast product lookup by product ID, shopping cart caching |
| Social Network | User ID mapping, session management |
| Campus Map | Building name to coordinate mapping |

Use Claude Code to help implement:
```
> "Add a hash table for fast product lookup by ID in my FastAPI app"
```

**Time**: 10 minutes

---

# Proj 2: Performance Comparison

Measure and record **sequential list search vs. hash table lookup**:

```python
import time

# List search: O(n)
start = time.time()
for _ in range(10000):
    result = next((p for p in products if p["id"] == target), None)
list_time = time.time() - start

# Hash table lookup: O(1) average
start = time.time()
for _ in range(10000):
    result = product_hash.get(target)
hash_time = time.time() - start
```

Record your results -- you will need them for the final presentation.

**Time**: 5 minutes

---

# Week 10 Milestone

By the end of this lab:

- Chaining hash table implemented and tested
- Open addressing (linear probing) implemented and tested
- Hash-based feature integrated into your project
- Performance comparison recorded (list vs. hash)

**Next week**: Graph traversal features + midpoint check-in
