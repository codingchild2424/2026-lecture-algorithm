"""
Week 12 Project -- Shortest Path Explorer
FastAPI backend with Dijkstra's algorithm, Bellman-Ford algorithm,
algorithm comparison, and campus map demo.
"""

from __future__ import annotations

import heapq
import math
import time
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI(title="Shortest Path Explorer")


# ---------------------------------------------------------------------------
# Core weighted graph representation
# ---------------------------------------------------------------------------

class WeightedGraph:
    """Adjacency-list graph supporting weighted, directed and undirected modes."""

    def __init__(self, directed: bool = False):
        self.directed = directed
        # adj[u] = [(v, weight), ...]
        self.adj: dict[str, list[tuple[str, float]]] = {}

    def add_node(self, node: str):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u: str, v: str, weight: float = 1.0):
        self.add_node(u)
        self.add_node(v)
        # Avoid duplicate edges
        if not any(nb == v for nb, _ in self.adj[u]):
            self.adj[u].append((v, weight))
        if not self.directed and not any(nb == u for nb, _ in self.adj[v]):
            self.adj[v].append((u, weight))

    def nodes(self) -> list[str]:
        return sorted(self.adj.keys())

    def edges(self) -> list[dict]:
        """Return deduplicated edge list as dicts."""
        result = []
        seen: set[tuple[str, str]] = set()
        for u in self.adj:
            for v, w in self.adj[u]:
                key = (u, v) if self.directed else tuple(sorted((u, v)))
                if key not in seen:
                    seen.add(key)
                    result.append({"from": u, "to": v, "weight": w})
        return result

    def all_directed_edges(self) -> list[tuple[str, str, float]]:
        """Return every directed edge (u, v, w) including both directions
        for undirected graphs."""
        result = []
        for u in self.adj:
            for v, w in self.adj[u]:
                result.append((u, v, w))
        return result

    def neighbors(self, node: str) -> list[tuple[str, float]]:
        return self.adj.get(node, [])

    def to_dict(self) -> dict:
        return {
            "directed": self.directed,
            "nodes": self.nodes(),
            "edges": self.edges(),
        }


# ---------------------------------------------------------------------------
# Dijkstra's Algorithm
# ---------------------------------------------------------------------------

def dijkstra(graph: WeightedGraph, source: str) -> dict:
    """Run Dijkstra from *source*. Returns step-by-step trace."""
    if source not in graph.adj:
        return {"error": f"Node '{source}' not in graph"}

    INF = float("inf")
    dist: dict[str, float] = {n: INF for n in graph.adj}
    dist[source] = 0.0
    parent: dict[str, Optional[str]] = {n: None for n in graph.adj}
    visited: set[str] = set()
    # Priority queue: (distance, node)
    pq: list[tuple[float, str]] = [(0.0, source)]
    steps: list[dict] = []
    relaxation_count = 0

    while pq:
        d, u = heapq.heappop(pq)
        if u in visited:
            continue
        visited.add(u)

        step: dict = {
            "action": "extract_min",
            "node": u,
            "distance": d,
            "priority_queue": [(dd, nn) for dd, nn in sorted(pq) if nn not in visited],
            "relaxations": [],
        }

        for v, w in graph.neighbors(u):
            if v in visited:
                continue
            new_dist = d + w
            relaxed = False
            if new_dist < dist[v]:
                old_dist = dist[v]
                dist[v] = new_dist
                parent[v] = u
                heapq.heappush(pq, (new_dist, v))
                relaxed = True
                relaxation_count += 1
                step["relaxations"].append({
                    "edge": f"{u} -> {v}",
                    "weight": w,
                    "old_dist": old_dist if old_dist != INF else "inf",
                    "new_dist": new_dist,
                    "relaxed": True,
                })
            else:
                step["relaxations"].append({
                    "edge": f"{u} -> {v}",
                    "weight": w,
                    "old_dist": dist[v],
                    "new_dist": new_dist,
                    "relaxed": False,
                })

        steps.append(step)

    # Build shortest path tree edges
    tree_edges = []
    for node, par in parent.items():
        if par is not None:
            tree_edges.append({"from": par, "to": node})

    # Convert inf to string for JSON
    final_dist = {}
    for n, d in dist.items():
        final_dist[n] = d if d != INF else "inf"

    return {
        "algorithm": "Dijkstra",
        "source": source,
        "distances": final_dist,
        "parent": parent,
        "tree_edges": tree_edges,
        "relaxation_count": relaxation_count,
        "steps": steps,
    }


# ---------------------------------------------------------------------------
# Bellman-Ford Algorithm
# ---------------------------------------------------------------------------

def bellman_ford(graph: WeightedGraph, source: str) -> dict:
    """Run Bellman-Ford from *source*. Returns iteration-by-iteration trace."""
    if source not in graph.adj:
        return {"error": f"Node '{source}' not in graph"}

    INF = float("inf")
    nodes = graph.nodes()
    n = len(nodes)
    dist: dict[str, float] = {nd: INF for nd in nodes}
    dist[source] = 0.0
    parent: dict[str, Optional[str]] = {nd: None for nd in nodes}

    all_edges = graph.all_directed_edges()
    steps: list[dict] = []
    relaxation_count = 0

    # n-1 iterations
    for i in range(n - 1):
        iteration_relaxations = []
        any_relaxed = False
        for u, v, w in all_edges:
            if dist[u] == INF:
                iteration_relaxations.append({
                    "edge": f"{u} -> {v}",
                    "weight": w,
                    "old_dist": "inf" if dist[v] == INF else dist[v],
                    "new_dist": "inf",
                    "relaxed": False,
                    "reason": "source unreachable",
                })
                continue
            new_dist = dist[u] + w
            if new_dist < dist[v]:
                old_dist = dist[v]
                dist[v] = new_dist
                parent[v] = u
                any_relaxed = True
                relaxation_count += 1
                iteration_relaxations.append({
                    "edge": f"{u} -> {v}",
                    "weight": w,
                    "old_dist": old_dist if old_dist != INF else "inf",
                    "new_dist": new_dist,
                    "relaxed": True,
                })
            else:
                iteration_relaxations.append({
                    "edge": f"{u} -> {v}",
                    "weight": w,
                    "old_dist": dist[v] if dist[v] != INF else "inf",
                    "new_dist": new_dist,
                    "relaxed": False,
                })

        # Snapshot of distances after this iteration
        dist_snapshot = {}
        for nd in nodes:
            dist_snapshot[nd] = dist[nd] if dist[nd] != INF else "inf"

        steps.append({
            "iteration": i + 1,
            "relaxations": iteration_relaxations,
            "any_relaxed": any_relaxed,
            "distances": dist_snapshot,
        })

        # Early termination
        if not any_relaxed:
            break

    # Negative cycle detection (one more iteration)
    negative_cycle = False
    negative_cycle_edges = []
    for u, v, w in all_edges:
        if dist[u] != INF and dist[u] + w < dist[v]:
            negative_cycle = True
            negative_cycle_edges.append({"from": u, "to": v, "weight": w})

    # Build shortest path tree edges
    tree_edges = []
    for node, par in parent.items():
        if par is not None and dist[node] != INF:
            tree_edges.append({"from": par, "to": node})

    final_dist = {}
    for nd, d in dist.items():
        final_dist[nd] = d if d != INF else "inf"

    return {
        "algorithm": "Bellman-Ford",
        "source": source,
        "distances": final_dist,
        "parent": parent,
        "tree_edges": tree_edges,
        "relaxation_count": relaxation_count,
        "negative_cycle": negative_cycle,
        "negative_cycle_edges": negative_cycle_edges,
        "steps": steps,
    }


# ---------------------------------------------------------------------------
# Path reconstruction
# ---------------------------------------------------------------------------

def reconstruct_path(parent: dict, source: str, target: str) -> list[str]:
    """Trace parent pointers to reconstruct path from source to target."""
    if parent.get(target) is None and target != source:
        return []
    path = []
    cur: Optional[str] = target
    seen: set[str] = set()
    while cur is not None:
        if cur in seen:
            return []  # cycle protection
        seen.add(cur)
        path.append(cur)
        cur = parent.get(cur)
    path.reverse()
    if path and path[0] == source:
        return path
    return []


# ---------------------------------------------------------------------------
# Campus Map Preset
# ---------------------------------------------------------------------------

CAMPUS_NODES = [
    "Library", "Cafeteria", "Dorm_A", "Dorm_B", "Gym",
    "Science", "Arts", "Admin", "Stadium", "Parking",
]

CAMPUS_EDGES = [
    ("Library", "Cafeteria", 3),
    ("Library", "Science", 4),
    ("Library", "Admin", 5),
    ("Cafeteria", "Dorm_A", 2),
    ("Cafeteria", "Arts", 6),
    ("Dorm_A", "Dorm_B", 1),
    ("Dorm_A", "Gym", 4),
    ("Dorm_B", "Gym", 3),
    ("Dorm_B", "Stadium", 5),
    ("Gym", "Stadium", 2),
    ("Science", "Arts", 3),
    ("Science", "Admin", 2),
    ("Arts", "Admin", 4),
    ("Arts", "Parking", 3),
    ("Admin", "Parking", 6),
    ("Stadium", "Parking", 4),
    ("Gym", "Science", 7),
]

# Fixed positions for the campus map (placed like a map layout)
CAMPUS_POSITIONS = {
    "Library":   {"x": 300, "y": 60},
    "Science":   {"x": 480, "y": 130},
    "Admin":     {"x": 480, "y": 280},
    "Cafeteria": {"x": 150, "y": 130},
    "Dorm_A":    {"x": 70,  "y": 260},
    "Dorm_B":    {"x": 70,  "y": 400},
    "Gym":       {"x": 230, "y": 370},
    "Arts":      {"x": 400, "y": 400},
    "Stadium":   {"x": 180, "y": 480},
    "Parking":   {"x": 500, "y": 480},
}


def build_campus_graph() -> WeightedGraph:
    g = WeightedGraph(directed=False)
    for node in CAMPUS_NODES:
        g.add_node(node)
    for u, v, w in CAMPUS_EDGES:
        g.add_edge(u, v, w)
    return g


# ---------------------------------------------------------------------------
# Layout helpers
# ---------------------------------------------------------------------------

def circular_layout(nodes: list[str], cx: float = 300, cy: float = 270,
                    r: float = 200) -> dict[str, dict]:
    """Place nodes evenly on a circle."""
    positions = {}
    n = len(nodes)
    if n == 0:
        return positions
    for i, node in enumerate(nodes):
        angle = 2 * math.pi * i / n - math.pi / 2
        positions[node] = {
            "x": round(cx + r * math.cos(angle), 1),
            "y": round(cy + r * math.sin(angle), 1),
        }
    return positions


# ---------------------------------------------------------------------------
# In-memory state
# ---------------------------------------------------------------------------

_graph: Optional[WeightedGraph] = None
_positions: Optional[dict] = None
_campus_graph: Optional[WeightedGraph] = None


# ---------------------------------------------------------------------------
# Pydantic request models
# ---------------------------------------------------------------------------

class WeightedEdge(BaseModel):
    u: str
    v: str
    w: float = 1.0


class GraphDef(BaseModel):
    directed: bool = False
    nodes: list[str] = []
    edges: list[list] = []  # [[u, v, weight], ...] or [[u, v], ...]


class AlgorithmRequest(BaseModel):
    algorithm: str = "dijkstra"
    source: str = ""


class PathRequest(BaseModel):
    source: str
    target: str


class CompareRequest(BaseModel):
    source: str = ""


class CampusPathRequest(BaseModel):
    source: str
    target: str


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")


# --- Graph Initialization ---

@app.post("/api/graph/init")
async def api_graph_init(req: GraphDef):
    """Initialize a weighted graph."""
    global _graph, _positions
    _graph = WeightedGraph(directed=req.directed)
    for n in req.nodes:
        _graph.add_node(n.strip())
    for edge in req.edges:
        if len(edge) >= 3:
            _graph.add_edge(str(edge[0]).strip(), str(edge[1]).strip(), float(edge[2]))
        elif len(edge) >= 2:
            _graph.add_edge(str(edge[0]).strip(), str(edge[1]).strip(), 1.0)
    _positions = circular_layout(_graph.nodes())
    return {
        "graph": _graph.to_dict(),
        "positions": _positions,
    }


@app.post("/api/graph/preset")
async def api_graph_preset():
    """Load a preset weighted undirected graph."""
    global _graph, _positions
    _graph = WeightedGraph(directed=False)
    preset_edges = [
        ("A", "B", 4), ("A", "C", 2), ("B", "C", 1),
        ("B", "D", 5), ("C", "D", 8), ("C", "E", 10),
        ("D", "E", 2), ("D", "F", 6), ("E", "F", 3),
    ]
    for u, v, w in preset_edges:
        _graph.add_edge(u, v, w)
    _positions = circular_layout(_graph.nodes())
    return {
        "graph": _graph.to_dict(),
        "positions": _positions,
    }


@app.post("/api/graph/preset-negative")
async def api_graph_preset_negative():
    """Load a preset directed graph with a negative weight edge (no negative cycle)."""
    global _graph, _positions
    _graph = WeightedGraph(directed=True)
    preset_edges = [
        ("S", "A", 6), ("S", "B", 7),
        ("A", "B", 8), ("A", "C", 5), ("A", "D", -4),
        ("B", "C", -3), ("B", "D", 9),
        ("C", "D", 7),
        ("D", "S", 2), ("D", "C", 7),
    ]
    for u, v, w in preset_edges:
        _graph.add_edge(u, v, w)
    _positions = circular_layout(_graph.nodes())
    return {
        "graph": _graph.to_dict(),
        "positions": _positions,
    }


@app.post("/api/graph/preset-negcycle")
async def api_graph_preset_negcycle():
    """Load a preset directed graph WITH a negative-weight cycle."""
    global _graph, _positions
    _graph = WeightedGraph(directed=True)
    preset_edges = [
        ("S", "A", 5), ("S", "B", 3),
        ("A", "B", 2), ("A", "C", 6),
        ("B", "C", 7), ("B", "D", 4),
        ("C", "D", -2),
        ("D", "B", -5),  # negative cycle: B -> D -> B (4 + (-5) = -1)
    ]
    for u, v, w in preset_edges:
        _graph.add_edge(u, v, w)
    _positions = circular_layout(_graph.nodes())
    return {
        "graph": _graph.to_dict(),
        "positions": _positions,
    }


# --- Dijkstra ---

@app.post("/api/dijkstra")
async def api_dijkstra(req: AlgorithmRequest):
    """Run Dijkstra's algorithm on the current graph."""
    global _graph, _positions
    if _graph is None:
        return {"error": "No graph initialized. Please create a graph first."}
    source = req.source.strip() or _graph.nodes()[0]
    t_start = time.perf_counter()
    result = dijkstra(_graph, source)
    t_end = time.perf_counter()
    result["time_ms"] = round((t_end - t_start) * 1000, 4)
    return {
        "graph": _graph.to_dict(),
        "positions": _positions,
        "result": result,
    }


@app.post("/api/dijkstra/path")
async def api_dijkstra_path(req: PathRequest):
    """Run Dijkstra and return shortest path between source and target."""
    global _graph, _positions
    if _graph is None:
        return {"error": "No graph initialized."}
    source = req.source.strip()
    target = req.target.strip()
    result = dijkstra(_graph, source)
    if "error" in result:
        return {"error": result["error"]}
    path = reconstruct_path(result["parent"], source, target)
    dist = result["distances"].get(target, "inf")
    return {
        "graph": _graph.to_dict(),
        "positions": _positions,
        "result": result,
        "path": path,
        "path_distance": dist,
    }


# --- Bellman-Ford ---

@app.post("/api/bellman-ford")
async def api_bellman_ford(req: AlgorithmRequest):
    """Run Bellman-Ford algorithm on the current graph."""
    global _graph, _positions
    if _graph is None:
        return {"error": "No graph initialized. Please create a graph first."}
    source = req.source.strip() or _graph.nodes()[0]
    t_start = time.perf_counter()
    result = bellman_ford(_graph, source)
    t_end = time.perf_counter()
    result["time_ms"] = round((t_end - t_start) * 1000, 4)
    return {
        "graph": _graph.to_dict(),
        "positions": _positions,
        "result": result,
    }


# --- Comparison ---

@app.post("/api/compare")
async def api_compare(req: CompareRequest):
    """Run both Dijkstra and Bellman-Ford and compare."""
    global _graph, _positions
    if _graph is None:
        return {"error": "No graph initialized. Please create a graph first."}
    source = req.source.strip() or _graph.nodes()[0]

    t0 = time.perf_counter()
    dijk = dijkstra(_graph, source)
    t1 = time.perf_counter()
    bf = bellman_ford(_graph, source)
    t2 = time.perf_counter()

    dijk["time_ms"] = round((t1 - t0) * 1000, 4)
    bf["time_ms"] = round((t2 - t1) * 1000, 4)

    return {
        "graph": _graph.to_dict(),
        "positions": _positions,
        "dijkstra": dijk,
        "bellman_ford": bf,
        "source": source,
    }


# --- Campus Map ---

@app.post("/api/campus/init")
async def api_campus_init():
    """Load the campus map preset."""
    global _campus_graph
    _campus_graph = build_campus_graph()
    return {
        "graph": _campus_graph.to_dict(),
        "positions": CAMPUS_POSITIONS,
        "buildings": _campus_graph.nodes(),
    }


@app.post("/api/campus/path")
async def api_campus_path(req: CampusPathRequest):
    """Find shortest path between two campus buildings."""
    global _campus_graph
    if _campus_graph is None:
        _campus_graph = build_campus_graph()
    source = req.source.strip()
    target = req.target.strip()
    result = dijkstra(_campus_graph, source)
    if "error" in result:
        return {"error": result["error"]}
    path = reconstruct_path(result["parent"], source, target)
    dist = result["distances"].get(target, "inf")
    return {
        "graph": _campus_graph.to_dict(),
        "positions": CAMPUS_POSITIONS,
        "result": result,
        "path": path,
        "path_distance": dist,
    }


# Mount static files LAST so /api routes take priority
app.mount("/static", StaticFiles(directory="static"), name="static")
