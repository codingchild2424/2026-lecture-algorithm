# === Ex 2: Algorithm Paradigm Identification Practice ===
# Week 07 Midterm Review - Algorithm paradigm identification training
# Practice identifying Brute Force, Divide & Conquer, Greedy, and DP paradigms through 10 problems
"""
Algorithm Paradigm Identification Practice

Read 10 algorithm problems and identify the appropriate paradigm for each.
Paradigms: Brute Force / Divide & Conquer / Greedy / Dynamic Programming

First read the problems and identify on your own, then check the solutions below.
"""


# ============================================================
#  Problems
#  Read each problem and think about which paradigm to use.
# ============================================================

# PROBLEMS list: 10 algorithm problems stored as dictionaries
# Each problem has id, title, and description fields
PROBLEMS = [
    {
        "id": 1,
        "title": "Two Sum in an Array",
        "description": """
Given an integer array nums and an integer target,
find all pairs of numbers in the array that sum to target.
The array size is at most 100.
""",
    },
    {
        "id": 2,
        "title": "Maximum Subarray Sum",
        "description": """
Given an integer array, find the maximum sum among all contiguous subarrays.
Example: [-2, 1, -3, 4, -1, 2, 1, -5, 4] -> Answer: 6 (subarray [4, -1, 2, 1])
""",
    },
    {
        "id": 3,
        "title": "Closest Pair of Points",
        "description": """
Given n points on a 2D plane,
find the pair of points with the smallest Euclidean distance.
n is at most 100,000.
""",
    },
    {
        "id": 4,
        "title": "Minimum Coin Change",
        "description": """
Given coin denominations coins = [1, 5, 7, 10] and an amount,
find the minimum number of coins needed to make the amount.
""",
    },
    {
        "id": 5,
        "title": "Activity Selection",
        "description": """
Given n activities with start and end times,
find the maximum number of activities a single person can perform.
(Activities must not overlap in time.)
""",
    },
    {
        "id": 6,
        "title": "String Permutation Check",
        "description": """
Given two strings s1 and s2,
determine whether s2 contains a permutation of s1 as a substring.
Example: s1 = "ab", s2 = "eidbaooo" -> True ("ba" is a permutation of s1)
""",
    },
    {
        "id": 7,
        "title": "Longest Increasing Subsequence (LIS)",
        "description": """
Given an integer array, find the length of the longest increasing subsequence.
Example: [10, 9, 2, 5, 3, 7, 101, 18] -> Answer: 4 ([2, 3, 7, 101])
""",
    },
    {
        "id": 8,
        "title": "Large Number Multiplication",
        "description": """
Efficiently multiply two very large integers (thousands of digits).
Standard multiplication is O(n^2), but can we do better?
""",
    },
    {
        "id": 9,
        "title": "Minimum Number of Meeting Rooms",
        "description": """
Given n meetings with start and end times,
find the minimum number of meeting rooms needed to schedule all meetings.
""",
    },
    {
        "id": 10,
        "title": "Edit Distance",
        "description": """
Given two strings word1 and word2,
find the minimum number of operations to convert word1 to word2.
Allowed operations: insert, delete, replace (each with cost 1)
""",
    },
]


# ============================================================
#  Solutions
#  Provide the appropriate paradigm and rationale for each problem
# ============================================================

SOLUTIONS = [
    {
        "id": 1,
        "paradigm": "Brute Force",
        "explanation": """
Since the array size is at most 100, checking all pairs is O(n^2) = 10,000 operations, which is sufficient.
A hash map can achieve O(n), but brute force is also appropriate at this scale.
Key: when constraints are small (n <= 100), consider brute force first.
""",
    },
    {
        "id": 2,
        "paradigm": "Dynamic Programming (or Divide & Conquer)",
        "explanation": """
DP solution (Kadane's Algorithm):
  dp[i] = max(arr[i], dp[i-1] + arr[i])
  "Maximum subarray sum ending at the i-th element"
  O(n) time, O(1) space.

Divide and conquer solution is also possible:
  Split the array in half and select the maximum among left/right/crossing cases.
  O(n log n) time.

Both paradigms are applicable, but DP is more efficient.
""",
    },
    {
        "id": 3,
        "paradigm": "Divide & Conquer",
        "explanation": """
A classic divide and conquer problem.
  1. Sort points by x-coordinate and split in half
  2. Find the minimum distance in each half
  3. Handle the boundary-crossing case in O(n) or O(n log n)
  Overall O(n log n).

Brute force is O(n^2), which is too slow for n=100,000.
""",
    },
    {
        "id": 4,
        "paradigm": "Dynamic Programming",
        "explanation": """
Since coins like [1, 5, 7, 10] are not in a multiple relationship, greedy fails.
Example: for amount=14, greedy gives 10+1+1+1+1 = 5 coins, optimal is 7+7 = 2 coins.

DP solution:
  dp[i] = min(dp[i - coin] + 1) for each coin
  O(amount * k) time (k = number of coin types)

Key: when the greedy choice property does not hold, use DP.
""",
    },
    {
        "id": 5,
        "paradigm": "Greedy",
        "explanation": """
A classic greedy problem (Activity Selection).
  1. Sort by end time
  2. Greedily select non-overlapping activities in order
  O(n log n) time.

The greedy choice property is proven:
"Selecting the activity with the earliest end time is always part of an optimal solution."
""",
    },
    {
        "id": 6,
        "paradigm": "Brute Force (Sliding Window)",
        "explanation": """
An O(n) solution is possible using the sliding window technique.
  - Slide a window of length len(s1) over s2
  - Check if the character frequency within the window matches s1's frequency

Strictly speaking, this is a sliding window, but it is essentially
an optimized version of brute force that "checks all positions."
It does not fall under DaC/Greedy/DP.
""",
    },
    {
        "id": 7,
        "paradigm": "Dynamic Programming",
        "explanation": """
LIS (Longest Increasing Subsequence) is a classic DP problem.

O(n^2) solution:
  dp[i] = length of LIS ending at the i-th element
  dp[i] = max(dp[j] + 1) for j < i where arr[j] < arr[i]

O(n log n) solution:
  Optimization using binary search (patience sorting)

Key: "previous choices affect future choices," so DP is needed.
""",
    },
    {
        "id": 8,
        "paradigm": "Divide & Conquer",
        "explanation": """
Karatsuba algorithm - divide and conquer.
  Split large numbers in half and solve with 3 multiplications.
  Time complexity: O(n^1.585) (standard multiplication is O(n^2))

  x = a * 10^(n/2) + b
  y = c * 10^(n/2) + d
  xy = ac * 10^n + ((a+b)(c+d) - ac - bd) * 10^(n/2) + bd

Key: divide the problem into independent subproblems and solve recursively.
""",
    },
    {
        "id": 9,
        "paradigm": "Greedy",
        "explanation": """
Event sweep + greedy.
  1. Sort start/end events by time
  2. Increment counter at each start event, decrement at each end event
  3. Maximum counter value = minimum number of meeting rooms needed
  O(n log n) time.

Alternatively, using a min-heap:
  1. Assign new meetings to the room with the earliest end time
  2. Reuse existing rooms if possible, otherwise add a new room

Key: the greedy choice of "assigning to the room that becomes available earliest" is optimal.
""",
    },
    {
        "id": 10,
        "paradigm": "Dynamic Programming",
        "explanation": """
Edit Distance is a classic DP problem.

dp[i][j] = minimum cost to transform the first i characters of word1
           into the first j characters of word2

Recurrence:
  word1[i] == word2[j]: dp[i][j] = dp[i-1][j-1]
  Different: dp[i][j] = 1 + min(
      dp[i-1][j],     # delete
      dp[i][j-1],     # insert
      dp[i-1][j-1]    # replace
  )

O(mn) time, O(mn) space.
A 2D DP with similar structure to LCS.
""",
    },
]


def print_problems():
    """Print only the problems (without solutions).

    Iterate through the PROBLEMS list and print each problem's title and description.
    Leave the answer blank so the user can identify the paradigm on their own.
    """
    print("=" * 65)
    print(" Algorithm Paradigm Identification Practice")
    print(" Read each problem and choose the appropriate paradigm.")
    print(" Paradigms: Brute Force / Divide & Conquer / Greedy / DP")
    print("=" * 65)

    for p in PROBLEMS:
        print(f"\n--- Problem {p['id']}: {p['title']} ---")
        print(p["description"].strip())
        print(f"  -> Your answer: _______________")


def print_solutions():
    """Print the solutions.

    Print the correct paradigm and detailed explanation for each problem.
    Includes why the paradigm is appropriate, time complexity, etc.
    """
    print("\n" + "=" * 65)
    print(" Solutions")
    print("=" * 65)

    for s in SOLUTIONS:
        p = PROBLEMS[s["id"] - 1]
        print(f"\n--- Problem {s['id']}: {p['title']} ---")
        print(f"  Answer: {s['paradigm']}")
        print(s["explanation"].rstrip())


def print_summary():
    """Print a summary by paradigm.

    Organize the characteristics and identification criteria of the 4 paradigms (BF, D&C, Greedy, DP).
    Provide a guide on the order to consider paradigms when approaching a problem.
    """
    print("\n" + "=" * 65)
    print(" Paradigm Identification Guide")
    print("=" * 65)
    print("""
  1. Brute Force
     - When constraints are small (n <= a few hundred)
     - "Enumerate/check all cases"
     - Default strategy when no other technique comes to mind

  2. Divide & Conquer
     - When the problem splits into independent subproblems
     - When there is no overlap between subproblems
     - When a recursive structure is natural
     - Examples: sorting, closest pair of points, large number multiplication

  3. Greedy
     - When "the best choice at each step" guarantees overall optimality
     - When the greedy choice property holds
     - When there is no need to backtrack after making a choice
     - Examples: activity selection, fractional knapsack, Huffman coding

  4. Dynamic Programming (DP)
     - Optimal substructure + overlapping subproblems
     - When "previous choices affect future ones"
     - When a recurrence relation can be formulated
     - Examples: LCS, 0-1 knapsack, edit distance, LIS

  Identification order:
     Read the problem -> Check constraints (small -> BF)
     -> Can it be independently divided? (D&C)
     -> Best at each step = globally best? (Greedy)
     -> Overlapping subproblems + optimal substructure? (DP)
""")


if __name__ == "__main__":
    print_problems()

    print("\n" + "=" * 65)
    input("  Press [Enter] to see the solutions...")
    print_solutions()
    print_summary()
