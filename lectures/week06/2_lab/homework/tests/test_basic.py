import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skeleton'))
import solution

def test_edit_distance_same():
    d, _ = solution.edit_distance("abc", "abc")
    assert d == 0

def test_edit_distance_basic():
    d, _ = solution.edit_distance("kitten", "sitting")
    assert d == 3

def test_floyd_warshall_basic():
    INF = float('inf')
    dist = [[0, 3, INF, 7], [8, 0, 2, INF], [5, INF, 0, 1], [2, INF, INF, 0]]
    result = solution.floyd_warshall(dist)
    assert result[0][2] == 5  # 0->1->2
    assert result[0][3] == 6  # 0->1->2->3
