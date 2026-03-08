# === A-1: 동전 교환 - 그리디 vs DP 상세 비교 ===
# 그리디 알고리즘이 최적해를 보장하는 조건과 실패하는 경우를 분석
#
# 핵심 개념:
# - 그리디 전략: 항상 가장 큰 동전부터 사용
# - 탐욕 선택 속성: 동전이 배수 관계일 때 성립
# - DP로 항상 최적해를 구할 수 있음
# - 시간 복잡도: 그리디 O(k), DP O(k * amount)
"""
동전 거스름돈 -- 그리디 알고리즘의 성공과 실패

그리디 전략: 항상 가장 큰 동전부터 사용한다.
- 표준 동전 세트에서는 최적해를 보장한다.
- 비표준 동전 세트에서는 최적해를 보장하지 않는다.
"""


def greedy_coin_change(coins, amount):
    """그리디 방식으로 거스름돈을 계산한다.

    큰 동전부터 최대한 많이 사용하는 전략.

    Args:
        coins: 동전 종류 리스트 (내림차순 정렬 불필요, 내부에서 정렬)
        amount: 거슬러 줄 금액

    Returns:
        (사용 동전 리스트, 총 동전 수) 또는 거스름돈을 만들 수 없으면 None
    """
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount

    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)
            remaining -= coin

    if remaining == 0:
        return result, len(result)
    return None


def dp_coin_change(coins, amount):
    """DP 방식으로 최소 동전 수를 계산한다.

    dp[i] = 금액 i를 만들기 위한 최소 동전 수

    Args:
        coins: 동전 종류 리스트
        amount: 거슬러 줄 금액

    Returns:
        (사용 동전 리스트, 총 동전 수) 또는 만들 수 없으면 None
    """
    INF = float("inf")
    dp = [INF] * (amount + 1)
    dp[0] = 0
    parent = [-1] * (amount + 1)  # 역추적을 위한 배열

    for i in range(1, amount + 1):
        for coin in coins:
            if coin <= i and dp[i - coin] + 1 < dp[i]:
                dp[i] = dp[i - coin] + 1
                parent[i] = coin

    if dp[amount] == INF:
        return None

    # 역추적으로 사용된 동전 복원
    result = []
    current = amount
    while current > 0:
        result.append(parent[current])
        current -= parent[current]

    return result, len(result)


def test_coin_set(coins, amount, label):
    """주어진 동전 세트로 그리디와 DP 결과를 비교한다."""
    print(f"\n{'='*60}")
    print(f"[{label}]")
    print(f"동전 종류: {coins}")
    print(f"거슬러 줄 금액: {amount}")
    print(f"{'='*60}")

    greedy_result = greedy_coin_change(coins, amount)
    dp_result = dp_coin_change(coins, amount)

    if greedy_result:
        g_coins, g_count = greedy_result
        print(f"\n  그리디 결과: {g_coins}")
        print(f"  동전 수: {g_count}개")
    else:
        print("\n  그리디: 거스름돈을 만들 수 없음")

    if dp_result:
        d_coins, d_count = dp_result
        print(f"\n  DP 결과 (최적): {d_coins}")
        print(f"  동전 수: {d_count}개")
    else:
        print("\n  DP: 거스름돈을 만들 수 없음")

    # 비교
    if greedy_result and dp_result:
        g_count = greedy_result[1]
        d_count = dp_result[1]
        if g_count == d_count:
            print(f"\n  --> 그리디 = 최적 (동일한 {g_count}개)")
        else:
            print(f"\n  --> 그리디 실패! 그리디({g_count}개) > 최적({d_count}개)")
            print(f"      그리디는 {g_count - d_count}개 더 사용")


if __name__ == "__main__":
    print("=" * 60)
    print(" 동전 거스름돈: 그리디 vs DP (최적)")
    print("=" * 60)

    # --- 성공 케이스: 표준 동전 세트 ---

    test_coin_set(
        coins=[500, 100, 50, 10],
        amount=770,
        label="성공 케이스 1: 한국 표준 동전",
    )

    test_coin_set(
        coins=[25, 10, 5, 1],
        amount=63,
        label="성공 케이스 2: 미국 표준 동전 (쿼터/다임/니켈/페니)",
    )

    # --- 실패 케이스: 비표준 동전 세트 ---

    test_coin_set(
        coins=[7, 5, 1],
        amount=10,
        label="실패 케이스 1: {7, 5, 1}원으로 10원",
    )
    # 그리디: 7+1+1+1 = 4개, 최적: 5+5 = 2개

    test_coin_set(
        coins=[6, 4, 1],
        amount=8,
        label="실패 케이스 2: {6, 4, 1}원으로 8원",
    )
    # 그리디: 6+1+1 = 3개, 최적: 4+4 = 2개

    test_coin_set(
        coins=[12, 9, 1],
        amount=18,
        label="실패 케이스 3: {12, 9, 1}원으로 18원",
    )
    # 그리디: 12+1*6 = 7개, 최적: 9+9 = 2개

    # --- 요약 ---
    print("\n" + "=" * 60)
    print(" 요약")
    print("=" * 60)
    print("""
  그리디가 최적인 조건:
  - 각 동전이 더 작은 동전의 배수일 때 (예: 500, 100, 50, 10)
  - 이 경우 '탐욕 선택 속성'이 성립함

  그리디가 실패하는 경우:
  - 동전 간의 배수 관계가 성립하지 않을 때
  - 이 경우 DP로 최적해를 구해야 함
  - 시간 복잡도: 그리디 O(k), DP O(k * amount)  (k = 동전 종류 수)
""")
