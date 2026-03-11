# === Ex 1: Dijkstra's Shortest Path Algorithm ===
# Week 12 Graph Algorithms 2 - Single-source shortest paths in non-negative weighted graphs
# Algorithm: Greedy approach using a min-heap (priority queue)
# Time complexity: O((V + E) log V) - using a binary heap
# Space complexity: O(V + E) - distance array + priority queue
"""Dijkstra's Algorithm using heapq."""
import heapq


def dijkstra(graph, start):
    """Find shortest distances from the start node to all nodes using Dijkstra's algorithm.

    Algorithm:
    1. Initialize the start node's distance to 0, all others to infinity
    2. Pop the node u with the smallest distance from the min-heap
    3. For all neighbors v of u, perform relaxation:
       if dist[u] + w(u,v) < dist[v], update dist[v]
    4. Push updated nodes onto the heap
    5. Repeat until the heap is empty

    Key condition: all edge weights must be non-negative (negative weights not allowed)
    Greedy correctness: the distance of a node popped from the min-heap is already finalized

    Args:
        graph: Adjacency list {node: [(neighbor, weight), ...]}
        start: Starting node

    Returns:
        (dist, prev) - dist: shortest distance dictionary, prev: previous node dictionary for path reconstruction

    Time complexity: O((V + E) log V) - heap operation O(log V) per node/edge
    Space complexity: O(V) - dist, prev dictionaries + heap
    """
    # Initialize all node distances to infinity
    dist = {node: float('inf') for node in graph}
    dist[start] = 0  # Start node distance is 0
    prev = {node: None for node in graph}  # Previous node for shortest path reconstruction
    pq = [(0, start)]  # Min-heap: (distance, node) pairs

    # TODO: Process nodes from the priority queue until it is empty
    #   1. Pop (d, u) from the min-heap using heapq.heappop(pq)
    #   2. Skip if d > dist[u] (already found a shorter path - lazy deletion)
    #   3. For each neighbor (v, w) in graph[u]:
    #      - If dist[u] + w < dist[v] (relaxation condition):
    #        a. Update dist[v] = dist[u] + w
    #        b. Set prev[v] = u
    #        c. Push (dist[v], v) onto the heap using heapq.heappush()
    pass  # TODO: implement

    return dist, prev


def get_path(prev, target):
    """Backtrack through the prev dictionary to reconstruct the path from start to target.

    Algorithm: Start from target, follow prev[node] to backtrack, then reverse
    Time complexity: O(V) - path length is at most V in the worst case
    """
    # TODO: Build the path by following prev[node] from target back to start
    # TODO: Reverse and return the path
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]  # Move to the previous node
    return list(reversed(path))  # Reverse to get start -> target order


if __name__ == "__main__":
    # Undirected weighted graph (adjacency list)
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    dist, prev = dijkstra(graph, 'A')

    # Print shortest distance and path to each node
    print("Shortest distances from A:")
    for node in sorted(dist):
        path = get_path(prev, node)
        print(f"  A -> {node}: dist={dist[node]}, path={' -> '.join(path)}")
