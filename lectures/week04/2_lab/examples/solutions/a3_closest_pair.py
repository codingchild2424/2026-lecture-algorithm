# === A-3: Closest Pair of Points ===
# Brute force O(n^2) vs divide and conquer O(n log n) comparison
# Finding the two closest points in a set of points on a 2D plane
"""Closest Pair of Points - brute force vs divide and conquer."""
import random
import math
import time


def dist(p1, p2):
    """Calculate the Euclidean distance between two points."""
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)


def closest_pair_bruteforce(points):
    """
    Brute force method
    - Algorithm: Compare all pairs of points to find the minimum distance
    - Time complexity: O(n^2) -- checks all n*(n-1)/2 pairs
    - Space complexity: O(1)
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
    Divide and conquer method
    - Algorithm: Sort by x-coordinate -> find closest pair via divide and conquer
    - Time complexity: O(n log^2 n) -- includes strip sorting at each level
      (Can be improved to O(n log n) by pre-sorting the strip by y-coordinate)
    - Space complexity: O(n) -- for sorting and strip array
    """
    # Sort by x-coordinate to prepare for division
    points_sorted = sorted(points, key=lambda p: p[0])
    return _closest_dc(points_sorted)


def _closest_dc(pts):
    """
    Divide and conquer recursive function
    - Splits the point set in half by x-coordinate
    - Finds the closest pair in each half (left/right)
    - Also checks pairs crossing the dividing line (strip)
    """
    n = len(pts)
    # Base case: use brute force for 3 or fewer points
    if n <= 3:
        return closest_pair_bruteforce(pts)

    mid = n // 2
    mid_x = pts[mid][0]  # x-coordinate of the dividing line
    # Find closest pair in the left and right halves respectively
    left_result = _closest_dc(pts[:mid])
    right_result = _closest_dc(pts[mid:])

    # Select the closer pair from left/right results
    d = min(left_result[0], right_result[0])
    best = left_result if left_result[0] <= right_result[0] else right_result

    # Strip region: extract only points within distance d from the dividing line
    # Must check since the closest pair may span across the dividing line
    strip = [p for p in pts if abs(p[0] - mid_x) < d]
    # Sort by y-coordinate -- for efficient comparison within the strip
    strip.sort(key=lambda p: p[1])

    # Compare point pairs within the strip
    # Key observation: no need to compare if y-coordinate difference >= d
    # Only up to 7 points need to be compared for each point -> strip check is O(n)
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
    # Verify correctness with a small example
    points = [(2, 3), (12, 30), (40, 50), (5, 1), (12, 10), (3, 4)]
    d1, pair1 = closest_pair_bruteforce(points)
    d2, pair2 = closest_pair_dc(points)
    print(f"Points: {points}")
    print(f"Brute force: dist={d1:.4f}, pair={pair1}")
    print(f"D&C:         dist={d2:.4f}, pair={pair2}")

    # Performance comparison: brute force vs divide and conquer by input size
    for n in [100, 1000, 5000]:
        pts = [(random.uniform(0, 10000), random.uniform(0, 10000)) for _ in range(n)]
        start = time.perf_counter()
        closest_pair_bruteforce(pts)
        t1 = time.perf_counter() - start
        start = time.perf_counter()
        closest_pair_dc(pts)
        t2 = time.perf_counter() - start
        print(f"\nN={n}: Brute force={t1:.4f}s, D&C={t2:.4f}s, Speedup={t1/t2:.1f}x")
