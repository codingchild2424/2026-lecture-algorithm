# Week 03 — Arrays, Stacks, Queues, and Basic Sorting Algorithms

## Overview
- **Learning Objectives**:
  - Review fundamental data structures: array, linked list, stack, queue, heap
  - Understand elementary sorting algorithms (selection, bubble, insertion) and their O(n^2) behavior
  - Understand advanced sorting algorithms (merge sort, quick sort, heap sort) and their O(n log n) behavior
  - Understand linear-time sorting (radix sort, counting sort) and the conditions that make them possible
  - Grasp the recursive structure of sorting algorithms and inductive reasoning
  - Compare all sorting algorithms by worst-case and average-case complexity
- **Textbook**: CLRS 3rd Edition, Chapters 6–8, 10
- **Quiz**: Quiz 1 (covers Week 02 content: algorithm design and complexity analysis)
- **Homework**: Assignment 2 (due next week)

## Class Schedule

### 1st Hour (Quiz + Theory Part 1) — 50 min
- [00:00–00:15] **Quiz 1** — Covers Week 02 (algorithm design, asymptotic notation, recurrence relations)
- [00:15–00:20] Review of fundamental data structures: linked list, stack, queue
- [00:20–00:25] Heap: definition, complete binary tree, min-heap / max-heap, array representation
- [00:25–00:30] Sorting algorithm landscape: O(n^2) vs O(n log n) vs O(n)
- [00:30–00:38] Selection sort: idea, pseudocode, step-by-step example, complexity analysis
- [00:38–00:45] Bubble sort: idea, pseudocode, step-by-step example, complexity analysis
- [00:45–00:50] Insertion sort: idea, pseudocode, step-by-step example, best/worst/average cases
- Slides: `theory/03_arrays_and_sorting_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00–00:05] Recursive structure of elementary sorts (insertion, selection, bubble)
- [00:05–00:15] Merge sort: divide-and-conquer idea, pseudocode, merge procedure, example
- [00:15–00:20] Merge sort complexity: recurrence T(n) = 2T(n/2) + Theta(n) => Theta(n log n)
- [00:20–00:35] Quick sort: partition procedure, pseudocode, worst/average/best case analysis
- [00:35–00:45] Heap sort: buildHeap, heapify, sorting phase, O(n log n) worst case
- [00:45–00:50] Linear-time sorting: radix sort, counting sort, complexity comparison table
- Slides: `theory/03_arrays_and_sorting_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **Type A — 알고리즘 구현** (35분)
  - [00:00–00:10] Selection Sort, Bubble Sort, Insertion Sort 구현
  - [00:10–00:25] Merge Sort, Quick Sort 구현
  - [00:25–00:35] 전체 정렬 벤치마크 (N=100~100,000)
- **Type B — 웹 코드 분석** (15분)
  - [00:35–00:50] 미니 쇼핑몰: Bubble Sort vs Quick Sort 페이지 로딩 시간 비교
- Guide: `lab/README.md`
- **Homework 2 출제** (다음 주 마감)

## Materials
- Theory: `theory/03_arrays_and_sorting_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md
- Homework: Assignment 2 (due next week)
- Quiz: Quiz 1 (Week 02 content, first 15 minutes of 1st hour)
