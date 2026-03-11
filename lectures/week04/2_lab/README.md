# Week 04 Lab — Advanced Divide and Conquer

## Objectives
- Understand the recursive structure of divide and conquer algorithms and trace their execution.
- Analyze real-world use cases of divide and conquer in web applications.

---

## Type A — Algorithm Implementation

### A-1: Merge Sort Tracing (10 min)

Run `examples/a1_merge_sort_trace.py` to observe the recursive call tree of Merge Sort.

Examine how the array is split and merged at each recursive call.

### A-2: Finding the k-th Smallest Element (15 min)

Refer to `examples/a2_kth_smallest.py` and implement the Randomized Select algorithm.

- An algorithm that finds the k-th smallest element in expected O(n) time
- Utilizes the partition step from Quick Sort

### A-3: Closest Pair of Points (10 min)

Refer to `examples/a3_closest_pair.py` and find the closest pair of points using divide and conquer.

- Brute force O(n²) vs. divide and conquer O(n log n) comparison

---

## Type B — Web Code Analysis

### B-1: Autocomplete API (15 min)

Run the Flask app in the `examples/b1_web_autocomplete/` folder:

```bash
cd examples/b1_web_autocomplete
python app.py
```

Prefix search over a dictionary of 100,000 words:
- `GET /autocomplete/linear?q=pre` — Sequential search
- `GET /autocomplete/binary?q=pre` — Sorted array + binary search

Type characters and experience the difference in response times.
