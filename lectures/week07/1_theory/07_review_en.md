---
theme: default
title: "Week 7 — Midterm Review"
info: "Algorithms"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Algorithms

Week 7 — Midterm Review and Problem Solving

Korea University Sejong Campus, Dept. of Computer Science & Software

---
layout: section
---

# Part 1. Review of Weeks 1–3

Quiz 5 (DP) + Foundations Review

---

# Today's Plan

| Hour | Content |
|------|---------|
| **1st** | Quiz 5 (DP, ~15 min) + Review of Weeks 1–3 |
| **2nd** | Review of Weeks 4–6 + Practice Problems |
| **3rd** | Exam prep / Open Q&A |

**Midterm Exam (Week 08)**
- Handwritten, 1 hour
- Covers Weeks 01–06
- No digital devices allowed

---

# Midterm Coverage at a Glance

| Week | Topic | CLRS |
|------|-------|------|
| 01 | Introduction to Algorithms | - |
| 02 | Algorithm Design and Complexity Analysis | Ch 1–3 |
| 03 | Arrays, Stacks, Queues, Sorting | Ch 6–8, 10 |
| 04 | Divide and Conquer | Ch 4, 9 |
| 05 | Greedy Algorithms | Ch 16 |
| 06 | Dynamic Programming | Ch 15 |

---
layout: section
---

# Week 01 Review

Introduction to Algorithms

---

# Week 01 — Key Concepts

**What is an Algorithm?**
- A step-by-step procedure for solving a problem
- Properties: **Correctness, Executability, Finiteness, Efficiency**

**Representation**
- Natural language, flowchart, **pseudocode**, programming language

**Algorithm vs. Data Structure**
- Algorithm = the procedure / Data Structure = how data is organized
- They are deeply interrelated

---

# Week 01 — Classic Introductory Problems

| Problem | Technique | Key Idea |
|---------|-----------|----------|
| Finding maximum | Linear scan | Compare each element, keep the best |
| Sequential search | Brute force | O(n) — check every element |
| Binary search | Divide & Conquer | O(log n) — halve the search space |
| Coin change (simple) | Greedy | Pick the largest denomination first |
| Euler path | Graph traversal | Exists iff 0 or 2 odd-degree vertices |
| Fake coin | D&C / Binary encoding | Halve candidates each step |

---
layout: section
---

# Week 02 Review

Algorithm Design and Complexity Analysis

---

# Week 02 — Asymptotic Notation

**Three Notations**

| Notation | Meaning | Intuition |
|----------|---------|-----------|
| **O(g(n))** | Upper bound | f(n) grows **at most** as fast as g(n) |
| **Omega(g(n))** | Lower bound | f(n) grows **at least** as fast as g(n) |
| **Theta(g(n))** | Tight bound | f(n) grows **exactly** as fast as g(n) |

**Formal definition of O:**
f(n) = O(g(n)) iff there exist constants c > 0 and n0 >= 1 such that f(n) <= c * g(n) for all n >= n0

---

# Week 02 — Common Growth Rates

```
O(1) < O(log n) < O(n) < O(n log n) < O(n^2) < O(n^3) < O(2^n) < O(n!)
```

| Complexity | Name | Example |
|-----------|------|---------|
| O(1) | Constant | Array access by index |
| O(log n) | Logarithmic | Binary search |
| O(n) | Linear | Linear search, counting sort |
| O(n log n) | Linearithmic | Merge sort, Heap sort |
| O(n^2) | Quadratic | Selection sort, Bubble sort |
| O(n^3) | Cubic | Floyd-Warshall |
| O(2^n) | Exponential | Naive recursive Fibonacci |

---

# Week 02 — Recurrence Relations

**Three methods for solving recurrences:**

**1. Repeated Substitution**
- Expand T(n) step by step until base case

**2. Guess and Prove (Substitution Method)**
- Guess the form, prove by induction

**3. Master Theorem** — for T(n) = aT(n/b) + f(n)

| Case | Condition | Result |
|------|-----------|--------|
| 1 | f(n) = O(n^(log_b(a) - e)) | T(n) = Theta(n^(log_b(a))) |
| 2 | f(n) = Theta(n^(log_b(a))) | T(n) = Theta(n^(log_b(a)) * log n) |
| 3 | f(n) = Omega(n^(log_b(a) + e)) | T(n) = Theta(f(n)) |

---

# Week 02 — Master Theorem Examples

**Merge Sort:** T(n) = 2T(n/2) + Theta(n)
- a = 2, b = 2, f(n) = n, n^(log_2(2)) = n^1
- Case 2: T(n) = **Theta(n log n)**

**Binary Search:** T(n) = T(n/2) + Theta(1)
- a = 1, b = 2, f(n) = 1, n^(log_2(1)) = n^0 = 1
- Case 2: T(n) = **Theta(log n)**

**Strassen:** T(n) = 7T(n/2) + Theta(n^2)
- a = 7, b = 2, n^(log_2(7)) ~ n^2.81
- Case 1: T(n) = **Theta(n^2.81)**

---
layout: section
---

# Week 03 Review

Data Structures and Sorting

---

# Week 03 — Basic Data Structures

| Structure | Access Pattern | Key Operations | Time |
|-----------|---------------|----------------|------|
| **Array/List** | Index-based | Access: O(1), Insert/Delete: O(n) | - |
| **Stack** | LIFO | push, pop: **O(1)** | - |
| **Queue** | FIFO | enqueue, dequeue: **O(1)** | - |
| **Heap** | Priority-based | insert: O(log n), extract-min/max: **O(log n)** | - |

**Heap Property (Max-Heap):**
- Complete binary tree
- key(parent) >= key(child)
- Stored in an array: children of node i are at 2i and 2i+1

---

# Week 03 — Sorting Algorithms Summary

| Algorithm | Best | Average | Worst | Space | Stable? |
|-----------|------|---------|-------|-------|---------|
| Selection Sort | O(n^2) | O(n^2) | O(n^2) | O(1) | No |
| Bubble Sort | O(n) | O(n^2) | O(n^2) | O(1) | Yes |
| Insertion Sort | O(n) | O(n^2) | O(n^2) | O(1) | Yes |
| Merge Sort | O(n log n) | O(n log n) | O(n log n) | O(n) | Yes |
| Quick Sort | O(n log n) | O(n log n) | O(n^2) | O(log n) | No |
| Heap Sort | O(n log n) | O(n log n) | O(n log n) | O(1) | No |
| Counting Sort | O(n+k) | O(n+k) | O(n+k) | O(k) | Yes |
| Radix Sort | O(d(n+k)) | O(d(n+k)) | O(d(n+k)) | O(n+k) | Yes |

---

# Week 03 — Key Sorting Insights

**Comparison-based sorting lower bound:** Omega(n log n)
- Any comparison-based sort needs at least n log n comparisons in the worst case
- Proved via decision tree argument (n! leaves, height >= log(n!))

**When to use which?**
- Small or nearly sorted data: **Insertion Sort** (fast in practice)
- General purpose, guaranteed O(n log n): **Merge Sort** or **Heap Sort**
- General purpose, fast in practice: **Quick Sort** (with randomized pivot)
- Integer keys in limited range: **Counting Sort** or **Radix Sort** — O(n)

**Recursive structure of sorting:**
- Selection/Bubble sort have recursive interpretations
- Merge sort and Quick sort are naturally recursive (Divide & Conquer)

---
layout: section
---

# Part 2. Review of Weeks 4–6

Algorithm Design Paradigms

---
layout: section
---

# Week 04 Review

Divide and Conquer

---

# Week 04 — Divide and Conquer Pattern

```
DivideAndConquer(P):
    if P is small enough:
        solve P directly (base case)
    else:
        1. DIVIDE P into subproblems P1, P2, ..., Pk
        2. CONQUER: recursively solve each Pi
        3. COMBINE the solutions of Pi into solution of P
```

**Key characteristic:** Subproblems are **independent** (no overlap)

**When it works well:** Subproblems' total input size ~ original input size

**When it fails:** Overlapping subproblems (e.g., naive Fibonacci) --> use DP instead

---

# Week 04 — D&C Algorithms

| Algorithm | Divide | Conquer | Combine | Time |
|-----------|--------|---------|---------|------|
| Merge Sort | Split array in half | Sort each half | Merge two sorted halves | O(n log n) |
| Quick Sort | Partition around pivot | Sort each partition | (trivial) | O(n log n) avg |
| Selection (avg) | Partition around pivot | Recurse on one side | (trivial) | O(n) avg |
| Selection (worst) | Groups of 5, median-of-medians | Recurse on one side | (trivial) | O(n) worst |
| Closest Pair | Split by x-coord | Find closest in each half | Check strip | O(n log n) |

---

# Week 04 — Selection Problem

**Problem:** Find the i-th smallest element in an unsorted array

**Average-case linear time:**
- Use Quick Sort's partition as subroutine
- Recurse on only one side --> T(n) = T(n/2) + O(n) = **O(n)** on average

**Worst-case linear time (Median-of-Medians):**
1. Divide into groups of 5
2. Find median of each group
3. Recursively find median of medians (M)
4. Partition around M
5. Recurse on the appropriate side
- Guarantees at least 3n/10 elements eliminated --> T(n) = T(n/5) + T(7n/10) + O(n) = **O(n)**

---

# Week 04 — Closest Pair of Points

**Problem:** Given n points in the plane, find the pair with minimum distance

**Brute force:** O(n^2) — check all pairs

**Divide and Conquer:**
1. Sort points by x-coordinate
2. Divide into left and right halves by vertical line
3. Recursively find closest pair in each half (distance d)
4. d = min(d_left, d_right)
5. Check the **strip** of width 2d around the dividing line
   - Only need to check at most 7 neighbors for each point in the strip
6. T(n) = 2T(n/2) + O(n log n) --> **O(n log^2 n)** or **O(n log n)** with optimization

---
layout: section
---

# Week 05 Review

Greedy Algorithms

---

# Week 05 — Greedy Algorithm Concept

**Core Idea:** At each step, make the **locally optimal** choice

```
Greedy(C):
    S = {}
    while C is not empty and S is not a complete solution:
        x = best-looking element in C
        remove x from C
        if adding x to S is feasible:
            S = S + {x}
    return S
```

**Key properties:**
- **Greedy-choice property:** A locally optimal choice leads to a globally optimal solution
- **No backtracking:** Once a choice is made, it is never revised
- Works only for specific problems — must prove optimality!

---

# Week 05 — When Does Greedy Work?

| Problem | Greedy Works? | Why? |
|---------|:------------:|------|
| Coin change (standard denominations) | Yes | Each denomination is a multiple of the smaller one |
| Coin change (arbitrary denominations) | **No** | Counter-example: {1, 3, 4}, amount=6 |
| Fractional knapsack | Yes | Can take fractions; sort by value/weight |
| 0/1 Knapsack | **No** | Cannot take fractions; need DP |
| MST (Kruskal, Prim) | Yes | Cut property / Matroid theory |
| Shortest path (Dijkstra) | Yes | Non-negative weights guarantee |
| Job scheduling | Yes | Sort by deadline, swap argument |
| Huffman coding | Yes | Prefix-free property + greedy merge |
| Set cover | **Approx** | Greedy gives O(log n)-approximation |

---

# Week 05 — Greedy Algorithms Detail

**Coin Change (Greedy):** Pick largest denomination not exceeding remaining amount
- O(n) per denomination type, works when denominations divide evenly

**Fractional Knapsack:** Sort items by value/weight ratio, take greedily
- Time: O(n log n)

**Kruskal's MST:** Sort edges by weight, add if no cycle (Union-Find)
- Time: O(E log E)

**Prim's MST:** Grow tree from a vertex, always add cheapest crossing edge
- Time: O(E log V) with binary heap

**Dijkstra's Shortest Path:** Like Prim, but relax edges; add closest unvisited vertex
- Time: O(E log V) with binary heap, or O(V^2) with array

**Huffman Coding:** Merge two lowest-frequency nodes repeatedly
- Time: O(n log n)

---
layout: section
---

# Week 06 Review

Dynamic Programming

---

# Week 06 — DP Concept

**Dynamic Programming (DP)** solves problems by:
1. Breaking them into **overlapping subproblems**
2. Solving each subproblem **once** and storing the result (memoization / table)
3. Building up solutions from **smaller to larger** subproblems

**Two required properties:**
- **Optimal substructure:** Optimal solution contains optimal solutions to subproblems
- **Overlapping subproblems:** Same subproblems recur many times

**Two approaches:**
- **Top-down (Memoization):** Recursive + cache
- **Bottom-up (Tabulation):** Fill table iteratively, small to large

---

# Week 06 — DP Problems Summary

| Problem | Subproblem | Recurrence | Time | Space |
|---------|-----------|------------|------|-------|
| Fibonacci | F(i) | F(i) = F(i-1) + F(i-2) | O(n) | O(n) |
| Matrix Path | C(i,j) = min cost to (i,j) | C(i,j) = m(i,j) + min(C(i-1,j), C(i,j-1)) | O(mn) | O(mn) |
| LCS | L(i,j) = LCS of X_1..i and Y_1..j | match: L(i-1,j-1)+1; else: max(L(i-1,j), L(i,j-1)) | O(mn) | O(mn) |
| Edit Distance | E(i,j) = edit dist of S_1..i, T_1..j | match: E(i-1,j-1); else: 1+min(E(i-1,j), E(i,j-1), E(i-1,j-1)) | O(mn) | O(mn) |
| 0/1 Knapsack | K(i,w) = max value with items 1..i, capacity w | max(K(i-1,w), v_i + K(i-1, w-w_i)) | O(nC) | O(nC) |
| Coin Change (DP) | C(j) = min coins for amount j | C(j) = 1 + min over d_i of C(j - d_i) | O(nk) | O(n) |
| Floyd-Warshall | D(i,j,k) = shortest path i to j via {1..k} | D(i,j,k) = min(D(i,j,k-1), D(i,k,k-1)+D(k,j,k-1)) | O(n^3) | O(n^2) |

---

# Week 06 — DP Recipe

**Step-by-step approach to solving DP problems:**

1. **Identify the subproblem** — What decision is left after one step?
2. **Define the recurrence** — How does the optimal solution relate to subproblems?
3. **Set the base cases** — What are the trivial subproblems?
4. **Determine computation order** — Bottom-up: smaller subproblems first
5. **Extract the answer** — Which table entry holds the final answer?
6. **(Optional) Trace back** — Recover the actual solution, not just its value

> **Tip:** Sketch the recurrence on paper first. Draw arrows showing dependencies.

---
layout: section
---

# Paradigm Comparison

Divide & Conquer vs. Greedy vs. DP

---

# Three Paradigms Compared

| Aspect | Divide & Conquer | Greedy | Dynamic Programming |
|--------|-----------------|--------|-------------------|
| **Approach** | Split, solve recursively, combine | Make locally best choice, never revisit | Solve all subproblems, combine optimally |
| **Subproblems** | Independent | N/A (no subproblems in the traditional sense) | Overlapping |
| **Optimality** | Depends on problem | Only if greedy-choice property holds | Guaranteed (if optimal substructure holds) |
| **Time** | Often O(n log n) | Often O(n log n) or O(n) | Often O(n^2) or O(n^3) |
| **Space** | O(log n) stack | O(1) to O(n) | O(n) to O(n^2) table |
| **Typical use** | Sorting, searching | Scheduling, MST, shortest paths | Sequence alignment, knapsack, chain optimization |

---

# Which Technique Should I Use?

**Decision Flowchart:**

```
Is the problem asking for an optimal value (min/max)?
├── No  --> Consider D&C or brute force
└── Yes
    ├── Can I make a greedy choice that is always safe?
    │   ├── Yes --> Greedy (prove correctness!)
    │   └── No
    │       ├── Do subproblems overlap?
    │       │   ├── Yes --> DP
    │       │   └── No  --> D&C
    │       └── Can the problem be divided into independent parts?
    │           ├── Yes --> D&C
    │           └── No  --> DP
```

**Rule of thumb:** If Greedy fails (counter-example exists), try DP.

---

# Common Pitfalls on the Exam

| Mistake | How to Avoid |
|---------|-------------|
| Confusing O, Omega, Theta | O = upper bound, Omega = lower bound, Theta = tight (both) |
| Applying Master Theorem when f(n) is not polynomial | Check regularity condition; use other methods if needed |
| Claiming Greedy is optimal without proof | Always look for a **counter-example** first |
| Wrong DP recurrence base case | Trace your recurrence on a small example (n=1, 2, 3) |
| Off-by-one errors in DP tables | Be clear about 0-indexed vs. 1-indexed |
| Confusing Fractional vs. 0/1 Knapsack | Fractional = Greedy; 0/1 = DP |
| Quick Sort worst case | O(n^2) when pivot is always min/max; randomized pivot avoids this |

---
layout: section
---

# Practice Problems

Representative Exam-Style Questions

---

# Practice Problem 1: Complexity Analysis

**Q:** Determine the time complexity using the Master Theorem.

```
T(n) = 4T(n/2) + n
```

**Solution:**
- a = 4, b = 2, f(n) = n
- n^(log_b(a)) = n^(log_2(4)) = n^2
- Compare f(n) = n vs. n^2
- f(n) = O(n^(2-epsilon)) for epsilon = 1 --> **Case 1**
- **T(n) = Theta(n^2)**

---

# Practice Problem 2: Greedy vs. DP

**Q:** You have coins with denominations {1, 3, 4} and need to make change for 6 cents using the minimum number of coins. Compare the Greedy and DP approaches.

**Greedy approach:**
- Pick 4 (remaining: 2), pick 1 (remaining: 1), pick 1 (remaining: 0)
- Result: {4, 1, 1} = **3 coins**

**DP approach:**

| j | 0 | 1 | 2 | 3 | 4 | 5 | 6 |
|---|---|---|---|---|---|---|---|
| C(j) | 0 | 1 | 2 | 1 | 1 | 2 | **2** |

- C(6) = min(C(6-1), C(6-3), C(6-4)) + 1 = min(C(5), C(3), C(2)) + 1 = min(2, 1, 2) + 1 = **2 coins** {3, 3}

**Conclusion:** Greedy gives 3 coins, DP gives 2 coins. Greedy is **not optimal** here.

---

# Practice Problem 3: DP — LCS

**Q:** Find the LCS of X = "ABCB" and Y = "BDCAB". Fill in the DP table.

|   |   | B | D | C | A | B |
|---|---|---|---|---|---|---|
|   | 0 | 0 | 0 | 0 | 0 | 0 |
| A | 0 | 0 | 0 | 0 | **1** | 1 |
| B | 0 | **1** | 1 | 1 | 1 | **2** |
| C | 0 | 1 | 1 | **2** | 2 | 2 |
| B | 0 | 1 | 1 | 2 | 2 | **3** |

**Answer:** LCS length = **3**, one LCS = "**BCB**"

**Traceback:** Follow the arrows — diagonal when characters match, otherwise go to the larger neighbor.

---
layout: section
---

# Exam Tips

---

# Exam Tips

**Preparation Strategy:**
1. **Understand, don't memorize** — Time is limited (1 hour)
2. **Practice by hand** — Fill DP tables, trace algorithms, solve recurrences on paper
3. **Prepare a summary sheet** — Key formulas, recurrences, complexity table
4. **Know the paradigm decision flow** — Given a new problem, which technique fits?

**During the Exam:**
1. **Read all questions first** — Allocate time proportionally to point values
2. **Show your work** — Partial credit for correct reasoning even if final answer is wrong
3. **Draw tables and diagrams** — DP tables, recursion trees, algorithm traces
4. **Verify with small examples** — Plug in n=1, n=2 to check your recurrence
5. **State which algorithm/technique you are using** — Be explicit

---

# Key Formulas to Have Ready

**Sorting complexities:** Know the full table (slide 15)

**Master Theorem:** T(n) = aT(n/b) + f(n)
- Case 1: f(n) = O(n^(log_b(a) - e)) --> Theta(n^(log_b(a)))
- Case 2: f(n) = Theta(n^(log_b(a))) --> Theta(n^(log_b(a)) * log n)
- Case 3: f(n) = Omega(n^(log_b(a) + e)) --> Theta(f(n))

**DP Recurrences:**
- LCS: L(i,j) = L(i-1,j-1)+1 if match, else max(L(i-1,j), L(i,j-1))
- Edit Distance: E(i,j) = E(i-1,j-1) if match, else 1+min(three neighbors)
- 0/1 Knapsack: K(i,w) = max(K(i-1,w), v_i + K(i-1,w-w_i))

---

# Final Checklist

- [ ] Can I classify a problem as D&C, Greedy, or DP?
- [ ] Can I solve recurrences using the Master Theorem?
- [ ] Can I fill a DP table by hand for LCS, Edit Distance, Knapsack?
- [ ] Do I know when Greedy fails and can I give a counter-example?
- [ ] Can I state and compare the time complexities of all sorting algorithms?
- [ ] Can I trace Kruskal, Prim, and Dijkstra on a small graph?
- [ ] Can I write the recurrence for a new DP problem?

**If you can check all boxes, you are ready for the midterm.**

---

# Q & A

codingchild@korea.ac.kr

Good luck on the midterm exam!
