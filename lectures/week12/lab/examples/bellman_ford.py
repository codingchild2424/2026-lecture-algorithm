"""Bellman-Ford Algorithm - handles negative weights."""


def bellman_ford(vertices, edges, start):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    prev = {v: None for v in vertices}

    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    # Check for negative cycles
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative cycle")

    return dist, prev


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', -1), ('B', 'D', 5),
        ('C', 'D', 8), ('C', 'E', 10),
        ('D', 'E', 2)
    ]

    dist, prev = bellman_ford(vertices, edges, 'A')
    print("Bellman-Ford from A (handles negative weights):")
    for v in sorted(dist):
        print(f"  A -> {v}: dist={dist[v]}")
