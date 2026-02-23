# Week 13 — NP-Completeness & Approximation Algorithms

## Overview
- **Learning Objectives**:
  - Distinguish between P and NP problem classes
  - Understand the difference between decision (Yes/No) problems and optimization problems
  - Define the class NP: problems whose "Yes" certificate can be verified in polynomial time
  - Understand NP-Hard and NP-Complete definitions and their relationship
  - Explain polynomial-time reduction and its role in proving NP-Hardness
  - Recognize famous NP-Complete problems: SAT, 3-SAT, Subset Sum, Vertex Cover, Clique, Graph Coloring, TSP, Hamiltonian Cycle, Longest Path, Bin Packing, Job Scheduling
  - Understand the practical implications of NP-Completeness: when to stop searching for efficient algorithms and resort to heuristics/approximation
  - Appreciate the open question P = NP vs P != NP and its significance
  - Understand why approximation algorithms are needed for NP-complete problems
  - Define approximation ratio and explain how indirect optimal solutions are used to compute it
  - Apply the MST-based approximation algorithm for TSP and prove its approximation ratio of 2.0
  - Apply the maximal matching algorithm for Vertex Cover and prove its approximation ratio of 2.0
  - Compare four greedy heuristics for Bin Packing (First Fit, Next Fit, Best Fit, Worst Fit) and prove their approximation ratios of 2.0
  - Apply greedy job scheduling to minimize makespan and prove its approximation ratio of 2.0
  - Apply the farthest-first-traversal algorithm for k-Clustering and prove its approximation ratio of 2.0
- **Textbook**: CLRS 3rd Edition, Chapters 34 & 35
- **Quiz**: Quiz 10 (covers Week 12 content) at the START of the 1st hour (~15 min) — last quiz
- **Homework**: None

## Class Schedule

### 1st Hour (Quiz + NP-Completeness) — 50 min
- [00:00–00:15] **Quiz 10** (covers Week 12 material) — last quiz of the semester
- [00:15–00:25] Motivation: the analogy of a boss assigning an impossibly hard problem; learning objectives
- [00:25–00:35] Problem classification: P (polynomial-time solvable), intractable, undecidable problems
  - Polynomial time = "tractable"; exponential/factorial time = "intractable"
  - NP-Complete problems sit between solvable and unsolvable
- [00:35–00:45] Famous NP-Complete problems overview: SAT, Subset Sum, Partition, 0-1 Knapsack, Vertex Cover, Independent Set, Clique, Graph Coloring, Set Cover, Longest Path, TSP, Hamiltonian Cycle, Bin Packing, Job Scheduling
- [00:45–00:50] Decision problems vs Optimization problems: every optimization problem has a corresponding decision version; if the decision version is hard, the optimization version is at least as hard
- Slides: `theory/13_np_completeness_en.md` (Parts 1 & 2)

### 2nd Hour (Approximation Algorithms) — 50 min
- [00:00–00:08] Why approximation algorithms? NP-complete problems and the three trade-offs; approximation ratio; indirect optimal solution concept
- [00:08–00:20] TSP approximation (Approx_MST_TSP): MST construction, DFS traversal order, shortcutting via triangle inequality, ratio proof (<= 2.0)
- [00:20–00:30] Vertex Cover approximation (Approx_Matching_VC): maximal matching approach, algorithm, worked example, ratio proof (= 2.0)
- [00:30–00:40] Bin Packing: four greedy heuristics (FF, NF, BF, WF), worked example, ratio proofs (<= 2.0)
- [00:40–00:46] Job Scheduling (Approx_JobScheduling): assign to earliest-finishing machine, worked example, ratio proof (<= 2.0)
- [00:46–00:50] Clustering (Approx_k_Clusters): farthest-first traversal, ratio proof (<= 2.0); summary table
- Slides: `theory/13_np_completeness_en.md` (Part 3)

### 3rd Hour (Lab) — 50 min
- Lab: Project final wrap-up + presentation prep (see lab materials)

## Materials
- Theory: `theory/13_np_completeness_en.md`
- Script: `theory/script.md`
- Homework: None
- Quiz: Quiz 10 (Week 12 content — last quiz, first 15 minutes of 1st hour)
