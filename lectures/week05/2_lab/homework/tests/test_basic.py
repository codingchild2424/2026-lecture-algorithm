import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skeleton'))
import solution

def test_kruskal_simple():
    edges = [(1, 0, 1), (2, 1, 2), (3, 0, 2)]
    total, mst = solution.kruskal_mst(3, edges)
    assert total == 3

def test_dijkstra_simple():
    graph = {0: [(1, 4), (2, 1)], 1: [(3, 1)], 2: [(1, 2), (3, 5)], 3: []}
    dist = solution.dijkstra(graph, 0)
    assert dist[0] == 0
    assert dist[3] == 4

def test_union_find():
    uf = solution.UnionFind(5)
    uf.union(0, 1)
    assert uf.find(0) == uf.find(1)
