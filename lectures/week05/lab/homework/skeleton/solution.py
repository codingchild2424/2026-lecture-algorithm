"""Homework 4: MST + Dijkstra"""
import heapq


class UnionFind:
    """
    TODO: Implement Union-Find (Disjoint Set).
    """
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # TODO: with path compression
        return x

    def union(self, x, y):
        # TODO: with union by rank
        pass


def kruskal_mst(n, edges):
    """
    Kruskal's MST algorithm.
    n: number of vertices (0 to n-1)
    edges: list of (weight, u, v)
    Returns: (total_weight, list of edges in MST)

    TODO: Implement.
    """
    return 0, []


def dijkstra(graph, start):
    """
    Dijkstra's shortest path.
    graph: dict of {node: [(neighbor, weight), ...]}
    start: starting node
    Returns: dict of {node: shortest_distance}

    TODO: Implement.
    """
    return {}
