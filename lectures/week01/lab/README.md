# Week 01 Lab — Introduction: Baekjoon Practice

## Overview
- **Duration**: 50 minutes
- **Format**: Solve 4 Baekjoon problems (individually or in pairs)
- **Goal**: Warm up with basic problems covering sorting, brute force, search, and simple math

---

## Problem 1: Sort Numbers (BOJ 2750) — Bronze I
- **Link**: https://www.acmicpc.net/problem/2750
- **Concept**: Basic sorting — read N numbers and print them in ascending order
- **Hint**: Any O(n²) sorting algorithm (selection sort, bubble sort, insertion sort) will work within the constraints
- **Time limit**: ~10 min

## Problem 2: Blackjack (BOJ 2798) — Bronze II
- **Link**: https://www.acmicpc.net/problem/2798
- **Concept**: Brute force — try all combinations of 3 cards to find the sum closest to M without exceeding it
- **Hint**: Use three nested loops to enumerate all 3-card combinations; N is small enough (≤ 100)
- **Time limit**: ~10 min

## Problem 3: Finding Numbers (BOJ 1920) — Silver IV
- **Link**: https://www.acmicpc.net/problem/1920
- **Concept**: Searching — determine whether each query number exists in a given set
- **Hint**: Sort the array first, then use binary search (or use a set for O(1) lookup)
- **Time limit**: ~15 min

## Problem 4: Sugar Delivery (BOJ 2839) — Silver IV
- **Link**: https://www.acmicpc.net/problem/2839
- **Concept**: Greedy / math — deliver exactly N kg of sugar using 3 kg and 5 kg bags with minimum bag count
- **Hint**: Start by using as many 5 kg bags as possible, then check if the remainder is divisible by 3
- **Time limit**: ~15 min

---

## Tips
- If you are new to Baekjoon, read the input/output format carefully — use `input()` and `print()` in Python
- Test your solution locally before submitting
- Do not worry if you cannot solve all 4 problems — focus on understanding the approach
