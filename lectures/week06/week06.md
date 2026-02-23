# Week 06 — Dynamic Programming

## Overview
- **Learning Objectives**:
  - Understand the dynamic programming (DP) paradigm and how it differs from divide-and-conquer
  - Identify the two key properties required for DP: optimal substructure and overlapping subproblems
  - Understand top-down (memoization) vs. bottom-up (tabulation) approaches
  - Apply DP to classic problems: Fibonacci, matrix path, LCS, 0-1 knapsack, coin change, Floyd-Warshall
  - Formulate recurrence relations and fill DP tables for each problem
  - Analyze time and space complexity of DP algorithms
- **Textbook**: CLRS 3rd Edition, Chapter 15
- **Quiz**: Quiz 4 (covers Week 05 content — Greedy Algorithms), given at the START of 1st hour (~15 min)
- **Homework**: Assignment 5 (last assignment, assigned this week)

## Class Schedule

### 1st Hour (Quiz + Theory Part 1) — 50 min
- [00:00–00:15] **Quiz 4** (about Week 05: Greedy Algorithms)
- [00:15–00:25] DP concept: motivation from recursive solutions, overlapping subproblems, optimal substructure
- [00:25–00:35] DP vs Divide-and-Conquer: subproblem reuse, bottom-up computation
- [00:35–00:45] Fibonacci: naive recursion O(2^n), memoization O(n), bottom-up DP O(n)
- [00:45–00:50] Matrix path problem: recurrence, DP table construction, O(n^2) solution
- Slides: `theory/06_dynamic_programming_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00–00:10] LCS (Longest Common Subsequence): recurrence, DP table step-by-step, O(mn) analysis
- [00:10–00:25] 0-1 Knapsack problem: subproblem definition K[i,w], recurrence, worked example, O(nC) analysis
- [00:25–00:35] Coin change problem: DP formulation, comparison with greedy, O(nk) analysis
- [00:35–00:45] Floyd-Warshall algorithm: all-pairs shortest paths, recurrence d_ij^k, O(n^3) analysis
- [00:45–00:50] DP summary: design strategy, implicit ordering of subproblems, comparison with greedy and DaC
- Slides: `theory/06_dynamic_programming_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **Type A — 알고리즘 구현** (35분)
  - [00:00–00:10] 피보나치: naive vs memoization vs tabulation
  - [00:10–00:25] LCS 구현 + DP 테이블 시각화
  - [00:25–00:35] 0-1 Knapsack 구현 + 역추적
- **Type B — 웹 코드 분석** (15분)
  - [00:35–00:50] 텍스트 diff 뷰어 (LCS 기반) 분석
- Guide: `lab/README.md`
- **Homework 5 출제** (마지막 과제, 다음 주 마감)

## Materials
- Theory: `theory/06_dynamic_programming_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md
- Homework: Assignment 5 (last assignment, assigned this week)
- Quiz: Quiz 4 (Week 05 content — Greedy Algorithms)
