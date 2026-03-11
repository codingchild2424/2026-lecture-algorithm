# Week 04 Lab Examples

## Exercises

### A-1: Merge Sort Trace (`a1_merge_sort_trace.py`)
Step-by-step visualization of recursive merge sort. Shows the Divide, Conquer,
and Combine phases with indented output to illustrate recursion depth.

This file is a **demo only** (no skeleton -- already complete).

```bash
python a1_merge_sort_trace.py
```

**Expected output:** Indented trace of recursive calls showing how `[38, 27, 43, 3, 9, 82, 10]` is split, sorted, and merged at each level.

---

### A-2: k-th Smallest Element (`a2_kth_smallest.py`)
Implement `partition` and `randomized_select` (Quickselect) to find the k-th
smallest element in O(n) average time without fully sorting.

```bash
python a2_kth_smallest.py
```

**Expected output:** The k-th smallest element for k=1..7, plus a performance comparison (Quickselect vs sort) on 1M elements.

---

### A-2: Randomized Select -- Detailed (`a2_randomized_select.py`)
Same algorithm as above with more detailed structure: input validation, a
sort-based reference function, and benchmarks at multiple input sizes.

```bash
python a2_randomized_select.py
```

**Expected output:** Correctness verification (OK for each k), then a performance table showing Quickselect speedup over sorting at N=100K, 500K, 1M.

---

### A-3: Closest Pair of Points (`a3_closest_pair.py`)
Implement `_closest_dc` (divide and conquer) to find the closest pair of 2D
points in O(n log^2 n). The brute force O(n^2) version is provided as reference.

```bash
python a3_closest_pair.py
```

**Expected output:** Closest pair result from both brute force and D&C on a small example, then performance comparison at N=100, 1000, 5000.

---

### B-1: Web Autocomplete (`b1_web_autocomplete/`)
Interactive web demo -- no modification needed. See the directory for its own instructions.

---

## Solutions

Complete implementations are available in the `solutions/` subdirectory.
Compare your work after attempting the exercises on your own.
