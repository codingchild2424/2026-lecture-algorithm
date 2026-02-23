# Week 05 — Greedy Algorithms

## Overview
- **Learning Objectives**:
  - Understand the greedy algorithm paradigm and its key properties (greedy-choice property, optimal substructure)
  - Distinguish problems where greedy yields optimal solutions from those where it does not
  - Apply greedy algorithms to classic problems: coin change, fractional knapsack, job scheduling, Huffman coding
  - Understand MST algorithms (Kruskal's, Prim's) and shortest path (Dijkstra's) as greedy algorithms
  - Analyze time complexity of each greedy algorithm
- **Textbook**: CLRS 3rd Edition, Chapter 16
- **Quiz 3**: Covers Week 04 content (Dynamic Programming), given at the START of 1st hour (~15 min)
- **Homework 4**: Assigned this week (see lab materials)

## Class Schedule

### 1st Hour (Quiz + Theory Part 1) — 50 min
- [00:00–00:15] **Quiz 3** (about Week 04: Dynamic Programming)
- [00:15–00:25] Greedy algorithm concept: definition, typical structure, greedy-choice property, optimal substructure
- [00:25–00:35] When greedy fails: binary tree path, non-standard coin denominations; Greedy vs DP comparison
- [00:35–00:45] Coin change problem (greedy approach, limitations, comparison with DP)
- [00:45–00:50] Fractional knapsack: idea and algorithm
- Slides: `theory/05_greedy_algorithms_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00–00:10] Fractional knapsack: worked example and complexity; 0-1 vs Fractional comparison
- [00:10–00:20] Job scheduling: earliest-start-time-first algorithm, worked example, complexity
- [00:20–00:30] Huffman coding: prefix property, algorithm, worked example, compression ratio, complexity
- [00:30–00:40] MST: Kruskal's and Prim's algorithms, pseudocode, complexity comparison
- [00:40–00:50] Dijkstra's shortest path: algorithm, edge relaxation, complexity; Summary
- Slides: `theory/05_greedy_algorithms_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **Type A — 알고리즘 구현** (35분)
  - [00:00–00:10] 동전 거스름돈: 그리디 성공/실패 케이스
  - [00:10–00:20] 분할 가능 배낭 문제 구현
  - [00:20–00:35] Huffman Coding 구현
- **Type B — 웹 코드 분석** (15분)
  - [00:35–00:50] 회의실 예약 시스템: Activity Selection 시각화
- Guide: `lab/README.md`
- **Homework 4 출제** (다음 주 마감)

## Materials
- Theory: `theory/05_greedy_algorithms_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md
- Homework: Assignment 4 (assigned this week)
- Quiz: Quiz 3 (Week 04 content — Dynamic Programming)
