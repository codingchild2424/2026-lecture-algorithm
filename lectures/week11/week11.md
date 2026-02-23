# Week 11 — Graph Algorithms I

## Overview
- **Learning Objectives**:
  - Understand graph concepts: vertices, edges, directed/undirected, weighted/unweighted graphs
  - Learn graph representation methods: adjacency matrix, adjacency list, adjacency array, and their trade-offs
  - Master Breadth-First Search (BFS): queue-based traversal, O(V+E) time complexity, shortest hop-count paths
  - Master Depth-First Search (DFS): recursive traversal, O(V+E) time complexity, traversal order
  - Understand topological sorting on DAGs: in-degree-based algorithm and DFS-based algorithm, both O(V+E)
  - Learn the concept of Minimum Spanning Tree (MST): spanning tree, minimum weight, connected undirected graph
  - Understand Prim's algorithm: greedy vertex-growing approach, O(E log V) with a heap
  - Understand Kruskal's algorithm: greedy edge-selection with Union-Find, O(E log V)
- **Textbook**: CLRS 3rd Edition, Chapters 22-23
- **Quiz**: Quiz 8 (covers Week 10 content: Hash Tables) at the START of the 1st hour (~15 min)
- **Homework**: None

## Class Schedule

### 1st Hour (Quiz + Theory Part 1) — 50 min
- [00:00–00:15] **Quiz 8** (covers Week 10: Hash Tables — hash functions, collision resolution, open addressing, load factor)
- [00:15–00:22] Graph basics: definition (G = (V, E)), directed/undirected, weighted/unweighted, adjacency
- [00:22–00:32] Graph representation 1 — Adjacency matrix: NxN matrix, O(1) edge lookup, O(N^2) space
  - Examples: undirected, directed, weighted variants
- [00:32–00:40] Graph representation 2 — Adjacency list: linked lists per vertex, O(V+E) space, O(degree) edge lookup
- [00:40–00:47] Graph representation 3 — Adjacency array: compact array variant, reduced pointer overhead
- [00:47–00:50] Comparison of representations: when to use matrix vs list (dense vs sparse graphs)
- Slides: `theory/11_graph_algorithms_1_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00–00:07] BFS: queue-based level-order traversal, algorithm pseudocode, O(V+E) analysis
  - Step-by-step example on a sample graph, shortest hop-count interpretation
- [00:07–00:15] DFS: recursive approach, algorithm pseudocode, O(V+E) analysis
  - Step-by-step example on a sample graph, visited array mechanism
- [00:15–00:22] Topological sorting: definition (DAG requirement), two algorithms
  - Algorithm 1: repeatedly remove zero in-degree vertices
  - Algorithm 2: DFS-based, insert at front of list upon finishing a vertex
- [00:22–00:30] MST concept: spanning tree, minimum weight, properties (n-1 edges for n vertices)
  - MST problem motivation (e.g., connecting cities with minimum road cost)
- [00:30–00:40] Prim's algorithm: grow MST from a starting vertex, extractMin with heap, relaxation
  - Step-by-step construction example, O(E log V) time complexity
- [00:40–00:48] Kruskal's algorithm: sort edges by weight, Union-Find for cycle detection
  - Step-by-step construction example, O(E log V) time complexity
- [00:48–00:50] Summary: graph representations, BFS vs DFS, Prim vs Kruskal
- Slides: `theory/11_graph_algorithms_1_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **알고리즘 실습** (25분)
  - [00:00–00:15] BFS 구현 + 최단 거리 계산
  - [00:15–00:25] DFS 구현 + 위상 정렬
- **프로젝트 작업** (25분)
  - [00:25–00:40] 프로젝트에 그래프 탐색 기능 추가 (추천, 연관 탐색 등)
  - [00:40–00:50] 팀별 중간 점검 & 진행 공유
- Guide: `lab/README.md`
- **프로젝트 마일스톤**: 그래프 탐색 기능 통합 + 중간 점검

## Materials
- Theory: `theory/11_graph_algorithms_1_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md
- Homework: None
- Quiz: Quiz 8 (Week 10 content — Hash Tables, first 15 minutes of 1st hour)
