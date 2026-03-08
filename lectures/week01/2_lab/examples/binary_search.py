# === 이진 탐색 (Binary Search) ===
# 정렬된 배열에서 특정 값을 효율적으로 찾는 알고리즘
# 반복(iterative) 방식과 재귀(recursive) 방식 두 가지 구현을 비교합니다.
#
# 시간 복잡도: O(log n) — 매 단계마다 탐색 범위가 절반으로 줄어듦
# 공간 복잡도: 반복 방식 O(1), 재귀 방식 O(log n) (호출 스택)
"""Binary Search - Iterative and Recursive implementations."""


def binary_search_iterative(arr, target):
    """
    반복적 이진 탐색: 정렬된 배열 arr에서 target의 인덱스를 반환합니다.
    찾지 못하면 -1을 반환합니다.

    알고리즘:
      1. 탐색 범위의 왼쪽(left)과 오른쪽(right) 경계를 설정
      2. 중간값(mid)과 target을 비교
      3. target이 더 크면 오른쪽 절반, 더 작으면 왼쪽 절반으로 범위를 좁힘
      4. 범위가 유효하지 않으면(left > right) 탐색 실패

    시간 복잡도: O(log n)
    공간 복잡도: O(1) — 추가 메모리 사용 없음
    """
    left, right = 0, len(arr) - 1  # 탐색 범위 초기화: 배열 전체
    while left <= right:  # 탐색 범위가 유효한 동안 반복
        mid = (left + right) // 2  # 중간 인덱스 계산 (정수 나눗셈)
        if arr[mid] == target:  # 중간값이 target과 일치하면 탐색 성공
            return mid
        elif arr[mid] < target:  # 중간값이 target보다 작으면 오른쪽 절반 탐색
            left = mid + 1
        else:  # 중간값이 target보다 크면 왼쪽 절반 탐색
            right = mid - 1
    return -1  # 탐색 범위를 모두 소진 → target이 배열에 없음


def binary_search_recursive(arr, target, left, right):
    """
    재귀적 이진 탐색: 정렬된 배열 arr[left..right]에서 target의 인덱스를 반환합니다.
    찾지 못하면 -1을 반환합니다.

    알고리즘:
      - 기저 조건(base case): left > right이면 탐색 실패
      - 재귀 단계: 중간값 비교 후 절반의 부분 배열에 대해 재귀 호출

    시간 복잡도: O(log n)
    공간 복잡도: O(log n) — 재귀 호출 스택 깊이
    """
    if left > right:  # 기저 조건: 탐색 범위가 비어있으면 실패
        return -1
    mid = (left + right) // 2  # 중간 인덱스 계산
    if arr[mid] == target:  # 중간값이 target이면 탐색 성공
        return mid
    elif arr[mid] < target:  # target이 오른쪽 절반에 있음
        return binary_search_recursive(arr, target, mid + 1, right)
    else:  # target이 왼쪽 절반에 있음
        return binary_search_recursive(arr, target, left, mid - 1)


if __name__ == "__main__":
    data = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]  # 정렬된 테스트 배열
    target = 7  # 찾고자 하는 값

    # 반복적 이진 탐색 실행
    idx = binary_search_iterative(data, target)
    print(f"Iterative: {target} found at index {idx}")

    # 재귀적 이진 탐색 실행
    idx = binary_search_recursive(data, target, 0, len(data) - 1)
    print(f"Recursive: {target} found at index {idx}")

    # 단계별 추적(trace): 이진 탐색이 범위를 좁혀가는 과정을 시각화
    print(f"\n--- Binary Search Trace for target={target} ---")
    left, right = 0, len(data) - 1
    step = 1
    while left <= right:
        mid = (left + right) // 2
        print(f"Step {step}: range=[{left},{right}], mid={mid}, arr[mid]={data[mid]}")
        if data[mid] == target:
            print(f"  -> Found at index {mid}!")
            break
        elif data[mid] < target:
            print(f"  -> {data[mid]} < {target}, search right half")
            left = mid + 1  # 오른쪽 절반으로 범위 축소
        else:
            print(f"  -> {data[mid]} > {target}, search left half")
            right = mid - 1  # 왼쪽 절반으로 범위 축소
        step += 1
