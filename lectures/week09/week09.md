# Week 09 — Search Trees

## Overview
- **Learning Objectives**:
  - Understand the recursive nature of trees and tree traversal complexity
  - Analyze BST operations (search, insert, delete) and their time complexity
  - Recognize the worst-case degradation of BST to O(n) with sorted input
  - Understand Red-Black Trees and how they guarantee O(log n) height
  - Learn RBT insertion: Double Red resolution via Restructuring and Recoloring
  - Understand B-Trees and how they minimize disk I/O through wide, shallow structure
  - Analyze B-Tree search, insertion (with/without splits), and deletion cases
- **Textbook**: CLRS 3rd Edition, Chapters 12–13
- **Quiz**: Quiz 6 (general review of Week 01–06 midterm content) at the START of the 1st hour (~15 min)
- **Homework**: None

## Class Schedule

### 1st Hour (Quiz + Theory Part 1) — 50 min
- [00:00–00:15] **Quiz 6** (covers Week 01–06 midterm content)
- [00:15–00:22] Tree basics: recursive definition, subtrees, divide-and-conquer connection
- [00:22–00:28] Tree traversal complexity: T(n) = 2T(n/2) + O(1) => Theta(n) by Master Theorem
- [00:28–00:38] BST fundamentals: left < root < right property, search and insert operations
- [00:38–00:45] BST average case: T(n) = T(n/2) + O(1) => O(log n), equivalent to binary search
- [00:45–00:50] BST worst case: sorted input => linked list shape, T(n) = T(n-1) + O(1) => O(n)
- Slides: `theory/09_search_trees_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00–00:07] BST deletion: in-order successor approach, three cases, complexity O(h)
- [00:07–00:15] Red-Black Tree: 5 properties, height bound h <= 2 log(n+1)
- [00:15–00:25] RBT insertion: new node is red, Double Red problem
  - Uncle is black => Restructuring (sort N, P, G; median becomes parent)
  - Uncle is red => Recoloring (P and U become black, G becomes red, propagate upward)
- [00:25–00:30] RBT operation complexities: search, insert, delete all O(log n)
- [00:30–00:40] B-Tree motivation: disk I/O bottleneck, wide and shallow structure
  - One node = one disk block, hundreds of keys per node
- [00:40–00:48] B-Tree operations: key search (traverse and descend), insertion (Case 1: no split, Case 2: split and promote), deletion overview (leaf cases, internal node cases, restructuring)
- [00:48–00:50] Summary: BST vs RBT vs B-Tree trade-offs
- Slides: `theory/09_search_trees_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **알고리즘 실습** (15분)
  - [00:00–00:10] BST 구현 (insert, search, delete)
  - [00:10–00:15] 정렬된 데이터 삽입 시 BST 퇴화 관찰
- **프로젝트 안내 & 작업** (35분)
  - [00:15–00:25] 팀 프로젝트 안내: 주제 소개, 평가 기준, 일정 공유
  - [00:25–00:35] 팀 구성 (3~4인) + 주제 선정
  - [00:35–00:50] 웹앱 뼈대 구축 (Flask + HTML 기본 구조)
- Guide: `lab/README.md`
- **프로젝트 마일스톤**: 팀 확정 + 주제 선정 + 웹앱 뼈대 시작

## Materials
- Theory: `theory/09_search_trees_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md
- Homework: None
- Quiz: Quiz 6 (Week 01–06 review, first 15 minutes of 1st hour)
