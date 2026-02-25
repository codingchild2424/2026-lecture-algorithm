# Week 07 Lab — Review: Baekjoon Practice

## Overview
- **Duration**: 50 minutes
- **Format**: Solve 4 Baekjoon problems (individually or in pairs)
- **Goal**: Review topics from weeks 01-06 (binary search, DP, greedy, divide and conquer)

---

## Problem 1: Number Card 2 (BOJ 10816) — Silver IV
- **Link**: https://www.acmicpc.net/problem/10816
- **Concept**: Counting occurrences — for each query, count how many times it appears in the given cards
- **Hint**: Use a dictionary/Counter for O(1) lookup, or sort and use `bisect_left` / `bisect_right` to count via binary search
- **Time limit**: ~10 min

## Problem 2: Stair Climbing (BOJ 2579) — Silver III
- **Link**: https://www.acmicpc.net/problem/2579
- **Concept**: DP with constraints — climb stairs to maximize score, but you cannot step on 3 consecutive stairs
- **Hint**: dp[i] = max score reaching stair i; consider two cases: (1) skip stair i-1 and come from i-2, or (2) step on i-1 but skip i-2 (come from i-3)
- **Time limit**: ~15 min

## Problem 3: Gas Station (BOJ 13305) — Silver III
- **Link**: https://www.acmicpc.net/problem/13305
- **Concept**: Greedy — travel between cities minimizing total fuel cost
- **Hint**: Track the minimum fuel price seen so far; at each city, if the current price is cheaper, update the minimum and use it for all subsequent distances until a cheaper city is found
- **Time limit**: ~15 min

## Problem 4: Z (BOJ 1074) — Silver I
- **Link**: https://www.acmicpc.net/problem/1074
- **Concept**: Divide and conquer / recursion — find the visit order of cell (r, c) in a Z-shaped traversal of a 2^n x 2^n grid
- **Hint**: Determine which quadrant (r, c) falls into; each quadrant contains (2^(n-1))^2 cells, so add the appropriate offset and recurse into that quadrant
- **Time limit**: ~10 min

---

## Tips
- This lab covers multiple topics — identify which technique each problem requires before coding
- If you get stuck, think about which week's lecture applies to the problem
- Use this session to identify your weak areas before the midterm
