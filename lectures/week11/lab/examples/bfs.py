"""BFS - Breadth First Search with shortest distance."""
from collections import deque


def bfs(graph, start):
    visited = {start}
    queue = deque([start])
    distance = {start: 0}
    order = []

    while queue:
        node = queue.popleft()
        order.append(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                distance[neighbor] = distance[node] + 1

    return order, distance


if __name__ == "__main__":
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    order, dist = bfs(graph, 'A')
    print(f"BFS order: {order}")
    print(f"Distances from A: {dist}")
