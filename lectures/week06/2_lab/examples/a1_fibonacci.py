# === A-1: 피보나치 수열 (Fibonacci) ===
# 동적 프로그래밍의 기본 예제: 세 가지 구현 방식 비교
#
# 핵심 개념:
# - 순수 재귀: 중복 부분 문제로 인해 지수적 시간 복잡도 O(2^n)
# - 메모이제이션 (top-down DP): 이미 계산한 값을 캐싱하여 O(n)
# - 타뷸레이션 (bottom-up DP): 작은 값부터 테이블을 채워 O(n)
# - DP의 핵심 조건: 최적 부분 구조 + 중복 부분 문제
"""피보나치 수열 -- 순수 재귀 vs 메모이제이션 vs 타뷸레이션 성능 비교."""
import time
import sys
# 메모이제이션 재귀를 위해 재귀 깊이 제한 확장
sys.setrecursionlimit(10000)


def fib_naive(n):
    """순수 재귀로 피보나치 수를 계산한다.

    시간 복잡도: O(2^n) -- 중복 계산이 지수적으로 발생
    공간 복잡도: O(n) -- 재귀 호출 스택 깊이

    fib(n) = fib(n-1) + fib(n-2)를 그대로 재귀 호출하면
    동일한 부분 문제가 반복적으로 계산된다.
    """
    if n <= 1:  # 기저 조건: fib(0)=0, fib(1)=1
        return n
    return fib_naive(n - 1) + fib_naive(n - 2)


def fib_memo(n, memo=None):
    """메모이제이션(top-down DP)으로 피보나치 수를 계산한다.

    시간 복잡도: O(n) -- 각 값을 한 번만 계산
    공간 복잡도: O(n) -- 메모 딕셔너리 + 재귀 호출 스택

    이미 계산한 값을 memo 딕셔너리에 저장하여
    중복 계산을 완전히 제거한다.
    """
    if memo is None:
        memo = {}
    if n in memo:  # 이미 계산한 값이면 바로 반환
        return memo[n]
    if n <= 1:  # 기저 조건
        return n
    # 계산 후 메모에 저장
    memo[n] = fib_memo(n - 1, memo) + fib_memo(n - 2, memo)
    return memo[n]


def fib_tab(n):
    """타뷸레이션(bottom-up DP)으로 피보나치 수를 계산한다.

    시간 복잡도: O(n) -- 배열을 한 번 순회
    공간 복잡도: O(n) -- DP 테이블 (O(1)로 최적화 가능)

    작은 값부터 순서대로 테이블을 채운다. 재귀 호출 없음.
    """
    if n <= 1:  # 기저 조건
        return n
    dp = [0] * (n + 1)  # DP 테이블 초기화
    dp[1] = 1
    # 점화식: dp[i] = dp[i-1] + dp[i-2]
    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]
    return dp[n]


if __name__ == "__main__":
    # 정확성 검증: 메모이제이션과 타뷸레이션 결과가 동일한지 확인
    for i in range(20):
        assert fib_memo(i) == fib_tab(i)

    # 성능 비교: n이 커질수록 순수 재귀와 DP의 차이가 극적으로 벌어짐
    print(f"{'N':>5} | {'Naive':>12} | {'Memo':>12} | {'Tabulation':>12}")
    print("-" * 50)

    for n in [10, 20, 30, 35, 40]:
        # 순수 재귀: n > 35이면 너무 느려서 생략
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
