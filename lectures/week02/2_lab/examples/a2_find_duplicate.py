# === A-2: 중복 원소 존재 여부 판별 ===
# 배열에 중복 원소가 있는지 판별하는 두 가지 알고리즘을 비교합니다.
# - 브루트포스(Brute Force): O(n²) — 모든 쌍을 비교
# - 해시셋(HashSet): O(n) — set을 사용한 선형 탐색
#
# N이 커질수록 O(n²)과 O(n)의 성능 차이가 극적으로 벌어지는 것을 확인합니다.
"""Find duplicate element - O(n^2) vs O(n) comparison.

NOTE: The n=50,000 brute-force case may take several minutes due to O(n^2)
complexity. This is intentional -- it demonstrates why quadratic algorithms
become impractical at scale. Reduce the last test size if you need faster runs.
"""
import random
from a1_timer_util import measure_time


def has_duplicate_bruteforce(arr):
    """
    브루트포스 중복 판별: 모든 원소 쌍을 비교합니다.

    알고리즘: 이중 반복문으로 arr[i]와 arr[j] (j > i)를 모두 비교
    시간 복잡도: O(n²) — n*(n-1)/2 번의 비교
    공간 복잡도: O(1) — 추가 메모리 사용 없음
    """
    n = len(arr)
    for i in range(n):  # 각 원소에 대해
        for j in range(i + 1, n):  # 그 뒤의 모든 원소와 비교
            if arr[i] == arr[j]:  # 같은 값이 있으면 중복 발견
                return True
    return False  # 모든 쌍을 비교해도 중복 없음


def has_duplicate_hashset(arr):
    """
    해시셋 중복 판별: set 자료구조를 활용하여 이미 본 원소를 추적합니다.

    알고리즘: 배열을 순회하며 각 원소가 set에 있는지 확인
    시간 복잡도: O(n) — set의 탐색/삽입이 평균 O(1)
    공간 복잡도: O(n) — 최악의 경우 모든 원소를 set에 저장
    """
    seen = set()  # 이미 확인한 원소를 저장하는 해시셋
    for x in arr:
        if x in seen:  # set에서 O(1) 탐색 → 중복 발견
            return True
        seen.add(x)  # 처음 보는 원소는 set에 추가
    return False  # 모든 원소가 고유함


if __name__ == "__main__":
    # 벤치마크 결과 테이블 헤더
    print(f"{'N':>10} | {'O(n²)':>12} | {'O(n)':>12} | {'Speedup':>8}")
    print("-" * 50)

    for n in [100, 1000, 10000, 50000]:
        # 중복 없는 데이터 생성 (최악의 경우: 모든 원소를 끝까지 비교해야 함)
        data = list(range(n))  # No duplicates (worst case for both)
        random.shuffle(data)  # 순서를 섞어 편향 방지

        t1, _ = measure_time(has_duplicate_bruteforce, data)  # O(n²) 측정
        t2, _ = measure_time(has_duplicate_hashset, data)  # O(n) 측정
        speedup = t1 / t2 if t2 > 0 else float('inf')  # 속도 향상 비율 계산

        print(f"{n:>10,} | {t1:>12.6f} | {t2:>12.6f} | {speedup:>7.1f}x")
