# === A-3: 최근접 점 쌍 (Closest Pair of Points) ===
# 브루트 포스 O(n^2) vs 분할 정복 O(n log n) 비교
# 2차원 평면의 점 집합에서 가장 가까운 두 점을 찾는 문제
"""Closest Pair of Points - brute force vs divide and conquer."""
import random
import math
import time


def dist(p1, p2):
    """두 점 사이의 유클리드 거리 계산"""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_pair_bruteforce(points):
    """
    브루트 포스 방법
    - 알고리즘: 모든 점 쌍을 비교하여 최소 거리를 찾음
    - 시간복잡도: O(n^2) — n*(n-1)/2 쌍을 모두 검사
    - 공간복잡도: O(1)
    """
    n = len(points)
    min_dist = float('inf')
    pair = None
    for i in range(n):
        for j in range(i + 1, n):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair


def closest_pair_dc(points):
    """
    분할 정복 방법
    - 알고리즘: x좌표로 정렬 → 분할 정복으로 최근접 쌍 탐색
    - 시간복잡도: O(n log^2 n) — 각 레벨에서 strip 정렬 포함
      (strip을 y좌표로 미리 정렬하면 O(n log n)으로 개선 가능)
    - 공간복잡도: O(n) — 정렬 및 strip 배열
    """
    # x좌표 기준으로 정렬하여 분할 준비
    points_sorted = sorted(points, key=lambda p: p[0])
    return _closest_dc(points_sorted)


def _closest_dc(pts):
    """
    분할 정복 재귀 함수
    - 점 집합을 x좌표 기준으로 반으로 분할
    - 왼쪽/오른쪽 각각에서 최근접 쌍을 찾고
    - 분할선 근처(strip)에서 경계를 넘는 쌍도 확인
    """
    n = len(pts)
    # 기저 조건: 점이 3개 이하이면 브루트 포스로 처리
    if n <= 3:
        return closest_pair_bruteforce(pts)

    mid = n // 2
    mid_x = pts[mid][0]  # 분할선의 x좌표
    # 왼쪽 절반과 오른쪽 절반에서 각각 최근접 쌍 탐색
    left_result = _closest_dc(pts[:mid])
    right_result = _closest_dc(pts[mid:])

    # 왼쪽/오른쪽 결과 중 더 가까운 쌍 선택
    d = min(left_result[0], right_result[0])
    best = left_result if left_result[0] <= right_result[0] else right_result

    # Strip 영역: 분할선으로부터 거리 d 이내의 점들만 추출
    # 최근접 쌍이 분할선을 걸쳐 있을 수 있으므로 반드시 검사 필요
    strip = [p for p in pts if abs(p[0] - mid_x) < d]
    # y좌표로 정렬 — strip 내에서 효율적으로 비교하기 위함
    strip.sort(key=lambda p: p[1])

    # Strip 내 점 쌍 비교
    # 핵심 관찰: y좌표 차이가 d 이상이면 비교 불필요
    # 각 점에 대해 최대 7개의 점만 비교하면 됨 → strip 검사는 O(n)
    for i in range(len(strip)):
        j = i + 1
        while j < len(strip) and strip[j][1] - strip[i][1] < d:
            dd = dist(strip[i], strip[j])
            if dd < d:
                d = dd
                best = (dd, (strip[i], strip[j]))
            j += 1

    return best


if __name__ == "__main__":
    # 소규모 예제로 정확성 확인
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    d1, pair1 = closest_pair_bruteforce(points)
    d2, pair2 = closest_pair_dc(points)
    print(f"Points: {points}")
    print(f"Brute force: dist={d1:.4f}, pair={pair1}")
    print(f"D&C:         dist={d2:.4f}, pair={pair2}")

    # 성능 비교: 입력 크기별 브루트 포스 vs 분할 정복
    for n in [100, 1000, 5000]:
        pts = [(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(n)]
        start = time.perf_counter()
        closest_pair_bruteforce(pts)
        t1 = time.perf_counter() - start
        start = time.perf_counter()
        closest_pair_dc(pts)
        t2 = time.perf_counter() - start
        print(f"\nN={n}: Brute force={t1:.4f}s, D&C={t2:.4f}s, Speedup={t1/t2:.1f}x")
