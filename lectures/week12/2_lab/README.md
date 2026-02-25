# Week 12 Lab — Shortest Paths + Project

## Objectives
- Implement Dijkstra's and Bellman-Ford algorithms.
- Add path-finding/optimization features to the project.

---

## Algorithm Exercises (20 min)

### Ex 1: Dijkstra (10 min)
`examples/dijkstra.py` — Dijkstra implementation using heapq.

### Ex 2: Bellman-Ford (10 min)
`examples/bellman_ford.py` — Shortest paths in graphs with negative edge weights.

---

## Project Demo: Shortest Path Explorer (10 min)

Run the reference project to see shortest path algorithms in action:
```bash
cd project
pip install fastapi uvicorn
uvicorn app:app --reload
```
Explore: Dijkstra step-by-step visualization, Bellman-Ford with negative cycle detection, algorithm comparison, and campus map route finding.

---

## Project Work (20 min)

### Proj 1: Add Optimization Features (10 min)
- Shopping mall: Optimal path based on similarity between recommended products
- Social network: Shortest path based on relationship closeness
- Campus map: Shortest path search between buildings

### Proj 2: Start Presentation Materials (10 min)
Outline the structure of your presentation:
1. Project introduction
2. List of algorithms applied
3. Before/after performance comparison for each algorithm
4. Demo
5. Conclusion

**Milestone**: Shortest path feature + presentation draft
