# Week 05 Lab — Greedy: Baekjoon Practice

## Overview
- **Duration**: 50 minutes
- **Format**: Solve 4 Baekjoon problems (individually or in pairs)
- **Goal**: Apply greedy strategies and understand when a greedy choice leads to an optimal solution

---

## Problem 1: Coin 0 (BOJ 11047) — Silver IV
- **Link**: https://www.acmicpc.net/problem/11047
- **Concept**: Classic coin change — use the fewest coins to make exactly K won
- **Hint**: Since each coin value divides the next, greedy works: use the largest coin first, then the next largest, and so on
- **Time limit**: ~10 min

## Problem 2: ATM (BOJ 11399) — Silver IV
- **Link**: https://www.acmicpc.net/problem/11399
- **Concept**: Scheduling to minimize total waiting time
- **Hint**: Sort people by their transaction time in ascending order — serving the fastest person first minimizes the cumulative wait
- **Time limit**: ~10 min

## Problem 3: Meeting Room Assignment (BOJ 1931) — Silver I
- **Link**: https://www.acmicpc.net/problem/1931
- **Concept**: Activity selection — maximize the number of non-overlapping meetings
- **Hint**: Sort by end time (break ties by start time); greedily select the next meeting that starts after the current one ends
- **Time limit**: ~15 min

## Problem 4: Lost Bracket (BOJ 1541) — Silver II
- **Link**: https://www.acmicpc.net/problem/1541
- **Concept**: Greedy minimization — minimize the value of an expression by placing brackets optimally
- **Hint**: Split the expression by `-`; the first group is added, and every subsequent group is subtracted entirely
- **Time limit**: ~15 min

---

## Tips
- Greedy problems require proving that the local optimal choice leads to the global optimum
- If you are unsure whether greedy works, try to find a counterexample with a small input
- For Problem 3, pay special attention to meetings where start time equals end time
