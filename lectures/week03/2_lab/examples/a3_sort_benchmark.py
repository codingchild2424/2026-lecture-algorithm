# === A-3: 정렬 알고리즘 벤치마크 ===
# 기본 정렬(O(n^2))과 고급 정렬(O(n log n))의 실행 시간을 비교 측정
# 입력 크기별 성능 차이를 시각적으로 확인
"""Benchmark all sorting algorithms."""
import time
import random
from a1_basic_sorts import selection_sort, bubble_sort, insertion_sort
from a2_advanced_sorts import merge_sort, quick_sort

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


def measure(func, data, repeat=1):
    """
    정렬 함수의 실행 시간을 측정
    - func: 측정할 정렬 함수
    - data: 입력 데이터
    - repeat: 반복 횟수 (평균값 계산용)
    - 반환값: 평균 실행 시간 (초)
    - perf_counter() 사용으로 높은 정밀도의 시간 측정
    """
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)  # 평균 실행 시간 반환


if __name__ == "__main__":
    # 테스트할 입력 크기 목록
    sizes = [100, 500, 1000, 5000, 10000]
    algorithms = {
        "Selection": selection_sort,
        "Bubble": bubble_sort,
        "Insertion": insertion_sort,
        "Merge": merge_sort,
        "Quick": quick_sort,
        "Python sorted()": sorted,  # 파이썬 내장 정렬 (Timsort, O(n log n))
    }
    results = {name: [] for name in algorithms}

    for n in sizes:
        # 동일한 무작위 데이터로 모든 알고리즘 비교
        data = [random.randint(1, 100000) for _ in range(n)]
        print(f"\nN = {n:,}")
        for name, func in algorithms.items():
            # O(n^2) 알고리즘은 큰 입력에서 너무 느리므로 건너뜀
            if n > 5000 and name in ("Selection", "Bubble"):
                results[name].append(None)
                print(f"  {name:>15}: skipped (too slow)")
                continue
            t = measure(func, data)
            results[name].append(t)
            print(f"  {name:>15}: {t:.6f} sec")

    # matplotlib이 설치되어 있으면 결과를 그래프로 시각화
    if HAS_MATPLOTLIB:
        plt.figure(figsize=(10, 6))
        for name, times in results.items():
            # None(건너뛴 결과)을 제외하고 유효한 데이터만 플롯
            valid = [(s, t) for s, t in zip(sizes, times) if t is not None]
            if valid:
                ss, ts = zip(*valid)
                plt.plot(ss, ts, marker='o', label=name)
        plt.xlabel("Input Size (N)")
        plt.ylabel("Time (seconds)")
        plt.title("Sorting Algorithm Benchmark")
        plt.legend()
        plt.grid(True)
        plt.savefig("sort_benchmark.png", dpi=150)
        plt.show()
