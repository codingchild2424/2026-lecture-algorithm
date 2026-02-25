"""
Randomized Select (Quickselect) — k번째 작은 원소 찾기
정렬 없이 평균 O(n)에 k번째 작은 원소를 찾습니다.
"""

import random
import time


def partition(arr, left, right, pivot_idx):
    """
    피벗을 기준으로 파티션합니다.
    피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 이동합니다.
    Returns: 피벗의 최종 위치
    """
    pivot_val = arr[pivot_idx]
    # 피벗을 끝으로 이동
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    store_idx = left
    for i in range(left, right):
        if arr[i] < pivot_val:
            arr[i], arr[store_idx] = arr[store_idx], arr[i]
            store_idx += 1
    # 피벗을 최종 위치로
    arr[store_idx], arr[right] = arr[right], arr[store_idx]
    return store_idx


def randomized_select(arr, left, right, k):
    """
    arr[left..right]에서 k번째(0-indexed) 작은 원소를 찾습니다.
    평균 시간복잡도: O(n)
    최악 시간복잡도: O(n^2) — 피벗이 항상 최솟값/최댓값일 때
    """
    if left == right:
        return arr[left]

    # 랜덤 피벗 선택
    pivot_idx = random.randint(left, right)
    pivot_idx = partition(arr, left, right, pivot_idx)

    if k == pivot_idx:
        return arr[k]
    elif k < pivot_idx:
        return randomized_select(arr, left, pivot_idx - 1, k)
    else:
        return randomized_select(arr, pivot_idx + 1, right, k)


def kth_smallest(arr, k):
    """
    배열에서 k번째(1-indexed) 작은 원소를 찾습니다.
    원본 배열을 변경하지 않습니다.
    """
    if k < 1 or k > len(arr):
        raise ValueError(f"k={k} is out of range [1, {len(arr)}]")
    a = arr[:]
    return randomized_select(a, 0, len(a) - 1, k - 1)


def kth_smallest_sort(arr, k):
    """
    정렬 기반 방법: O(n log n)
    비교를 위한 참조 구현.
    """
    return sorted(arr)[k - 1]


if __name__ == "__main__":
    print("=" * 60)
    print("Randomized Select (Quickselect) Demo")
    print("=" * 60)

    # 정확성 검증
    data = [7, 10, 4, 3, 20, 15, 8]
    print(f"\n배열: {data}")
    print(f"정렬: {sorted(data)}")
    print()

    for k in range(1, len(data) + 1):
        qs_result = kth_smallest(data, k)
        sort_result = kth_smallest_sort(data, k)
        status = "OK" if qs_result == sort_result else "MISMATCH"
        print(f"  {k}번째 작은 수: {qs_result} ({status})")

    # 성능 비교
    print("\n" + "=" * 60)
    print("성능 비교: Quickselect vs Sort")
    print("=" * 60)

    for n in [100_000, 500_000, 1_000_000]:
        big_data = [random.randint(1, 10**9) for _ in range(n)]
        k = n // 2  # 중앙값 찾기

        # Quickselect
        start = time.perf_counter()
        result_qs = kth_smallest(big_data, k)
        t_qs = time.perf_counter() - start

        # Sort + index
        start = time.perf_counter()
        result_sort = kth_smallest_sort(big_data, k)
        t_sort = time.perf_counter() - start

        speedup = t_sort / t_qs if t_qs > 0 else float("inf")
        print(f"\n  N = {n:>10,}, k = {k:,} (중앙값)")
        print(f"    Quickselect:  {t_qs:.4f}초")
        print(f"    Sort+index:   {t_sort:.4f}초")
        print(f"    Speedup:      {speedup:.1f}x")
