"""
전반부 알고리즘 총정리 -- 5개 미니 문제

Week 02~06의 핵심 알고리즘을 각 1문제씩 복습한다.
각 문제에 skeleton 함수와 solution 함수가 있다.
먼저 skeleton을 직접 구현해 본 후, solution과 비교한다.
"""


# ============================================================
#  문제 1: 복잡도 분석 (Week 02)
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
    """문제 1 풀이."""
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
    # 검증
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

    result = mystery(16)
    print(f"  검증: mystery(16) = {result}")


# ============================================================
#  문제 2: 정렬 응용 (Week 03)
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

    시간 복잡도: O(n log n)
    공간 복잡도: O(n)
    """
    merge_count = [0]  # 리스트로 감싸서 내부 함수에서 수정 가능하게

    def merge_sort(a):
        if len(a) <= 1:
            return a

        mid = len(a) // 2
        left = merge_sort(a[:mid])
        right = merge_sort(a[mid:])

        return merge(left, right)

    def merge(left, right):
        merge_count[0] += 1
        result = []
        i = j = 0

        while i < len(left) and j < len(right):
            if left[i] <= right[j]:  # <= for stability
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1

        result.extend(left[i:])
        result.extend(right[j:])
        return result

    sorted_arr = merge_sort(arr)
    return sorted_arr, merge_count[0]


# ============================================================
#  문제 3: 분할정복 (Week 04)
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

    시간 복잡도: O(n)
    비교 횟수: n - 1 (최적)
    T(n) = 2T(n/2) + 1 -> O(n)
    """
    comparisons = [0]

    def find_max(a, lo, hi):
        if lo == hi:
            return a[lo]

        mid = (lo + hi) // 2
        left_max = find_max(a, lo, mid)
        right_max = find_max(a, mid + 1, hi)

        comparisons[0] += 1
        return left_max if left_max >= right_max else right_max

    if not arr:
        return None, 0

    result = find_max(arr, 0, len(arr) - 1)
    return result, comparisons[0]


# ============================================================
#  문제 4: 그리디 (Week 05)
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

    그리디 전략: 종료 시간이 빠른 순으로 정렬 후, 겹치지 않는 강의를 선택.
    시간 복잡도: O(n log n)
    """
    # (종료시간, 시작시간, 원래 인덱스) 기준 정렬
    indexed = [(end, start, i) for i, (start, end) in enumerate(lectures)]
    indexed.sort()

    selected = []
    last_end = -1

    for end, start, idx in indexed:
        if start >= last_end:
            selected.append(idx)
            last_end = end

    return len(selected), selected


# ============================================================
#  문제 5: DP (Week 06)
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

    dp[i] = i번째 계단에 도달하기까지의 최소 비용
    dp[i] = cost[i] + min(dp[i-1], dp[i-2])

    시간 복잡도: O(n)
    공간 복잡도: O(1) (최적화 시)
    """
    n = len(cost)
    if n == 0:
        return 0
    if n == 1:
        return cost[0]

    # 공간 최적화 버전
    prev2 = cost[0]
    prev1 = cost[1]

    for i in range(2, n):
        current = cost[i] + min(prev1, prev2)
        prev2, prev1 = prev1, current

    # 꼭대기에 도달: 마지막 계단 또는 그 전 계단에서 점프
    return min(prev1, prev2)


# ============================================================
#  메인 실행
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
