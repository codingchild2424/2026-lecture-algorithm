# Week 03 Lab — Sorting Algorithm Implementation & Benchmark

## Objectives
- Implement fundamental sorting algorithms and compare their performance.
- Experience how the choice of sorting algorithm affects user experience in a web application.

---

## Type A — Algorithm Implementation

### A-1: Basic Sorting Implementation (10 min)

Fill in the TODOs in `examples/basic_sorts.py` to implement Selection Sort, Bubble Sort, and Insertion Sort.

Each function takes a list and returns a new sorted list.

Test:
```bash
python examples/basic_sorts.py
```

### A-2: Advanced Sorting Implementation (15 min)

Fill in the TODOs in `examples/advanced_sorts.py` to implement Merge Sort and Quick Sort.

### A-3: Benchmark (10 min)

Run `examples/sort_benchmark.py` to compare the performance of all sorting algorithms.

```bash
python examples/sort_benchmark.py
```

Measure the execution time of each algorithm at N=100, 1,000, 10,000, and 100,000, and examine the resulting graphs.

**Question**: At what point does the difference between O(n²) and O(n log n) algorithms become noticeable?

---

## Type B — Web Code Analysis

### B-1: Mini Shopping Mall Sort Comparison (15 min)

Run the Flask app in `examples/web_sort_demo/`:

```bash
cd examples/web_sort_demo
pip install flask
python app.py
```

Open `http://localhost:5000` in your browser and:
1. Click the "Sort with Bubble Sort" button and check the loading time
2. Click the "Sort with Quick Sort" button and check the loading time
3. Change the number of products from 1,000 to 10,000 to 50,000 and feel the difference

**Question**: What would happen if a real online shopping mall used an O(n²) sorting algorithm?

---

## Homework 2
See `homework/README.md` for assignment details.
