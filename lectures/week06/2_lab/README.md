# Week 06 Lab — Dynamic Programming

## Objectives
- Understand and implement the core DP patterns (memoization, tabulation).
- Analyze real-world examples of how DP is used in web applications.

---

## Type A — Algorithm Implementation

### A-1: Fibonacci Comparison (10 min)

Run `examples/fibonacci.py` to compare the performance of three approaches:
- Naive recursion: O(2^n)
- Memoization: O(n)
- Tabulation: O(n)

### A-2: LCS + DP Table Visualization (15 min)

Implement Longest Common Subsequence in `examples/lcs.py` and print the DP table.

### A-3: 0-1 Knapsack + Backtracking (10 min)

Solve the 0-1 knapsack problem in `examples/knapsack.py` and backtrack to determine which items were selected.

---

## Type B — Web Code Analysis

### B-1: Text Diff Viewer (15 min)

Run the Flask app in `examples/web_diff/`:

```bash
cd examples/web_diff
python app.py
```

Enter two texts and the app will highlight the differences based on LCS.
- GitHub's diff feature works on the same principle.

---

## Homework 5 (Final Assignment)
See `homework/README.md` for assignment details.
