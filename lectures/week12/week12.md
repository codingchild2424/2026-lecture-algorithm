# Week 12 — Graph Algorithms II

## Overview
- **Learning Objectives**:
  - Understand the properties of shortest paths: optimal substructure and relaxation
  - Master Dijkstra's algorithm for single-source shortest paths with non-negative weights
  - Master the Bellman-Ford algorithm for single-source shortest paths with negative weights
  - Detect negative-weight cycles using the Bellman-Ford algorithm
  - Understand the Floyd-Warshall algorithm for all-pairs shortest paths (both edge-based and node-based formulations)
  - Understand shortest paths in DAGs using topological sort
  - Learn the concept of strongly connected components (SCCs) and Kosaraju's algorithm
  - Analyze the time complexity of each algorithm and select the appropriate one based on graph characteristics
- **Textbook**: CLRS 3rd Edition, Chapters 24--25
- **Quiz**: Quiz 9 (covers Week 11 content: Graph Algorithms I -- BFS, DFS, Topological Sort, MST) at the START of the 1st hour (~15 min)
- **Homework**: None

## Class Schedule

### 1st Hour (Quiz + Theory Part 1) — 50 min
- [00:00--00:15] **Quiz 9** (covers Week 11: Graph Algorithms I -- BFS, DFS, Topological Sort, MST)
- [00:15--00:25] Shortest path overview: definitions, conditions (weighted directed graphs), negative-weight cycles
  - Single-source vs all-pairs shortest paths
  - Key property 1: subpaths of shortest paths are also shortest paths
  - Key property 2: relaxation (distance update)
- [00:25--00:40] Dijkstra's algorithm: greedy strategy with priority queue, pseudocode, step-by-step trace
  - Why non-negative weights are required (greedy correctness)
  - Time complexity: O(|E| log |V|) with a binary heap
- [00:40--00:50] Bellman-Ford algorithm: pseudocode, handling negative weights, negative-cycle detection
  - Relaxation over all edges, |V|-1 iterations
  - Time complexity: Theta(|V||E|)
- Slides: `theory/12_graph_algorithms_2_en.md` (Part 1)

### 2nd Hour (Theory Part 2) — 50 min
- [00:00--00:10] Bellman-Ford worked example with negative weights: parallel vs sequential update comparison
- [00:10--00:15] Bellman-Ford as dynamic programming: d_t^k recurrence
- [00:15--00:30] Floyd-Warshall algorithm: all-pairs shortest paths
  - Edge-based formulation: l_ij^(m) = min_k { l_ik^(m-1) + w_kj }, matrix "multiplication" analogy
  - Node-based formulation: d_ij^(k) = min { d_ij^(k-1), d_ik^(k-1) + d_kj^(k-1) }
  - Step-by-step D^(0) through D^(n) computation
  - Predecessor matrix for path reconstruction
  - Time complexity: Theta(|V|^3)
- [00:30--00:40] DAG shortest paths: topological sort + single-pass relaxation, Theta(|V|+|E|)
- [00:40--00:50] Strongly connected components: definition, Kosaraju's algorithm (two DFS passes on G and G^R)
  - Correctness sketch (finish-time ordering), time complexity: Theta(|V|+|E|)
- Slides: `theory/12_graph_algorithms_2_en.md` (Part 2)

### 3rd Hour (Lab) — 50 min
- **알고리즘 실습** (20분)
  - [00:00–00:10] Dijkstra 구현 (heapq 활용)
  - [00:10–00:20] Bellman-Ford 구현 (음수 가중치)
- **프로젝트 작업** (30분)
  - [00:20–00:35] 프로젝트에 최단 경로/최적화 기능 추가
  - [00:35–00:50] 발표자료 작성 시작 (구조 잡기)
- Guide: `lab/README.md`
- **프로젝트 마일스톤**: 최단 경로 기능 추가 + 발표자료 초안

## Materials
- Theory: `theory/12_graph_algorithms_2_en.md`
- Script: `theory/script.md`
- Lab: lab/README.md
- Homework: None
- Quiz: Quiz 9 (Week 11 content -- Graph Algorithms I)
