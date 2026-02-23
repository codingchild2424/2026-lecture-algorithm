# Week 04 — Divide and Conquer Algorithms

## Overview
- **Learning Objectives**:
  - Understand the divide-and-conquer paradigm (divide, conquer, combine)
  - Analyze merge sort using recurrence relations and the Master Theorem
  - Apply binary search as a divide-and-conquer algorithm
  - Understand quick sort: pivot selection, partitioning, average and worst-case analysis
  - Solve the selection problem (k-th smallest) in average and worst-case linear time
  - Understand the closest pair problem using divide-and-conquer
  - Recognize when divide-and-conquer is inappropriate (e.g., Fibonacci)
- **Textbook**: CLRS 3rd Edition, Chapters 4, 9
- **Quiz**: Quiz 2 (about Week 03 content) at the START of the 1st hour (~15 min)
- **Homework**: Assignment 3 (assigned this week)

## Class Schedule

### 1st Hour (Quiz + Theory Part 1) — 50 min
- [00:00–00:15] **Quiz 2** (covers Week 03 material)
- [00:15–00:25] Divide-and-Conquer concept: divide, conquer, combine, subproblems and subsolutions
- [00:25–00:35] Classification of DaC algorithms by recurrence: T(n) = aT(n/b) + O(f(n))
- [00:35–00:45] Master Theorem intuition via recursion trees (leaf cost vs. merge cost)
- [00:45–00:50] Merge sort review: DaC structure, recurrence T(n) = 2T(n/2) + O(n), time O(n log n)
- Slides: `theory/04_divide_and_conquer_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00–00:05] Binary search as DaC: T(n) = T(n/2) + O(1), time O(log n)
- [00:05–00:20] Quick sort: pivot, partition procedure (step-by-step example), recurrence analysis
  - Best/average case: O(n log n), worst case: O(n^2)
- [00:20–00:35] Selection problem (k-th smallest element)
  - Average linear time algorithm: Randomized Select
  - Worst-case linear time algorithm: Median-of-Medians (groups of 5)
- [00:35–00:45] Closest pair problem: DaC approach, middle strip handling, O(n log^2 n) analysis
- [00:45–00:50] When DaC is inappropriate: Fibonacci example, overlapping subproblems
- Slides: `theory/04_divide_and_conquer_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **Type A — 알고리즘 구현** (35분)
  - [00:00–00:10] Merge Sort 트레이싱 (재귀 호출 트리 출력)
  - [00:10–00:25] k번째 작은 수 찾기 (Randomized Select) 구현
  - [00:25–00:35] 최근접 점의 쌍 (Closest Pair) 구현
- **Type B — 웹 코드 분석** (15분)
  - [00:35–00:50] 자동완성 API: 순차탐색 vs 정렬+이진탐색 응답시간 비교
- Guide: `lab/README.md`
- **Homework 3 출제** (다음 주 마감)

## Materials
- Theory: `theory/04_divide_and_conquer_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md
- Homework: Assignment 3
- Quiz: Quiz 2 (about Week 03)
