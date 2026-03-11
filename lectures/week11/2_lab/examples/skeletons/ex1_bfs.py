# === Ex 1: BFS - Breadth First Search ===
# Week 11 Graph Algorithms 1 - Graph traversal and shortest distance computation using BFS
# Algorithm: Uses a queue (FIFO) to visit nodes in order of proximity from the start node
# Time complexity: O(V + E) - V is the number of vertices, E is the number of edges
# Space complexity: O(V) - visited set, queue, distance dictionary
"""BFS - Breadth First Search with shortest distance."""
from collections import deque


def bfs(graph, start):
    """Perform Breadth First Search (BFS) and return the visit order and shortest distances.

    Algorithm:
    1. Mark the start node as visited and enqueue it
    2. Dequeue a node (popleft), mark unvisited neighbors as visited, and enqueue them
    3. Repeat until the queue is empty

    Key properties of BFS:
    - Guarantees shortest paths in unweighted graphs
    - Visits all nodes at the same level (distance) before proceeding to the next level

    Args:
        graph: Graph represented as an adjacency list (dictionary)
        start: Starting node for traversal

    Returns:
        (visit order list, shortest distance dictionary from the start node)

    Time complexity: O(V + E) - each vertex and edge is processed exactly once
    Space complexity: O(V) - queue and visited store at most V nodes
    """
    visited = {start}           # Set of visited nodes (prevents duplicate visits)
    queue = deque([start])      # BFS traversal queue (FIFO)
    distance = {start: 0}       # Shortest distance from the start node
    order = []                  # Record of visit order

    # TODO: Process nodes from the queue until it is empty
    #   1. Dequeue a node from the front using queue.popleft()
    #   2. Append the node to the order list
    #   3. For each neighbor of the current node (use graph.get(node, [])):
    #      - If the neighbor has not been visited:
    #        a. Add it to the visited set
    #        b. Append it to the queue
    #        c. Set its distance = current node's distance + 1
    pass  # TODO: implement

    return order, distance


if __name__ == "__main__":
    # Undirected graph example (adjacency list)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    order, dist = bfs(graph, 'A')
    print(f"BFS order: {order}")         # Visit in level order starting from A
    print(f"Distances from A: {dist}")   # Shortest distance to each node (number of edges)
