# === A-2: 분할 가능 배낭 문제 (Fractional Knapsack) ===
# 그리디 알고리즘으로 최적해를 보장하는 배낭 문제
#
# 핵심 개념:
# - 그리디 전략: 단위 무게당 가치(가치/무게 비율)가 높은 물건부터 선택
# - 물건을 쪼갤 수 있으므로 그리디가 항상 최적해를 보장
# - 0-1 배낭과의 차이: 분할 가능 -> 그리디 최적, 분할 불가 -> DP 필요
# - 시간 복잡도: O(n log n) (정렬이 지배적)
# - 공간 복잡도: O(n)
"""
분할 가능 배낭 문제 (Fractional Knapsack)

그리디 전략: 가치/무게 비율이 높은 물건부터 넣는다.
물건을 쪼갤 수 있으므로 그리디가 항상 최적해를 보장한다.
"""


def fractional_knapsack(capacity, items):
    """분할 가능 배낭 문제를 그리디로 풀이한다.

    Args:
        capacity: 배낭의 최대 무게
        items: [(이름, 무게, 가치), ...] 리스트

    Returns:
        (최대 가치, 선택된 항목 리스트)
        선택된 항목: [(이름, 넣은 무게, 넣은 가치, 비율, 분할 여부), ...]
    """
    # 가치/무게 비율로 내림차순 정렬
    sorted_items = sorted(items, key=lambda x: x[2] / x[1], reverse=True)

    total_value = 0.0
    remaining_capacity = capacity
    selected = []

    print(f"\n  배낭 용량: {capacity}kg")
    print(f"  물건 수: {len(items)}개")
    print(f"\n  가치/무게 비율 순 정렬:")
    print(f"  {'이름':<10} {'무게':>6} {'가치':>8} {'비율':>10}")
    print(f"  {'-'*36}")

    for name, weight, value in sorted_items:
        ratio = value / weight
        print(f"  {name:<10} {weight:>5.1f}kg {value:>7.0f}원 {ratio:>9.1f}원/kg")

    print(f"\n  --- 그리디 선택 과정 ---")

    for name, weight, value in sorted_items:
        if remaining_capacity <= 0:
            break

        ratio = value / weight

        if weight <= remaining_capacity:
            # 물건 전체를 넣을 수 있음
            selected.append((name, weight, value, ratio, False))
            total_value += value
            remaining_capacity -= weight
            print(f"  + {name}: 전체 {weight}kg 넣음 "
                  f"(가치 {value:.0f}원, 남은 용량 {remaining_capacity:.1f}kg)")
        else:
            # 물건을 쪼개서 넣음
            fraction = remaining_capacity / weight
            partial_value = value * fraction
            selected.append((name, remaining_capacity, partial_value, ratio, True))
            total_value += partial_value
            print(f"  + {name}: {fraction:.1%} ({remaining_capacity:.1f}kg) 넣음 "
                  f"(가치 {partial_value:.0f}원, 남은 용량 0.0kg)")
            remaining_capacity = 0

    return total_value, selected


def knapsack_01_bruteforce(capacity, items):
    """0-1 배낭 문제를 브루트포스로 풀이한다 (비교용).

    Args:
        capacity: 배낭의 최대 무게
        items: [(이름, 무게, 가치), ...] 리스트

    Returns:
        (최대 가치, 선택된 항목 인덱스 리스트)
    """
    n = len(items)
    best_value = 0
    best_selection = []

    for mask in range(1 << n):
        total_weight = 0
        total_value = 0
        selection = []

        for i in range(n):
            if mask & (1 << i):
                name, weight, value = items[i]
                total_weight += weight
                total_value += value
                selection.append(i)

        if total_weight <= capacity and total_value > best_value:
            best_value = total_value
            best_selection = selection

    return best_value, best_selection


if __name__ == "__main__":
    print("=" * 60)
    print(" 분할 가능 배낭 문제 (Fractional Knapsack)")
    print("=" * 60)

    # 예제 1: 기본 예제
    items1 = [
        ("금괴",   10.0, 600),
        ("은괴",   20.0, 500),
        ("동괴",   30.0, 400),
        ("보석",    5.0, 300),
        ("도자기", 15.0, 200),
    ]

    print("\n" + "=" * 60)
    print("[예제 1] 기본 배낭 문제")
    print("=" * 60)

    total_value, selected = fractional_knapsack(40, items1)

    print(f"\n  === 결과 ===")
    print(f"  최대 가치: {total_value:.0f}원")
    print(f"  선택된 항목:")
    for name, weight, value, ratio, is_fraction in selected:
        marker = " (분할)" if is_fraction else ""
        print(f"    - {name}: {weight:.1f}kg, {value:.0f}원{marker}")

    # 예제 2: 0-1 배낭과 비교
    items2 = [
        ("A",  10.0, 60),
        ("B",  20.0, 100),
        ("C",  30.0, 120),
    ]

    print("\n" + "=" * 60)
    print("[예제 2] 분할 가능 vs 0-1 배낭 비교")
    print("=" * 60)

    frac_value, frac_selected = fractional_knapsack(50, items2)

    print(f"\n  === 분할 가능 배낭 결과 ===")
    print(f"  최대 가치: {frac_value:.0f}원")

    # 0-1 배낭 (브루트포스)
    bf_value, bf_selection = knapsack_01_bruteforce(50, items2)

    print(f"\n  === 0-1 배낭 결과 (브루트포스) ===")
    print(f"  최대 가치: {bf_value:.0f}원")
    print(f"  선택된 항목:")
    for i in bf_selection:
        name, weight, value = items2[i]
        print(f"    - {name}: {weight:.1f}kg, {value:.0f}원")

    print(f"\n  분할 가능 배낭({frac_value:.0f}원) >= 0-1 배낭({bf_value:.0f}원)")
    print(f"  분할 가능 배낭은 항상 0-1 배낭 이상의 가치를 얻을 수 있음")

    # 요약
    print("\n" + "=" * 60)
    print(" 요약")
    print("=" * 60)
    print("""
  분할 가능 배낭 -- 그리디 전략:
  1. 각 물건의 가치/무게 비율을 계산한다
  2. 비율이 높은 순으로 정렬한다
  3. 배낭에 남은 용량만큼 물건을 넣는다 (필요시 분할)

  시간 복잡도: O(n log n) -- 정렬이 지배적
  공간 복잡도: O(n)

  그리디가 최적인 이유:
  - 단위 무게당 가치가 가장 높은 물건을 우선 선택하면
    남은 용량에 대해서도 최적 선택이 유지됨
  - 물건을 쪼갤 수 있으므로 "넣을까 말까"가 아니라
    "얼마나 넣을까"의 문제가 됨
""")
