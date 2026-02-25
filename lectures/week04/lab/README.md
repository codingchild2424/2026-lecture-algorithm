# Week 04 Lab — Divide and Conquer: Baekjoon Practice

## Overview
- **Duration**: 50 minutes
- **Format**: Solve 4 Baekjoon problems (individually or in pairs)
- **Goal**: Apply divide and conquer and binary search techniques

---

## Problem 1: Making Colored Paper (BOJ 2630) — Silver V
- **Link**: https://www.acmicpc.net/problem/2630
- **Concept**: Recursive partitioning — count white and blue paper pieces by dividing an N×N grid into quadrants
- **Hint**: If all cells in the current region are the same color, count it; otherwise split into 4 equal quadrants and recurse
- **Time limit**: ~10 min

## Problem 2: Number of Paper Pieces (BOJ 1780) — Silver II
- **Link**: https://www.acmicpc.net/problem/1780
- **Concept**: Recursive partitioning (3×3) — same idea as colored paper but splitting into 9 sub-regions
- **Hint**: Check if all values are identical; if not, divide into 9 equal N/3 × N/3 blocks and recurse
- **Time limit**: ~15 min

## Problem 3: Quadtree (BOJ 1992) — Silver I
- **Link**: https://www.acmicpc.net/problem/1992
- **Concept**: Quadtree compression — represent a black-and-white image as a compressed string
- **Hint**: If the region is uniform, output 0 or 1; otherwise output `(` + four quadrant results + `)`
- **Time limit**: ~15 min

## Problem 4: Cutting Trees (BOJ 2805) — Silver II
- **Link**: https://www.acmicpc.net/problem/2805
- **Concept**: Binary search on the answer — find the maximum cutter height that yields at least M meters of wood
- **Hint**: Binary search on the cutter height H (0 to max tree height); for each H, compute total wood collected and check if it is ≥ M
- **Time limit**: ~10 min

---

## Tips
- For recursive partitioning problems, draw the recursion tree on paper to understand the splitting process
- Binary search on the answer is a powerful technique — whenever you see "find the maximum/minimum value satisfying a condition," think binary search
- Watch out for integer overflow when summing wood lengths in Problem 4
