# Week 12 Lab - Graph Algorithms 2

## Exercises

### Ex 1: Dijkstra's Algorithm (`ex1_dijkstra.py`)
Implement Dijkstra's shortest path algorithm using a min-heap priority queue.
You need to implement the main loop that processes nodes from the heap and performs edge relaxation. The `get_path()` helper is provided.

### Ex 2: Bellman-Ford Algorithm (`ex2_bellman_ford.py`)
Implement the Bellman-Ford shortest path algorithm that handles negative edge weights.
You need to implement the V-1 relaxation loop and the negative cycle detection check.

## How to Run

```bash
python ex1_dijkstra.py
python ex2_bellman_ford.py
```

## Expected Output

- **Ex 1**: Prints shortest distances and paths from node A to all other nodes in an undirected weighted graph.
- **Ex 2**: Prints shortest distances from node A to all other nodes in a directed graph that includes a negative weight edge (B->C with weight -1).

## Solutions

Complete reference implementations are available in the `solutions/` subdirectory.
