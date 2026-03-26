"""Homework 4: Reference Solution — Closest Pair of Points"""
import math
import random
import time


def dist(p1, p2):
    """Euclidean distance between two 2D points."""
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def closest_pair_bruteforce(points):
    """
    Brute force: check all pairs — O(n^2).
    Returns (distance, (point1, point2)).
    """
    n = len(points)
    min_dist = float("inf")
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
    Divide and conquer: O(n log^2 n).
    Returns (distance, (point1, point2)).
    """
    pts = sorted(points, key=lambda p: p[0])
    return _closest_dc(pts)


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


def benchmark(sizes=None):
    if sizes is None:
        sizes = [100, 1000, 5000]
    results = {"bruteforce": {}, "dc": {}}
    for n in sizes:
        pts = [(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(n)]
        start = time.perf_counter()
        closest_pair_bruteforce(pts)
        results["bruteforce"][n] = time.perf_counter() - start
        start = time.perf_counter()
        closest_pair_dc(pts)
        results["dc"][n] = time.perf_counter() - start
    return results
