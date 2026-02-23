# Week 02 — Algorithm Design and Complexity Analysis

## Overview
- **Learning Objectives**:
  - Understand algorithm representation methods (pseudocode, flowchart)
  - Know the six major algorithm classification types
  - Express algorithm efficiency using time complexity
  - Use asymptotic notation (Big-O, Big-Omega, Big-Theta)
  - Understand recurrence relations and the Master Theorem
- **Textbook**: CLRS 3rd Edition, Chapters 1–3

## Class Schedule

### 1st Hour (Theory Part 1) — 50 min
- [00:00–00:05] Review: What is an algorithm? Properties of algorithms
- [00:05–00:15] Euclid's GCD algorithm (history, recursive/iterative, stack trace)
- [00:15–00:25] Algorithm representation (natural language, pseudocode, flowchart)
- [00:25–00:40] Algorithm classification (Divide-and-Conquer, Greedy, DP, Approximation, Backtracking, Branch-and-Bound)
- [00:40–00:50] Time complexity introduction: elementary operations, examples O(1) through O(n^3)
- Slides: `theory/02_design_and_analysis_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00–00:05] Complexity analysis types (worst, average, best, amortized)
- [00:05–00:20] Asymptotic notation: Big-O, Big-Omega, Big-Theta (formal definitions, examples, proofs)
- [00:20–00:30] Common complexity classes and growth rate comparison
- [00:30–00:35] Why efficient algorithms matter (sorting 1 billion numbers)
- [00:35–00:50] Recurrence relations: repeated substitution, guess-and-verify, Master Theorem with examples
- Slides: `theory/02_design_and_analysis_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **Type A — 알고리즘 구현** (35분)
  - [00:00–00:10] 시간 측정 유틸 작성 (`utils/timer.py`)
  - [00:10–00:25] 배열에서 중복 원소 찾기: O(n²) → O(n) 개선
  - [00:25–00:35] 입력 크기 N을 변화시키며 실행 시간 그래프 그리기
- **Type B — 웹 코드 분석** (15분)
  - [00:35–00:50] 상품 검색 API 분석: 선형탐색 vs 이진탐색 응답시간 비교
- Guide: `lab/README.md`
- **Homework 1 출제** (다음 주 마감)

## Materials
- Theory: `theory/02_design_and_analysis_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md, lab/examples/
- Homework: Assignment 1 — Complexity Analysis (see lab/homework/)
- Quiz: None (quizzes start Week 03)
