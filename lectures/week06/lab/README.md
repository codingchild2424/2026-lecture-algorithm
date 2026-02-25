# Week 06 Lab — Dynamic Programming: Baekjoon Practice

## Overview
- **Duration**: 50 minutes
- **Format**: Solve 4 Baekjoon problems (individually or in pairs)
- **Goal**: Practice defining recurrence relations and building DP tables

---

## Problem 1: Making 1 (BOJ 1463) — Silver III
- **Link**: https://www.acmicpc.net/problem/1463
- **Concept**: Basic DP — find the minimum number of operations to reduce N to 1 (divide by 3, divide by 2, or subtract 1)
- **Hint**: Define dp[i] = minimum operations to reach 1 from i; dp[i] = min(dp[i/3], dp[i/2], dp[i-1]) + 1 (only use dp[i/k] when i is divisible by k)
- **Time limit**: ~10 min

## Problem 2: RGB Street (BOJ 1149) — Silver I
- **Link**: https://www.acmicpc.net/problem/1149
- **Concept**: DP with constraints — paint N houses with 3 colors such that no two adjacent houses share the same color, minimizing total cost
- **Hint**: dp[i][c] = min cost to paint houses 1..i with house i painted color c; transition from dp[i-1][other colors]
- **Time limit**: ~15 min

## Problem 3: LCS (BOJ 9251) — Gold V
- **Link**: https://www.acmicpc.net/problem/9251
- **Concept**: Longest Common Subsequence — find the length of the LCS of two strings
- **Hint**: Classic 2D DP; if characters match, dp[i][j] = dp[i-1][j-1] + 1; otherwise dp[i][j] = max(dp[i-1][j], dp[i][j-1])
- **Time limit**: ~15 min

## Problem 4: Normal Knapsack (BOJ 12865) — Gold V
- **Link**: https://www.acmicpc.net/problem/12865
- **Concept**: 0/1 Knapsack — maximize total value without exceeding weight capacity K
- **Hint**: dp[i][w] = max value using items 1..i with capacity w; for each item, choose to include it or skip it. Can optimize to 1D array iterating w in reverse
- **Time limit**: ~10 min

---

## Tips
- Always start by defining the DP state and writing the recurrence before coding
- Draw a small DP table by hand to verify your recurrence is correct
- Bottom-up (tabulation) is generally easier to debug than top-down (memoization) for beginners
- For LCS problems, remember that subsequence ≠ substring — elements do not need to be contiguous
