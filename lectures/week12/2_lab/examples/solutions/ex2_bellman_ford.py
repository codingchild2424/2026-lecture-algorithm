# === Ex 2: Bellman-Ford Shortest Path Algorithm ===
# Week 12 Graph Algorithms 2 - Single-source shortest paths allowing negative weights
# Algorithm: Repeat relaxation on all edges V-1 times
# Time complexity: O(V * E) - slower than Dijkstra but handles negative weights
# Space complexity: O(V) - distance array and previous node array
"""Bellman-Ford Algorithm - handles negative weights."""


def bellman_ford(vertices, edges, start):
    """Find shortest distances using the Bellman-Ford algorithm.

    Algorithm:
    1. Initialize the start node's distance to 0, all others to infinity
    2. Repeat V-1 times, performing relaxation on all edges:
       if dist[u] + w < dist[v], update dist[v] = dist[u] + w
    3. If additional relaxation is possible on the V-th iteration, a negative cycle exists

    Differences from Dijkstra:
    - Bellman-Ford can handle edges with negative weights
    - It can detect negative cycles
    - O(VE), which is slower than Dijkstra's O((V+E)log V)

    Why V-1 iterations?
    - A shortest path contains at most V-1 edges (when there are no cycles)
    - After the i-th iteration, shortest paths using at most i edges are finalized

    Args:
        vertices: List of vertices
        edges: List of edges [(source, destination, weight), ...]
        start: Starting vertex

    Returns:
        (dist, prev) - dist: shortest distance dictionary, prev: path reconstruction dictionary

    Raises:
        ValueError: If a negative cycle exists

    Time complexity: O(V * E)
    Space complexity: O(V)
    """
    # Initialize all vertex distances to infinity
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0  # Start node distance 0
    prev = {v: None for v in vertices}  # For path reconstruction

    # V-1 iterations: perform relaxation on all edges each iteration
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            # Relaxation: update if a shorter path is found
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    # Negative cycle detection: if further relaxation is possible on V-th iteration, a negative cycle exists
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative cycle")

    return dist, prev


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    # Directed weighted graph - edge B->C includes a negative weight (-1)
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', -1), ('B', 'D', 5),   # B->C: negative weight
        ('C', 'D', 8), ('C', 'E', 10),
        ('D', 'E', 2)
    ]

    dist, prev = bellman_ford(vertices, edges, 'A')
    print("Bellman-Ford from A (handles negative weights):")
    for v in sorted(dist):
        print(f"  A -> {v}: dist={dist[v]}")
