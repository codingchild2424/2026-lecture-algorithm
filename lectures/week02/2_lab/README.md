# Week 02 Lab — Complexity Analysis Practice

## Objectives
- Measure time complexity experimentally and compare it with theoretical analysis.
- Experience how algorithm choice affects response time in a web API.

---

## Type A — Algorithm Implementation

### A-1: Write a Timing Utility (10 min)

Refer to `examples/skeletons/a1_timer_util.py` and write a utility that measures execution time.

### A-2: Finding Duplicates — O(n²) to O(n) Optimization (15 min)

**Problem**: Given an array of integers, determine whether it contains any duplicate elements.

1. **O(n²) solution**: Compare all pairs using nested for loops
2. **O(n) solution**: Use a hash set (set)

Refer to `examples/skeletons/a2_find_duplicate.py`.

Compare the execution times of both solutions at N=100, 1,000, 10,000, and 100,000.

### A-3: Execution Time Graphs (10 min)

Run `examples/skeletons/a3_complexity_plot.py` to plot execution time graphs for O(1), O(n), O(n log n), and O(n²).

---

## Type B — Web Code Analysis

### B-1: Product Search API Comparison (15 min)

Run the Flask app in the `examples/b1_web_search/` folder:

```bash
cd examples/b1_web_search
pip install flask
python app.py
```

Compare the two search endpoints:
- `GET /search/linear?q=product_name` — Linear search O(n)
- `GET /search/binary?q=product_name` — Binary search O(log n)

Measure and compare response times with N=100, 10,000, and 1,000,000 products.

**Question**: How does the difference between the two approaches change as the data grows larger?
