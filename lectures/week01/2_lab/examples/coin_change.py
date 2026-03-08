# === 거스름돈 문제 (Coin Change) — 탐욕(Greedy) 접근법 ===
# 주어진 금액을 동전으로 거슬러 줄 때, 항상 가장 큰 동전부터 사용하는 탐욕 알고리즘
#
# 주의: 탐욕 알고리즘은 항상 최적해를 보장하지 않습니다!
# - 표준 화폐 단위(예: 500, 100, 50, 10)에서는 최적
# - 비표준 단위(예: 1, 3, 4)에서는 최적이 아닐 수 있음
#   → 최적해가 필요하면 동적 프로그래밍(DP)을 사용해야 합니다.
#
# 시간 복잡도: O(amount / 최소동전 + k log k), k = 동전 종류 수
# 공간 복잡도: O(amount / 최소동전) — 결과 리스트 크기
"""Coin Change - Greedy approach demonstration."""


def coin_change_greedy(amount, coins):
    """
    탐욕적 거스름돈 알고리즘: 항상 가능한 가장 큰 동전부터 선택합니다.
    사용한 동전의 리스트를 반환합니다.

    알고리즘:
      1. 동전을 내림차순으로 정렬 (큰 동전 우선)
      2. 각 동전에 대해 사용 가능한 만큼 반복적으로 사용
      3. 남은 금액이 0이 되면 성공, 아니면 실패(None 반환)

    주의: 탐욕법은 항상 최적해(최소 동전 개수)를 보장하지 않습니다!
    """
    coins_sorted = sorted(coins, reverse=True)  # 동전을 큰 것부터 정렬
    result = []  # 사용한 동전을 저장할 리스트
    remaining = amount  # 아직 거슬러 줘야 할 남은 금액

    for coin in coins_sorted:  # 큰 동전부터 순서대로 시도
        while remaining >= coin:  # 현재 동전을 사용할 수 있는 동안 반복
            result.append(coin)  # 동전 사용 기록
            remaining -= coin  # 남은 금액에서 차감

    if remaining > 0:  # 정확히 거슬러 줄 수 없는 경우
        return None  # Cannot make exact change
    return result


if __name__ == "__main__":
    # 사례 1: 탐욕법이 최적인 경우 (표준 화폐 단위)
    # 500, 100, 50, 10원은 큰 단위가 작은 단위의 배수 → 탐욕법이 최적
    coins1 = [500, 100, 50, 10]
    amount1 = 1260
    result1 = coin_change_greedy(amount1, coins1)
    print(f"Amount: {amount1}, Coins: {coins1}")
    print(f"Greedy result: {result1} ({len(result1)} coins)\n")

    # 사례 2: 탐욕법이 실패하는 경우 (비표준 동전)
    # 6 = 4+1+1 (탐욕: 3개) vs 6 = 3+3 (최적: 2개)
    # 탐욕법은 가장 큰 동전(4)부터 선택하므로 최적해를 놓침
    coins2 = [1, 3, 4]
    amount2 = 6
    result2 = coin_change_greedy(amount2, coins2)
    print(f"Amount: {amount2}, Coins: {coins2}")
    print(f"Greedy result: {result2} ({len(result2)} coins)")
    print(f"Optimal: [3, 3] (2 coins) — Greedy is NOT optimal here!")
