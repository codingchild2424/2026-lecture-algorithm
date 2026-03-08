# === A-1: 병합 정렬 추적 ===
# 병합 정렬의 재귀 호출 과정을 단계별로 시각화
# 분할(Divide) → 정복(Conquer) → 병합(Combine) 과정을 들여쓰기로 표현
"""Merge Sort with step-by-step tracing."""


def merge_sort_trace(arr, depth=0):
    """
    병합 정렬 + 재귀 호출 시각화
    - 알고리즘: 배열을 반으로 분할 → 재귀 정렬 → 두 정렬된 배열 병합
    - 시간복잡도: O(n log n)
    - 공간복잡도: O(n log n) — 재귀 깊이 O(log n) x 각 레벨 O(n)
    - depth 매개변수로 재귀 깊이를 추적하여 들여쓰기 출력
    """
    indent = "  " * depth  # 재귀 깊이에 따른 들여쓰기
    print(f"{indent}merge_sort({arr})")

    # 기저 조건: 원소가 1개 이하이면 더 이상 분할 불가
    if len(arr) <= 1:
        return arr[:]

    mid = len(arr) // 2  # 중간 인덱스로 분할 지점 결정
    left = merge_sort_trace(arr[:mid], depth + 1)    # 왼쪽 절반 재귀 정렬
    right = merge_sort_trace(arr[mid:], depth + 1)   # 오른쪽 절반 재귀 정렬

    # 병합 단계: 두 정렬된 부분 배열을 하나로 합침
    merged = []
    i = j = 0  # 왼쪽/오른쪽 배열의 현재 비교 위치
    # 두 배열에서 작은 원소를 순서대로 선택
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    # 한쪽 배열이 소진된 후 나머지 원소 추가
    merged.extend(left[i:])
    merged.extend(right[j:])

    print(f"{indent}  -> merged: {merged}")  # 병합 결과 출력
    return merged


if __name__ == "__main__":
    data = [38, 27, 43, 3, 9, 82, 10]
    print("=== Merge Sort Trace ===\n")
    result = merge_sort_trace(data)
    print(f"\nFinal result: {result}")
