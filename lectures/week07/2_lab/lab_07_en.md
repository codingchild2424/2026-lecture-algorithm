---
theme: default
title: "Week 07 Lab — Midterm Exam Preparation"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 07 Lab
## Midterm Exam Preparation

Algorithms Lab

---
layout: section
---

# Overview

---

# Today's Objectives

- Prepare for the midterm by solving **past exam-style problems** hands-on
- Develop the ability to **identify the appropriate algorithm paradigm** for a given problem
- **Review** the key algorithms from Weeks 02 through 06

<br>

### Lab Structure (50 min)

| Order | Exercise | Time | Resource |
|-------|----------|------|----------|
| **Ex 1** | Solving exam problems with an AI agent | 20 min | (using an agent) |
| **Ex 2** | Algorithm paradigm identification | 15 min | `examples/ex2_paradigm_practice.py` |
| **Ex 3** | First-half review & code review | 15 min | `examples/ex3_review_problems.py` |

---
layout: section
---

# Ex 1
## Solving Exam Problems with an AI Agent

---

# Ex 1: AI Agent Practice -- Problem

**Objective**: Work with an AI agent (e.g., Claude) to solve midterm-style problems.

### How to Proceed

```
1. Ask the agent for a problem
2. Try solving it on your own (5 min)
3. Have the agent check your solution
4. If incorrect, get a hint and try again
5. Repeat for 2-3 problems
```

### Recommended Prompt

```
"Give me an algorithm problem from the Week 02-06 scope
that could appear on the midterm.
Please cover a mix of: complexity analysis, sorting,
divide and conquer, greedy, and DP.
After giving the problem, please grade my solution
when I submit it."
```

### Scope

- Complexity analysis (Week 02)
- Sorting algorithms (Week 03)
- Divide and Conquer (Week 04)
- Greedy algorithms (Week 05)
- Dynamic Programming (Week 06)

---

# Ex 1: Example Interaction

```
You:   "Give me a midterm-style algorithm problem."

Agent: "Problem: Given an array of n integers, find the
        maximum sum of a contiguous subarray.
        Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> 6
        Which paradigm would you use? Write the solution."

You:   "I would use DP (Kadane's algorithm).
        dp[i] = max(arr[i], dp[i-1] + arr[i])
        Answer = max(dp[0..n-1])"

Agent: "Correct! Time: O(n), Space: O(1) with optimization.
        Here's a follow-up: can you also solve this
        with divide and conquer? What's the complexity?"
```

### Tips

- Start with problems you find **difficult** -- that is where review is most valuable
- Ask for **hints** rather than full solutions when stuck
- Practice **explaining your reasoning** -- the exam may require written explanations

---
layout: section
---

# Ex 2
## Algorithm Paradigm Identification

---

# Ex 2: Paradigm Identification -- Problem

**Objective**: Read a problem and determine which paradigm to apply.

### The Four Paradigms

| Paradigm | Key Characteristics |
|----------|---------------------|
| **Brute Force** | Explores all possibilities; constraints are small |
| **Divide & Conquer** | Splits into **independent** subproblems to solve |
| **Greedy** | Best choice at each step; greedy choice property |
| **DP** | Optimal substructure + **overlapping** subproblems |

### How to Proceed

1. Open `examples/ex2_paradigm_practice.py` and read the 10 problems
2. For each problem, decide which paradigm to use
3. Briefly note your reasoning
4. Compare with the answers at the bottom of the file

Run: `python examples/ex2_paradigm_practice.py`

---

# Ex 2: Practice Problems (1-5)

**Problem 1**: Two Sum -- find all pairs in an array that sum to a target. Array size <= 100.

**Problem 2**: Maximum Subarray Sum -- find the contiguous subarray with the largest sum.

**Problem 3**: Closest Pair of Points -- given n points (n <= 100,000), find the closest two.

**Problem 4**: Coin Change -- coins = [1, 5, 7, 10], find minimum coins for a given amount.

**Problem 5**: Activity Selection -- given meetings with start/end times, maximize non-overlapping count.

<br>

Think about each one before moving to the next slide...

---

# Ex 2: Answers (1-5)

| # | Problem | Paradigm | Reasoning |
|---|---------|----------|-----------|
| 1 | Two Sum (n<=100) | **Brute Force** | n^2 = 10,000 -- small enough for O(n^2) |
| 2 | Max Subarray | **DP** (or D&C) | Kadane's: dp[i] = max(a[i], dp[i-1]+a[i]) |
| 3 | Closest Pair | **D&C** | Split by x, solve halves, check strip. O(n log n) |
| 4 | Coin Change | **DP** | Coins lack divisor property; greedy fails on [1,5,7,10] |
| 5 | Activity Selection | **Greedy** | Sort by end time, pick greedily. Proven optimal |

### Key insight for #4

```
Coins = [1, 5, 7, 10], Amount = 14

Greedy: 10 + 1 + 1 + 1 + 1 = 5 coins
DP:     7 + 7             = 2 coins  <-- optimal!
```

---

# Ex 2: Practice Problems (6-10)

**Problem 6**: Permutation in String -- does s2 contain a permutation of s1 as a substring?

**Problem 7**: Longest Increasing Subsequence (LIS) -- find the longest strictly increasing subsequence.

**Problem 8**: Large Number Multiplication -- multiply two numbers with thousands of digits efficiently.

**Problem 9**: Minimum Meeting Rooms -- given meetings, find the minimum number of rooms needed.

**Problem 10**: Edit Distance -- minimum insertions, deletions, and replacements to transform one string into another.

<br>

Think about each one before moving to the next slide...

---

# Ex 2: Answers (6-10)

| # | Problem | Paradigm | Reasoning |
|---|---------|----------|-----------|
| 6 | Permutation in String | **Brute Force** (sliding window) | Check all windows of size len(s1) |
| 7 | LIS | **DP** | dp[i] = length of LIS ending at index i |
| 8 | Large Number Multiply | **D&C** | Karatsuba: split digits, 3 multiplications. O(n^1.585) |
| 9 | Min Meeting Rooms | **Greedy** | Event sweep: +1 at start, -1 at end, track max |
| 10 | Edit Distance | **DP** | 2D table like LCS. dp[i][j] = min ops for prefixes |

---

# Ex 2: Paradigm Decision Flowchart

```
         Read the problem
              |
              v
     Are constraints small?
    (n <= a few hundred)
         /         \
       YES          NO
        |            |
        v            v
   Brute Force   Can you split into
                 INDEPENDENT subproblems?
                    /          \
                  YES           NO
                   |             |
                   v             v
              Divide &     Does a local optimum
              Conquer      lead to a global optimum?
                              /          \
                            YES           NO
                             |             |
                             v             v
                          Greedy    Overlapping subproblems
                                   + optimal substructure?
                                        |
                                        v
                                       DP
```

---
layout: section
---

# Ex 3
## First-Half Review Problems

---

# Ex 3: Review -- Problem Overview

**Objective**: Review key algorithms from Weeks 02-06 through 5 mini problems.

| # | Topic | Related Week | Core Concept |
|---|-------|--------------|--------------|
| 1 | Complexity Analysis | Week 02 | Nested loop analysis |
| 2 | Sorting | Week 03 | Merge Sort implementation |
| 3 | Divide & Conquer | Week 04 | Recursive max finding |
| 4 | Greedy | Week 05 | Activity Selection |
| 5 | DP | Week 06 | Climbing Stairs |

### How to Proceed

1. Open `examples/ex3_review_problems.py`
2. Implement each skeleton function yourself
3. Compare with the provided solution
4. If short on time, reading and understanding the solutions is also effective

Run: `python examples/ex3_review_problems.py`

---

# Ex 3: Problem 1 -- Complexity Analysis (Week 02)

**Problem**: What is the time complexity of this function?

```python
def mystery(n):
    count = 0
    i = 1
    while i < n:        # How many times does this run?
        j = 0
        while j < n:    # How many times does this run?
            count += 1
            j += 1
        i *= 2           # <-- key: i doubles each iteration
    return count
```

**Questions**:
- (a) What is the Big-O time complexity of `mystery(n)`?
- (b) What is `mystery(16)`?

---

# Ex 3: Problem 1 -- Solution

```
Outer loop: i = 1, 2, 4, 8, ..., until i >= n
            i doubles each time -> runs O(log n) times

Inner loop: j = 0, 1, 2, ..., n-1
            runs O(n) times per outer iteration

Total: O(n) * O(log n) = O(n log n)
```

### mystery(16):

```
i = 1:   j loops 0..15  -> 16 iterations
i = 2:   j loops 0..15  -> 16 iterations
i = 4:   j loops 0..15  -> 16 iterations
i = 8:   j loops 0..15  -> 16 iterations
i = 16:  while condition fails, loop ends

count = 16 * 4 = 64
```

**Answer**: (a) **O(n log n)** &nbsp;&nbsp; (b) **64**

---

# Ex 3: Problem 2 -- Merge Sort (Week 03)

**Problem**: Implement Merge Sort and count the number of merge operations.

```python
def merge_sort(arr):
    """Returns (sorted_array, merge_count)."""
    if len(arr) <= 1:
        return arr[:], 0

    mid = len(arr) // 2
    left, lc = merge_sort(arr[:mid])
    right, rc = merge_sort(arr[mid:])

    # Merge step
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:      # <= for stability
            merged.append(left[i]); i += 1
        else:
            merged.append(right[j]); j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])

    return merged, lc + rc + 1
```

```
Input:  [38, 27, 43, 3, 9, 82, 10]
Output: [3, 9, 10, 27, 38, 43, 82]  (6 merges)
```

---

# Ex 3: Problem 3 -- Divide & Conquer Max (Week 04)

**Problem**: Find the maximum value in an array using divide and conquer.

```python
def find_max_dc(arr):
    """Returns (max_value, comparison_count)."""
    comparisons = [0]

    def helper(a, lo, hi):
        if lo == hi:
            return a[lo]
        mid = (lo + hi) // 2
        left_max = helper(a, lo, mid)
        right_max = helper(a, mid + 1, hi)
        comparisons[0] += 1
        return left_max if left_max >= right_max else right_max

    return helper(arr, 0, len(arr) - 1), comparisons[0]
```

```
Input: [3, 7, 2, 9, 1, 8, 4, 6, 5]
Max: 9,  Comparisons: 8 (= n - 1, which is optimal)

Recurrence: T(n) = 2T(n/2) + 1  ->  O(n)
```

---

# Ex 3: Problem 4 -- Activity Selection (Week 05)

**Problem**: Given lectures with (start, end), find the maximum number that fit in one room.

```python
def activity_selection(lectures):
    """Returns (count, selected_indices)."""
    indexed = [(end, start, i) for i, (start, end) in enumerate(lectures)]
    indexed.sort()                  # sort by end time

    selected = []
    last_end = -1
    for end, start, idx in indexed:
        if start >= last_end:
            selected.append(idx)
            last_end = end
    return len(selected), selected
```

```
Lectures: [(1,3),(2,5),(3,6),(5,7),(6,8),(8,10),(9,11)]

Selected: (1,3) -> (5,7) -> (8,10) = 3 lectures
```

**Key**: Sort by end time, greedily pick non-overlapping. O(n log n).

---

# Ex 3: Problem 5 -- Climbing Stairs (Week 06)

**Problem**: n stairs, each with a cost. You can climb 1 or 2 stairs at a time. Start from stair 0 or 1. Find the minimum cost to reach the top.

```python
def min_cost_climbing(cost):
    n = len(cost)
    if n <= 1:
        return cost[0] if n == 1 else 0

    prev2 = cost[0]        # dp[0]
    prev1 = cost[1]        # dp[1]

    for i in range(2, n):
        current = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, current

    return min(prev1, prev2)    # can reach top from last or second-to-last
```

```
cost = [10, 15, 20]           -> min cost: 15
cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1] -> min cost: 6
```

**Recurrence**: dp[i] = cost[i] + min(dp[i-1], dp[i-2])

**Time**: O(n) &nbsp;&nbsp; **Space**: O(1) with optimization

---
layout: section
---

# Wrap-Up

---

# Exam Review Cheat Sheet

| Week | Topic | Key Algorithms | Complexity |
|------|-------|---------------|------------|
| 02 | Complexity | Big-O, loop analysis | -- |
| 03 | Sorting | Merge Sort, Quick Sort | O(n log n) |
| 04 | D&C | Binary Search, Closest Pair | O(log n), O(n log n) |
| 05 | Greedy | Activity Selection, Huffman, Fractional Knapsack | O(n log n) |
| 06 | DP | Fibonacci, LCS, 0-1 Knapsack | O(n), O(mn), O(nW) |

### Exam Tips

```
1. Complexity: Watch for i *= 2 (log n) vs i += 1 (n) patterns
2. Sorting:    Know time/space complexity AND stability of each sort
3. D&C:        Write the recurrence -> apply Master Theorem
4. Greedy:     Explain WHY the greedy choice property holds
5. DP:         Define subproblem -> recurrence -> base case -> fill order
```

<br>

### Homework 6

See `../3_assignment/README.md` for assignment details.

### Good luck on the midterm!
