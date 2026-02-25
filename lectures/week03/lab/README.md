# Week 03 Lab — Sorting: Baekjoon Practice

## Overview
- **Duration**: 50 minutes
- **Format**: Solve 4 Baekjoon problems (individually or in pairs)
- **Goal**: Apply various sorting techniques and understand when to use each one

---

## Problem 1: Sort Inside (BOJ 1427) — Silver V
- **Link**: https://www.acmicpc.net/problem/1427
- **Concept**: Descending sort — sort the digits of a number in non-increasing order
- **Hint**: Convert the number to a list of digits, sort in descending order, and join them back
- **Time limit**: ~10 min

## Problem 2: Sort Numbers 2 (BOJ 2751) — Silver V
- **Link**: https://www.acmicpc.net/problem/2751
- **Concept**: Efficient sorting — sort up to 1,000,000 numbers in ascending order
- **Hint**: O(n²) sorts will TLE; use Python's built-in `sorted()` which runs in O(n log n)
- **Time limit**: ~10 min

## Problem 3: Sort Numbers 3 (BOJ 10989) — Bronze I
- **Link**: https://www.acmicpc.net/problem/10989
- **Concept**: Counting sort — sort up to 10,000,000 numbers where each value is at most 10,000
- **Hint**: Values are bounded by 10,000 — use a counting array instead of comparison-based sort; also use `sys.stdin` for fast I/O
- **Time limit**: ~15 min

## Problem 4: Coordinate Sort (BOJ 11650) — Silver V
- **Link**: https://www.acmicpc.net/problem/11650
- **Concept**: Multi-key sorting — sort 2D coordinates by x first, then by y
- **Hint**: Python's `sort()` naturally handles tuples in lexicographic order — just sort a list of (x, y) pairs
- **Time limit**: ~15 min

---

## Tips
- In Python, use `sys.stdin.readline` for fast input when N is large
- Know when comparison sort O(n log n) is sufficient vs. when counting sort O(n + k) is needed
- Python's Timsort is highly optimized — prefer built-in sort unless the problem requires a specific algorithm
