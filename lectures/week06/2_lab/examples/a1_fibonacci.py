# === A-1: Fibonacci Sequence ===
# Basic example of dynamic programming: comparing three implementation approaches
#
# Key concepts:
# - Pure recursion: exponential time complexity O(2^n) due to overlapping subproblems
# - Memoization (top-down DP): caches previously computed values for O(n)
# - Tabulation (bottom-up DP): fills table from small values upward for O(n)
# - Core requirements for DP: optimal substructure + overlapping subproblems
"""Fibonacci sequence -- performance comparison of pure recursion vs memoization vs tabulation."""
import time
import sys
# Increase recursion depth limit for memoization recursion
sys.setrecursionlimit(10000)


def fib_naive(n):
    """Compute the Fibonacci number using pure recursion.

    Time complexity: O(2^n) -- redundant computations grow exponentially
    Space complexity: O(n) -- recursion call stack depth

    Directly calling fib(n) = fib(n-1) + fib(n-2) recursively
    causes the same subproblems to be computed repeatedly.
    """
    if n <= 1:  # Base case: fib(0)=0, fib(1)=1
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    """Compute the Fibonacci number using memoization (top-down DP).

    Time complexity: O(n) -- each value is computed only once
    Space complexity: O(n) -- memo dictionary + recursion call stack

    Previously computed values are stored in a memo dictionary,
    completely eliminating redundant computations.
    """
    if memo is None:
        memo = {}
    if n in memo:  # Return immediately if already computed
        return memo[n]
    if n <= 1:  # Base case
        return n
    # Compute and store in memo
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tab(n):
    """Compute the Fibonacci number using tabulation (bottom-up DP).

    Time complexity: O(n) -- single pass through the array
    Space complexity: O(n) -- DP table (can be optimized to O(1))

    Fills the table sequentially from small values. No recursive calls.
    """
    if n <= 1:  # Base case
        return n
    dp = [0] * (n + 1)  # Initialize DP table
    dp[1] = 1
    # Recurrence: dp[i] = dp[i-1] + dp[i-2]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    # Correctness verification: confirm memoization and tabulation produce the same results
    for i in range(20):
        assert fib_memo(i) == fib_tab(i)

    # Performance comparison: as n grows, the gap between pure recursion and DP becomes dramatic
    print(f"{'N':>5} | {'Naive':>12} | {'Memo':>12} | {'Tabulation':>12}")
    print("-" * 50)

    for n in [10, 20, 30, 35, 40]:
        # Pure recursion: skip if n > 35 (too slow)
        if n <= 35:
            start = time.perf_counter()
            fib_naive(n)
            t_naive = time.perf_counter() - start
        else:
            t_naive = None

        start = time.perf_counter()
        fib_memo(n, {})
        t_memo = time.perf_counter() - start

        start = time.perf_counter()
        fib_tab(n)
        t_tab = time.perf_counter() - start

        naive_str = f"{t_naive:.6f}" if t_naive is not None else "too slow"
        print(f"{n:>5} | {naive_str:>12} | {t_memo:>12.6f} | {t_tab:>12.6f}")
