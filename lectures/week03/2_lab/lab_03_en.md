---
theme: default
title: "Week 03 Lab — Sorting Algorithm Implementation & Benchmark"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 03 Lab
## Sorting Algorithm Implementation & Benchmark

Algorithms Lab

---
layout: section
---

# Overview

---

# Today's Objectives

- Implement **basic** sorting algorithms: Selection, Bubble, Insertion Sort
- Implement **advanced** sorting algorithms: Merge Sort, Quick Sort
- **Benchmark** all algorithms and compare performance
- Experience sorting performance in a **web application** context

<br>

### Lab Structure

| Section | Topic | Time |
|---------|-------|------|
| **A-1** | Basic sorting implementation | 10 min |
| **A-2** | Advanced sorting implementation | 15 min |
| **A-3** | Benchmark all algorithms | 10 min |
| **B-1** | Mini shopping mall sort comparison | 15 min |

---
layout: section
---

# Type A -- Algorithm Implementation

---
layout: section
---

# A-1
## Basic Sorting Algorithms

---

# Selection Sort -- Problem

**Idea**: Find the minimum element, swap it to the front. Repeat.

```text
[64, 34, 25, 12, 22, 11, 90]

Pass 1: Find min=11    -> [11, 34, 25, 12, 22, 64, 90]
                         ^^^^
Pass 2: Find min=12    -> [11, 12, 25, 34, 22, 64, 90]
                              ^^^^
Pass 3: Find min=22    -> [11, 12, 22, 34, 25, 64, 90]
                                   ^^^^
Pass 4: Find min=25    -> [11, 12, 22, 25, 34, 64, 90]
                                        ^^^^
Done!                     [11, 12, 22, 25, 34, 64, 90]
```

**Complexity**: O(n^2) always -- scans remaining elements each pass

---

# Selection Sort -- Solution

```python
def selection_sort(arr):
    """Selection Sort: find minimum, swap to front. O(n^2)"""
    a = arr[:]
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        a[i], a[min_idx] = a[min_idx], a[i]
    return a
```

---

# Bubble Sort -- Problem

**Idea**: Repeatedly swap adjacent elements if out of order. Largest elements "bubble up" to the end.

```text
[64, 34, 25, 12]

Pass 1: [34, 64, 25, 12]  swap(64,34)
         [34, 25, 64, 12]  swap(64,25)
         [34, 25, 12, 64]  swap(64,12)  <- 64 is in place
                      ^^^^
Pass 2: [25, 34, 12, 64]  swap(34,25)
         [25, 12, 34, 64]  swap(34,12)  <- 34 is in place
                  ^^^^
Pass 3: [12, 25, 34, 64]  swap(25,12)  <- 25 is in place
              ^^^^
Done!   [12, 25, 34, 64]
```

**Optimization**: If no swaps occur in a pass, the array is already sorted -- stop early!

---

# Bubble Sort -- Solution

```python
def bubble_sort(arr):
    """Bubble Sort: repeatedly swap adjacent elements. O(n^2)"""
    a = arr[:]
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        if not swapped:
            break
    return a
```

The `swapped` flag enables early termination -- best case becomes O(n) for already-sorted input.

---

# Insertion Sort -- Problem

**Idea**: Take each element and insert it into its correct position in the already-sorted prefix.

```text
[64, 34, 25, 12, 22]

Step 1: [64 | 34, 25, 12, 22]  Insert 34 -> [34, 64 | 25, 12, 22]
Step 2: [34, 64 | 25, 12, 22]  Insert 25 -> [25, 34, 64 | 12, 22]
Step 3: [25, 34, 64 | 12, 22]  Insert 12 -> [12, 25, 34, 64 | 22]
Step 4: [12, 25, 34, 64 | 22]  Insert 22 -> [12, 22, 25, 34, 64]

         sorted part  |  unsorted part
```

**Best case**: O(n) when nearly sorted -- great for small or nearly-sorted data!

---

# Insertion Sort -- Solution

```python
def insertion_sort(arr):
    """Insertion Sort: insert each element into sorted prefix. O(n^2)"""
    a = arr[:]
    for i in range(1, len(a)):
        key = a[i]
        j = i - 1
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a
```

### Run and test

```bash
python examples/solutions/a1_basic_sorts.py
```

---
layout: section
---

# A-2
## Advanced Sorting Algorithms

---

# Merge Sort -- Problem

**Idea**: Divide the array in half, sort each half recursively, then merge.

```text
         [38, 27, 43, 3, 9, 82, 10]
                    /     \
         [38, 27, 43, 3]   [9, 82, 10]
            /     \           /     \
       [38, 27]  [43, 3]  [9, 82]  [10]
        /   \     /   \    /   \      |
      [38] [27] [43]  [3] [9] [82]  [10]
        \   /     \   /    \   /      |
       [27, 38]  [3, 43]  [9, 82]  [10]
            \     /           \     /
        [3, 27, 38, 43]   [9, 10, 82]
                    \     /
         [3, 9, 10, 27, 38, 43, 82]
```

**Complexity**: O(n log n) always -- guaranteed performance!

---

# Merge Sort -- Solution

```python
def merge_sort(arr):
    """Merge Sort: divide, sort halves, merge. O(n log n)"""
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    return _merge(left, right)

def _merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result
```

---

# Quick Sort -- Problem

**Idea**: Pick a pivot, partition into elements less than / equal to / greater than pivot, recurse.

```text
Pivot = 43
[38, 27, 43, 3, 9, 82, 10]

 < 43          == 43         > 43
[38, 27, 3, 9, 10]  [43]    [82]
       |                       |
  quicksort(...)          quicksort(...)
       |                       |
 [3, 9, 10, 27, 38]          [82]

Result: [3, 9, 10, 27, 38] + [43] + [82]
      = [3, 9, 10, 27, 38, 43, 82]
```

**Complexity**: O(n log n) average, O(n^2) worst case

---

# Quick Sort -- Solution

```python
def quick_sort(arr):
    """Quick Sort: partition around pivot, sort subarrays. O(n log n) avg."""
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot]
    middle = [x for x in arr if x == pivot]
    right = [x for x in arr if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)
```

### Run and test

```bash
python examples/solutions/a2_advanced_sorts.py
```

---

# Sorting Algorithms Comparison

| Algorithm | Best | Average | Worst | Stable? | In-place? |
|-----------|------|---------|-------|---------|-----------|
| Selection | O(n^2) | O(n^2) | O(n^2) | No | Yes |
| Bubble | O(n) | O(n^2) | O(n^2) | Yes | Yes |
| Insertion | O(n) | O(n^2) | O(n^2) | Yes | Yes |
| Merge | O(n log n) | O(n log n) | O(n log n) | Yes | No |
| Quick | O(n log n) | O(n log n) | O(n^2) | No | Yes* |

*\* The list-comprehension version above uses extra space.*

---
layout: section
---

# A-3
## Benchmark

---

# A-3: Benchmark -- Run It

```bash
python examples/skeletons/a3_sort_benchmark.py
```

Measure execution time at N = 100, 1,000, 10,000, and 100,000:

```text
Algorithm        N=100     N=1,000    N=10,000   N=100,000
---------------------------------------------------------
Selection Sort   0.001s    0.050s     5.0s        500s
Bubble Sort      0.001s    0.080s     8.0s        800s
Insertion Sort   0.001s    0.030s     3.0s        300s
Merge Sort       0.001s    0.005s     0.05s       0.5s
Quick Sort       0.001s    0.003s     0.03s       0.3s
```

*(Approximate values -- your results will vary)*

**Question**: At what N does the O(n^2) vs O(n log n) difference become noticeable?

---

# A-3: Benchmark -- Visualizing the Gap

```text
Time (s)
  ^
  |
8 |  x                                   x = Bubble Sort
  |                                       o = Selection Sort
6 |                                       + = Insertion Sort
  |  o                                    * = Merge Sort
4 |                                       # = Quick Sort
  |
2 |  +
  |
0 |  *#     *#     *#      *#
  +-----+------+------+-------> N
    100  1,000 10,000 100,000
```

The O(n^2) algorithms shoot up dramatically while O(n log n) algorithms remain nearly flat at this scale.

---
layout: section
---

# Type B -- Web Code Analysis

---
layout: section
---

# B-1
## Mini Shopping Mall Sort Comparison

---

# B-1: Setup

Run the Flask app:

```bash
cd examples/solutions/b1_web_sort
pip install flask
python app.py
```

Open **http://localhost:5000** in your browser.

```text
+--------------------------------------------------+
|  Mini Shopping Mall - Product Sorting Demo        |
|                                                   |
|  Number of products: [1,000 v]                    |
|                                                   |
|  [Sort with Bubble Sort]  [Sort with Quick Sort]  |
|                                                   |
|  Loading time: ______ ms                          |
|                                                   |
|  Product list:                                    |
|  1. Product A - $12.99                            |
|  2. Product B - $24.50                            |
|  ...                                              |
+--------------------------------------------------+
```

---

# B-1: Experiment

### Try these steps

1. Click **"Sort with Bubble Sort"** -- note the loading time
2. Click **"Sort with Quick Sort"** -- note the loading time
3. Increase products: **1,000 -> 10,000 -> 50,000**
4. Feel the difference!

### Expected results

| N products | Bubble Sort | Quick Sort | User Experience |
|-----------|-------------|------------|-----------------|
| 1,000 | ~100 ms | ~5 ms | Both feel instant |
| 10,000 | ~10 sec | ~50 ms | Bubble is painfully slow |
| 50,000 | ~4 min | ~300 ms | Bubble is unusable |

### Discussion

> What would happen if a real online shopping mall used an O(n^2) sorting algorithm?

Every page load, every filter change, every sort-by-price click would make users wait and leave!

---
layout: section
---

# Wrap-Up

---

# Summary

### What we learned today

- Implemented **3 basic sorts**: Selection, Bubble, Insertion -- all O(n^2)
- Implemented **2 advanced sorts**: Merge Sort and Quick Sort -- O(n log n)
- Benchmarked all algorithms and saw the **performance gap** grow with N
- Experienced the impact of sort choice on **web application UX**

### Key takeaway

> For small data, any sort works. For real-world data sizes,
> O(n log n) algorithms are essential.

<br>

### Homework 2

See `../3_assignment/README.md` for assignment details.

### Next week

**Week 04**: Advanced Divide and Conquer -- Merge Sort tracing, k-th smallest, and closest pair of points.
