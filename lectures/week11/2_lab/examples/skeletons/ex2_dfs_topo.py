# === Ex 2: DFS - Depth First Search & Topological Sort ===
# Week 11 Graph Algorithms 1 - Recursive DFS implementation and DAG topological sort
# DFS time complexity: O(V + E), Space complexity: O(V) (including recursion stack)
# Topological sort time complexity: O(V + E)
"""DFS and Topological Sort."""


def dfs(graph, start, visited=None):
    """Perform Depth First Search (DFS) recursively.

    Algorithm:
    1. Mark the current node as visited
    2. Recursively perform DFS on unvisited neighbors
    3. Backtrack when there are no more nodes to visit

    Properties of DFS:
    - Explores one path to the end before moving to another path
    - Uses a stack (here, the recursion call stack)

    Args:
        graph: Graph represented as an adjacency list (dictionary)
        start: Starting node for traversal
        visited: Set of visited nodes (shared across recursive calls)

    Returns:
        Visit order list

    Time complexity: O(V + E) - each vertex and edge is processed once
    Space complexity: O(V) - maximum recursion stack depth V, visited set
    """
    if visited is None:
        visited = set()  # Create an empty set on the first call

    # TODO: Add start to visited set
    # TODO: Initialize order list with [start]
    # TODO: For each neighbor in graph.get(start, []):
    #       - If neighbor not in visited, recursively call dfs()
    #         and extend order with the result
    # TODO: Return order
    pass  # TODO: implement
    return []


def topological_sort(graph):
    """Perform topological sort on a DAG (Directed Acyclic Graph).

    Algorithm (DFS-based):
    1. Perform DFS on all nodes
    2. After visiting all successors of a node in DFS (i.e., when DFS finishes),
       push the node onto a stack
    3. Reversing the stack yields the topological order

    Key idea:
    - By pushing node u onto the stack after its DFS exploration is complete,
      all nodes that depend on u will be positioned after u
    - Reversing the stack produces the correct dependency order

    Args:
        graph: Adjacency list of a directed graph (dictionary)

    Returns:
        List of nodes in topological order

    Time complexity: O(V + E)
    Space complexity: O(V) - visited set + recursion stack
    """
    visited = set()
    stack = []  # Stack to store DFS completion order

    def _dfs(node):
        """Internal DFS function: pushes node onto stack after exploration is complete."""
        # TODO: Add node to visited
        # TODO: For each neighbor in graph.get(node, []):
        #       - If neighbor not in visited, recursively call _dfs(neighbor)
        # TODO: Append node to stack (post-order: after all successors are visited)
        pass  # TODO: implement

    # Perform DFS for all nodes (handles disconnected components as well)
    for node in graph:
        if node not in visited:
            _dfs(node)

    # Reversing the stack yields the topological order
    return list(reversed(stack))


if __name__ == "__main__":
    # DFS test on an undirected graph
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C']}
    print(f"DFS from A: {dfs(graph, 'A')}")

    # Topological sort test on a DAG (Directed Acyclic Graph)
    # Course prerequisite relationships: CS101 -> CS201, CS202 -> CS301 -> CS401
    dag = {
        'CS101': ['CS201', 'CS202'],
        'CS201': ['CS301'],
        'CS202': ['CS301'],
        'CS301': ['CS401'],
        'MATH101': ['CS201'],
        'CS401': []
    }
    print(f"\nCourse prerequisites (DAG):")
    for course, prereqs_for in dag.items():
        if prereqs_for:
            print(f"  {course} -> {prereqs_for}")
    print(f"Topological order: {topological_sort(dag)}")  # Prerequisites appear first
