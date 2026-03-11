---
theme: default
title: "Week 05 Lab — Greedy Algorithms"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 05 Lab
## Greedy Algorithms

Algorithms Lab

---
layout: section
---

# Overview

---

# Today's Objectives

- Experimentally verify the **success and failure** conditions of greedy algorithms
- Experience how greedy strategies are applied to **real scheduling** problems

<br>

### Lab Structure

| Section | Topic | Time |
|---------|-------|------|
| **A-1** | Coin Change (greedy success/failure) | 10 min |
| **A-2** | Fractional Knapsack | 10 min |
| **A-3** | Huffman Coding | 15 min |
| **B-1** | Meeting Room Reservation System | 15 min |

---
layout: section
---

# Type A -- Algorithm Implementation

---
layout: section
---

# A-1
## Coin Change

---

# A-1: Coin Change -- Problem

**Goal**: Observe when the greedy approach works and when it fails.

### Case 1: Greedy succeeds

```
Coins: [500, 100, 50, 10]    Amount: 1260

Greedy strategy: always pick the largest coin possible
  500 -> 500 -> 100 -> 100 -> 50 -> 10
  = 6 coins  (this IS optimal)
```

### Case 2: Greedy fails

```
Coins: [1, 3, 4]    Amount: 6

Greedy: pick largest first
  4 -> 1 -> 1 = 3 coins

Optimal (DP):
  3 -> 3     = 2 coins  <-- fewer coins!
```

**Why does greedy fail?** The coins are not in a divisor relationship -- picking the locally best coin can block a globally better combination.

---

# A-1: Coin Change -- Greedy Code

```python
def coin_change_greedy(amount, coins):
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount
    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin
    return result if remaining == 0 else None
```

Run: `python examples/solutions/a1_coin_change.py`

---

# A-1: Coin Change -- DP Comparison

```python
def coin_change_dp(amount, coins):
    """DP solution -- always finds optimal answer."""
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)
    for i in range(1, amount + 1):
        for c in coins:
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                parent[i] = c
    # Backtrack to find coins used
    result = []
    cur = amount
    while cur > 0:
        result.append(parent[cur])
        cur -= parent[cur]
    return result
```

### Key takeaway

| Coin set | Greedy | DP | Same? |
|----------|--------|----|-------|
| [500, 100, 50, 10] | Optimal | Optimal | Yes |
| [1, 3, 4] | 3 coins | **2 coins** | **No** |

Greedy works when coins have the **divisor property** (each coin divides the next larger one).

---
layout: section
---

# A-2
## Fractional Knapsack

---

# A-2: Fractional Knapsack -- Problem

**Problem**: Given items with weights and values, maximize total value in a knapsack of limited capacity. Items **can be split**.

```
Knapsack capacity: 50 kg

Item      Weight    Value    Value/kg
--------------------------------------
A         10 kg     60       6.0
B         20 kg     100      5.0
C         30 kg     120      4.0
```

**Greedy strategy**: Sort by value-per-weight ratio (descending), then fill greedily.

```
Step 1: Take all of A  (10 kg, value 60)   remaining: 40 kg
Step 2: Take all of B  (20 kg, value 100)  remaining: 20 kg
Step 3: Take 2/3 of C  (20 kg, value 80)   remaining: 0 kg
                                   Total value: 240
```

---

# A-2: Fractional Knapsack -- Solution

```python
def fractional_knapsack(capacity, items):
    # Sort by value/weight ratio (descending)
    sorted_items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)
    total_value = 0.0
    remaining = capacity

    for name, weight, value in sorted_items:
        if remaining <= 0:
            break
        if weight <= remaining:
            # Take the whole item
            total_value += value
            remaining -= weight
        else:
            # Take a fraction
            fraction = remaining / weight
            total_value += value * fraction
            remaining = 0

    return total_value
```

Run: `python examples/solutions/a2_fractional_knapsack.py`

---

# A-2: Fractional vs 0-1 Knapsack

```
                 Fractional              0-1 Knapsack
                 (can split)             (all or nothing)
              +-----------------+     +-----------------+
              | Greedy works!   |     | Greedy FAILS    |
              | O(n log n)      |     | Need DP: O(nW)  |
              +-----------------+     +-----------------+
                  value: 240              value: 220

Why the difference?
  Fractional: "How much to take?" -> continuous choice
  0-1:        "Take or skip?"     -> discrete choice
```

### Why greedy is optimal for fractional knapsack

- Picking the highest ratio first is always at least as good as any alternative
- If you can split items, there is no "wasted capacity" dilemma
- **Time complexity**: O(n log n) -- dominated by sorting

---
layout: section
---

# A-3
## Huffman Coding

---

# A-3: Huffman Coding -- Problem

**Problem**: Given character frequencies, build an optimal prefix-free binary code.

```
Text: "abracadabra"

Character frequencies:
  'a': 5    'b': 2    'r': 2    'c': 1    'd': 1
```

**Greedy strategy**: Repeatedly merge the two lowest-frequency nodes.

```
Step 1: Merge 'c'(1) + 'd'(1) = [2]
Step 2: Merge 'b'(2) + 'r'(2) = [4]
Step 3: Merge [2]   + [4]     = [6]
Step 4: Merge 'a'(5) + [6]    = [11]
```

### Key property: Prefix-free code

No codeword is a prefix of another, so decoding is unambiguous without delimiters.

---

# A-3: Huffman Tree

```
              [11]
             /    \
          (0)      (1)
          /          \
       'a'(5)       [6]
                   /    \
                (0)      (1)
                /          \
             [2]           [4]
            /   \         /   \
         (0)   (1)     (0)   (1)
         /       \     /       \
      'c'(1)  'd'(1) 'b'(2)  'r'(2)
```

### Resulting codes

| Char | Freq | Code | Bits |
|------|------|------|------|
| a | 5 | `0` | 1 |
| b | 2 | `110` | 3 |
| r | 2 | `111` | 3 |
| c | 1 | `100` | 3 |
| d | 1 | `101` | 3 |

High frequency = short code, low frequency = long code.

---

# A-3: Huffman Coding -- Core Code

```python
import heapq

class HuffmanNode:
    def __init__(self, char=None, freq=0, left=None, right=None):
        self.char, self.freq = char, freq
        self.left, self.right = left, right
    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(freq_table):
    heap = [HuffmanNode(char=c, freq=f) for c, f in freq_table.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        left = heapq.heappop(heap)      # lowest freq
        right = heapq.heappop(heap)     # 2nd lowest
        merged = HuffmanNode(
            freq=left.freq + right.freq,
            left=left, right=right)
        heapq.heappush(heap, merged)
    return heapq.heappop(heap)

def generate_codes(root, prefix="", codes=None):
    if codes is None: codes = {}
    if root.char is not None:           # leaf node
        codes[root.char] = prefix or "0"
        return codes
    generate_codes(root.left, prefix + "0", codes)
    generate_codes(root.right, prefix + "1", codes)
    return codes
```

Run: `python examples/solutions/a3_huffman.py`

---

# A-3: Huffman -- Compression Results

```
Text: "abracadabra" (11 chars)

                    Bits     Bits/char
-------------------------------------
ASCII (8-bit):      88       8.000
Fixed-length (3b):  33       3.000
Huffman:            23       2.091
Entropy (lower bd): 21.2     1.927
```

### Why is Huffman greedy?

- At each step, merge the **two least frequent** nodes
- This locally optimal choice leads to a globally optimal prefix code
- Proven optimal among all prefix-free codes

### Time complexity: O(n log n)

- n = number of distinct characters
- Each heap operation is O(log n), performed n-1 times

---
layout: section
---

# Type B -- Web Code Analysis

---
layout: section
---

# B-1
## Meeting Room Reservation System

---

# B-1: Meeting Room Scheduler -- Problem

Run the Flask app:

```bash
cd examples/solutions/b1_web_scheduler
python app.py
```

**Problem**: Given a list of meeting requests with start/end times, find the **maximum number of non-overlapping meetings** that can be scheduled.

```
Meeting requests:
  A: [1, 4)    B: [3, 5)    C: [0, 6)
  D: [5, 7)    E: [3, 9)    F: [5, 9)
  G: [6, 8)    H: [8, 11)   I: [8, 12)

Timeline:
  A: |===|
  B:   |==|
  C: |======|
  D:     |==|
  E:   |======|
  F:     |====|
  G:      |==|
  H:        |===|
  I:        |====|
```

Which meetings should we select to maximize the count?

---

# B-1: Activity Selection -- Solution

**Greedy strategy**: Sort by **end time**, then greedily pick non-overlapping activities.

```
Sorted by end time:
  A: [1,4)  B: [3,5)  C: [0,6)  D: [5,7)  G: [6,8)
  E: [3,9)  F: [5,9)  H: [8,11)  I: [8,12)

Selection process:
  Pick A [1,4)    last_end = 4
  Skip B [3,5)    3 < 4, overlaps
  Skip C [0,6)    0 < 4, overlaps
  Pick D [5,7)    5 >= 4, OK!  last_end = 7
  Skip G [6,8)    6 < 7, overlaps
  Skip E [3,9)    3 < 7, overlaps
  Skip F [5,9)    5 < 7, overlaps
  Pick H [8,11)   8 >= 7, OK!  last_end = 11
  Skip I [8,12)   8 < 11, overlaps

Result: {A, D, H} = 3 meetings
```

---

# B-1: Activity Selection -- Code

```python
def activity_selection(meetings):
    """Select maximum non-overlapping meetings.

    Args: meetings = [(start, end), ...]
    Returns: list of selected meeting indices
    """
    # Sort by end time
    indexed = sorted(enumerate(meetings), key=lambda x: x[1][1])

    selected = []
    last_end = -1

    for idx, (start, end) in indexed:
        if start >= last_end:
            selected.append(idx)
            last_end = end

    return selected
```

### Why sorting by end time works

- Choosing the meeting that **finishes earliest** leaves the most room for future meetings
- This greedy choice property is provably optimal
- **Time complexity**: O(n log n) for sorting

---
layout: section
---

# Wrap-Up

---

# Summary

### What we learned today

- **Coin Change**: Greedy works for standard denominations but fails for arbitrary coin sets
- **Fractional Knapsack**: Greedy by value/weight ratio is optimal when items can be split
- **Huffman Coding**: Greedy merging of lowest-frequency nodes produces optimal prefix codes
- **Activity Selection**: Sorting by end time and greedily picking gives maximum non-overlapping set

### When does greedy work?

```
Greedy works when:
  1. Greedy Choice Property -- a locally optimal choice
     is part of a globally optimal solution
  2. Optimal Substructure -- after making a greedy choice,
     the remaining subproblem is also optimally solvable
```

<br>

### Homework 4

See `../3_assignment/README.md` for assignment details.

### Next week

**Week 06**: Dynamic Programming -- when greedy is not enough!
