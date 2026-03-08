# === A-3: 0-1 배낭 문제 (0-1 Knapsack) ===
# DP를 이용한 0-1 배낭 문제 풀이 + 역추적
#
# 핵심 개념:
# - 각 물건을 넣거나(1) 안 넣거나(0)만 가능
# - 점화식: dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
#     - dp[i-1][w]: i번째 물건을 안 넣는 경우
#     - dp[i-1][w-w_i] + v_i: i번째 물건을 넣는 경우
# - 역추적: dp[i][w] != dp[i-1][w]이면 i번째 물건이 선택된 것
# - 시간 복잡도: O(n * W) (n = 물건 수, W = 배낭 용량, 의사 다항식)
# - 공간 복잡도: O(n * W), 1차원 배열로 O(W) 최적화 가능
"""0-1 배낭 문제 -- DP + 역추적으로 최적해와 선택된 물건을 구한다."""


def knapsack_01(capacity, items):
    """0-1 배낭 문제를 DP로 풀이한다.

    알고리즘:
    1. dp[i][j] = 처음 i개 물건으로 무게 j 이하에서의 최대 가치
    2. 각 물건에 대해 넣는 경우 / 안 넣는 경우 중 큰 값 선택
    3. 역추적으로 실제 선택된 물건 복원

    시간 복잡도: O(n * capacity)
    공간 복잡도: O(n * capacity)

    Args:
        capacity: 배낭의 최대 무게 (정수)
        items: [(가치, 무게, 이름), ...] 리스트

    Returns:
        (최대 가치, 선택된 물건 리스트)
    """
    n = len(items)
    # DP 테이블 초기화: dp[i][j] = 처음 i개 물건, 무게 제한 j에서의 최대 가치
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 테이블 채우기
    for i in range(1, n + 1):
        v, w, _ = items[i - 1]  # i번째 물건의 가치, 무게
        for j in range(capacity + 1):
            dp[i][j] = dp[i - 1][j]  # 안 넣는 경우 (이전 행의 값 복사)
            # 넣는 경우: 무게가 허용되고, 넣었을 때 더 큰 가치를 얻을 수 있으면
            if w <= j and dp[i - 1][j - w] + v > dp[i][j]:
                dp[i][j] = dp[i - 1][j - w] + v

    # 역추적: dp 테이블을 거슬러 올라가며 선택된 물건 복원
    selected = []
    j = capacity
    for i in range(n, 0, -1):
        # dp[i][j] != dp[i-1][j]이면 i번째 물건이 선택된 것
        if dp[i][j] != dp[i - 1][j]:
            selected.append(items[i - 1])
            j -= items[i - 1][1]  # 선택한 물건의 무게만큼 남은 용량 감소

    return dp[n][capacity], list(reversed(selected))


if __name__ == "__main__":
    items = [
        (60, 10, "Laptop"),
        (100, 20, "Camera"),
        (120, 30, "Painting"),
        (40, 5, "Book"),
    ]
    capacity = 50

    print(f"Items: {[(name, f'v={v}, w={w}') for v, w, name in items]}")
    print(f"Capacity: {capacity}\n")

    max_val, selected = knapsack_01(capacity, items)
    print(f"Maximum value: {max_val}")
    print(f"Selected items:")
    total_weight = 0
    for v, w, name in selected:
        print(f"  {name}: value={v}, weight={w}")
        total_weight += w
    print(f"Total weight: {total_weight}/{capacity}")
