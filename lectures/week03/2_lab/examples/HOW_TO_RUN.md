# Week 03 Lab - Sorting Algorithms

## Exercises

### A-1: Basic Sorting Algorithms (`a1_basic_sorts.py`)
Implement three O(n^2) sorting algorithms:
- **Selection Sort** — find minimum, swap to front
- **Bubble Sort** — compare adjacent pairs, bubble up (with early termination)
- **Insertion Sort** — insert each element into sorted prefix

### A-2: Advanced Sorting Algorithms (`a2_advanced_sorts.py`)
Implement two O(n log n) divide-and-conquer sorting algorithms:
- **Merge Sort** — split, recurse, merge two sorted halves
- **Quick Sort** — 3-way partition around pivot, recurse

### A-3: Sorting Benchmark (`a3_sort_benchmark.py`)
Runs all sorting algorithms on increasing input sizes and compares execution times.
No implementation needed — this file imports from A-1 and A-2.

### B-1: Web Sort Demo (`solutions/b1_web_sort/`)
Interactive web visualization of sorting algorithms. No changes needed.

## How to Run

```bash
# Run from the examples/ directory
cd lectures/week03/2_lab/examples/

# A-1: Basic sorts (implement first, then run to verify)
python3 a1_basic_sorts.py

# A-2: Advanced sorts (implement first, then run to verify)
python3 a2_advanced_sorts.py

# A-3: Benchmark (run after completing A-1 and A-2)
python3 a3_sort_benchmark.py
```

## Expected Output

- **A-1 / A-2**: Prints the original array and sorted results, then runs 100 random correctness checks. If your implementation is correct, you will see `All tests passed!`.
- **A-3**: Prints timing results for each algorithm at various input sizes. If `matplotlib` is installed, a benchmark graph is saved as `sort_benchmark.png`.

## Solutions

Complete reference implementations are available in the `solutions/` subdirectory.
