---
theme: default
title: "Week 12 Lab — Shortest Paths + Project"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 12 Lab
## Shortest Paths + Project

**Objectives**: Implement Dijkstra's and Bellman-Ford algorithms; add path-finding features to the project

---
layout: section
---

# Algorithm Exercises
20 minutes

---

# Ex 1: Dijkstra -- Problem

Implement **Dijkstra's algorithm** to find shortest paths from a source node in a weighted graph.

```
    4       5
A ----- B ----- D
|       |       |
2       1       2
|       |       |
C ------+       E
    8      10
C ----------- E
```

**Requirements**:
- Use a min-heap (priority queue) for efficiency
- Return shortest distances and predecessor map
- Reconstruct the shortest path to any target

Refer to `examples/ex1_dijkstra.py` | **Time**: 10 min

---

# Ex 1: Dijkstra -- Solution

```python
import heapq

def dijkstra(graph, start):
    dist = {node: float('inf') for node in graph}
    dist[start] = 0
    prev = {node: None for node in graph}
    pq = [(0, start)]

    while pq:
        d, u = heapq.heappop(pq)
        if d > dist[u]:
            continue                    # Skip outdated entry
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u
                heapq.heappush(pq, (dist[v], v))
    return dist, prev

def get_path(prev, target):
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]
    return list(reversed(path))
```

```
A -> E: dist=9, path=A -> C -> B -> D -> E
```

---

# Ex 2: Bellman-Ford -- Problem

Implement **Bellman-Ford** to find shortest paths in a graph that may contain **negative edge weights**.

```
A --4--> B --(-1)--> C --8--> D --2--> E
A --2--> C                    C --10-> E
         B --5--> D
```

**Requirements**:
- Relax all edges `|V| - 1` times
- Detect negative cycles (raise exception if found)
- Return shortest distances and predecessor map

**Question**: Why can Dijkstra not handle negative weights?

Refer to `examples/ex2_bellman_ford.py` | **Time**: 10 min

---

# Ex 2: Bellman-Ford -- Solution

```python
def bellman_ford(vertices, edges, start):
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0
    prev = {v: None for v in vertices}

    # Relax all edges |V| - 1 times
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
```

```python
vertices = ['A', 'B', 'C', 'D', 'E']
edges = [('A','B',4), ('A','C',2), ('B','C',-1),
         ('B','D',5), ('C','D',8), ('C','E',10), ('D','E',2)]
# A->A: 0, A->B: 4, A->C: 2, A->D: 8, A->E: 10
```

---

# Dijkstra vs. Bellman-Ford

| Aspect | Dijkstra | Bellman-Ford |
|--------|----------|--------------|
| Time complexity | O((V + E) log V) | O(V * E) |
| Negative weights | Not supported | Supported |
| Negative cycles | Cannot detect | Detects and reports |
| Data structure | Min-heap (priority queue) | Simple edge list |
| Best for | Sparse graphs, non-negative weights | Graphs with negative weights |

**Key insight**: Dijkstra is greedy (processes closest node first), so negative weights can invalidate earlier decisions. Bellman-Ford relaxes all edges repeatedly, guaranteeing correctness.

---
layout: section
---

# Project Demo: Shortest Path Explorer
10 minutes

---

# Run the Reference Project

```bash
cd project
pip install fastapi uvicorn
uvicorn app:app --reload
```

**Explore**:
- Dijkstra step-by-step visualization
- Bellman-Ford with negative cycle detection
- Algorithm comparison (Dijkstra vs. Bellman-Ford on same graph)
- Campus map route finding

---
layout: section
---

# Project Work
20 minutes

---

# Proj 1: Add Optimization Features

Integrate shortest path algorithms into your project:

| Topic | Shortest Path Feature Ideas |
|-------|----------------------------|
| Shopping Mall | Optimal path through recommended products by similarity |
| Social Network | Shortest path based on relationship closeness |
| Campus Map | Shortest route between buildings |

**Example**: Campus route finding

```python
@app.get("/route/{start}/{end}")
def find_route(start: str, end: str):
    dist, prev = dijkstra(campus_graph, start)
    path = get_path(prev, end)
    return {"distance": dist[end], "path": path}
```

**Time**: 10 minutes

---

# Proj 2: Start Presentation Materials

Outline the structure of your final presentation (Week 13):

| Section | Content |
|---------|---------|
| 1. Project Introduction | Web app topic and feature description |
| 2. Algorithms Applied | At least 4, with brief explanation of each |
| 3. Performance Comparison | Before/after measurement results |
| 4. Demo | Walk through the running web app |
| 5. Conclusion | Lessons learned and key takeaways |

Create your slide deck and fill in sections 1-2 today.

**Time**: 10 minutes

---

# Week 12 Milestone

By the end of this lab:

- Dijkstra's algorithm implemented and tested
- Bellman-Ford algorithm implemented and tested
- Path-finding / optimization feature integrated into your project
- Presentation outline and draft started

**Progress check**:
| Week | Milestone | Status |
|------|-----------|--------|
| 09 | Team formed, skeleton running | Done |
| 10 | Hash-based feature integrated | Done |
| 11 | Graph feature + midpoint check-in | Done |
| **12** | **Path finding + presentation draft** | **Today** |
| 13 | Code + slides complete | Next |

**Next week**: Final code polish + team presentations
