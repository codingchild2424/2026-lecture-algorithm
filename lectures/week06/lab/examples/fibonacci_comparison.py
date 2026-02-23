"""
피보나치 수열 -- 세 가지 구현 방식 성능 비교

1. fib_naive(n)  -- 순수 재귀: O(2^n)
2. fib_memo(n)   -- 메모이제이션 (top-down DP): O(n)
3. fib_tab(n)    -- 타뷸레이션 (bottom-up DP): O(n)
"""

import time
import sys

# 재귀 깊이 제한 확장 (메모이제이션용)
sys.setrecursionlimit(10000)


# ===== 구현 1: 순수 재귀 (Naive) =====

def fib_naive(n):
    """순수 재귀로 피보나치 수를 계산한다.

    시간 복잡도: O(2^n) -- 중복 계산이 지수적으로 발생
    공간 복잡도: O(n) -- 재귀 호출 스택 깊이

    fib(5)를 구하려면:
      fib(5) = fib(4) + fib(3)
      fib(4) = fib(3) + fib(2)   <-- fib(3) 중복!
      fib(3) = fib(2) + fib(1)   <-- fib(2) 중복!
      ...
    """
    if n <= 1:
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


# ===== 구현 2: 메모이제이션 (Top-Down DP) =====

def fib_memo(n, memo=None):
    """메모이제이션으로 피보나치 수를 계산한다.

    시간 복잡도: O(n) -- 각 값을 한 번만 계산
    공간 복잡도: O(n) -- 메모 테이블 + 재귀 스택

    이미 계산한 값은 memo 딕셔너리에 저장하여 재사용.
    """
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n <= 1:
        return n

    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


# ===== 구현 3: 타뷸레이션 (Bottom-Up DP) =====

def fib_tab(n):
    """타뷸레이션으로 피보나치 수를 계산한다.

    시간 복잡도: O(n) -- 배열을 한 번 순회
    공간 복잡도: O(n) -- DP 테이블 (O(1)로 최적화 가능)

    작은 값부터 순서대로 테이블을 채움. 재귀 호출 없음.
    """
    if n <= 1:
        return n

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]


# ===== 공간 최적화 버전 (참고) =====

def fib_optimized(n):
    """공간 O(1)로 최적화된 타뷸레이션.

    시간 복잡도: O(n)
    공간 복잡도: O(1) -- 이전 두 값만 유지
    """
    if n <= 1:
        return n

    prev2, prev1 = 0, 1
    for _ in range(2, n + 1):
        prev2, prev1 = prev1, prev2 + prev1

    return prev1


# ===== 벤치마크 =====

def benchmark(func, n, timeout=10.0):
    """함수 실행 시간을 측정한다.

    Args:
        func: 실행할 함수
        n: 인자
        timeout: 최대 실행 시간(초). 초과 시 None 반환.

    Returns:
        (결과값, 실행시간) 또는 (None, None) (타임아웃)
    """
    start = time.perf_counter()
    result = func(n)
    elapsed = time.perf_counter() - start
    return result, elapsed


def format_time(seconds):
    """실행 시간을 읽기 좋은 형태로 포맷한다."""
    if seconds is None:
        return "TIMEOUT"
    if seconds < 0.001:
        return f"{seconds * 1_000_000:.1f} us"
    if seconds < 1:
        return f"{seconds * 1_000:.2f} ms"
    return f"{seconds:.3f} s"


if __name__ == "__main__":
    print("=" * 70)
    print(" 피보나치 수열: naive vs memoization vs tabulation 성능 비교")
    print("=" * 70)

    test_values = [10, 20, 30, 35]

    # 결과 검증 -- 세 방식이 같은 값을 반환하는지 확인
    print("\n[검증] 세 방식이 동일한 결과를 반환하는지 확인:")
    for n in [0, 1, 2, 5, 10]:
        r1 = fib_naive(n)
        r2 = fib_memo(n)
        r3 = fib_tab(n)
        status = "OK" if r1 == r2 == r3 else "FAIL"
        print(f"  fib({n:>2}) = {r1:<10}  [{status}]")

    # 벤치마크
    print(f"\n{'='*70}")
    print(f"{'n':>4} | {'fib(n)':>15} | {'naive':>12} | {'memo':>12} | {'tabulation':>12}")
    print(f"{'-'*4}-+-{'-'*15}-+-{'-'*12}-+-{'-'*12}-+-{'-'*12}")

    for n in test_values:
        # naive: n이 40 이상이면 스킵 (너무 오래 걸림)
        if n <= 35:
            r_naive, t_naive = benchmark(fib_naive, n)
        else:
            r_naive, t_naive = None, None

        r_memo, t_memo = benchmark(fib_memo, n)
        r_tab, t_tab = benchmark(fib_tab, n)

        fib_val = r_tab  # 확실한 값
        print(f"{n:>4} | {fib_val:>15} | {format_time(t_naive):>12} | "
              f"{format_time(t_memo):>12} | {format_time(t_tab):>12}")

    # 추가: 큰 수에 대한 DP 성능
    print(f"\n{'='*70}")
    print("[추가] 큰 n에서 DP 방식의 성능 (naive는 불가능한 영역):")
    print(f"{'n':>8} | {'tabulation':>12} | {'fib(n) (처음 20자리)':>25}")
    print(f"{'-'*8}-+-{'-'*12}-+-{'-'*25}")

    for n in [100, 500, 1000, 5000]:
        r, t = benchmark(fib_tab, n)
        fib_str = str(r)
        display = fib_str[:20] + "..." if len(fib_str) > 20 else fib_str
        print(f"{n:>8} | {format_time(t):>12} | {display:>25}")

    # 호출 횟수 비교
    print(f"\n{'='*70}")
    print("[분석] naive 재귀의 함수 호출 횟수:")

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
        print(f"  fib({n:>2}): {call_count:>12,}번 호출  "
              f"(2^{n} = {2**n:>12,})")

    # 요약
    print(f"\n{'='*70}")
    print(" 요약")
    print("=" * 70)
    print("""
  방식          | 시간 복잡도 | 공간 복잡도 | 특징
  --------------|-------------|-------------|---------------------------
  naive 재귀    | O(2^n)      | O(n)        | 중복 계산이 지수적으로 발생
  메모이제이션  | O(n)        | O(n)        | top-down, 재귀 스택 사용
  타뷸레이션    | O(n)        | O(n) / O(1) | bottom-up, 반복문 사용

  DP의 핵심:
  - 중복 부분 문제(overlapping subproblems)가 있을 때
  - "이미 풀어본 문제는 다시 풀지 않는다"
  - 메모이제이션: 필요한 부분 문제만 푼다 (lazy)
  - 타뷸레이션: 모든 부분 문제를 순서대로 푼다 (eager)
""")
