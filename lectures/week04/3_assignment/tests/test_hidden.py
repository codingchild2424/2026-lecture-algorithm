import pytest, sys, os, random, math
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skeleton'))
import solution


def dist(p1, p2):
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)


def bruteforce_reference(points):
    min_dist = float("inf")
    pair = None
    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = dist(points[i], points[j])
            if d < min_dist:
                min_dist = d
                pair = (points[i], points[j])
    return min_dist, pair


def test_closest_pair_dc_small():
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    d_dc, _ = solution.closest_pair_dc(points)
    d_bf, _ = bruteforce_reference(points)
    assert abs(d_dc - d_bf) < 1e-9


def test_closest_pair_dc_random():
    for _ in range(10):
        n = random.randint(4, 200)
        points = [(random.uniform(0, 1000), random.uniform(0, 1000)) for _ in range(n)]
        d_dc, _ = solution.closest_pair_dc(points)
        d_bf, _ = bruteforce_reference(points)
        assert abs(d_dc - d_bf) < 1e-9


def test_closest_pair_dc_collinear():
    points = [(i, 0) for i in range(20)]
    d_dc, _ = solution.closest_pair_dc(points)
    assert abs(d_dc - 1.0) < 1e-9
