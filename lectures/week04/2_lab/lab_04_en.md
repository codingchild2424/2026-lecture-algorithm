---
theme: default
title: "Week 04 Lab — Advanced Divide and Conquer"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 04 Lab
## Advanced Divide and Conquer

Algorithms Lab

---
layout: section
---

# Overview

---

# Today's Objectives

- **Trace** the recursive call tree of Merge Sort
- Implement **Randomized Select** to find the k-th smallest element in O(n) average
- Solve the **closest pair of points** problem using divide and conquer
- Compare **linear vs binary** prefix search in an autocomplete API

<br>

### Lab Structure

| Section | Topic | Time |
|---------|-------|------|
| **A-1** | Merge Sort tracing | 10 min |
| **A-2** | Finding the k-th smallest element | 15 min |
| **A-3** | Closest pair of points | 10 min |
| **B-1** | Autocomplete API comparison | 15 min |

---
layout: section
---

# Type A -- Algorithm Implementation

---
layout: section
---

# A-1
## Merge Sort Tracing

---

# A-1: Merge Sort Trace -- Problem

**Goal**: Understand the recursive structure of Merge Sort by visualizing the call tree.

```
merge_sort([38, 27, 43, 3, 9, 82, 10])
  merge_sort([38, 27, 43, 3])
    merge_sort([38, 27])
      merge_sort([38])
      merge_sort([27])
      -> merged: [27, 38]
    merge_sort([43, 3])
      merge_sort([43])
      merge_sort([3])
      -> merged: [3, 43]
    -> merged: [3, 27, 38, 43]
  merge_sort([9, 82, 10])
    merge_sort([9, 82])
      merge_sort([9])
      merge_sort([82])
      -> merged: [9, 82]
    merge_sort([10])
    -> merged: [9, 10, 82]
  -> merged: [3, 9, 10, 27, 38, 43, 82]
```

Run: `python examples/a1_merge_sort_trace.py`

---

# A-1: Merge Sort Trace -- Code

```python
def merge_sort_trace(arr, depth=0):
    """Merge sort with recursive call visualization."""
    indent = "  " * depth
    print(f"{indent}merge_sort({arr})")

    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2
    left = merge_sort_trace(arr[:mid], depth + 1)
    right = merge_sort_trace(arr[mid:], depth + 1)

    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])

    print(f"{indent}  -> merged: {merged}")
    return merged
```

### Key observation

The `depth` parameter controls indentation, revealing the **recursion tree** structure.

---
layout: section
---

# A-2
## Finding the k-th Smallest Element

---

# A-2: k-th Smallest -- Problem

**Problem**: Find the k-th smallest element in an unsorted array.

```
Array: [7, 10, 4, 3, 20, 15, 8]
Sorted: [3, 4, 7, 8, 10, 15, 20]

1st smallest = 3
2nd smallest = 4
3rd smallest = 7
4th smallest = 8    <-- median
```

### Two approaches

| Approach | Method | Complexity |
|----------|--------|------------|
| Naive | Sort, then index | O(n log n) |
| **Randomized Select** | Partition like Quick Sort | **O(n) average** |

Why sort the entire array when we only need one element?

---

# A-2: Randomized Select -- How It Works

Uses the **partition** step from Quick Sort, but only recurses into ONE side.

```
Find 4th smallest in [7, 10, 4, 3, 20, 15, 8]
                             k = 3 (0-indexed)

Step 1: Pick random pivot = 10, partition:
        [7, 4, 3, 8]  [10]  [20, 15]
        ^-- 4 elements   ^-- index 4
        k=3 < 4, so search LEFT side only

Step 2: Pick random pivot = 4, partition:
        [3]  [4]  [7, 8]
              ^-- index 1
        k=3 > 1, so search RIGHT side
        new k = 3 - 2 = 1 (in the right subarray)

Step 3: Pick random pivot = 7, partition:
        []  [7]  [8]
             ^-- index 0
        k=1 > 0, so search RIGHT -> [8]
        Wait... Let me re-index. k=3 overall -> result = 8
```

---

# A-2: Randomized Select -- Solution

```python
def partition(arr, left, right, pivot_idx):
    pivot = arr[pivot_idx]
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    store = left
    for i in range(left, right):
        if arr[i] < pivot:
            arr[i], arr[store] = arr[store], arr[i]
            store += 1
    arr[store], arr[right] = arr[right], arr[store]
    return store

def randomized_select(arr, left, right, k):
    """Find the k-th smallest element (0-indexed)."""
    if left == right:
        return arr[left]
    pivot_idx = random.randint(left, right)
    pivot_idx = partition(arr, left, right, pivot_idx)
    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return randomized_select(arr, left, pivot_idx - 1, k)
    else:
        return randomized_select(arr, pivot_idx + 1, right, k)
```

File: `examples/a2_kth_smallest.py`

---

# A-2: Performance Comparison

```python
# Randomized Select: O(n) average
result1 = kth_smallest(big_data, n // 2)

# Sort + index: O(n log n)
result2 = sorted(big_data)[n // 2 - 1]
```

### Results at N = 1,000,000

```
Method               Time      Complexity
-----------------------------------------
Randomized Select    0.15s     O(n) average
Sort + index         0.85s     O(n log n)
```

**Key insight**: Randomized Select only processes one branch at each level, so it does O(n) + O(n/2) + O(n/4) + ... = O(2n) = O(n) total work on average.

---
layout: section
---

# A-3
## Closest Pair of Points

---

# A-3: Closest Pair -- Problem

**Problem**: Given n points in a 2D plane, find the two points with the smallest distance.

```
         50 |          o (12,30)
            |                        o (40,50)
         30 |
            |
         10 |          o (12,10)
            |
          4 |  o (3,4)
          3 | o (2,3)     <-- closest pair: dist = sqrt(2) ~ 1.41
          1 |     o (5,1)
            +--+--+--+--+--+--+--+--+---> x
               2  5  12       40
```

### Two approaches

| Approach | Complexity | Method |
|----------|------------|--------|
| Brute force | O(n^2) | Check all n(n-1)/2 pairs |
| **Divide & Conquer** | **O(n log n)** | Split, solve halves, check strip |

---

# A-3: Closest Pair -- D&C Strategy

```
1. Sort points by x-coordinate
2. Split into LEFT and RIGHT halves at midpoint

   LEFT          |  RIGHT
   o    o        |     o       o
      o          |        o
         o       |  o
                 |
                mid_x

3. Recursively find closest pair in LEFT  -> d_L
4. Recursively find closest pair in RIGHT -> d_R
5. d = min(d_L, d_R)

6. Check the STRIP: points within distance d of mid_x
   (The closest pair might span the two halves!)

        |<- d ->|<- d ->|
        |  strip region  |
        |   o        o   |  <- only check these
        |      o         |
```

---

# A-3: Closest Pair -- Solution (Key Parts)

```python
def closest_pair_dc(points):
    """O(n log n): Divide and conquer approach."""
    points_sorted = sorted(points, key=lambda p: p[0])
    return _closest_dc(points_sorted)

def _closest_dc(pts):
    n = len(pts)
    if n <= 3:
        return closest_pair_bruteforce(pts)

    mid = n // 2
    mid_x = pts[mid][0]
    left_result = _closest_dc(pts[:mid])
    right_result = _closest_dc(pts[mid:])

    d = min(left_result[0], right_result[0])
    best = left_result if left_result[0] <= right_result[0] \
                       else right_result

    # Check the strip
    strip = [p for p in pts if abs(p[0] - mid_x) < d]
    strip.sort(key=lambda p: p[1])
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < d:
            dd = dist(strip[i], strip[j])
            if dd < d:
                d = dd
                best = (dd, (strip[i], strip[j]))
            j += 1
    return best
```

---

# A-3: Performance Comparison

Run `examples/a3_closest_pair.py`:

```
N       Brute Force     D&C           Speedup
----------------------------------------------
100     0.0030s         0.0020s       1.5x
1,000   0.3000s         0.0100s       30x
5,000   7.5000s         0.0600s       125x
```

*(Approximate values -- your results will vary)*

The brute force approach becomes impractical quickly, while D&C scales gracefully.

```
Time
  ^
  | x                            x = Brute Force O(n^2)
  |                              o = D&C O(n log n)
  |   x
  |
  |      x
  |
  | o  o   o    o     o
  +-------------------------> N
   100  1K  5K  10K  50K
```

---
layout: section
---

# Type B -- Web Code Analysis

---
layout: section
---

# B-1
## Autocomplete API

---

# B-1: Autocomplete API -- Setup

Run the Flask app:

```bash
cd examples/b1_web_autocomplete
python app.py
```

Prefix search over a dictionary of **100,000 words**.

### Two endpoints

| Endpoint | Algorithm | Complexity |
|----------|-----------|------------|
| `GET /autocomplete/linear?q=pre` | Sequential scan | O(n) |
| `GET /autocomplete/binary?q=pre` | Sorted + binary search | O(log n + k) |

```
  User types: "pre"
       |
       v
  +-------------------+      +-------------------+
  | Linear search     |      | Binary search     |
  | Scan all 100K     |      | Jump to "pre"     |
  | words one by one  |      | section in O(log n)|
  | O(n) per query    |      | O(log n + k)      |
  +-------------------+      +-------------------+
       |                           |
       v                           v
  [predict, prefix,          [predict, prefix,
   prepare, present, ...]     prepare, present, ...]
```

*k = number of matching results*

---

# B-1: Experiment

### Try these queries

Type characters in the search box and observe response times:

| Query | Linear Search | Binary Search |
|-------|--------------|---------------|
| `a` | ~50 ms | ~0.5 ms |
| `pre` | ~50 ms | ~0.3 ms |
| `algorithm` | ~50 ms | ~0.2 ms |

### Key observations

- Linear search time is **constant** regardless of query -- it always scans everything
- Binary search is **fast** for all queries -- it jumps directly to the right region
- With 100K words, the difference is already noticeable
- Imagine a real search engine with millions of entries!

### Discussion

> Real autocomplete systems use even more advanced structures like **tries** and **inverted indexes** -- but binary search on sorted data is a great starting point.

---
layout: section
---

# Wrap-Up

---

# Summary

### What we learned today

- **Traced** Merge Sort's recursive call tree to understand divide and conquer
- Implemented **Randomized Select** -- finding k-th smallest in O(n) average
- Solved the **closest pair** problem: brute force O(n^2) vs D&C O(n log n)
- Compared **linear vs binary** prefix search in a web autocomplete API

### Divide and Conquer Pattern

```
1. DIVIDE   -- Split the problem into smaller subproblems
2. CONQUER  -- Solve each subproblem recursively
3. COMBINE  -- Merge the subproblem solutions
```

<br>

### Homework 3

See `../3_assignment/README.md` for assignment details.

### Next week

**Week 05**: New topics ahead -- keep practicing!
