"""Closest Pair of Points - brute force vs divide and conquer."""
import random
import math
import time


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_pair_bruteforce(points):
    """O(n^2): Check all pairs."""
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
    """O(n log n): Divide and conquer approach."""
    points_sorted = sorted(points, key=lambda p: p[0])
    return _closest_dc(points_sorted)


def _closest_dc(pts):
    n = len(pts)
    if n <= 3:
        return closest_pair_bruteforce(pts)

    mid = n // 2
    mid_x = pts[mid][0]
    left_result = _closest_dc(pts[:mid])
    right_result = _closest_dc(pts[mid:])

    d = min(left_result[0], right_result[0])
    best = left_result if left_result[0] <= right_result[0] else right_result

    strip = [p for p in pts if abs(p[0] - mid_x) < d]
    strip.sort(key=lambda p: p[1])

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
    # Small example
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    d1, pair1 = closest_pair_bruteforce(points)
    d2, pair2 = closest_pair_dc(points)
    print(f"Points: {points}")
    print(f"Brute force: dist={d1:.4f}, pair={pair1}")
    print(f"D&C:         dist={d2:.4f}, pair={pair2}")

    # Performance comparison
    for n in [100, 1000, 5000]:
        pts = [(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(n)]
        start = time.perf_counter()
        closest_pair_bruteforce(pts)
        t1 = time.perf_counter() - start
        start = time.perf_counter()
        closest_pair_dc(pts)
        t2 = time.perf_counter() - start
        print(f"\nN={n}: Brute force={t1:.4f}s, D&C={t2:.4f}s, Speedup={t1/t2:.1f}x")
