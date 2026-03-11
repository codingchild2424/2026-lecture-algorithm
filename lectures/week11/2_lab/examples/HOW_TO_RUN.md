# Week 11 Lab - Graph Algorithms 1

## Exercises

### Ex 1: BFS - Breadth First Search (`ex1_bfs.py`)
Implement BFS traversal on an undirected graph using a queue.
You need to implement the main BFS loop that processes nodes level by level and tracks shortest distances.

### Ex 2: DFS & Topological Sort (`ex2_dfs_topo.py`)
Implement recursive DFS traversal and DFS-based topological sort on a DAG.
You need to implement the `dfs()` function and the inner `_dfs()` helper in `topological_sort()`.

## How to Run

```bash
python ex1_bfs.py
python ex2_dfs_topo.py
```

## Expected Output

- **Ex 1**: Prints BFS visit order starting from node A and shortest distances (in number of edges) from A to all reachable nodes.
- **Ex 2**: Prints DFS visit order from node A on an undirected graph, then prints course prerequisite relationships and their topological ordering.

## Solutions

Complete reference implementations are available in the `solutions/` subdirectory.
