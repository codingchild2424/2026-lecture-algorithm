"""Fibonacci - naive vs memoization vs tabulation."""
import time
import sys
sys.setrecursionlimit(10000)


def fib_naive(n):
    """O(2^n): Exponential - extremely slow."""
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    """O(n): Top-down with memoization."""
    if memo is None:
        memo = {}
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tab(n):
    """O(n): Bottom-up tabulation."""
    if n <= 1:
        return n
    dp = [0] * (n + 1)
    dp[1] = 1
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    # Correctness check
    for i in range(20):
        assert fib_memo(i) == fib_tab(i)

    # Performance comparison
    print(f"{'N':>5} | {'Naive':>12} | {'Memo':>12} | {'Tabulation':>12}")
    print("-" * 50)

    for n in [10, 20, 30, 35, 40]:
        # Naive (skip for large n)
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
