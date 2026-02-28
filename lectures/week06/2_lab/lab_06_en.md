---
theme: default
title: "Week 06 Lab — Dynamic Programming"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 06 Lab
## Dynamic Programming

Algorithms Lab

---
layout: section
---

# Overview

---

# Today's Objectives

- Understand and implement the core DP patterns: **memoization** and **tabulation**
- Analyze real-world examples of how DP is used in **web applications**

<br>

### Lab Structure

| Section | Topic | Time |
|---------|-------|------|
| **A-1** | Fibonacci Comparison | 10 min |
| **A-2** | LCS + DP Table Visualization | 15 min |
| **A-3** | 0-1 Knapsack + Backtracking | 10 min |
| **B-1** | Text Diff Viewer | 15 min |

---
layout: section
---

# Type A -- Algorithm Implementation

---
layout: section
---

# A-1
## Fibonacci Comparison

---

# A-1: Fibonacci -- Problem

**Goal**: Compare three approaches to computing Fibonacci numbers.

```
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2)   for n >= 2
```

### Why is naive recursion so slow?

```
                    F(5)
                   /    \
               F(4)      F(3)
              /    \     /    \
          F(3)   F(2)  F(2)  F(1)
         /   \   / \   / \
       F(2) F(1) ...  ...
       / \
     F(1) F(0)

Overlapping subproblems!  F(3) computed 2 times, F(2) computed 3 times...
Total calls for F(n): O(2^n)
```

---

# A-1: Fibonacci -- Three Approaches

```python
# 1. Naive recursion: O(2^n) -- exponentially slow
def fib_naive(n):
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)

# 2. Memoization (top-down): O(n) -- cache results
def fib_memo(n, memo=None):
    if memo is None: memo = {}
    if n in memo: return memo[n]
    if n <= 1: return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]

# 3. Tabulation (bottom-up): O(n) -- fill table iteratively
def fib_tab(n):
    if n <= 1: return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]
```

Run: `python examples/fibonacci.py`

---

# A-1: Fibonacci -- Performance Results

```
  N   |     Naive      |     Memo       |  Tabulation
------+--------------+----------------+----------------
  10  |   0.000005s  |   0.000003s    |   0.000002s
  20  |   0.001200s  |   0.000004s    |   0.000002s
  30  |   0.150000s  |   0.000005s    |   0.000003s
  35  |   1.800000s  |   0.000005s    |   0.000003s
  40  |   too slow   |   0.000006s    |   0.000003s
```

*(Approximate -- your results will vary)*

### Key comparison

| Approach | Time | Space | Direction |
|----------|------|-------|-----------|
| Naive recursion | O(2^n) | O(n) stack | -- |
| Memoization | O(n) | O(n) cache + stack | Top-down |
| Tabulation | O(n) | O(n) table | Bottom-up |

**Memoization** = recursion + caching. **Tabulation** = iterative table-filling.
Both eliminate overlapping subproblems. Tabulation avoids recursion overhead.

---
layout: section
---

# A-2
## LCS + DP Table Visualization

---

# A-2: LCS -- Problem

**Problem**: Find the Longest Common Subsequence of two strings.

A **subsequence** preserves order but not necessarily contiguity.

```
X = "ABCBDAB"
Y = "BDCAB"

Common subsequences: "B", "AB", "BD", "BCB", "BCAB", ...
Longest: "BCAB" (length 4)

X: A B C B D A B
       ^   ^   ^ ^
Y: B D C A B
   ^   ^ ^ ^
```

### Recurrence

```
If X[i] == Y[j]:   dp[i][j] = dp[i-1][j-1] + 1   (match!)
If X[i] != Y[j]:   dp[i][j] = max(dp[i-1][j], dp[i][j-1])
```

**Time**: O(m * n) &nbsp;&nbsp; **Space**: O(m * n)

---

# A-2: LCS -- DP Table

```
X = "ABCBDAB",  Y = "BDCAB"

          ""   B    D    C    A    B
          0    1    2    3    4    5
    ----------------------------------
 "" 0 |   0    0    0    0    0    0
  A 1 |   0    0    0    0   [1]   1
  B 2 |   0   [1]   1    1    1    1
  C 3 |   0    1    1   [2]   2    2
  B 4 |   0    1    1    2    2   [3]
  D 5 |   0    1   (2)   2    2    3
  A 6 |   0    1    2    2   (3)   3
  B 7 |   0    1    2    2    3   [4]

  [n] = match (diagonal move, included in LCS)
  (n) = backtrack path
```

**LCS = "BCAB"** (length 4)

---

# A-2: LCS -- Solution Code

```python
def build_lcs_table(x, y):
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp

def backtrack_lcs(dp, x, y):
    lcs = []
    i, j = len(x), len(y)
    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs.append(x[i - 1])
            i -= 1; j -= 1          # diagonal
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1                   # up
        else:
            j -= 1                   # left
    return "".join(reversed(lcs))
```

Run: `python examples/lcs.py`

---

# A-2: LCS -- Backtracking Visualization

```
Start at dp[7][5] = 4, trace back to dp[0][0]:

  (7,5): X[7]='B' == Y[5]='B' -> diagonal (MATCH: 'B')
  (6,4): X[6]='A' == Y[4]='A' -> diagonal (MATCH: 'A')
  (5,3): X[5]='D' != Y[3]='C' -> up  (dp[4][3]=2 >= dp[5][2]=1)
  (4,4): was (5,3)->up->(4,3)
         X[4]='B' != Y[3]='C' -> left... (continuing trace)
  ...eventually:
  (3,3): X[3]='C' == Y[3]='C' -> diagonal (MATCH: 'C')
  (2,1): X[2]='B' == Y[1]='B' -> diagonal (MATCH: 'B')

Collected (reversed): B -> C -> A -> B = "BCAB"
```

### Applications of LCS

- **git diff** -- comparing file versions line by line
- **DNA sequence alignment** -- comparing genetic sequences
- **Edit distance** -- minimum edits to transform one string into another

---
layout: section
---

# A-3
## 0-1 Knapsack + Backtracking

---

# A-3: 0-1 Knapsack -- Problem

**Problem**: Select items to maximize value without exceeding capacity. Items **cannot be split** (take it or leave it).

```
Capacity: 50

Item       Value   Weight
--------------------------
Laptop      60      10
Camera     100      20
Painting   120      30
Book        40       5
```

### Recurrence

```
dp[i][j] = maximum value using first i items with capacity j

If weight_i > j:   dp[i][j] = dp[i-1][j]          (can't take item i)
Otherwise:         dp[i][j] = max(
                       dp[i-1][j],                  (skip item i)
                       dp[i-1][j - weight_i] + v_i  (take item i)
                   )
```

Which items should we pick?

---

# A-3: 0-1 Knapsack -- DP Table & Backtracking

```
          Capacity ->  0   5  10  15  20  25  30  35  40  45  50
          ---------------------------------------------------------
(none)  0 |            0   0   0   0   0   0   0   0   0   0   0
Laptop  1 |            0   0  60  60  60  60  60  60  60  60  60
Camera  2 |            0   0  60  60 100 100 160 160 160 160 160
Paint.  3 |            0   0  60  60 100 100 160 160 180 180 220
Book    4 |            0  40  60 100 100 140 140 200 200 220 220

Answer: dp[4][50] = 220

Backtrack from dp[4][50]:
  dp[4][50]=220 != dp[3][50]=220 -> skip Book?
  Wait: dp[4][50]=220 == dp[3][50]=220 -> skip Book
  dp[3][50]=220 != dp[2][50]=160 -> TAKE Painting (j: 50->20)
  dp[2][20]=100 != dp[1][20]=60  -> TAKE Camera   (j: 20->0)
  dp[1][0]=0 == dp[0][0]=0      -> skip Laptop

Selected: Camera (100, 20kg) + Painting (120, 30kg) = 220
```

---

# A-3: 0-1 Knapsack -- Solution Code

```python
def knapsack_01(capacity, items):
    """items: list of (value, weight, name)
       Returns: max value, selected items."""
    n = len(items)
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        v, w, _ = items[i - 1]
        for j in range(capacity + 1):
            dp[i][j] = dp[i - 1][j]           # skip
            if w <= j and dp[i - 1][j - w] + v > dp[i][j]:
                dp[i][j] = dp[i - 1][j - w] + v  # take

    # Backtrack to find selected items
    selected = []
    j = capacity
    for i in range(n, 0, -1):
        if dp[i][j] != dp[i - 1][j]:
            selected.append(items[i - 1])
            j -= items[i - 1][1]               # subtract weight

    return dp[n][capacity], list(reversed(selected))
```

Run: `python examples/knapsack.py`

**Time**: O(n * W) &nbsp;&nbsp; **Space**: O(n * W) &nbsp;&nbsp; (W = capacity)

---
layout: section
---

# Type B -- Web Code Analysis

---
layout: section
---

# B-1
## Text Diff Viewer

---

# B-1: Text Diff Viewer -- Setup

Run the Flask app:

```bash
cd examples/web_diff
python app.py
```

Enter two texts and the app highlights the differences based on **LCS**.

```
  Text A: "The quick brown fox"
  Text B: "The slow brown dog"

  Diff output:
    "The "
    [-quick-] [+slow+]
    " brown "
    [-fox-] [+dog+]
```

This is the same principle behind **GitHub's diff feature**.

---

# B-1: How Diff Works

```
1. Split texts into tokens (words or lines)
2. Compute LCS of the two token sequences
3. Tokens in LCS      -> unchanged (white)
   Tokens only in A   -> deleted   (red)
   Tokens only in B   -> inserted  (green)

  Text A tokens: [The, quick, brown, fox]
  Text B tokens: [The, slow,  brown, dog]

  LCS: [The, brown]

  Alignment:
    The    The      <- same (LCS)
    quick  ---      <- deleted
    ---    slow     <- inserted
    brown  brown    <- same (LCS)
    fox    ---      <- deleted
    ---    dog      <- inserted
```

### Experiment

- Try short sentences with a few word changes
- Try longer paragraphs -- observe how LCS captures the common structure
- Think about why this is O(m * n) where m, n are the token counts

---
layout: section
---

# Wrap-Up

---

# Summary

### What we learned today

- **Fibonacci**: Naive O(2^n) vs memoization/tabulation O(n) -- eliminating overlapping subproblems
- **LCS**: 2D DP table + backtracking to recover the actual subsequence
- **0-1 Knapsack**: DP table construction + backtracking to find selected items
- **Text Diff**: LCS applied to a real web application (like GitHub diff)

### The DP Recipe

```
1. Define the subproblem   -- what does dp[i][j] represent?
2. Write the recurrence    -- how does dp[i][j] relate to smaller subproblems?
3. Identify base cases     -- dp[0][...] = ?, dp[...][0] = ?
4. Determine fill order    -- usually left-to-right, top-to-bottom
5. Backtrack if needed     -- recover the actual solution, not just the value
```

<br>

### Homework 5 (Final Assignment)

See `homework/README.md` for assignment details.

### Next week

**Week 07**: Midterm Exam Preparation -- review everything from Weeks 02-06!
