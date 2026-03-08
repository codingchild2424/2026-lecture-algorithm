# === A-1: 기본 정렬 알고리즘 ===
# 선택 정렬, 버블 정렬, 삽입 정렬의 구현
# 세 알고리즘 모두 시간복잡도 O(n^2), 공간복잡도 O(n) (복사본 사용)
"""Basic sorting algorithms - implement the TODOs."""
import random


def selection_sort(arr):
    """
    선택 정렬 (Selection Sort)
    - 알고리즘: 정렬되지 않은 부분에서 최솟값을 찾아 현재 위치와 교환
    - 시간복잡도: O(n^2) — 항상 모든 쌍을 비교
    - 공간복잡도: O(1) (in-place, 복사본 제외)
    - 특징: 교환 횟수가 O(n)으로 적음, 불안정 정렬
    """
    a = arr[:]  # 원본 배열 보존을 위해 복사
    n = len(a)
    for i in range(n):
        min_idx = i  # 현재 위치를 최솟값 인덱스로 가정
        # 정렬되지 않은 나머지 부분에서 최솟값 탐색
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # 찾은 최솟값을 현재 위치로 교환
        a[i], a[min_idx] = a[min_idx], a[i]
    return a


def bubble_sort(arr):
    """
    버블 정렬 (Bubble Sort)
    - 알고리즘: 인접한 두 원소를 비교하여 큰 값을 뒤로 교환 (반복)
    - 시간복잡도: O(n^2) 최악/평균, O(n) 최선 (이미 정렬된 경우)
    - 공간복잡도: O(1) (in-place, 복사본 제외)
    - 특징: 조기 종료 최적화 적용 — 교환이 없으면 정렬 완료
    """
    a = arr[:]  # 원본 배열 보존을 위해 복사
    n = len(a)
    for i in range(n):
        swapped = False  # 이번 패스에서 교환 발생 여부 추적
        # 매 패스마다 가장 큰 원소가 끝으로 이동하므로 범위 축소
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]  # 인접 원소 교환
                swapped = True
        # 교환이 한 번도 없었으면 이미 정렬 완료 → 조기 종료
        if not swapped:
            break
    return a


def insertion_sort(arr):
    """
    삽입 정렬 (Insertion Sort)
    - 알고리즘: 각 원소를 이미 정렬된 앞부분의 올바른 위치에 삽입
    - 시간복잡도: O(n^2) 최악/평균, O(n) 최선 (이미 정렬된 경우)
    - 공간복잡도: O(1) (in-place, 복사본 제외)
    - 특징: 거의 정렬된 데이터에서 매우 효율적, 안정 정렬
    """
    a = arr[:]  # 원본 배열 보존을 위해 복사
    for i in range(1, len(a)):
        key = a[i]  # 삽입할 원소를 임시 저장
        j = i - 1
        # key보다 큰 원소들을 오른쪽으로 한 칸씩 이동
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        # key를 올바른 위치에 삽입
        a[j + 1] = key
    return a


if __name__ == "__main__":
    test_data = [64, 34, 25, 12, 22, 11, 90]
    print(f"Original: {test_data}")
    print(f"Selection Sort: {selection_sort(test_data)}")
    print(f"Bubble Sort:    {bubble_sort(test_data)}")
    print(f"Insertion Sort: {insertion_sort(test_data)}")

    # 무작위 데이터 100회로 정확성 검증
    for _ in range(100):
        data = [random.randint(-100, 100) for _ in range(50)]
        expected = sorted(data)
        assert selection_sort(data) == expected, "Selection Sort failed!"
        assert bubble_sort(data) == expected, "Bubble Sort failed!"
        assert insertion_sort(data) == expected, "Insertion Sort failed!"
    print("\nAll tests passed!")
