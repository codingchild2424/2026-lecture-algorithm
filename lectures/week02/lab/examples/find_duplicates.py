"""
중복 원소 찾기 — O(n^2) vs O(n) 비교
"""

import time
import random


def find_duplicates_bruteforce(arr):
    """
    이중 for 루프로 중복 원소를 찾습니다. O(n^2)
    """
    duplicates = set()
    n = len(arr)
    for i in range(n):
        for j in range(i + 1, n):
            if arr[i] == arr[j]:
                duplicates.add(arr[i])
    return duplicates


def find_duplicates_hashset(arr):
    """
    set을 사용하여 중복 원소를 찾습니다. O(n)
    """
    seen = set()
    duplicates = set()
    for x in arr:
        if x in seen:
            duplicates.add(x)
        else:
            seen.add(x)
    return duplicates


def generate_test_data(n, duplicate_ratio=0.3):
    """
    중복이 포함된 테스트 데이터를 생성합니다.
    duplicate_ratio만큼의 원소가 중복됩니다.
    """
    unique_count = int(n * (1 - duplicate_ratio))
    base = list(range(unique_count))
    extras = [random.randint(0, unique_count - 1) for _ in range(n - unique_count)]
    data = base + extras
    random.shuffle(data)
    return data


def benchmark_one(func, data, repeat=3):
    """함수의 실행 시간을 반복 측정하여 평균을 반환합니다."""
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


if __name__ == "__main__":
    print("=" * 65)
    print("중복 원소 찾기: O(n²) vs O(n) 벤치마크")
    print("=" * 65)

    # 정확성 검증
    test = [1, 2, 3, 2, 4, 5, 1, 6]
    bf_result = find_duplicates_bruteforce(test)
    hs_result = find_duplicates_hashset(test)
    print(f"\n검증 데이터: {test}")
    print(f"Bruteforce 결과: {bf_result}")
    print(f"HashSet 결과:    {hs_result}")
    assert bf_result == hs_result, "결과가 다릅니다!"
    print("-> 두 결과 일치 확인\n")

    # 벤치마크
    sizes = [1000, 2000, 5000, 10000]
    print(f"{'N':>8s} | {'O(n²) [초]':>12s} | {'O(n) [초]':>12s} | {'배율':>8s}")
    print("-" * 50)

    for n in sizes:
        data = generate_test_data(n)

        # O(n^2)은 N이 크면 너무 오래 걸리므로 제한
        if n <= 10000:
            t_bf = benchmark_one(find_duplicates_bruteforce, data, repeat=1)
        else:
            t_bf = float("inf")

        t_hs = benchmark_one(find_duplicates_hashset, data, repeat=3)

        if t_bf != float("inf"):
            ratio = t_bf / t_hs if t_hs > 0 else float("inf")
            print(f"{n:>8d} | {t_bf:>12.6f} | {t_hs:>12.6f} | {ratio:>7.1f}x")
        else:
            print(f"{n:>8d} | {'(skip)':>12s} | {t_hs:>12.6f} | {'N/A':>8s}")

    print("\n결론: N이 커질수록 O(n²)과 O(n)의 차이가 극적으로 벌어집니다.")
    print("N이 2배가 되면 O(n²)은 약 4배, O(n)은 약 2배 증가합니다.")
