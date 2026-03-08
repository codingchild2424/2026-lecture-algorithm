# === A-1: 타이머 유틸리티 ===
# 함수의 실행 시간을 정밀하게 측정하기 위한 유틸리티 모듈
# time.perf_counter()를 사용하여 고해상도 타이머로 측정합니다.
# 여러 번 반복 실행하여 평균 시간을 계산함으로써 측정 오차를 줄입니다.
"""Timer utility for measuring execution time."""
import time


def measure_time(func, *args, repeat=3):
    """
    함수의 실행 시간을 반복 측정하여 평균 시간을 반환합니다.

    매개변수:
      func   — 측정할 함수
      *args  — func에 전달할 인자들
      repeat — 반복 측정 횟수 (기본값: 3)

    반환값: (평균 시간(초), 마지막 실행 결과) 튜플

    알고리즘:
      1. repeat 횟수만큼 func(*args)를 실행
      2. 각 실행의 소요 시간을 기록
      3. 평균 시간과 마지막 결과를 반환

    시간 복잡도: O(repeat * T(func)) — func의 시간 복잡도에 비례
    공간 복잡도: O(repeat) — 각 실행 시간을 저장하는 리스트
    """
    times = []  # 각 반복의 실행 시간을 저장할 리스트
    for _ in range(repeat):
        start = time.perf_counter()  # 고해상도 시작 시간 기록
        result = func(*args)  # 측정 대상 함수 실행
        end = time.perf_counter()  # 고해상도 종료 시간 기록
        times.append(end - start)  # 소요 시간 저장
    avg = sum(times) / len(times)  # 평균 실행 시간 계산
    return avg, result


if __name__ == "__main__":
    import random

    # 테스트용 함수: 배열의 모든 원소를 합산 — O(n)
    def sum_list(arr):
        total = 0
        for x in arr:
            total += x
        return total

    # 입력 크기(N)를 늘려가며 실행 시간 변화를 관찰
    # N이 10배 증가할 때 시간도 약 10배 증가하면 O(n)임을 확인 가능
    for n in [1000, 10000, 100000, 1000000]:
        data = [random.randint(1, 100) for _ in range(n)]  # 랜덤 테스트 데이터 생성
        elapsed, _ = measure_time(sum_list, data)  # 실행 시간 측정
        print(f"N={n:>10,}: {elapsed:.6f} sec")
