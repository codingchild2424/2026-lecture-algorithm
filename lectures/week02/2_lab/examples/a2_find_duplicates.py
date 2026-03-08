# === A-2: 중복 원소 찾기 (모든 중복 원소 반환) ===
# 배열에서 중복된 모든 원소를 찾아 반환하는 두 가지 알고리즘을 비교합니다.
# - 브루트포스(Brute Force): O(n²) — 이중 루프로 모든 쌍 비교
# - 해시셋(HashSet): O(n) — set 두 개를 사용한 선형 탐색
#
# a2_find_duplicate.py와의 차이:
#   - find_duplicate: 중복 "존재 여부"만 판별 (True/False)
#   - find_duplicates: 중복된 "모든 원소"를 찾아 반환 (set)
"""
중복 원소 찾기 — O(n^2) vs O(n) 비교
"""

import time
import random


def find_duplicates_bruteforce(arr):
    """
    브루트포스로 모든 중복 원소를 찾습니다.

    알고리즘: 이중 반복문으로 모든 (i, j) 쌍을 비교하여 같은 값을 수집
    시간 복잡도: O(n²) — n*(n-1)/2 번의 비교
    공간 복잡도: O(d) — d는 중복 원소의 개수
    """
    duplicates = set()  # 발견된 중복 원소를 저장할 set
    n = len(arr)
    for i in range(n):  # 각 원소에 대해
        for j in range(i + 1, n):  # 뒤의 모든 원소와 비교
            if arr[i] == arr[j]:  # 같은 값이면 중복
                duplicates.add(arr[i])  # 중복 원소 기록
    return duplicates


def find_duplicates_hashset(arr):
    """
    해시셋을 사용하여 모든 중복 원소를 찾습니다.

    알고리즘:
      - seen: 지금까지 본 원소를 저장
      - duplicates: 두 번 이상 등장한 원소를 저장
      - 배열을 한 번 순회하면서 seen에 있으면 duplicates에 추가

    시간 복잡도: O(n) — set의 탐색/삽입이 평균 O(1)
    공간 복잡도: O(n) — seen set이 최대 n개의 원소를 저장
    """
    seen = set()  # 이미 확인한 원소
    duplicates = set()  # 중복으로 확인된 원소
    for x in arr:
        if x in seen:  # 이전에 본 적 있는 원소 → 중복
            duplicates.add(x)
        else:
            seen.add(x)  # 처음 보는 원소 → seen에 추가
    return duplicates


def generate_test_data(n, duplicate_ratio=0.3):
    """
    중복이 포함된 테스트 데이터를 생성합니다.

    매개변수:
      n              — 전체 데이터 크기
      duplicate_ratio — 중복 비율 (기본값: 0.3 = 30%)

    알고리즘:
      1. 고유 원소 개수 = n * (1 - duplicate_ratio)
      2. 나머지는 기존 범위에서 랜덤으로 선택하여 중복 생성
      3. 전체를 섞어(shuffle) 반환

    시간 복잡도: O(n)
    공간 복잡도: O(n)
    """
    unique_count = int(n * (1 - duplicate_ratio))  # 고유 원소 개수 계산
    base = list(range(unique_count))  # 0부터 unique_count-1까지 고유 원소
    extras = [random.randint(0, unique_count - 1) for _ in range(n - unique_count)]  # 중복 원소 생성
    data = base + extras  # 고유 원소 + 중복 원소 합침
    random.shuffle(data)  # 순서를 랜덤으로 섞음
    return data


def benchmark_one(func, data, repeat=3):
    """
    함수의 실행 시간을 반복 측정하여 평균을 반환합니다.

    시간 복잡도: O(repeat * T(func))
    """
    times = []
    for _ in range(repeat):
        start = time.perf_counter()  # 고해상도 시작 시간
        func(data)
        end = time.perf_counter()  # 고해상도 종료 시간
        times.append(end - start)
    return sum(times) / len(times)  # 평균 반환


if __name__ == "__main__":
    print("=" * 65)
    print("중복 원소 찾기: O(n²) vs O(n) 벤치마크")
    print("=" * 65)

    # 정확성 검증: 두 알고리즘이 같은 결과를 내는지 확인
    test = [1, 2, 3, 2, 4, 5, 1, 6]
    bf_result = find_duplicates_bruteforce(test)  # 브루트포스 결과
    hs_result = find_duplicates_hashset(test)  # 해시셋 결과
    print(f"\n검증 데이터: {test}")
    print(f"Bruteforce 결과: {bf_result}")
    print(f"HashSet 결과:    {hs_result}")
    assert bf_result == hs_result, "결과가 다릅니다!"
    print("-> 두 결과 일치 확인\n")

    # 벤치마크: 입력 크기별 실행 시간 비교
    sizes = [1000, 2000, 5000, 10000]
    print(f"{'N':>8s} | {'O(n²) [초]':>12s} | {'O(n) [초]':>12s} | {'배율':>8s}")
    print("-" * 50)

    for n in sizes:
        data = generate_test_data(n)  # 중복 포함 테스트 데이터 생성

        # O(n²)은 N이 크면 너무 오래 걸리므로 제한
        if n <= 10000:
            t_bf = benchmark_one(find_duplicates_bruteforce, data, repeat=1)
        else:
            t_bf = float("inf")  # 너무 느려서 건너뜀

        t_hs = benchmark_one(find_duplicates_hashset, data, repeat=3)

        if t_bf != float("inf"):
            ratio = t_bf / t_hs if t_hs > 0 else float("inf")  # 속도 향상 비율
            print(f"{n:>8d} | {t_bf:>12.6f} | {t_hs:>12.6f} | {ratio:>7.1f}x")
        else:
            print(f"{n:>8d} | {'(skip)':>12s} | {t_hs:>12.6f} | {'N/A':>8s}")

    # 핵심 결론: 알고리즘 복잡도가 실제 성능에 미치는 영향
    print("\n결론: N이 커질수록 O(n²)과 O(n)의 차이가 극적으로 벌어집니다.")
    print("N이 2배가 되면 O(n²)은 약 4배, O(n)은 약 2배 증가합니다.")
