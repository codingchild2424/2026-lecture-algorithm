---
theme: default
title: "Week 11 Lab — Graph Traversal + Project"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 11 Lab
## Graph Traversal + Project

**Objectives**: Implement BFS and DFS; add graph-based features to the project

---
layout: section
---

# Algorithm Exercises
25 minutes

---

# Ex 1: BFS -- Problem

Implement **Breadth-First Search** that computes shortest distances from a start node.

**Input graph**:
```
A -- B -- D
|    |
C    E -- F
|         |
+----F----+
```

**Requirements**:
- Use a queue (FIFO) for traversal
- Track visited nodes to avoid cycles
- Compute distance from start to each reachable node
- Return traversal order and distance dictionary

Refer to `examples/skeletons/ex1_bfs.py` | **Time**: 15 min

---

# Ex 1: BFS -- Solution

```python
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
```

```python
graph = {
    'A': ['B', 'C'], 'B': ['A', 'D', 'E'],
    'C': ['A', 'F'], 'D': ['B'],
    'E': ['B', 'F'], 'F': ['C', 'E']
}
order, dist = bfs(graph, 'A')
# order: ['A', 'B', 'C', 'D', 'E', 'F']
# dist:  {'A': 0, 'B': 1, 'C': 1, 'D': 2, 'E': 2, 'F': 2}
```

---

# Ex 2: DFS + Topological Sort -- Problem

**Part A**: Implement recursive **Depth-First Search**.

**Part B**: Implement **topological sort** on a DAG of course prerequisites.

```
MATH101 -> CS201 -> CS301 -> CS401
CS101  -> CS201
CS101  -> CS202 -> CS301
```

**Question**: In what order should a student take these courses?

Refer to `examples/skeletons/ex2_dfs_topo.py` | **Time**: 10 min

---

# Ex 2: DFS + Topological Sort -- Solution

```python
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
        stack.append(node)      # Post-order: append after children
    for node in graph:
        if node not in visited:
            _dfs(node)
    return list(reversed(stack))
```

```python
# Result: ['MATH101', 'CS101', 'CS202', 'CS201', 'CS301', 'CS401']
```

---

# BFS vs. DFS Summary

| Aspect | BFS | DFS |
|--------|-----|-----|
| Data structure | Queue (FIFO) | Stack / Recursion |
| Explores | Level by level | As deep as possible first |
| Shortest path | Yes (unweighted) | No |
| Topological sort | No (use Kahn's variant) | Yes (post-order reversal) |
| Memory | O(width of graph) | O(depth of graph) |
| Use cases | Shortest path, friend suggestions | Cycle detection, topo sort |

---
layout: section
---

# Project Demo: Graph Traversal Explorer
10 minutes

---

# Run the Reference Project

```bash
cd project
pip install fastapi uvicorn
uvicorn app:app --reload
```

**Explore**:
- Interactive graph visualization
- BFS/DFS step-by-step animation
- Topological sort on course prerequisites
- Cycle detection
- Social network friend suggestions

---
layout: section
---

# Project Work
15 minutes

---

# Proj 1: Add Graph Features

Integrate graph traversal into your project:

| Topic | Graph Feature Ideas |
|-------|---------------------|
| Shopping Mall | "Customers who bought this also bought..." (graph traversal) |
| Social Network | Friend suggestions via BFS (2nd-degree connections) |
| Campus Map | Build a connectivity graph between buildings |

**Example**: Friend suggestions with BFS

```python
def suggest_friends(graph, user):
    """Find 2nd-degree connections (friends of friends)."""
    friends = set(graph[user])
    suggestions = set()
    for friend in friends:
        for fof in graph[friend]:
            if fof != user and fof not in friends:
                suggestions.add(fof)
    return suggestions
```

**Time**: 10 minutes

---

# Proj 2: Midpoint Check-In

Each team shares current progress (2 min per team):

1. **What is working?** -- Demo your current features
2. **Algorithms integrated so far?** -- Which ones, how are they used?
3. **Blockers or challenges?** -- What do you need help with?
4. **Plan for remaining weeks?** -- What features are left?

Receive feedback from the instructor and peers.

**Time**: 5 minutes

---

# Week 11 Milestone

By the end of this lab:

- BFS implemented with shortest distance computation
- DFS + topological sort implemented
- Graph-based feature integrated into your project
- Midpoint check-in completed

**Progress check**:
| Week | Milestone | Status |
|------|-----------|--------|
| 09 | Team formed, skeleton running | Done |
| 10 | Hash-based feature integrated | Done |
| **11** | **Graph feature + midpoint check-in** | **Today** |
| 12 | Path finding + presentation draft | Next |
| 13 | Code + slides complete | Final |

**Next week**: Shortest path features + start presentation
