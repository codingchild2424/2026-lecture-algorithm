---
theme: default
title: "Week 01 Lab — Environment Setup & Coding Agents"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 01 Lab
## Environment Setup & Coding Agents

Algorithms Lab

---
layout: section
---

# Overview

---

# Today's Objectives

- Install and configure a **coding agent** (Claude Code, Gemini CLI, or OpenCode)
- Verify your **Python development environment**
- Implement **binary search** using the RALPH prompting technique
- Create an **algorithm visualization** script
- Solve your **first Baekjoon** Online Judge problem

<br>

### Prerequisites

- Python 3.10+ installed
- Text editor or IDE (VS Code recommended)

---
layout: section
---

# Task 1
## Install a Coding Agent

---

# Task 1: Install a Coding Agent (10 min)

Choose and install one of the following:

| Agent | Install Command |
|-------|----------------|
| **Claude Code** | `npm install -g @anthropic-ai/claude-code` |
| **Gemini CLI** | `npm install -g @google/gemini-cli` |
| **OpenCode** | `go install github.com/opencode-ai/opencode@latest` |

<br>

### After installation

1. Open your terminal
2. Run the agent command (e.g., `claude`)
3. Verify it launches and responds correctly
4. Try a simple prompt: *"Hello, can you help me with algorithms?"*

---
layout: section
---

# Task 2
## Verify Dev Environment

---

# Task 2: Verify Dev Environment (10 min)

### Step 1 -- Check Python version

```bash
python3 --version
# Expected: Python 3.10.x or higher
```

### Step 2 -- Install required packages

```bash
pip install matplotlib
```

### Step 3 -- Create a Baekjoon Online Judge account

Go to: **https://www.acmicpc.net/**

```
+----------------------------------------------+
|        Baekjoon Online Judge (BOJ)           |
|                                              |
|   [Sign Up] to create your account           |
|   You will submit solutions here all         |
|   semester long!                             |
+----------------------------------------------+
```

---
layout: section
---

# Task 3
## Binary Search with RALPH Technique

---

# The RALPH Technique

A structured approach to prompting coding agents:

```
+-------------------------------------------+
|  R - Role      Assign a role              |
|  A - Ask       Make a request             |
|  L - Limit     Set constraints            |
|  P - Provide   Supply input/context       |
|  H - Hint      Give a hint or direction   |
+-------------------------------------------+
```

<br>

### Example for Binary Search

| Letter | Prompt |
|--------|--------|
| **R** | "You are an algorithm tutor" |
| **A** | "Implement binary search in Python" |
| **L** | "Both recursive and iterative versions" |
| **P** | "Find 7 in the sorted list [1,3,5,7,9,11]" |
| **H** | "Also explain why the time complexity is O(log n)" |

---

# Task 3: Your Turn (15 min)

### Exercise

1. Open your coding agent
2. Craft a RALPH prompt for binary search
3. Compare the agent's output with `examples/binary_search.py`

<br>

### Think about

- Did the agent produce correct code?
- How does it compare to the reference implementation?
- Did the explanation of O(log n) make sense?

---

# Binary Search -- Problem

Given a **sorted** array, find the index of a target value.

```
Array: [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
Target: 7

Step 1:  [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
          L              M                  R     mid=9 > 7, go left

Step 2:  [1, 3, 5, 7, 9]
          L     M     R                           mid=5 < 7, go right

Step 3:        [7, 9]
                L  R                              mid=7 == 7, found!
                M
```

**Time Complexity**: O(log n) -- halving the search space each step

---

# Binary Search -- Iterative Solution

```python
def binary_search_iterative(arr, target):
    """Return the index of target in sorted arr, or -1 if not found."""
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
```

```python
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
idx = binary_search_iterative(data, 7)
print(f"Found at index {idx}")   # Found at index 3
```

---

# Binary Search -- Recursive Solution

```python
def binary_search_recursive(arr, target, left, right):
    """Return the index of target in arr[left..right], or -1."""
    if left > right:
        return -1
    mid = (left + right) // 2
    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, right)
    else:
        return binary_search_recursive(arr, target, left, mid - 1)
```

```python
data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]
idx = binary_search_recursive(data, 7, 0, len(data) - 1)
print(f"Found at index {idx}")   # Found at index 3
```

---
layout: section
---

# Task 4
## Algorithm Visualization

---

# Task 4: Visualization Script (10 min)

Ask your coding agent to create a step-by-step trace of binary search.

### Example prompt

> "Create a Python script that prints the binary search process step by step.
> At each step, show the current search range and the mid value."

### Expected output

```
--- Binary Search Trace for target=7 ---
Step 1: range=[0,9], mid=4, arr[mid]=9
  -> 9 > 7, search left half
Step 2: range=[0,3], mid=1, arr[mid]=3
  -> 3 < 7, search right half
Step 3: range=[2,3], mid=2, arr[mid]=5
  -> 5 < 7, search right half
Step 4: range=[3,3], mid=3, arr[mid]=7
  -> Found at index 3!
```

---
layout: section
---

# Task 5
## First BOJ Problem

---

# Task 5: BOJ 1920 -- Finding Numbers (5 min)

**Problem**: https://www.acmicpc.net/problem/1920

Given N integers and M query integers, determine whether each query exists in the N integers.

```
Input:                    Output:
5                         1
4 1 5 2 3                 1
5                         0
1 3 7 9 5
```

### Strategy

1. Read the N integers into a **set** (or sort + binary search)
2. For each query, check membership

```python
n = int(input())
a = set(map(int, input().split()))
m = int(input())
for x in map(int, input().split()):
    print(1 if x in a else 0)
```

Use the agent to develop your strategy, then **submit on BOJ**!

---
layout: section
---

# Semester Project Preview

---

# Semester Project (Weeks 09--13)

Teams of 3--4 will build a **web application** incorporating course algorithms.

| Phase | Week | Activity |
|-------|------|----------|
| Kickoff | 09 | Claude Code tutorial + team formation |
| Sprint 1 | 10 | Hash table features + performance comparison |
| Sprint 2 | 11 | Graph traversal features + mid-check |
| Sprint 3 | 12 | Shortest path features + presentation prep |
| Final | 13 | Code finalization + team presentations |

### Grading

| Criterion | Weight |
|-----------|--------|
| Algorithm application (4+ algorithms) | 40% |
| Performance comparison | 20% |
| Completeness (working app, code quality) | 20% |
| Presentation (slides, explanation, Q&A) | 20% |

---
layout: section
---

# Wrap-Up

---

# Summary

### What we did today

- Installed a **coding agent** and learned the RALPH technique
- Verified our **Python environment** and created BOJ accounts
- Implemented **binary search** (iterative + recursive)
- Created a **visualization** of binary search
- Solved **BOJ 1920** -- our first online judge submission

### Homework 1

See `homework/README.md` for assignment details.

<br>

### Next week

**Week 02**: Complexity Analysis Practice -- measuring and comparing O(n^2) vs O(n) experimentally!
