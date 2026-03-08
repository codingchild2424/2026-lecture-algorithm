# === A-2: Randomized Select (Quickselect) — 상세 구현 ===
# k번째 작은 원소를 정렬 없이 평균 O(n)에 찾는 알고리즘
# 성능 비교 벤치마크 포함 (Quickselect vs Sort+index)
"""
Randomized Select (Quickselect) — k번째 작은 원소 찾기
정렬 없이 평균 O(n)에 k번째 작은 원소를 찾습니다.
"""

import random
import time


def partition(arr, left, right, pivot_idx):
    """
    피벗을 기준으로 파티션합니다.
    - Lomuto 파티션 스킴 사용
    - 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 이동합니다.
    - 시간복잡도: O(right - left) — 범위 내 원소를 한 번씩 순회
    - Returns: 피벗의 최종 위치
    """
    pivot_val = arr[pivot_idx]
    # 피벗을 끝으로 이동 — 파티션 중 피벗이 방해되지 않도록
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    store_idx = left  # 피벗보다 작은 원소가 배치될 다음 위치
    for i in range(left, right):
        # 피벗보다 작은 원소를 발견하면 store_idx 위치로 교환
        if arr[i] < pivot_val:
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1
    # 피벗을 최종 위치로 — store_idx 왼쪽은 모두 피벗보다 작고 오른쪽은 큼
    arr[store_idx], arr[right] = arr[right], arr[store_idx]
    return store_idx


def randomized_select(arr, left, right, k):
    """
    arr[left..right]에서 k번째(0-indexed) 작은 원소를 찾습니다.
    - 알고리즘: 랜덤 피벗 선택 → 파티션 → 피벗 위치에 따라 한쪽만 재귀
    - 평균 시간복잡도: O(n) — T(n) = T(n/2) + O(n)
    - 최악 시간복잡도: O(n^2) — 피벗이 항상 최솟값/최댓값일 때
    - 핵심 아이디어: 퀵 정렬과 달리 한쪽만 재귀하므로 선형 시간 달성
    """
    # 기저 조건: 범위에 원소가 1개이면 그것이 답
    if left == right:
        return arr[left]

    # 랜덤 피벗 선택 — 최악의 경우를 확률적으로 방지
    pivot_idx = random.randint(left, right)
    pivot_idx = partition(arr, left, right, pivot_idx)

    # 피벗의 최종 위치와 k를 비교하여 탐색 범위 결정
    if k == pivot_idx:
        return arr[k]  # 피벗 자체가 k번째 원소
    elif k < pivot_idx:
        return randomized_select(arr, left, pivot_idx - 1, k)   # 왼쪽 부분만 탐색
    else:
        return randomized_select(arr, pivot_idx + 1, right, k)  # 오른쪽 부분만 탐색


def kth_smallest(arr, k):
    """
    배열에서 k번째(1-indexed) 작은 원소를 찾습니다.
    - 원본 배열을 변경하지 않기 위해 복사본 사용
    - k 범위 검증 포함 (1 <= k <= len(arr))
    """
    if k < 1 or k > len(arr):
        raise ValueError(f"k={k} is out of range [1, {len(arr)}]")
    a = arr[:]  # 원본 보존 — partition이 배열을 in-place로 변경하므로
    return randomized_select(a, 0, len(a) - 1, k - 1)


def kth_smallest_sort(arr, k):
    """
    정렬 기반 방법: O(n log n)
    - 전체 배열을 정렬한 후 k-1 인덱스에 접근
    - Quickselect와 성능 비교를 위한 참조 구현
    """
    return sorted(arr)[k - 1]


if __name__ == "__main__":
    print("=" * 60)
    print("Randomized Select (Quickselect) Demo")
    print("=" * 60)

    # 정확성 검증: Quickselect 결과와 정렬 기반 결과 비교
    data = [7, 10, 4, 3, 20, 15, 8]
    print(f"\n배열: {data}")
    print(f"정렬: {sorted(data)}")
    print()

    for k in range(1, len(data) + 1):
        qs_result = kth_smallest(data, k)
        sort_result = kth_smallest_sort(data, k)
        status = "OK" if qs_result == sort_result else "MISMATCH"
        print(f"  {k}번째 작은 수: {qs_result} ({status})")

    # 성능 비교: 다양한 입력 크기에서 Quickselect vs Sort
    # Quickselect는 O(n), Sort는 O(n log n)이므로 n이 클수록 차이가 커짐
    print("\n" + "=" * 60)
    print("성능 비교: Quickselect vs Sort")
    print("=" * 60)

    for n in [100_000, 500_000, 1_000_000]:
        big_data = [random.randint(1, 10**9) for _ in range(n)]
        k = n // 2  # 중앙값 찾기 — 가장 불리한 위치

        # Quickselect 측정
        start = time.perf_counter()
        result_qs = kth_smallest(big_data, k)
        t_qs = time.perf_counter() - start

        # Sort + index 측정
        start = time.perf_counter()
        result_sort = kth_smallest_sort(big_data, k)
        t_sort = time.perf_counter() - start

        speedup = t_sort / t_qs if t_qs > 0 else float("inf")
        print(f"\n  N = {n:>10,}, k = {k:,} (중앙값)")
        print(f"    Quickselect:  {t_qs:.4f}초")
        print(f"    Sort+index:   {t_sort:.4f}초")
        print(f"    Speedup:      {speedup:.1f}x")
