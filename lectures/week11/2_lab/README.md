# Week 11 Lab — Graph Traversal + Project

## Objectives
- Implement BFS and DFS, and understand their applications in graph traversal.
- Add graph-based features to the project.

---

## Algorithm Exercises (25 min)

### Ex 1: BFS (15 min)
Refer to `examples/bfs.py` and implement BFS to compute shortest distances.

### Ex 2: DFS + Topological Sort (10 min)
Refer to `examples/dfs_topo.py` and implement DFS-based topological sorting.

---

## Project Demo: Graph Traversal Explorer (10 min)

Run the reference project to see graph traversal in action:
```bash
cd project
pip install fastapi uvicorn
uvicorn app:app --reload
```
Explore: interactive graph visualization, BFS/DFS step-by-step animation, topological sort, cycle detection, and social network friend suggestions.

---

## Project Work (15 min)

### Proj 1: Add Graph Features (10 min)
- Shopping Mall: "Customers who bought this also bought" recommendations (graph traversal)
- Social Network: Friend suggestions (BFS to find 2nd-degree connections)
- Campus Map: Build a connectivity graph between buildings

### Proj 2: Midpoint Check-In (5 min)
Each team shares their current progress and receives feedback.

**Milestone**: Graph traversal feature integration + midpoint check-in
