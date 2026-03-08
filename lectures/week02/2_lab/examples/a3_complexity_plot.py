# === A-3: 복잡도 클래스별 실행 시간 시각화 ===
# O(1), O(n), O(n log n), O(n²) 네 가지 복잡도 클래스의 실행 시간을
# 입력 크기(N)에 따라 측정하고 그래프로 비교합니다.
#
# 이 실험을 통해 이론적 복잡도가 실제 실행 시간에 어떻게 반영되는지 확인할 수 있습니다.
"""Plot execution times for different complexity classes."""
import time
import random
import math

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("matplotlib not installed. Install with: pip install matplotlib")


def o_1(arr):
    """
    O(1) — 상수 시간: 배열의 첫 번째 원소에 접근합니다.
    입력 크기에 관계없이 항상 일정한 시간이 소요됩니다.
    """
    return arr[0] if arr else None


def o_n(arr):
    """
    O(n) — 선형 시간: 배열의 모든 원소를 한 번씩 순회하여 합산합니다.
    입력 크기에 정비례하여 시간이 증가합니다.
    """
    total = 0
    for x in arr:  # 모든 원소를 한 번씩 방문
        total += x
    return total


def o_n_log_n(arr):
    """
    O(n log n) — 선형 로그 시간: 배열을 정렬합니다.
    Python의 Timsort 알고리즘은 O(n log n) 보장.
    """
    return sorted(arr)


def o_n_squared(arr):
    """
    O(n²) — 이차 시간: 이중 반복문으로 n*n번 연산합니다.
    입력 크기가 2배가 되면 시간은 약 4배 증가합니다.
    """
    n = len(arr)
    count = 0
    for i in range(n):  # 바깥 루프: n번
        for j in range(n):  # 안쪽 루프: n번 → 총 n² 번 반복
            count += 1
    return count


def measure(func, arr, repeat=3):
    """
    함수의 실행 시간을 repeat 횟수만큼 반복 측정하여 평균을 반환합니다.

    시간 복잡도: O(repeat * T(func))
    """
    times = []
    for _ in range(repeat):
        start = time.perf_counter()  # 고해상도 시작 시간
        func(arr)
        end = time.perf_counter()  # 고해상도 종료 시간
        times.append(end - start)
    return sum(times) / len(times)  # 평균 실행 시간 반환


if __name__ == "__main__":
    sizes = [100, 500, 1000, 2000, 5000, 10000]  # 테스트할 입력 크기들
    results = {"O(1)": [], "O(n)": [], "O(n log n)": [], "O(n²)": []}  # 결과 저장 딕셔너리

    # 각 입력 크기에 대해 네 가지 복잡도 클래스의 실행 시간 측정
    for n in sizes:
        data = [random.randint(1, 1000) for _ in range(n)]  # 랜덤 테스트 데이터 생성
        results["O(1)"].append(measure(o_1, data))  # 상수 시간 측정
        results["O(n)"].append(measure(o_n, data))  # 선형 시간 측정
        results["O(n log n)"].append(measure(o_n_log_n, data))  # 선형 로그 시간 측정
        results["O(n²)"].append(measure(o_n_squared, data))  # 이차 시간 측정
        print(f"N={n:>6}: O(1)={results['O(1)'][-1]:.6f}, O(n)={results['O(n)'][-1]:.6f}, "
              f"O(n log n)={results['O(n log n)'][-1]:.6f}, O(n²)={results['O(n²)'][-1]:.6f}")

    # matplotlib이 설치되어 있으면 그래프 생성
    if HAS_MATPLOTLIB:
        plt.figure(figsize=(10, 6))
        for label, times in results.items():  # 각 복잡도 클래스별 선 그래프
            plt.plot(sizes, times, marker='o', label=label)
        plt.xlabel("Input Size (N)")  # x축: 입력 크기
        plt.ylabel("Time (seconds)")  # y축: 실행 시간
        plt.title("Execution Time by Complexity Class")  # 그래프 제목
        plt.legend()  # 범례 표시
        plt.grid(True)  # 격자 표시
        plt.savefig("complexity_plot.png", dpi=150)  # 그래프를 이미지로 저장
        plt.show()
        print("Graph saved as complexity_plot.png")
