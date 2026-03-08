# === A-1: 동전 교환 (Coin Change) ===
# 그리디 알고리즘의 성공/실패 사례와 DP를 이용한 최적해 비교
#
# 핵심 개념:
# - 그리디: 큰 동전부터 최대한 사용 (표준 동전에서만 최적)
# - DP: 모든 경우를 고려하여 항상 최적해 보장
# - 시간 복잡도: 그리디 O(k), DP O(k * amount) (k = 동전 종류 수)
"""동전 교환 -- 그리디의 성공과 실패 사례."""


def coin_change_greedy(amount, coins):
    """그리디 방식으로 거스름돈을 계산한다.

    알고리즘: 가장 큰 동전부터 최대한 많이 사용
    시간 복잡도: O(k * amount/min_coin) (k = 동전 종류 수)
    공간 복잡도: O(amount/min_coin) (결과 리스트)

    Args:
        amount: 거슬러 줄 금액
        coins: 동전 종류 리스트

    Returns:
        사용한 동전 리스트 또는 None (불가능한 경우)
    """
    # 동전을 큰 순서로 정렬 (그리디 선택의 핵심)
    coins_sorted = sorted(coins, reverse=True)
    result = []
    remaining = amount
    # 각 동전에 대해 가능한 만큼 최대로 사용
    for coin in coins_sorted:
        while remaining >= coin:
            result.append(coin)  # 현재 동전 사용
            remaining -= coin     # 남은 금액 감소
    # 남은 금액이 0이면 성공, 아니면 실패
    return result if remaining == 0 else None


def coin_change_dp(amount, coins):
    """DP 방식으로 최소 동전 수를 계산한다 (항상 최적해 보장).

    알고리즘: dp[i] = 금액 i를 만들기 위한 최소 동전 수
    점화식: dp[i] = min(dp[i - c] + 1) (모든 동전 c에 대해)
    시간 복잡도: O(k * amount)
    공간 복잡도: O(amount)

    Args:
        amount: 거슬러 줄 금액
        coins: 동전 종류 리스트

    Returns:
        최적의 동전 리스트 또는 None (불가능한 경우)
    """
    # dp[i]: 금액 i를 만들기 위한 최소 동전 수 (초기값: 무한대)
    dp = [float('inf')] * (amount + 1)
    dp[0] = 0  # 기저 조건: 금액 0은 동전 0개
    parent = [-1] * (amount + 1)  # 역추적용: 각 금액에서 마지막으로 사용한 동전
    # 모든 금액에 대해 모든 동전을 시도
    for i in range(1, amount + 1):
        for c in coins:
            # 동전 c를 사용할 수 있고, 더 적은 동전 수로 만들 수 있는 경우
            if c <= i and dp[i - c] + 1 < dp[i]:
                dp[i] = dp[i - c] + 1
                parent[i] = c  # 역추적을 위해 사용한 동전 기록
    # 금액을 만들 수 없는 경우
    if dp[amount] == float('inf'):
        return None
    # 역추적: parent 배열을 따라 사용된 동전 복원
    result = []
    cur = amount
    while cur > 0:
        result.append(parent[cur])
        cur -= parent[cur]
    return result


if __name__ == "__main__":
    # 케이스 1: 그리디가 최적해를 찾는 경우 (표준 동전)
    print("=== Case 1: Standard coins ===")
    coins1, amount1 = [500, 100, 50, 10], 1260
    g1 = coin_change_greedy(amount1, coins1)
    print(f"Coins: {coins1}, Amount: {amount1}")
    print(f"Greedy: {g1} ({len(g1)} coins)")

    # 케이스 2: 그리디가 실패하는 경우 (비표준 동전)
    # {1, 3, 4}로 6을 만들 때: 그리디는 4+1+1=3개, 최적은 3+3=2개
    print("\n=== Case 2: Non-standard coins ===")
    coins2, amount2 = [1, 3, 4], 6
    g2 = coin_change_greedy(amount2, coins2)
    d2 = coin_change_dp(amount2, coins2)
    print(f"Coins: {coins2}, Amount: {amount2}")
    print(f"Greedy:  {g2} ({len(g2)} coins)")
    print(f"Optimal: {d2} ({len(d2)} coins)")
    print(f"-> Greedy is NOT optimal here!")
