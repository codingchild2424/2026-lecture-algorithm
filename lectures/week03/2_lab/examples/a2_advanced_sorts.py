# === A-2: 고급 정렬 알고리즘 ===
# 병합 정렬과 퀵 정렬 — 분할 정복(Divide and Conquer) 기반 정렬
# 두 알고리즘 모두 평균 시간복잡도 O(n log n)
"""Advanced sorting algorithms - Merge Sort and Quick Sort."""
import random


def merge_sort(arr):
    """
    병합 정렬 (Merge Sort)
    - 알고리즘: 배열을 반으로 분할 → 재귀적으로 정렬 → 병합
    - 시간복잡도: O(n log n) — 항상 동일 (최선/평균/최악)
    - 공간복잡도: O(n) — 병합 시 추가 배열 필요
    - 특징: 안정 정렬, 데이터 분포에 무관하게 일정한 성능
    """
    # 기저 조건: 원소가 1개 이하이면 이미 정렬됨
    if len(arr) <= 1:
        return arr[:]
    mid = len(arr) // 2  # 배열을 절반으로 분할
    left = merge_sort(arr[:mid])    # 왼쪽 절반 재귀 정렬
    right = merge_sort(arr[mid:])   # 오른쪽 절반 재귀 정렬
    return _merge(left, right)      # 정렬된 두 부분을 병합


def _merge(left, right):
    """
    두 정렬된 배열을 하나의 정렬된 배열로 병합
    - 두 배열의 앞에서부터 비교하며 작은 원소를 순서대로 추가
    - 시간복잡도: O(n) — 각 원소를 한 번씩만 처리
    """
    result = []
    i = j = 0  # 각 배열의 현재 비교 위치
    # 두 배열 모두 원소가 남아있는 동안 비교하며 병합
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])  # 왼쪽이 작거나 같으면 왼쪽 추가 (안정 정렬 보장)
            i += 1
        else:
            result.append(right[j])  # 오른쪽이 작으면 오른쪽 추가
            j += 1
    # 남은 원소를 결과에 추가 (한쪽이 먼저 소진되었으므로)
    result.extend(left[i:])
    result.extend(right[j:])
    return result


def quick_sort(arr):
    """
    퀵 정렬 (Quick Sort)
    - 알고리즘: 피벗 선택 → 피벗 기준으로 분할 → 재귀 정렬 → 결합
    - 시간복잡도: O(n log n) 평균, O(n^2) 최악 (피벗이 항상 최솟/최댓값일 때)
    - 공간복잡도: O(n) — 리스트 컴프리헨션 방식으로 추가 공간 사용
    - 특징: 실제로 가장 빠른 범용 정렬 중 하나, 캐시 효율이 좋음
    - 이 구현은 간결한 3-way 파티션 방식 (Dutch National Flag)
    """
    # 기저 조건: 원소가 1개 이하이면 이미 정렬됨
    if len(arr) <= 1:
        return arr[:]
    pivot = arr[len(arr) // 2]  # 중간 원소를 피벗으로 선택
    # 3-way 파티션: 피벗보다 작은/같은/큰 원소로 분류
    left = [x for x in arr if x < pivot]      # 피벗보다 작은 원소
    middle = [x for x in arr if x == pivot]    # 피벗과 같은 원소
    right = [x for x in arr if x > pivot]      # 피벗보다 큰 원소
    # 왼쪽과 오른쪽을 재귀 정렬하고 결합
    return quick_sort(left) + middle + quick_sort(right)


if __name__ == "__main__":
    test_data = [38, 27, 43, 3, 9, 82, 10]
    print(f"Original:   {test_data}")
    print(f"Merge Sort: {merge_sort(test_data)}")
    print(f"Quick Sort: {quick_sort(test_data)}")

    # 무작위 데이터 100회로 정확성 검증
    for _ in range(100):
        data = [random.randint(-100, 100) for _ in range(50)]
        expected = sorted(data)
        assert merge_sort(data) == expected, "Merge Sort failed!"
        assert quick_sort(data) == expected, "Quick Sort failed!"
    print("\nAll tests passed!")
