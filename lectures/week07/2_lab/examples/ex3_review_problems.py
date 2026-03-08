# === Ex 3: 전반부 알고리즘 총정리 -- 5개 미니 문제 ===
# Week 07 중간고사 리뷰 - Week 02~06 핵심 알고리즘 복습
# 복잡도 분석, 정렬, 분할정복, 그리디, DP를 각 1문제씩 다룬다
"""
전반부 알고리즘 총정리 -- 5개 미니 문제

Week 02~06의 핵심 알고리즘을 각 1문제씩 복습한다.
각 문제에 skeleton 함수와 solution 함수가 있다.
먼저 skeleton을 직접 구현해 본 후, solution과 비교한다.
"""


# ============================================================
#  문제 1: 복잡도 분석 (Week 02)
#  중첩 루프의 시간 복잡도를 Big-O로 분석하는 문제
# ============================================================

def problem1_description():
    """문제 1: 다음 함수의 시간 복잡도를 분석하라."""
    print("""
  문제 1: 복잡도 분석 (Week 02)
  ==============================
  다음 함수의 시간 복잡도를 Big-O로 나타내라.

  def mystery(n):
      count = 0
      i = 1
      while i < n:
          j = 0
          while j < n:
              count += 1
              j += 1
          i *= 2
      return count

  (a) mystery(n)의 시간 복잡도는?
  (b) mystery(16)의 count 값은?
""")


def problem1_solution():
    """문제 1 풀이.

    분석:
    - 바깥 루프: i가 1에서 시작하여 매번 2배 증가 -> O(log n)번 반복
    - 안쪽 루프: j가 0에서 n-1까지 -> O(n)번 반복
    - 전체 시간 복잡도: O(n log n)
    """
    print("""
  풀이:
  - 바깥 루프: i = 1, 2, 4, 8, ..., < n  -->  O(log n)번 반복
  - 안쪽 루프: j = 0, 1, ..., n-1  -->  O(n)번 반복
  - 전체: O(n log n)

  (b) mystery(16):
    i=1:  j는 0~15 -> 16번
    i=2:  j는 0~15 -> 16번
    i=4:  j는 0~15 -> 16번
    i=8:  j는 0~15 -> 16번
    i=16: 루프 종료
    count = 16 * 4 = 64
""")
    # 검증용 mystery 함수 구현
    def mystery(n):
        count = 0
        i = 1
        while i < n:  # 바깥 루프: i *= 2이므로 O(log n)
            j = 0
            while j < n:  # 안쪽 루프: O(n)
                count += 1
                j += 1
            i *= 2
        return count

    result = mystery(16)
    print(f"  검증: mystery(16) = {result}")


# ============================================================
#  문제 2: 정렬 응용 (Week 03)
#  Merge Sort 구현 및 merge 횟수 추적
# ============================================================

def problem2_description():
    """문제 2: Merge Sort를 구현하라."""
    print("""
  문제 2: 정렬 (Week 03)
  ==============================
  Merge Sort를 구현하라.
  정렬 과정에서 merge 횟수를 세어 반환하라.
""")


def problem2_skeleton(arr):
    """Merge Sort skeleton -- 직접 구현해 보세요.

    Args:
        arr: 정렬할 리스트

    Returns:
        (정렬된 리스트, merge 횟수)
    """
    # TODO: 구현하세요
    pass


def problem2_solution(arr):
    """Merge Sort 풀이.

    알고리즘: 배열을 반으로 분할하여 재귀적으로 정렬 후 병합
    시간 복잡도: O(n log n) - 분할 O(log n) * 병합 O(n)
    공간 복잡도: O(n) - 병합 시 임시 배열 필요
    안정 정렬: 동일 값의 상대적 순서가 유지됨 (left[i] <= right[j])
    """
    merge_count = [0]  # 리스트로 감싸서 내부 함수에서 수정 가능하게 (클로저)

    def merge_sort(a):
        """재귀적으로 배열을 분할한다.

        기저 조건: 길이가 1 이하면 이미 정렬된 상태
        """
        if len(a) <= 1:
            return a

        mid = len(a) // 2  # 중간 지점에서 분할
        left = merge_sort(a[:mid])   # 왼쪽 절반 재귀 정렬
        right = merge_sort(a[mid:])  # 오른쪽 절반 재귀 정렬

        return merge(left, right)  # 정렬된 두 배열을 병합

    def merge(left, right):
        """정렬된 두 배열을 하나의 정렬된 배열로 병합한다.

        투 포인터 기법으로 두 배열의 원소를 비교하며 작은 것부터 결과에 추가.
        시간 복잡도: O(n) - n은 left + right의 전체 길이
        """
        merge_count[0] += 1
        result = []
        i = j = 0  # 왼쪽/오른쪽 배열의 포인터

        # 두 배열 모두 원소가 남아 있는 동안 비교하며 병합
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:  # <= 사용으로 안정 정렬 보장
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        # 남은 원소들을 결과에 추가
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_arr = merge_sort(arr)
    return sorted_arr, merge_count[0]


# ============================================================
#  문제 3: 분할정복 (Week 04)
#  배열의 최대값을 분할정복으로 찾기
# ============================================================

def problem3_description():
    """문제 3: 배열의 최대값을 분할정복으로 구하라."""
    print("""
  문제 3: 분할정복 (Week 04)
  ==============================
  정수 배열에서 최대값을 분할정복으로 구하라.
  배열을 반으로 나누어 각각의 최대값을 구한 후 합치는 방식을 사용하라.
  비교 횟수도 함께 반환하라.
""")


def problem3_skeleton(arr):
    """분할정복 최대값 skeleton -- 직접 구현해 보세요.

    Args:
        arr: 정수 리스트

    Returns:
        (최대값, 비교 횟수)
    """
    # TODO: 구현하세요
    pass


def problem3_solution(arr):
    """분할정복 최대값 풀이.

    알고리즘: 배열을 반으로 나누어 각 부분의 최대값을 재귀적으로 구한 후,
             두 최대값을 비교하여 전체 최대값을 결정
    시간 복잡도: O(n) - T(n) = 2T(n/2) + 1, Master Theorem으로 O(n)
    비교 횟수: n - 1 (이론적 최소치와 동일)
    """
    comparisons = [0]  # 비교 횟수 추적용 (클로저)

    def find_max(a, lo, hi):
        """구간 [lo, hi]에서 최대값을 분할정복으로 찾는다.

        기저 조건: 원소가 하나뿐이면 그 원소가 최대값
        """
        if lo == hi:
            return a[lo]

        mid = (lo + hi) // 2  # 중간 지점에서 분할
        left_max = find_max(a, lo, mid)       # 왼쪽 절반의 최대값
        right_max = find_max(a, mid + 1, hi)  # 오른쪽 절반의 최대값

        comparisons[0] += 1  # 좌/우 최대값 비교 1회
        return left_max if left_max >= right_max else right_max

    if not arr:
        return None, 0

    result = find_max(arr, 0, len(arr) - 1)
    return result, comparisons[0]


# ============================================================
#  문제 4: 그리디 (Week 05)
#  활동 선택 문제 (Activity Selection Problem)
# ============================================================

def problem4_description():
    """문제 4: 강의실 배정 (Activity Selection)."""
    print("""
  문제 4: 그리디 (Week 05)
  ==============================
  n개의 강의가 (시작시간, 종료시간)으로 주어진다.
  하나의 강의실에서 최대 몇 개의 강의를 배정할 수 있는지 구하라.
  선택된 강의 목록도 반환하라.
""")


def problem4_skeleton(lectures):
    """Activity Selection skeleton -- 직접 구현해 보세요.

    Args:
        lectures: [(start, end), ...] 리스트

    Returns:
        (최대 강의 수, 선택된 강의 인덱스 리스트)
    """
    # TODO: 구현하세요
    pass


def problem4_solution(lectures):
    """Activity Selection 풀이.

    알고리즘: 종료 시간이 빠른 순으로 정렬 후, 겹치지 않는 강의를 탐욕적으로 선택
    그리디 선택 속성: "종료 시간이 가장 빠른 활동을 선택하면 항상 최적 해의 일부"
    시간 복잡도: O(n log n) - 정렬이 지배적
    공간 복잡도: O(n) - 선택된 강의 인덱스 저장
    """
    # (종료시간, 시작시간, 원래 인덱스) 기준으로 정렬
    # 종료 시간이 같으면 시작 시간이 빠른 순으로 정렬
    indexed = [(end, start, i) for i, (start, end) in enumerate(lectures)]
    indexed.sort()

    selected = []
    last_end = -1  # 마지막으로 선택한 강의의 종료 시간

    for end, start, idx in indexed:
        # 현재 강의의 시작 시간이 마지막 선택된 강의의 종료 시간 이후이면 선택
        if start >= last_end:
            selected.append(idx)
            last_end = end  # 종료 시간 갱신

    return len(selected), selected


# ============================================================
#  문제 5: DP (Week 06)
#  계단 오르기 (Climbing Stairs with Cost)
# ============================================================

def problem5_description():
    """문제 5: 계단 오르기 (Climbing Stairs)."""
    print("""
  문제 5: DP (Week 06)
  ==============================
  n개의 계단이 있고, 한 번에 1칸 또는 2칸을 오를 수 있다.
  각 계단 i에는 비용 cost[i]가 있다.
  계단 0 또는 계단 1에서 출발할 수 있다.
  꼭대기(n번째 위치)에 도달하기 위한 최소 비용을 구하라.

  예: cost = [10, 15, 20]
  -> 답: 15 (계단 1에서 출발하여 2칸 점프 -> 비용 15)

  예: cost = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
  -> 답: 6
""")


def problem5_skeleton(cost):
    """계단 오르기 skeleton -- 직접 구현해 보세요.

    Args:
        cost: 각 계단의 비용 리스트

    Returns:
        꼭대기까지의 최소 비용
    """
    # TODO: 구현하세요
    pass


def problem5_solution(cost):
    """계단 오르기 풀이.

    알고리즘: 바텀업 DP로 각 계단까지의 최소 비용을 계산
    점화식: dp[i] = cost[i] + min(dp[i-1], dp[i-2])
      - i번째 계단에 도달하려면 i-1 또는 i-2번째에서 올 수 있음
      - 두 경우 중 비용이 작은 쪽을 선택
    최종 답: min(dp[n-1], dp[n-2]) - 마지막 또는 그 전 계단에서 꼭대기로 점프

    시간 복잡도: O(n) - 계단 수만큼 한 번 순회
    공간 복잡도: O(1) - 이전 두 값만 유지 (공간 최적화)
    """
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    # 공간 최적화: dp 배열 대신 이전 두 값만 유지
    prev2 = cost[0]  # dp[i-2]에 해당
    prev1 = cost[1]  # dp[i-1]에 해당

    for i in range(2, n):
        current = cost[i] + min(prev1, prev2)  # 점화식 적용
        prev2, prev1 = prev1, current  # 슬라이딩 윈도우 방식으로 갱신

    # 꼭대기에 도달: 마지막 계단 또는 그 전 계단에서 점프
    return min(prev1, prev2)


# ============================================================
#  메인 실행
#  5개 문제를 순서대로 출제하고 풀이를 확인한다
# ============================================================

if __name__ == "__main__":
    print("=" * 65)
    print(" 전반부 알고리즘 총정리 -- 5개 미니 문제")
    print("=" * 65)

    # --- 문제 1: 복잡도 분석 ---
    print(f"\n{'='*65}")
    problem1_description()
    input("  [Enter]를 누르면 풀이를 확인합니다...")
    problem1_solution()

    # --- 문제 2: 정렬 ---
    print(f"\n{'='*65}")
    problem2_description()
    input("  [Enter]를 누르면 풀이를 확인합니다...")

    test_arr = [38, 27, 43, 3, 9, 82, 10]
    sorted_arr, count = problem2_solution(test_arr[:])
    print(f"  입력: {test_arr}")
    print(f"  정렬: {sorted_arr}")
    print(f"  merge 횟수: {count}")

    # --- 문제 3: 분할정복 ---
    print(f"\n{'='*65}")
    problem3_description()
    input("  [Enter]를 누르면 풀이를 확인합니다...")

    test_arr = [3, 7, 2, 9, 1, 8, 4, 6, 5]
    max_val, comparisons = problem3_solution(test_arr)
    print(f"  입력: {test_arr}")
    print(f"  최대값: {max_val}")
    print(f"  비교 횟수: {comparisons} (이론적 최소: {len(test_arr) - 1})")

    # --- 문제 4: 그리디 ---
    print(f"\n{'='*65}")
    problem4_description()
    input("  [Enter]를 누르면 풀이를 확인합니다...")

    lectures = [(1, 3), (2, 5), (3, 6), (5, 7), (6, 8), (8, 10), (9, 11)]
    count, selected = problem4_solution(lectures)
    print(f"  강의 목록: {lectures}")
    print(f"  최대 강의 수: {count}")
    print(f"  선택된 강의: {[lectures[i] for i in selected]}")

    # --- 문제 5: DP ---
    print(f"\n{'='*65}")
    problem5_description()
    input("  [Enter]를 누르면 풀이를 확인합니다...")

    cost1 = [10, 15, 20]
    cost2 = [1, 100, 1, 1, 1, 100, 1, 1, 100, 1]
    print(f"  cost = {cost1} -> 최소 비용: {problem5_solution(cost1)}")
    print(f"  cost = {cost2} -> 최소 비용: {problem5_solution(cost2)}")

    # --- 요약 ---
    print(f"\n{'='*65}")
    print(" 요약")
    print("=" * 65)
    print("""
  문제 1 (복잡도):  중첩 루프 분석, O(n log n)
  문제 2 (정렬):    Merge Sort, O(n log n), 안정 정렬
  문제 3 (분할정복): 배열 최대값, T(n) = 2T(n/2) + 1
  문제 4 (그리디):  Activity Selection, 종료시간 기준 정렬
  문제 5 (DP):     계단 오르기, dp[i] = cost[i] + min(dp[i-1], dp[i-2])

  시험 팁:
  - 복잡도 분석: 루프 구조를 정확히 파악 (특히 i *= 2 같은 패턴)
  - 정렬: 각 정렬 알고리즘의 시간/공간 복잡도, 안정성 암기
  - 분할정복: 재귀식 세우기 + Master Theorem 적용
  - 그리디: 탐욕 선택 속성이 왜 성립하는지 설명 가능해야 함
  - DP: 부분 문제 정의 -> 재귀식 -> 베이스 케이스 -> 순서
""")
