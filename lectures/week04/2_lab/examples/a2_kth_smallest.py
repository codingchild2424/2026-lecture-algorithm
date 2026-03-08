# === A-2: k번째 최솟값 찾기 (Randomized Select) ===
# 정렬 없이 평균 O(n) 시간에 k번째 작은 원소를 찾는 알고리즘
# 퀵 정렬의 파티션을 활용한 선택 알고리즘 (Quickselect)
"""Randomized Select - find k-th smallest element in O(n) average."""
import random


def partition(arr, left, right, pivot_idx):
    """
    Lomuto 파티션 스킴
    - 피벗을 기준으로 배열을 두 부분으로 분할
    - 피벗보다 작은 원소는 왼쪽, 큰 원소는 오른쪽으로 배치
    - 시간복잡도: O(n) — 범위 내 모든 원소를 한 번씩 비교
    - 반환값: 피벗의 최종 위치 (인덱스)
    """
    pivot = arr[pivot_idx]
    # 피벗을 배열 끝으로 이동 (파티션 과정에서 방해되지 않도록)
    arr[pivot_idx], arr[right] = arr[right], arr[pivot_idx]
    store = left  # 피벗보다 작은 원소가 저장될 다음 위치
    for i in range(left, right):
        # 현재 원소가 피벗보다 작으면 store 위치로 교환
        if arr[i] < pivot:
            arr[i], arr[store] = arr[store], arr[i]
            store += 1
    # 피벗을 최종 위치(store)로 이동
    arr[store], arr[right] = arr[right], arr[store]
    return store


def randomized_select(arr, left, right, k):
    """
    Randomized Select (Quickselect)
    - arr[left..right] 범위에서 k번째(0-indexed) 작은 원소를 찾음
    - 알고리즘: 랜덤 피벗으로 파티션 후, k가 있는 쪽만 재귀 탐색
    - 시간복잡도: O(n) 평균, O(n^2) 최악
    - 공간복잡도: O(log n) 평균 (재귀 스택), O(n) 최악
    - 핵심: 퀵 정렬과 달리 한쪽만 재귀하므로 평균 O(n)
    """
    # 기저 조건: 원소가 1개이면 그것이 답
    if left == right:
        return arr[left]

    # 랜덤 피벗 선택 → 최악의 경우를 확률적으로 회피
    pivot_idx = random.randint(left, right)
    pivot_idx = partition(arr, left, right, pivot_idx)

    # 피벗 위치와 k를 비교하여 탐색 방향 결정
    if k == pivot_idx:
        return arr[k]           # 피벗이 k번째 원소
    elif k < pivot_idx:
        return randomized_select(arr, left, pivot_idx - 1, k)   # 왼쪽 탐색
    else:
        return randomized_select(arr, pivot_idx + 1, right, k)  # 오른쪽 탐색


def kth_smallest(arr, k):
    """
    k번째 작은 원소 찾기 (1-indexed 인터페이스)
    - 원본 배열을 변경하지 않기 위해 복사본 사용
    - 내부적으로 0-indexed randomized_select 호출
    """
    a = arr[:]  # 원본 보존을 위한 복사
    return randomized_select(a, 0, len(a) - 1, k - 1)


if __name__ == "__main__":
    data = [7, 10, 4, 3, 20, 15, 8]
    print(f"Array: {data}")
    print(f"Sorted: {sorted(data)}")
    for k in range(1, len(data) + 1):
        result = kth_smallest(data, k)
        print(f"  {k}-th smallest: {result}")

    # 성능 비교: Quickselect O(n) vs 정렬 후 인덱스 접근 O(n log n)
    import time
    n = 1000000
    big_data = [random.randint(1, 10**9) for _ in range(n)]

    start = time.perf_counter()
    result1 = kth_smallest(big_data, n // 2)
    t1 = time.perf_counter() - start

    start = time.perf_counter()
    result2 = sorted(big_data)[n // 2 - 1]
    t2 = time.perf_counter() - start

    print(f"\nN={n:,}, finding median:")
    print(f"  Randomized Select: {t1:.4f}s (result={result1})")
    print(f"  Sort + index:      {t2:.4f}s (result={result2})")
