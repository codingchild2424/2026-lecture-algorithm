---
theme: default
title: "Week 02 Lab — Complexity Analysis Practice"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 02 Lab
## Complexity Analysis Practice

Algorithms Lab

---
layout: section
---

# Overview

---

# Today's Objectives

- Build a **timer utility** to measure execution time
- Compare **O(n^2) vs O(n)** approaches to finding duplicates
- Visualize complexity curves with **matplotlib**
- Compare **linear vs binary search** in a web API context

<br>

### Lab Structure

| Section | Topic | Time |
|---------|-------|------|
| **A-1** | Timer utility | 10 min |
| **A-2** | Finding duplicates: O(n^2) to O(n) | 15 min |
| **A-3** | Execution time graphs | 10 min |
| **B-1** | Web search API comparison | 15 min |

---
layout: section
---

# Type A -- Algorithm Implementation

---
layout: section
---

# A-1
## Write a Timing Utility

---

# A-1: Timer Utility -- Problem

**Goal**: Write a reusable function that measures how long another function takes to run.

### Requirements

- Accept any function and its arguments
- Run the function multiple times (default: 3) for averaging
- Return both the average elapsed time and the function's result
- Use `time.perf_counter()` for high-resolution timing

```
 measure_time(func, *args, repeat=3)
       |
       v
  Run func(*args) 3 times
       |
       v
  Return (avg_time, result)
```

---

# A-1: Timer Utility -- Solution

```python
import time

def measure_time(func, *args, repeat=3):
    """Run func(*args) multiple times and return average time in seconds."""
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        times.append(end - start)
    avg = sum(times) / len(times)
    return avg, result
```

### Usage

```python
for n in [1_000, 10_000, 100_000, 1_000_000]:
    data = [random.randint(1, 100) for _ in range(n)]
    elapsed, _ = measure_time(sum_list, data)
    print(f"N={n:>10,}: {elapsed:.6f} sec")
```

File: `examples/solutions/a1_timer_util.py`

---
layout: section
---

# A-2
## Finding Duplicates: O(n^2) to O(n)

---

# A-2: Finding Duplicates -- Problem

**Problem**: Given an array of integers, determine whether it contains any duplicates.

### Two approaches

```
Approach 1: Brute Force O(n^2)          Approach 2: Hash Set O(n)
+----------------------------+          +----------------------------+
| for i in range(n):         |          | seen = set()               |
|   for j in range(i+1, n): |          | for x in arr:              |
|     if arr[i] == arr[j]:  |          |   if x in seen:            |
|       return True          |          |     return True            |
|                            |          |   seen.add(x)              |
+----------------------------+          +----------------------------+
  Compares all pairs                      One pass with O(1) lookup
```

### Task

- Implement both approaches
- Compare execution times at N = 100, 1,000, 10,000, and 50,000
- Calculate the speedup factor

---

# A-2: Finding Duplicates -- Brute Force O(n^2)

```python
def has_duplicate_bruteforce(arr):
    """O(n^2): Check all pairs."""
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                return True
    return False
```

### How many comparisons?

```
N = 5:   arr = [3, 1, 4, 1, 5]

  i=0: compare (0,1) (0,2) (0,3) (0,4)     4 comparisons
  i=1: compare (1,2) (1,3) (1,4)            3 comparisons
  i=2: compare (2,3) (2,4)                  2 comparisons
  i=3: compare (3,4)                        1 comparison
                                       Total: 10 = n(n-1)/2
```

---

# A-2: Finding Duplicates -- Hash Set O(n)

```python
def has_duplicate_hashset(arr):
    """O(n): Use a set."""
    seen = set()
    for x in arr:
        if x in seen:
            return True
        seen.add(x)
    return False
```

### How it works

```
arr = [3, 1, 4, 1, 5]

Step 1: x=3  seen={}        -> add 3    seen={3}
Step 2: x=1  seen={3}       -> add 1    seen={3,1}
Step 3: x=4  seen={3,1}     -> add 4    seen={3,1,4}
Step 4: x=1  seen={3,1,4}   -> 1 in seen! Return True
```

Only **4 steps** instead of 10 comparisons!

---

# A-2: Benchmark Results

Run `examples/solutions/a2_find_duplicate.py` and compare:

```
         N |        O(n^2) |         O(n) |  Speedup
--------------------------------------------------
       100 |     0.000150  |     0.000005 |    30.0x
     1,000 |     0.015000  |     0.000050 |   300.0x
    10,000 |     1.500000  |     0.000500 | 3,000.0x
    50,000 |    37.500000  |     0.002500 |15,000.0x
```

*(Approximate values -- your results will vary)*

**Key insight**: The speedup grows proportionally with N!

As N doubles, O(n^2) takes ~4x longer, but O(n) takes only ~2x longer.

---
layout: section
---

# A-3
## Execution Time Graphs

---

# A-3: Complexity Plot (10 min)

Run `examples/skeletons/a3_complexity_plot.py` to visualize growth rates:

```bash
python examples/skeletons/a3_complexity_plot.py
```

```
Time
 ^
 |                                        .  O(n^2)
 |                                    .
 |                                .
 |                           .
 |                      .            ....... O(n log n)
 |                .          ........
 |           .        .......
 |       .     .......
 |    . ........ . . . . . . . . . . . . .   O(n)
 | .....
 |............................................... O(1)
 +---------------------------------------------> N
```

### What to observe

- O(1) stays flat -- constant regardless of input size
- O(n) grows linearly -- double N, double time
- O(n log n) grows slightly faster than linear
- O(n^2) grows dramatically -- quickly becomes impractical

---
layout: section
---

# Type B -- Web Code Analysis

---
layout: section
---

# B-1
## Product Search API Comparison

---

# B-1: Web Search API -- Setup

Run the Flask app to compare search strategies in a web context:

```bash
cd examples/b1_web_search
pip install flask
python app.py
```

### Two endpoints

| Endpoint | Algorithm | Complexity |
|----------|-----------|------------|
| `GET /search/linear?q=name` | Linear search | O(n) |
| `GET /search/binary?q=name` | Binary search | O(log n) |

```
  Client                    Server
    |                          |
    | GET /search/linear?q=abc |
    |------------------------->|  Scan all N products...
    |<-------------------------|  Found! (slow)
    |                          |
    | GET /search/binary?q=abc |
    |------------------------->|  Binary search sorted list...
    |<-------------------------|  Found! (fast)
```

---

# B-1: Measuring the Difference

Test with increasing data sizes:

| N (products) | Linear O(n) | Binary O(log n) | Ratio |
|-------------|-------------|-----------------|-------|
| 100 | ~0.1 ms | ~0.01 ms | ~10x |
| 10,000 | ~10 ms | ~0.02 ms | ~500x |
| 1,000,000 | ~1,000 ms | ~0.03 ms | ~33,000x |

### Discussion question

> How does the difference between the two approaches change as the data grows larger?

**Answer**: Linear search time grows proportionally with N, while binary search time grows logarithmically. At 1 million products, linear search takes ~1 second per query -- unacceptable for a real web service!

---
layout: section
---

# Wrap-Up

---

# Summary

### What we learned today

- Built a **timer utility** for measuring execution time
- Experienced the dramatic difference between **O(n^2) and O(n)**
- Visualized **complexity growth curves** with matplotlib
- Saw how algorithm choice affects **web API response times**

### Key takeaway

> Algorithm complexity is not just theory -- it directly impacts
> user experience, especially as data grows.

<br>

### Homework 1

See `../3_assignment/README.md` for assignment details.

### Next week

**Week 03**: Sorting Algorithm Implementation & Benchmark
