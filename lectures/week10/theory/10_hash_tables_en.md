---
theme: default
title: "Week 10 — Hash Tables and Set Data Structures"
info: "Algorithms"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Hash Tables and Set Data Structures

Week 10 — Algorithms

Chosun University, Department of Computer Engineering

---
layout: section
---

# Part 1. Hash Tables

---

# What is Hashing?

**Hash**: Transform data of arbitrary size into data of fixed size

- Use a **key** to quickly look up a **value**
- Store key-value pairs in a **hash table**
- A **hash function** converts the key into an **index** that determines where data is stored

```
Key  ──►  Hash Function  ──►  Hash Value (Index)  ──►  Hash Table
```

<br>

**Goal**: Achieve **O(1)** average-case time for search, insert, and delete

---

# Hash Table Structure

Three core components:

| Component | Role |
|-----------|------|
| **Key** | Unique identifier (string, integer, etc.) for each data item |
| **Hash Function** | Converts a key into a hash value (table index) |
| **Hash Table** | Array where data is stored at the index computed by the hash function |

```
  Key: "Alice"                    Hash Table
       │                    ┌───┬───────────┐
       ▼                    │ 0 │           │
  h("Alice") = 3            │ 1 │           │
       │                    │ 2 │           │
       ▼                    │ 3 │  "Alice"  │ ◄── stored here
  Index = 3                 │ 4 │           │
                            │ 5 │           │
                            └───┴───────────┘
```

---

# Hash Function

A hash function **h(k)** maps a key **k** to an index in the table of size **m**

**Division method** (most common):

$$h(k) = k \bmod m$$

**Example**: Table size m = 10

| Key (k) | h(k) = k mod 10 | Index |
|---------|-----------------|-------|
| 25 | 25 mod 10 | 5 |
| 37 | 37 mod 10 | 7 |
| 42 | 42 mod 10 | 2 |
| 55 | 55 mod 10 | 5 |

Note: Keys 25 and 55 both map to index 5 -- this is a **collision**!

---

# Properties of a Good Hash Function

A well-designed hash function should satisfy:

1. **Deterministic**: Same key always produces the same hash value
2. **Uniform distribution**: Keys should be spread evenly across the table
3. **Efficient**: Computed in O(1) time

<br>

**Choosing m (table size)**:

- Avoid powers of 2 (h(k) depends only on lower-order bits)
- A **prime number** not close to a power of 2 is recommended (CLRS)

<br>

**Multiplication method** (alternative):

$$h(k) = \lfloor m \cdot (k \cdot A \bmod 1) \rfloor \quad \text{where } 0 < A < 1$$

- Advantage: The value of m is not critical
- Knuth suggests $A \approx (\sqrt{5} - 1)/2 \approx 0.618$

---

# Hash Collision

**Collision**: Two different keys produce the same hash value

```
  Key: 25  ──►  h(25) = 5  ──┐
                              ├──►  Index 5  (Collision!)
  Key: 55  ──►  h(55) = 5  ──┘
```

<br>

**Why collisions are inevitable**:

- **Pigeonhole principle**: If we have more keys than table slots, at least two keys must share a slot
- Even with fewer keys, a hash function maps a large key space to a small index space

<br>

**Two main strategies to resolve collisions**:

| Strategy | Also Known As | Idea |
|----------|--------------|------|
| Separate Chaining | Open Hashing | Each slot stores a linked list of colliding elements |
| Open Addressing | Closed Hashing | Find another empty slot within the table |

---
layout: section
---

# Collision Resolution

---

# Separate Chaining (Open Hashing)

Each table slot holds a **linked list** of all key-value pairs that hash to that index

```
  Hash Table
  ┌───┬──────────────────────────────┐
  │ 0 │ → NULL                       │
  │ 1 │ → [11] → [21] → NULL        │
  │ 2 │ → [42] → NULL               │
  │ 3 │ → [13] → [33] → [73] → NULL │
  │ 4 │ → NULL                       │
  │ 5 │ → [25] → [55] → NULL        │
  │ 6 │ → NULL                       │
  │ 7 │ → [37] → NULL               │
  │ 8 │ → NULL                       │
  │ 9 │ → [19] → NULL               │
  └───┴──────────────────────────────┘
```

**Operations**:
- **Insert(k)**: Compute h(k), prepend to the list at slot h(k) -- O(1)
- **Search(k)**: Compute h(k), traverse the list at slot h(k) -- O(chain length)
- **Delete(k)**: Search for k, then remove from the list -- O(chain length)

---

# Separate Chaining — Complexity

**Simple Uniform Hashing Assumption (SUHA)**:
Any key is equally likely to hash to any of the m slots

**Load factor**: $\alpha = n / m$ (n = number of stored keys, m = table size)

Under SUHA, the expected length of each chain is $\alpha$

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| Search (unsuccessful) | $\Theta(1 + \alpha)$ | $\Theta(n)$ |
| Search (successful) | $\Theta(1 + \alpha)$ | $\Theta(n)$ |
| Insert | $O(1)$ | $O(1)$ |
| Delete | $\Theta(1 + \alpha)$ | $\Theta(n)$ |

If $n = O(m)$, then $\alpha = O(1)$, and **all operations are O(1) on average**

Worst case: All n keys hash to the same slot -- degenerates to a linked list search

---

# Open Addressing (Closed Hashing)

All elements are stored **directly in the table** -- no linked lists

When a collision occurs, **probe** for the next available slot

**General probe sequence**: $h(k, i)$ for $i = 0, 1, 2, \ldots, m-1$

<br>

**Three probing strategies**:

| Method | Probe Sequence | Formula |
|--------|---------------|---------|
| Linear Probing | Check consecutive slots | $h(k,i) = (h'(k) + i) \bmod m$ |
| Quadratic Probing | Check with quadratic gaps | $h(k,i) = (h'(k) + c_1 i + c_2 i^2) \bmod m$ |
| Double Hashing | Use a second hash function | $h(k,i) = (h_1(k) + i \cdot h_2(k)) \bmod m$ |

where $h'(k)$ is the original hash function

---

# Linear Probing — Example

Insert keys **{25, 37, 42, 55, 73}** into a table of size m = 10, using h(k) = k mod 10

```
Step 1: Insert 25 → h(25)=5             Step 2: Insert 37 → h(37)=7
┌───┬────┐                              ┌───┬────┐
│ 5 │ 25 │                              │ 5 │ 25 │
│ 7 │    │                              │ 7 │ 37 │
└───┴────┘                              └───┴────┘

Step 3: Insert 42 → h(42)=2             Step 4: Insert 55 → h(55)=5
┌───┬────┐                              ┌───┬────┐
│ 2 │ 42 │                              │ 2 │ 42 │
│ 5 │ 25 │                              │ 5 │ 25 │ ← occupied!
│ 7 │ 37 │                              │ 6 │ 55 │ ← probe to 6
└───┴────┘                              │ 7 │ 37 │
                                        └───┴────┘

Step 5: Insert 73 → h(73)=3
┌───┬────┐
│ 2 │ 42 │
│ 3 │ 73 │
│ 5 │ 25 │
│ 6 │ 55 │
│ 7 │ 37 │
└───┴────┘
```

---

# Clustering Problem

**Primary clustering** in linear probing:

- Occupied slots tend to form **long contiguous blocks**
- A new key that hashes anywhere into a cluster must probe to the end of the cluster
- Clusters grow larger over time, degrading performance

```
  ┌───┬────┐
  │ 0 │    │
  │ 1 │    │
  │ 2 │ 42 │ ┐
  │ 3 │ 73 │ │ cluster
  │ 4 │ ?? │ │ (growing)
  │ 5 │ 25 │ │
  │ 6 │ 55 │ ┘
  │ 7 │ 37 │
  │ 8 │    │
  │ 9 │    │
  └───┴────┘
```

**Quadratic probing** reduces primary clustering but may cause **secondary clustering**

**Double hashing** produces the best distribution -- nearly eliminates clustering

---

# Double Hashing

Uses **two hash functions**:

$$h(k, i) = (h_1(k) + i \cdot h_2(k)) \bmod m$$

- $h_1(k)$: Determines the initial slot
- $h_2(k)$: Determines the probe step size

**Requirements**:
- $h_2(k) \neq 0$ for any key k
- $h_2(k)$ should be relatively prime to m

**Common choice**: m is prime, $h_2(k) = 1 + (k \bmod m')$ where $m' = m - 1$

**Example**: m = 7, $h_1(k) = k \bmod 7$, $h_2(k) = 1 + (k \bmod 5)$

For k = 15: $h_1(15) = 1$, $h_2(15) = 1 + (15 \bmod 5) = 1$

Probe sequence: 1, 2, 3, 4, 5, 6, 0

For k = 22: $h_1(22) = 1$, $h_2(22) = 1 + (22 \bmod 5) = 3$

Probe sequence: 1, 4, 0, 3, 6, 2, 5

---
layout: section
---

# Part 2. Performance Analysis

---

# Load Factor

**Load factor** $\alpha$: The ratio of stored elements to table size

$$\alpha = \frac{n}{m}$$

| $\alpha$ range | Meaning | Performance |
|------------|---------|-------------|
| $\alpha < 0.5$ | Table is mostly empty | Excellent -- near O(1) |
| $0.5 \leq \alpha < 0.75$ | Table is moderately full | Good -- acceptable |
| $\alpha \geq 0.75$ | Table is getting crowded | Degraded -- more collisions |
| $\alpha = 1.0$ | Table is full (open addressing) | Very poor -- long probe sequences |
| $\alpha > 1.0$ | Possible with chaining only | Chains become long |

<br>

**Rule of thumb**:
- Separate chaining: keep $\alpha \leq 1.0$
- Open addressing: keep $\alpha \leq 0.7$ (resize before this threshold)

---

# Rehashing

When the load factor exceeds a threshold, **rehash** (resize the table):

1. Allocate a **new table** of size $m' \approx 2m$ (typically the next prime after 2m)
2. **Recompute** h(k) for every existing key using the new table size
3. **Insert** all elements into the new table
4. **Free** the old table

```
  Old table (m=5, n=4, alpha=0.8)      New table (m=11, n=4, alpha=0.36)
  ┌───┬────┐                            ┌────┬────┐
  │ 0 │ 25 │    rehash                  │  0 │    │
  │ 1 │ 11 │  ─────────►               │  1 │ 11 │
  │ 2 │ 42 │                            │  2 │    │
  │ 3 │ 73 │                            │  3 │ 25 │
  │ 4 │    │                            │  4 │ 73 │
  └───┴────┘                            │  5 │    │
                                        │  6 │    │
                                        │  7 │ 42 │
                                        │  8 │    │
                                        │  9 │    │
                                        │ 10 │    │
                                        └────┴────┘
```

**Cost**: O(n) for one rehash, but **amortized O(1)** over all insertions

---

# Hash Table — Overall Complexity

| Operation | Average Case | Worst Case |
|-----------|-------------|------------|
| Search | **O(1)** | O(n) |
| Insert | **O(1)** amortized | O(n) |
| Delete | **O(1)** | O(n) |

<br>

**Why O(1) on average?**
- Under SUHA, expected chain length (or probe length) is $\Theta(1 + \alpha)$
- If we maintain $\alpha = O(1)$ via rehashing, operations are O(1)

<br>

**When does worst case O(n) happen?**
- All keys hash to the same slot (adversarial or pathological input)
- Hash function is poorly chosen

<br>

**Comparison with other data structures**:

| Operation | Sorted Array | BST (balanced) | Hash Table (avg) |
|-----------|-------------|----------------|------------------|
| Search | O(log n) | O(log n) | **O(1)** |
| Insert | O(n) | O(log n) | **O(1)** |
| Delete | O(n) | O(log n) | **O(1)** |
| Ordered traversal | O(n) | O(n) | **O(n log n)** |

---

# Set and Map Data Structures

Hash tables power two fundamental data structures:

**Set**: A collection of **unique elements** (no duplicates)
- Operations: `add(x)`, `contains(x)`, `remove(x)` -- all O(1) average
- Example: Python `set()`, Java `HashSet`, C++ `unordered_set`

**Map (Dictionary)**: A collection of **key-value pairs**
- Operations: `put(k, v)`, `get(k)`, `remove(k)` -- all O(1) average
- Example: Python `dict`, Java `HashMap`, C++ `unordered_map`

```python
# Python Set example                  # Python Dict (Map) example
visited = set()                        phone = {}
visited.add("A")                       phone["Alice"] = "010-1234"
visited.add("B")                       phone["Bob"]   = "010-5678"
visited.add("A")   # duplicate!       print(phone["Alice"])  # O(1)
print(len(visited))  # 2              print("Bob" in phone)  # O(1)
print("A" in visited) # True, O(1)
```

These are among the most frequently used data structures in coding interviews and competitive programming.

---

# Hash Table vs BST — When to Use Which?

| Criterion | Hash Table | Balanced BST (e.g., RBT) |
|-----------|-----------|--------------------------|
| Average search | **O(1)** | O(log n) |
| Worst-case search | O(n) | **O(log n)** guaranteed |
| Ordered iteration | Not supported | **O(n)** in-order |
| Range queries | Not supported | **O(log n + k)** |
| Memory overhead | Array + chains/probes | Pointers per node |
| Implementation | Needs good hash function | Self-balancing logic |

<br>

**Use hash tables when**:
- You only need lookup / insert / delete by exact key
- Average-case O(1) matters more than worst-case guarantees

**Use balanced BSTs when**:
- You need ordered traversal, range queries, or min/max operations
- Worst-case O(log n) guarantee is required

---

# Summary

1. **Hash function** maps a key to an index: $h(k) = k \bmod m$
2. **Collisions** are inevitable -- resolve them via:
   - **Separate chaining**: linked lists at each slot
   - **Open addressing**: probe for empty slots (linear, quadratic, double hashing)
3. **Load factor** $\alpha = n/m$ controls performance
   - Keep $\alpha$ bounded via **rehashing** (double the table when $\alpha$ exceeds threshold)
4. **Average-case O(1)** for search, insert, delete under uniform hashing
5. **Set** and **Map** are the most common hash-based data structures
6. Hash tables trade ordered operations for speed -- use BSTs when order matters

**CLRS Reference**: Chapter 11 (Hash Tables)

---

# Q & A

uglee@chosun.ac.kr
