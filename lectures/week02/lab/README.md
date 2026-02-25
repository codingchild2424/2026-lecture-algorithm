# Week 02 Lab — Complexity: Baekjoon Practice

## Overview
- **Duration**: 50 minutes
- **Format**: Solve 4 Baekjoon problems (individually or in pairs)
- **Goal**: Analyze algorithm execution time by reading pseudocode and counting operations

---

## Problem 1: Algorithm Execution Time 1 (BOJ 24262) — Bronze V
- **Link**: https://www.acmicpc.net/problem/24262
- **Concept**: Constant-time algorithm analysis — determine the number of operations and Big-O for a given pseudocode
- **Hint**: The pseudocode runs a fixed number of operations regardless of input size
- **Time limit**: ~10 min

## Problem 2: Algorithm Execution Time 2 (BOJ 24263) — Bronze IV
- **Link**: https://www.acmicpc.net/problem/24263
- **Concept**: Linear-time algorithm analysis — count operations in a single loop
- **Hint**: A single loop from 1 to n executes exactly n times
- **Time limit**: ~10 min

## Problem 3: Algorithm Execution Time 3 (BOJ 24264) — Bronze III
- **Link**: https://www.acmicpc.net/problem/24264
- **Concept**: Quadratic-time algorithm analysis — count operations in nested loops
- **Hint**: Two nested loops each running n times give n × n total operations
- **Time limit**: ~15 min

## Problem 4: Algorithm Execution Time 4 (BOJ 24265) — Bronze III
- **Link**: https://www.acmicpc.net/problem/24265
- **Concept**: Quadratic-time algorithm analysis (variant) — count operations in dependent nested loops
- **Hint**: The inner loop starts from i+1, so total operations = n(n−1)/2
- **Time limit**: ~15 min

---

## Tips
- Read the pseudocode carefully — the answer is about counting, not coding
- Express the operation count as a function of n, then determine the Big-O class
- Remember: O(1) ⊂ O(log n) ⊂ O(n) ⊂ O(n log n) ⊂ O(n²) ⊂ O(n³) ⊂ O(2ⁿ)
