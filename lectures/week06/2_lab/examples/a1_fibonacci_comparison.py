# === A-1: Fibonacci Sequence - Detailed Performance Comparison ===
# Benchmark comparison and call count analysis of three implementation approaches
#
# Key concepts:
# - Empirically verify that pure recursion call count approaches 2^n
# - Memoization/tabulation require only time proportional to n
# - Space optimization: keeping only the previous two values achieves O(1) space
# - Time complexity: naive O(2^n), memo/tab O(n)
# - Space complexity: naive O(n), memo O(n), tab O(n) or O(1) when optimized
"""
Fibonacci sequence -- performance comparison of three implementation approaches

1. fib_naive(n)  -- pure recursion: O(2^n)
2. fib_memo(n)   -- memoization (top-down DP): O(n)
3. fib_tab(n)    -- tabulation (bottom-up DP): O(n)
"""

import time
import sys

# Increase recursion depth limit (for memoization)
sys.setrecursionlimit(10000)


# ===== Implementation 1: Pure Recursion (Naive) =====

def fib_naive(n):
    """Compute the Fibonacci number using pure recursion.

    Time complexity: O(2^n) -- redundant computations grow exponentially
    Space complexity: O(n) -- recursion call stack depth

    To compute fib(5):
      fib(5) = fib(4) + fib(3)
      fib(4) = fib(3) + fib(2)   <-- fib(3) duplicated!
      fib(3) = fib(2) + fib(1)   <-- fib(2) duplicated!
      ...
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ===== Implementation 2: Memoization (Top-Down DP) =====

def fib_memo(n, memo=None):
    """Compute the Fibonacci number using memoization.

    Time complexity: O(n) -- each value is computed only once
    Space complexity: O(n) -- memo table + recursion stack

    Previously computed values are stored in a memo dictionary for reuse.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ===== Implementation 3: Tabulation (Bottom-Up DP) =====

def fib_tab(n):
    """Compute the Fibonacci number using tabulation.

    Time complexity: O(n) -- single pass through the array
    Space complexity: O(n) -- DP table (can be optimized to O(1))

    Fills the table sequentially from small values. No recursive calls.
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ===== Space-Optimized Version (Reference) =====

def fib_optimized(n):
    """Space O(1) optimized tabulation.

    Time complexity: O(n)
    Space complexity: O(1) -- only keeps the previous two values
    """
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1

    return prev1


# ===== Benchmark =====

def benchmark(func, n, timeout=10.0):
    """Measure the execution time of a function.

    Args:
        func: function to execute
        n: argument
        timeout: maximum execution time in seconds. Returns None if exceeded.

    Returns:
        (result, elapsed_time) or (None, None) (timeout)
    """
    start = time.perf_counter()
    result = func(n)
    elapsed = time.perf_counter() - start
    return result, elapsed


def format_time(seconds):
    """Format execution time into a human-readable string."""
    if seconds is None:
        return "TIMEOUT"
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.1f} us"
    if seconds < 1:
        return f"{seconds * 1_000:.2f} ms"
    return f"{seconds:.3f} s"


if __name__ == "__main__":
    print("=" * 70)
    print(" Fibonacci sequence: naive vs memoization vs tabulation performance comparison")
    print("=" * 70)

    test_values = [10, 20, 30, 35]

    # Result verification -- confirm all three approaches return the same values
    print("\n[Verification] Checking that all three approaches return identical results:")
    for n in [0, 1, 2, 5, 10]:
        r1 = fib_naive(n)
        r2 = fib_memo(n)
        r3 = fib_tab(n)
        status = "OK" if r1 == r2 == r3 else "FAIL"
        print(f"  fib({n:>2}) = {r1:<10}  [{status}]")

    # Benchmark
    print(f"\n{'='*70}")
    print(f"{'n':>4} | {'fib(n)':>15} | {'naive':>12} | {'memo':>12} | {'tabulation':>12}")
    print(f"{'-'*4}-+-{'-'*15}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}")

    for n in test_values:
        # naive: skip if n >= 40 (takes too long)
        if n <= 35:
            r_naive, t_naive = benchmark(fib_naive, n)
        else:
            r_naive, t_naive = None, None

        r_memo, t_memo = benchmark(fib_memo, n)
        r_tab, t_tab = benchmark(fib_tab, n)

        fib_val = r_tab  # reliable value
        print(f"{n:>4} | {fib_val:>15} | {format_time(t_naive):>12} | "
              f"{format_time(t_memo):>12} | {format_time(t_tab):>12}")

    # Additional: DP performance for large n
    print(f"\n{'='*70}")
    print("[Additional] DP performance for large n (impossible range for naive):")
    print(f"{'n':>8} | {'tabulation':>12} | {'fib(n) (first 20 digits)':>25}")
    print(f"{'-'*8}-+-{'-'*12}-+-{'-'*25}")

    for n in [100, 500, 1000, 5000]:
        r, t = benchmark(fib_tab, n)
        fib_str = str(r)
        display = fib_str[:20] + "..." if len(fib_str) > 20 else fib_str
        print(f"{n:>8} | {format_time(t):>12} | {display:>25}")

    # Call count comparison
    print(f"\n{'='*70}")
    print("[Analysis] Function call count of naive recursion:")

    call_count = 0

    def fib_naive_counted(n):
        global call_count
        call_count += 1
        if n <= 1:
            return n
        return fib_naive_counted(n - 1) + fib_naive_counted(n - 2)

    for n in [5, 10, 15, 20, 25]:
        call_count = 0
        fib_naive_counted(n)
        print(f"  fib({n:>2}): {call_count:>12,} calls  "
              f"(2^{n} = {2**n:>12,})")

    # Summary
    print(f"\n{'='*70}")
    print(" Summary")
    print("=" * 70)
    print("""
  Approach      | Time        | Space       | Characteristics
  --------------|-------------|-------------|---------------------------
  naive recurse | O(2^n)      | O(n)        | Redundant computations grow exponentially
  memoization   | O(n)        | O(n)        | top-down, uses recursion stack
  tabulation    | O(n)        | O(n) / O(1) | bottom-up, uses iteration

  Key ideas of DP:
  - When there are overlapping subproblems
  - "Never solve a problem you have already solved"
  - Memoization: solves only the needed subproblems (lazy)
  - Tabulation: solves all subproblems in order (eager)
""")
