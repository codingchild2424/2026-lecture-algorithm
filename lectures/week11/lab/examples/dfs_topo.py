"""DFS and Topological Sort."""


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    order = [start]
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))
    return order


def topological_sort(graph):
    visited = set()
    stack = []

    def _dfs(node):
        visited.add(node)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)
        stack.append(node)

    for node in graph:
        if node not in visited:
            _dfs(node)

    return list(reversed(stack))


if __name__ == "__main__":
    # Undirected graph for DFS
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C']}
    print(f"DFS from A: {dfs(graph, 'A')}")

    # DAG for topological sort
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
    print(f"Topological order: {topological_sort(dag)}")
