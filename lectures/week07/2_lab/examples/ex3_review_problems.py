# === Ex 3: First-Half Algorithm Review -- 5 Mini Problems ===
# Week 07 Midterm Review - Reviewing key algorithms from Weeks 02-06
# Covers complexity analysis, sorting, divide & conquer, greedy, and DP with one problem each
"""
First-Half Algorithm Review -- 5 Mini Problems

Review key algorithms from Weeks 02-06, one problem per topic.
Each problem has a skeleton function and a solution function.
Try implementing the skeleton first, then compare with the solution.
"""


# ============================================================
#  Problem 1: Complexity Analysis (Week 02)
#  Analyze the time complexity of nested loops in Big-O notation
# ============================================================

def problem1_description():
    """Problem 1: Analyze the time complexity of the following function."""
    print("""
  Problem 1: Complexity Analysis (Week 02)
  ==============================
  Express the time complexity of the following function in Big-O notation.

  def mystery(n):
      count = 0
      i = 1
      while i < n:
          j = 0
          while j < n:
              count += 1
              j += 1
          i *= 2
      return count

  (a) What is the time complexity of mystery(n)?
  (b) What is the value of count for mystery(16)?
""")


def problem1_solution():
    """Problem 1 solution.

    Analysis:
    - Outer loop: i starts at 1 and doubles each time -> O(log n) iterations
    - Inner loop: j goes from 0 to n-1 -> O(n) iterations
    - Overall time complexity: O(n log n)
    """
    print("""
  Solution:
  - Outer loop: i = 1, 2, 4, 8, ..., < n  -->  O(log n) iterations
  - Inner loop: j = 0, 1, ..., n-1  -->  O(n) iterations
  - Overall: O(n log n)

  (b) mystery(16):
    i=1:  j goes 0~15 -> 16 times
    i=2:  j goes 0~15 -> 16 times
    i=4:  j goes 0~15 -> 16 times
    i=8:  j goes 0~15 -> 16 times
    i=16: loop ends
    count = 16 * 4 = 64
""")
    # Verification mystery function implementation
    def mystery(n):
        count = 0
        i = 1
        while i < n:  # Outer loop: i *= 2 so O(log n)
            j = 0
            while j < n:  # Inner loop: O(n)
                count += 1
                j += 1
            i *= 2
        return count

    result = mystery(16)
    print(f"  Verification: mystery(16) = {result}")


# ============================================================
#  Problem 2: Sorting Application (Week 03)
#  Implement Merge Sort and track the number of merges
# ============================================================

def problem2_description():
    """Problem 2: Implement Merge Sort."""
    print("""
  Problem 2: Sorting (Week 03)
  ==============================
  Implement Merge Sort.
  Count and return the number of merges during the sorting process.
""")


def problem2_skeleton(arr):
    """Merge Sort skeleton -- try implementing it yourself.

    Args:
        arr: list to sort

    Returns:
        (sorted list, number of merges)
    """
    # TODO: implement this
    pass


def problem2_solution(arr):
    """Merge Sort solution.

    Algorithm: recursively split the array in half, sort each half, then merge
    Time complexity: O(n log n) - O(log n) splits * O(n) merge
    Space complexity: O(n) - temporary array needed for merging
    Stable sort: relative order of equal values is preserved (left[i] <= right[j])
    """
    merge_count = [0]  # Wrapped in a list to allow modification from inner function (closure)

    def merge_sort(a):
        """Recursively split the array.

        Base case: already sorted if length is 1 or less
        """
        if len(a) <= 1:
            return a

        mid = len(a) // 2  # Split at midpoint
        left = merge_sort(a[:mid])   # Recursively sort left half
        right = merge_sort(a[mid:])  # Recursively sort right half

        return merge(left, right)  # Merge the two sorted arrays

    def merge(left, right):
        """Merge two sorted arrays into one sorted array.

        Uses two-pointer technique to compare elements and append the smaller one.
        Time complexity: O(n) - n is the total length of left + right
        """
        merge_count[0] += 1
        result = []
        i = j = 0  # Pointers for left/right arrays

        # Compare and merge while both arrays have remaining elements
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:  # Using <= ensures stable sort
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # Append remaining elements to the result
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_arr = merge_sort(arr)
    return sorted_arr, merge_count[0]


# ============================================================
#  Problem 3: Divide & Conquer (Week 04)
#  Find the maximum value in an array using divide and conquer
# ============================================================

def problem3_description():
    """Problem 3: Find the maximum value in an array using divide and conquer."""
    print("""
  Problem 3: Divide & Conquer (Week 04)
  ==============================
  Find the maximum value in an integer array using divide and conquer.
  Split the array in half, find the maximum in each half, then combine.
  Also return the number of comparisons.
""")


def problem3_skeleton(arr):
    """Divide and conquer maximum skeleton -- try implementing it yourself.

    Args:
        arr: list of integers

    Returns:
        (maximum value, number of comparisons)
    """
    # TODO: implement this
    pass


def problem3_solution(arr):
    """Divide and conquer maximum solution.

    Algorithm: split the array in half, recursively find the maximum of each part,
               then compare the two maximums to determine the overall maximum
    Time complexity: O(n) - T(n) = 2T(n/2) + 1, by Master Theorem O(n)
    Number of comparisons: n - 1 (matches the theoretical minimum)
    """
    comparisons = [0]  # For tracking comparisons (closure)

    def find_max(a, lo, hi):
        """Find the maximum in the range [lo, hi] using divide and conquer.

        Base case: if there is only one element, it is the maximum
        """
        if lo == hi:
            return a[lo]

        mid = (lo + hi) // 2  # Split at midpoint
        left_max = find_max(a, lo, mid)       # Maximum of left half
        right_max = find_max(a, mid + 1, hi)  # Maximum of right half

        comparisons[0] += 1  # One comparison of left/right maximums
        return left_max if left_max >= right_max else right_max

    if not arr:
        return None, 0

    result = find_max(arr, 0, len(arr) - 1)
    return result, comparisons[0]


# ============================================================
#  Problem 4: Greedy (Week 05)
#  Activity Selection Problem
# ============================================================

def problem4_description():
    """Problem 4: Lecture Room Assignment (Activity Selection)."""
    print("""
  Problem 4: Greedy (Week 05)
  ==============================
  Given n lectures as (start_time, end_time),
  find the maximum number of lectures that can be assigned to one room.
  Also return the list of selected lectures.
""")


def problem4_skeleton(lectures):
    """Activity Selection skeleton -- try implementing it yourself.

    Args:
        lectures: [(start, end), ...] list

    Returns:
        (maximum number of lectures, list of selected lecture indices)
    """
    # TODO: implement this
    pass


def problem4_solution(lectures):
    """Activity Selection solution.

    Algorithm: sort by end time, then greedily select non-overlapping lectures
    Greedy choice property: "Selecting the activity with the earliest end time is always part of an optimal solution"
    Time complexity: O(n log n) - dominated by sorting
    Space complexity: O(n) - storing selected lecture indices
    """
    # Sort by (end_time, start_time, original_index)
    # If end times are equal, sort by earlier start time
    indexed = [(end, start, i) for i, (start, end) in enumerate(lectures)]
    indexed.sort()

    selected = []
    last_end = -1  # End time of the last selected lecture

    for end, start, idx in indexed:
        # Select if the current lecture's start time is after the last selected lecture's end time
        if start >= last_end:
            selected.append(idx)
            last_end = end  # Update end time

    return len(selected), selected


# ============================================================
#  Problem 5: DP (Week 06)
#  Climbing Stairs with Cost
# ============================================================

def problem5_description():
    """Problem 5: Climbing Stairs."""
    print("""
  Problem 5: DP (Week 06)
  ==============================
  There are n stairs, and you can climb 1 or 2 steps at a time.
  Each stair i has a cost cost[i].
  You can start from stair 0 or stair 1.
  Find the minimum cost to reach the top (position n).

  Example: cost = [10, 15, 20]
  -> Answer: 15 (start from stair 1, jump 2 steps -> cost 15)

  Example: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
  -> Answer: 6
""")


def problem5_skeleton(cost):
    """Climbing stairs skeleton -- try implementing it yourself.

    Args:
        cost: list of costs for each stair

    Returns:
        minimum cost to reach the top
    """
    # TODO: implement this
    pass


def problem5_solution(cost):
    """Climbing stairs solution.

    Algorithm: bottom-up DP to compute the minimum cost to each stair
    Recurrence: dp[i] = cost[i] + min(dp[i-1], dp[i-2])
      - To reach stair i, you can come from stair i-1 or i-2
      - Choose the one with lower cost
    Final answer: min(dp[n-1], dp[n-2]) - jump to the top from the last or second-to-last stair

    Time complexity: O(n) - single pass through the stairs
    Space complexity: O(1) - only keep the previous two values (space optimized)
    """
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    # Space optimization: keep only the previous two values instead of a dp array
    prev2 = cost[0]  # corresponds to dp[i-2]
    prev1 = cost[1]  # corresponds to dp[i-1]

    for i in range(2, n):
        current = cost[i] + min(prev1, prev2)  # Apply recurrence
        prev2, prev1 = prev1, current  # Update in sliding window fashion

    # Reach the top: jump from the last stair or the second-to-last stair
    return min(prev1, prev2)


# ============================================================
#  Main Execution
#  Present all 5 problems in order and reveal solutions
# ============================================================

if __name__ == "__main__":
    print("=" * 65)
    print(" First-Half Algorithm Review -- 5 Mini Problems")
    print("=" * 65)

    # --- Problem 1: Complexity Analysis ---
    print(f"\n{'='*65}")
    problem1_description()
    input("  Press [Enter] to see the solution...")
    problem1_solution()

    # --- Problem 2: Sorting ---
    print(f"\n{'='*65}")
    problem2_description()
    input("  Press [Enter] to see the solution...")

    test_arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr, count = problem2_solution(test_arr[:])
    print(f"  Input: {test_arr}")
    print(f"  Sorted: {sorted_arr}")
    print(f"  Merge count: {count}")

    # --- Problem 3: Divide & Conquer ---
    print(f"\n{'='*65}")
    problem3_description()
    input("  Press [Enter] to see the solution...")

    test_arr = [3, 7, 2, 9, 1, 8, 4, 6, 5]
    max_val, comparisons = problem3_solution(test_arr)
    print(f"  Input: {test_arr}")
    print(f"  Maximum: {max_val}")
    print(f"  Comparisons: {comparisons} (theoretical minimum: {len(test_arr) - 1})")

    # --- Problem 4: Greedy ---
    print(f"\n{'='*65}")
    problem4_description()
    input("  Press [Enter] to see the solution...")

    lectures = [(1, 3), (2, 5), (3, 6), (5, 7), (6, 8), (8, 10), (9, 11)]
    count, selected = problem4_solution(lectures)
    print(f"  Lecture list: {lectures}")
    print(f"  Maximum lectures: {count}")
    print(f"  Selected lectures: {[lectures[i] for i in selected]}")

    # --- Problem 5: DP ---
    print(f"\n{'='*65}")
    problem5_description()
    input("  Press [Enter] to see the solution...")

    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(f"  cost = {cost1} -> minimum cost: {problem5_solution(cost1)}")
    print(f"  cost = {cost2} -> minimum cost: {problem5_solution(cost2)}")

    # --- Summary ---
    print(f"\n{'='*65}")
    print(" Summary")
    print("=" * 65)
    print("""
  Problem 1 (Complexity):    Nested loop analysis, O(n log n)
  Problem 2 (Sorting):       Merge Sort, O(n log n), stable sort
  Problem 3 (Divide & Conquer): Array maximum, T(n) = 2T(n/2) + 1
  Problem 4 (Greedy):        Activity Selection, sort by end time
  Problem 5 (DP):            Climbing Stairs, dp[i] = cost[i] + min(dp[i-1], dp[i-2])

  Exam tips:
  - Complexity analysis: identify loop structure precisely (especially patterns like i *= 2)
  - Sorting: memorize time/space complexity and stability of each sorting algorithm
  - Divide & Conquer: formulate recurrence + apply Master Theorem
  - Greedy: be able to explain why the greedy choice property holds
  - DP: define subproblems -> recurrence -> base case -> order
""")
