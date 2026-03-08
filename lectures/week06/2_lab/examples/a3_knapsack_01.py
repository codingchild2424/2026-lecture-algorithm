# === A-3: 0-1 배낭 문제 - 상세 DP 테이블 시각화 ===
# DP 테이블 구성 과정을 시각적으로 보여주고, 역추적 과정을 상세히 설명
#
# 핵심 개념:
# - dp[i][w] = 처음 i개 물건으로 무게 제한 w에서의 최대 가치
# - 점화식: dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
# - 역추적: dp[i][w] != dp[i-1][w]이면 i번째 물건 선택
# - 그리디(비율순)는 0-1 배낭에서 실패할 수 있음을 예제로 증명
# - 시간 복잡도: O(n * W) (pseudo-polynomial)
# - 공간 복잡도: O(n * W), 1차원 배열로 O(W) 최적화 가능
"""
0-1 배낭 문제 (0-1 Knapsack) -- DP + 역추적

각 물건을 넣거나(1) 안 넣거나(0)만 가능한 배낭 문제.
DP 테이블을 구성하고, 역추적으로 선택된 항목을 복원한다.

재귀식:
  dp[i][w] = max(
      dp[i-1][w],                          # i번째 물건을 안 넣는 경우
      dp[i-1][w - weight[i]] + value[i]     # i번째 물건을 넣는 경우 (weight[i] <= w)
  )
"""


def knapsack_01(capacity, items):
    """0-1 배낭 문제를 DP로 풀이한다.

    Args:
        capacity: 배낭의 최대 무게 (정수)
        items: [(이름, 무게, 가치), ...] 리스트

    Returns:
        (최대 가치, DP 테이블, 선택된 항목 인덱스 리스트)
    """
    n = len(items)

    # DP 테이블: dp[i][w] = 처음 i개 물건으로 무게 w 이하에서의 최대 가치
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    # 테이블 채우기
    for i in range(1, n + 1):
        name, weight, value = items[i - 1]
        for w in range(capacity + 1):
            # 안 넣는 경우
            dp[i][w] = dp[i - 1][w]

            # 넣는 경우 (무게가 허용될 때만)
            if weight <= w:
                dp[i][w] = max(dp[i][w], dp[i - 1][w - weight] + value)

    # 역추적: 어떤 물건이 선택되었는지 복원
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            # i번째 물건이 선택됨
            selected.append(i - 1)  # 0-indexed
            w -= items[i - 1][1]  # 해당 물건의 무게만큼 감소

    selected.reverse()

    return dp[n][capacity], dp, selected


def print_dp_table(dp, items, capacity, selected):
    """DP 테이블을 시각적으로 출력한다.

    Args:
        dp: DP 테이블
        items: 물건 리스트
        capacity: 배낭 용량
        selected: 선택된 항목 인덱스 리스트
    """
    n = len(items)

    # 용량이 크면 일부만 표시
    max_cols = min(capacity + 1, 20)
    if capacity + 1 > max_cols:
        print(f"    (용량이 크므로 w=0~{max_cols-1} 부분만 표시)")

    # 헤더 (무게)
    print(f"    {'물건':<8} ", end="")
    for w in range(max_cols):
        print(f"{w:>4}", end=" ")
    if capacity + 1 > max_cols:
        print(f" ... {capacity:>4}", end="")
    print()

    print(f"    {'-'*8}-", end="")
    for w in range(max_cols):
        print(f"{'----'}", end="-")
    print()

    # 테이블 본체
    for i in range(n + 1):
        if i == 0:
            label = "(없음)"
        else:
            name, weight, value = items[i - 1]
            marker = " *" if (i - 1) in selected else ""
            label = f"{name}{marker}"

        print(f"    {label:<8} ", end="")
        for w in range(max_cols):
            val = dp[i][w]
            if val > 0:
                print(f"{val:>4}", end=" ")
            else:
                print(f"{'0':>4}", end=" ")

        if capacity + 1 > max_cols:
            print(f" ... {dp[i][capacity]:>4}", end="")
        print()

    print()


if __name__ == "__main__":
    print("=" * 65)
    print(" 0-1 배낭 문제 (0-1 Knapsack) -- DP + 역추적")
    print("=" * 65)

    # ===== 예제 1: 기본 예제 =====
    print(f"\n{'='*65}")
    print("[예제 1] 기본 배낭 문제")
    print(f"{'='*65}")

    items1 = [
        ("금괴",   3, 60),
        ("은괴",   4, 70),
        ("보석",   2, 40),
        ("도자기", 5, 90),
    ]
    capacity1 = 10

    print(f"\n  배낭 용량: {capacity1}kg")
    print(f"  물건 목록:")
    print(f"  {'이름':<8} {'무게':>4} {'가치':>6} {'비율':>8}")
    print(f"  {'-'*28}")
    for name, weight, value in items1:
        print(f"  {name:<8} {weight:>3}kg {value:>5}원 {value/weight:>7.1f}원/kg")

    max_value, dp, selected = knapsack_01(capacity1, items1)

    print(f"\n  --- DP 테이블 (* = 선택된 물건) ---")
    print_dp_table(dp, items1, capacity1, selected)

    print(f"  === 결과 ===")
    print(f"  최대 가치: {max_value}원")
    print(f"  선택된 물건:")
    total_weight = 0
    for idx in selected:
        name, weight, value = items1[idx]
        total_weight += weight
        print(f"    - {name}: {weight}kg, {value}원")
    print(f"  총 무게: {total_weight}kg / {capacity1}kg")

    # ===== 예제 2: 교과서 예제 =====
    print(f"\n{'='*65}")
    print("[예제 2] 교과서 예제")
    print(f"{'='*65}")

    items2 = [
        ("A", 2, 12),
        ("B", 1,  10),
        ("C", 3, 20),
        ("D", 2, 15),
    ]
    capacity2 = 5

    print(f"\n  배낭 용량: {capacity2}kg")
    print(f"  물건 목록:")
    print(f"  {'이름':<8} {'무게':>4} {'가치':>6}")
    print(f"  {'-'*20}")
    for name, weight, value in items2:
        print(f"  {name:<8} {weight:>3}kg {value:>5}원")

    max_value, dp, selected = knapsack_01(capacity2, items2)

    print(f"\n  --- DP 테이블 (* = 선택된 물건) ---")
    print_dp_table(dp, items2, capacity2, selected)

    # 역추적 과정 상세 설명
    print(f"  --- 역추적 과정 ---")
    n = len(items2)
    w = capacity2
    print(f"  시작: dp[{n}][{w}] = {dp[n][w]}")
    for i in range(n, 0, -1):
        name, weight, value = items2[i - 1]
        if dp[i][w] != dp[i - 1][w]:
            print(f"  i={i} ({name}): dp[{i}][{w}]={dp[i][w]} != dp[{i-1}][{w}]={dp[i-1][w]}"
                  f" -> 선택! (w: {w} -> {w - weight})")
            w -= weight
        else:
            print(f"  i={i} ({name}): dp[{i}][{w}]={dp[i][w]} == dp[{i-1}][{w}]={dp[i-1][w]}"
                  f" -> 미선택")

    print(f"\n  === 결과 ===")
    print(f"  최대 가치: {max_value}원")
    print(f"  선택된 물건:")
    total_weight = 0
    for idx in selected:
        name, weight, value = items2[idx]
        total_weight += weight
        print(f"    - {name}: {weight}kg, {value}원")
    print(f"  총 무게: {total_weight}kg / {capacity2}kg")

    # ===== 예제 3: 그리디가 실패하는 케이스 =====
    print(f"\n{'='*65}")
    print("[예제 3] 그리디(비율순)가 실패하는 케이스")
    print(f"{'='*65}")

    items3 = [
        ("A", 3, 31),   # 비율 10.3
        ("B", 4, 40),   # 비율 10.0
        ("C", 5, 45),   # 비율 9.0
    ]
    capacity3 = 8

    print(f"\n  배낭 용량: {capacity3}kg")
    print(f"  물건 목록 (비율순):")
    sorted_items = sorted(items3, key=lambda x: x[2] / x[1], reverse=True)
    for name, weight, value in sorted_items:
        print(f"    {name}: {weight}kg, {value}원 (비율: {value/weight:.1f}원/kg)")

    # 그리디 (비율순)
    print(f"\n  그리디 결과 (비율순으로 넣기):")
    greedy_value = 0
    greedy_weight = 0
    greedy_items = []
    remaining = capacity3
    for name, weight, value in sorted_items:
        if weight <= remaining:
            greedy_items.append(name)
            greedy_value += value
            greedy_weight += weight
            remaining -= weight
            print(f"    + {name}: {weight}kg, {value}원 (남은 용량: {remaining}kg)")
    print(f"  그리디 총 가치: {greedy_value}원 (무게: {greedy_weight}kg)")

    # DP
    max_value, dp, selected = knapsack_01(capacity3, items3)
    print(f"\n  DP 결과:")
    print(f"  최대 가치: {max_value}원")
    print(f"  선택된 물건:")
    for idx in selected:
        name, weight, value = items3[idx]
        print(f"    - {name}: {weight}kg, {value}원")

    if greedy_value < max_value:
        print(f"\n  -> 그리디({greedy_value}원) < DP({max_value}원): 그리디 실패!")
    else:
        print(f"\n  -> 그리디 = DP: 이 경우에는 동일")

    # 요약
    print(f"\n{'='*65}")
    print(" 요약")
    print("=" * 65)
    print("""
  0-1 배낭 DP:
  - dp[i][w] = 처음 i개 물건, 무게 제한 w에서의 최대 가치
  - 재귀식: dp[i][w] = max(dp[i-1][w], dp[i-1][w-w_i] + v_i)
  - 시간 복잡도: O(n * W) (pseudo-polynomial)
  - 공간 복잡도: O(n * W), 1차원 배열로 O(W) 가능

  역추적:
  - dp[n][W]에서 시작
  - dp[i][w] != dp[i-1][w]이면 i번째 물건 선택
  - 선택 시 w를 w - w_i로 감소

  그리디 vs DP:
  - 분할 가능 배낭: 그리디 최적 (비율순)
  - 0-1 배낭: 그리디 실패 가능 -> DP 필요
""")
