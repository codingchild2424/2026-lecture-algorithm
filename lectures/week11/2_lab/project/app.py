"""
Week 11 Project -- Graph Traversal Explorer
FastAPI backend with BFS/DFS implementations, topological sort, cycle
detection, shortest path, and social-network friend suggestions.
"""

from __future__ import annotations

import math
import random
from collections import deque
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI(title="Graph Traversal Explorer")


# ---------------------------------------------------------------------------
# Core graph representation
# ---------------------------------------------------------------------------

class Graph:
    """Simple adjacency-list graph supporting directed and undirected modes."""

    def __init__(self, directed: bool = False):
        self.directed = directed
        self.adj: dict[str, list[str]] = {}

    def add_node(self, node: str):
        if node not in self.adj:
            self.adj[node] = []

    def add_edge(self, u: str, v: str):
        self.add_node(u)
        self.add_node(v)
        if v not in self.adj[u]:
            self.adj[u].append(v)
        if not self.directed and u not in self.adj[v]:
            self.adj[v].append(u)

    def nodes(self) -> list[str]:
        return sorted(self.adj.keys())

    def edges(self) -> list[tuple[str, str]]:
        result = []
        seen = set()
        for u in self.adj:
            for v in self.adj[u]:
                key = (u, v) if self.directed else tuple(sorted((u, v)))
                if key not in seen:
                    seen.add(key)
                    result.append((u, v))
        return result

    def neighbors(self, node: str) -> list[str]:
        return self.adj.get(node, [])

    def to_dict(self) -> dict:
        return {
            "directed": self.directed,
            "nodes": self.nodes(),
            "edges": [{"from": u, "to": v} for u, v in self.edges()],
            "adjacency": {k: sorted(v) for k, v in self.adj.items()},
        }


# ---------------------------------------------------------------------------
# BFS
# ---------------------------------------------------------------------------

def bfs(graph: Graph, start: str) -> dict:
    """Run BFS from *start* and return the visit order and BFS tree."""
    if start not in graph.adj:
        return {"error": f"Node '{start}' not in graph"}

    visited_order: list[str] = []
    parent: dict[str, Optional[str]] = {start: None}
    level: dict[str, int] = {start: 0}
    queue = deque([start])
    steps: list[dict] = []

    while queue:
        node = queue.popleft()
        visited_order.append(node)
        step = {
            "action": "visit",
            "node": node,
            "level": level[node],
            "queue": list(queue),
        }
        for nb in sorted(graph.neighbors(node)):
            if nb not in parent:
                parent[nb] = node
                level[nb] = level[node] + 1
                queue.append(nb)
                step.setdefault("enqueued", []).append(nb)
        steps.append(step)

    tree_edges = []
    for node, par in parent.items():
        if par is not None:
            tree_edges.append({"from": par, "to": node})

    return {
        "algorithm": "BFS",
        "start": start,
        "visit_order": visited_order,
        "levels": level,
        "parent": parent,
        "tree_edges": tree_edges,
        "steps": steps,
    }


# ---------------------------------------------------------------------------
# DFS
# ---------------------------------------------------------------------------

def dfs(graph: Graph, start: str) -> dict:
    """Run iterative DFS from *start* and return visit order and DFS tree."""
    if start not in graph.adj:
        return {"error": f"Node '{start}' not in graph"}

    visited_order: list[str] = []
    visited: set[str] = set()
    parent: dict[str, Optional[str]] = {start: None}
    stack: list[str] = [start]
    steps: list[dict] = []

    while stack:
        node = stack.pop()
        if node in visited:
            continue
        visited.add(node)
        visited_order.append(node)
        step = {
            "action": "visit",
            "node": node,
            "stack": list(stack),
        }
        pushed = []
        for nb in sorted(graph.neighbors(node), reverse=True):
            if nb not in visited:
                stack.append(nb)
                if nb not in parent:
                    parent[nb] = node
                pushed.append(nb)
        step["pushed"] = list(reversed(pushed))
        steps.append(step)

    tree_edges = []
    for node, par in parent.items():
        if par is not None:
            tree_edges.append({"from": par, "to": node})

    return {
        "algorithm": "DFS",
        "start": start,
        "visit_order": visited_order,
        "parent": parent,
        "tree_edges": tree_edges,
        "steps": steps,
    }


# ---------------------------------------------------------------------------
# BFS Shortest Path (unweighted)
# ---------------------------------------------------------------------------

def bfs_shortest_path(graph: Graph, start: str, end: str) -> dict:
    """Find the shortest path between two nodes using BFS (unweighted)."""
    if start not in graph.adj:
        return {"error": f"Node '{start}' not in graph"}
    if end not in graph.adj:
        return {"error": f"Node '{end}' not in graph"}

    parent: dict[str, Optional[str]] = {start: None}
    level: dict[str, int] = {start: 0}
    queue = deque([start])
    steps: list[dict] = []

    found = False
    while queue:
        node = queue.popleft()
        step = {
            "action": "visit",
            "node": node,
            "level": level[node],
            "queue": list(queue),
        }
        if node == end:
            found = True
            steps.append(step)
            break
        for nb in sorted(graph.neighbors(node)):
            if nb not in parent:
                parent[nb] = node
                level[nb] = level[node] + 1
                queue.append(nb)
                step.setdefault("enqueued", []).append(nb)
        steps.append(step)

    if not found:
        return {
            "start": start,
            "end": end,
            "found": False,
            "distance": -1,
            "path": [],
            "steps": steps,
        }

    # Reconstruct path
    path = []
    cur: Optional[str] = end
    while cur is not None:
        path.append(cur)
        cur = parent[cur]
    path.reverse()

    return {
        "start": start,
        "end": end,
        "found": True,
        "distance": len(path) - 1,
        "path": path,
        "steps": steps,
    }


# ---------------------------------------------------------------------------
# Topological Sort (Kahn's algorithm)
# ---------------------------------------------------------------------------

def topological_sort(graph: Graph) -> dict:
    """Kahn's algorithm for topological sort on a directed graph."""
    if not graph.directed:
        return {"error": "Topological sort requires a directed graph"}

    in_degree: dict[str, int] = {n: 0 for n in graph.adj}
    for u in graph.adj:
        for v in graph.adj[u]:
            in_degree[v] = in_degree.get(v, 0) + 1

    queue = deque(sorted(n for n in in_degree if in_degree[n] == 0))
    order: list[str] = []
    steps: list[dict] = []

    while queue:
        node = queue.popleft()
        order.append(node)
        step = {
            "action": "remove",
            "node": node,
            "queue": list(queue),
            "reduced": [],
        }
        for nb in sorted(graph.adj.get(node, [])):
            in_degree[nb] -= 1
            step["reduced"].append({"node": nb, "new_in_degree": in_degree[nb]})
            if in_degree[nb] == 0:
                queue.append(nb)
                step.setdefault("newly_zero", []).append(nb)
        steps.append(step)

    has_cycle = len(order) != len(graph.adj)
    return {
        "algorithm": "topological_sort",
        "has_cycle": has_cycle,
        "order": order if not has_cycle else [],
        "processed": len(order),
        "total_nodes": len(graph.adj),
        "steps": steps,
    }


# ---------------------------------------------------------------------------
# Cycle Detection (DFS-based, for directed graphs)
# ---------------------------------------------------------------------------

def detect_cycle(graph: Graph) -> dict:
    """DFS-based cycle detection for a directed graph.
    Returns whether a cycle exists and, if so, the cycle path."""
    if not graph.directed:
        return {"error": "Cycle detection demo requires a directed graph"}

    WHITE, GRAY, BLACK = 0, 1, 2
    color: dict[str, int] = {n: WHITE for n in graph.adj}
    parent: dict[str, Optional[str]] = {n: None for n in graph.adj}
    steps: list[dict] = []
    cycle_path: list[str] = []

    def _dfs(u: str) -> bool:
        color[u] = GRAY
        steps.append({"action": "enter", "node": u, "state": "GRAY"})
        for v in sorted(graph.adj.get(u, [])):
            if color[v] == GRAY:
                # Back edge found => cycle
                steps.append({
                    "action": "back_edge",
                    "from": u,
                    "to": v,
                    "state": "CYCLE",
                })
                # Reconstruct cycle
                path = [v, u]
                cur = u
                while cur != v:
                    cur = parent[cur]
                    if cur is None:
                        break
                    path.append(cur)
                path.reverse()
                cycle_path.extend(path)
                return True
            if color[v] == WHITE:
                parent[v] = u
                if _dfs(v):
                    return True
        color[u] = BLACK
        steps.append({"action": "finish", "node": u, "state": "BLACK"})
        return False

    has_cycle = False
    for node in sorted(graph.adj):
        if color[node] == WHITE:
            if _dfs(node):
                has_cycle = True
                break

    return {
        "algorithm": "cycle_detection",
        "has_cycle": has_cycle,
        "cycle": cycle_path if has_cycle else [],
        "steps": steps,
    }


# ---------------------------------------------------------------------------
# Social Network
# ---------------------------------------------------------------------------

SOCIAL_PRESETS: dict[str, list[str]] = {
    "Alice":   ["Bob", "Charlie", "Diana"],
    "Bob":     ["Alice", "Eve", "Frank"],
    "Charlie": ["Alice", "Grace"],
    "Diana":   ["Alice", "Hank"],
    "Eve":     ["Bob", "Ivy"],
    "Frank":   ["Bob", "Grace", "Jack"],
    "Grace":   ["Charlie", "Frank"],
    "Hank":    ["Diana", "Ivy"],
    "Ivy":     ["Eve", "Hank"],
    "Jack":    ["Frank"],
}


def build_social_graph() -> Graph:
    g = Graph(directed=False)
    for person, friends in SOCIAL_PRESETS.items():
        g.add_node(person)
        for f in friends:
            g.add_edge(person, f)
    return g


def friend_suggestions(graph: Graph, user: str, depth: int = 2) -> dict:
    """Use BFS to find friend-of-friend suggestions up to *depth* hops."""
    if user not in graph.adj:
        return {"error": f"User '{user}' not in the social network"}

    direct_friends = set(graph.neighbors(user))
    parent: dict[str, Optional[str]] = {user: None}
    level: dict[str, int] = {user: 0}
    queue = deque([user])
    steps: list[dict] = []

    while queue:
        node = queue.popleft()
        step = {
            "action": "visit",
            "node": node,
            "level": level[node],
            "queue": list(queue),
        }
        if level[node] >= depth:
            steps.append(step)
            continue
        for nb in sorted(graph.neighbors(node)):
            if nb not in parent:
                parent[nb] = node
                level[nb] = level[node] + 1
                queue.append(nb)
                step.setdefault("enqueued", []).append(nb)
        steps.append(step)

    suggestions = []
    for person, lv in sorted(level.items(), key=lambda x: (x[1], x[0])):
        if person == user:
            continue
        if person in direct_friends:
            continue
        if lv <= depth:
            # Trace the mutual connection
            path = []
            cur: Optional[str] = person
            while cur is not None:
                path.append(cur)
                cur = parent[cur]
            path.reverse()
            suggestions.append({
                "person": person,
                "distance": lv,
                "via_path": path,
                "mutual_connection": path[1] if len(path) > 1 else None,
            })

    return {
        "user": user,
        "direct_friends": sorted(direct_friends),
        "suggestions": suggestions,
        "bfs_tree": {
            "parent": parent,
            "levels": level,
            "tree_edges": [
                {"from": par, "to": node}
                for node, par in parent.items()
                if par is not None
            ],
        },
        "steps": steps,
    }


# ---------------------------------------------------------------------------
# Layout helpers -- assign positions to nodes for SVG rendering
# ---------------------------------------------------------------------------

def circular_layout(nodes: list[str], cx: float = 300, cy: float = 250,
                    r: float = 180) -> dict[str, dict]:
    """Place nodes evenly on a circle."""
    positions = {}
    n = len(nodes)
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

_traversal_graph: Optional[Graph] = None
_dag_graph: Optional[Graph] = None
_social_graph: Optional[Graph] = None


# ---------------------------------------------------------------------------
# Pydantic request / response models
# ---------------------------------------------------------------------------

class GraphDef(BaseModel):
    directed: bool = False
    nodes: list[str] = []
    edges: list[list[str]] = []  # [[u, v], ...]


class TraversalRequest(BaseModel):
    algorithm: str = "bfs"  # "bfs" or "dfs"
    start: str = ""


class ShortestPathRequest(BaseModel):
    start: str
    end: str


class DAGRequest(BaseModel):
    nodes: list[str] = []
    edges: list[list[str]] = []


class SocialRequest(BaseModel):
    user: str
    depth: int = 2


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")


# --- Graph Traversal Visualization ---

@app.post("/api/graph/init")
async def api_graph_init(req: GraphDef):
    """Initialize a graph for traversal visualization."""
    global _traversal_graph
    _traversal_graph = Graph(directed=req.directed)
    for n in req.nodes:
        _traversal_graph.add_node(n.strip())
    for edge in req.edges:
        if len(edge) >= 2:
            _traversal_graph.add_edge(edge[0].strip(), edge[1].strip())
    positions = circular_layout(_traversal_graph.nodes())
    return {
        "graph": _traversal_graph.to_dict(),
        "positions": positions,
    }


@app.post("/api/graph/preset")
async def api_graph_preset():
    """Load a preset undirected graph for traversal demo."""
    global _traversal_graph
    _traversal_graph = Graph(directed=False)
    preset_edges = [
        ("A", "B"), ("A", "C"), ("B", "D"), ("B", "E"),
        ("C", "F"), ("D", "G"), ("E", "G"), ("F", "G"),
        ("E", "F"),
    ]
    for u, v in preset_edges:
        _traversal_graph.add_edge(u, v)
    positions = circular_layout(_traversal_graph.nodes())
    return {
        "graph": _traversal_graph.to_dict(),
        "positions": positions,
    }


@app.post("/api/graph/traverse")
async def api_graph_traverse(req: TraversalRequest):
    """Run BFS or DFS on the current traversal graph."""
    global _traversal_graph
    if _traversal_graph is None:
        return {"error": "No graph initialized. Please create a graph first."}
    start = req.start.strip()
    if not start:
        nodes = _traversal_graph.nodes()
        start = nodes[0] if nodes else ""
    if req.algorithm == "dfs":
        result = dfs(_traversal_graph, start)
    else:
        result = bfs(_traversal_graph, start)
    positions = circular_layout(_traversal_graph.nodes())
    return {
        "graph": _traversal_graph.to_dict(),
        "positions": positions,
        "result": result,
    }


@app.post("/api/graph/shortest-path")
async def api_graph_shortest_path(req: ShortestPathRequest):
    """Find the shortest path between two nodes using BFS."""
    global _traversal_graph
    if _traversal_graph is None:
        return {"error": "No graph initialized. Please create a graph first."}
    result = bfs_shortest_path(_traversal_graph, req.start.strip(), req.end.strip())
    positions = circular_layout(_traversal_graph.nodes())
    return {
        "graph": _traversal_graph.to_dict(),
        "positions": positions,
        "result": result,
    }


# --- DAG: Topological Sort & Cycle Detection ---

@app.post("/api/dag/init")
async def api_dag_init(req: DAGRequest):
    """Initialize a directed graph for topo sort / cycle detection."""
    global _dag_graph
    _dag_graph = Graph(directed=True)
    for n in req.nodes:
        _dag_graph.add_node(n.strip())
    for edge in req.edges:
        if len(edge) >= 2:
            _dag_graph.add_edge(edge[0].strip(), edge[1].strip())
    positions = circular_layout(_dag_graph.nodes())
    return {
        "graph": _dag_graph.to_dict(),
        "positions": positions,
    }


@app.post("/api/dag/preset-dag")
async def api_dag_preset_dag():
    """Load a preset DAG (no cycles)."""
    global _dag_graph
    _dag_graph = Graph(directed=True)
    edges = [
        ("CS101", "CS201"), ("CS101", "CS202"),
        ("CS201", "CS301"), ("CS202", "CS301"),
        ("CS202", "CS303"), ("CS301", "CS401"),
        ("CS303", "CS401"), ("MATH1", "CS202"),
        ("MATH1", "MATH2"), ("MATH2", "CS303"),
    ]
    for u, v in edges:
        _dag_graph.add_edge(u, v)
    positions = circular_layout(_dag_graph.nodes())
    return {
        "graph": _dag_graph.to_dict(),
        "positions": positions,
    }


@app.post("/api/dag/preset-cycle")
async def api_dag_preset_cycle():
    """Load a preset directed graph WITH a cycle."""
    global _dag_graph
    _dag_graph = Graph(directed=True)
    edges = [
        ("A", "B"), ("B", "C"), ("C", "D"),
        ("D", "B"),  # cycle: B -> C -> D -> B
        ("A", "E"), ("E", "F"),
    ]
    for u, v in edges:
        _dag_graph.add_edge(u, v)
    positions = circular_layout(_dag_graph.nodes())
    return {
        "graph": _dag_graph.to_dict(),
        "positions": positions,
    }


@app.post("/api/dag/toposort")
async def api_dag_toposort():
    """Run topological sort on the current DAG."""
    global _dag_graph
    if _dag_graph is None:
        return {"error": "No directed graph initialized."}
    result = topological_sort(_dag_graph)
    positions = circular_layout(_dag_graph.nodes())
    return {
        "graph": _dag_graph.to_dict(),
        "positions": positions,
        "result": result,
    }


@app.post("/api/dag/cycle")
async def api_dag_cycle():
    """Run cycle detection on the current directed graph."""
    global _dag_graph
    if _dag_graph is None:
        return {"error": "No directed graph initialized."}
    result = detect_cycle(_dag_graph)
    positions = circular_layout(_dag_graph.nodes())
    return {
        "graph": _dag_graph.to_dict(),
        "positions": positions,
        "result": result,
    }


# --- Social Network ---

@app.post("/api/social/init")
async def api_social_init():
    """Load the preset social network."""
    global _social_graph
    _social_graph = build_social_graph()
    positions = circular_layout(_social_graph.nodes())
    return {
        "graph": _social_graph.to_dict(),
        "positions": positions,
        "users": _social_graph.nodes(),
    }


@app.post("/api/social/suggest")
async def api_social_suggest(req: SocialRequest):
    """Get friend suggestions for a user via BFS."""
    global _social_graph
    if _social_graph is None:
        _social_graph = build_social_graph()
    depth = max(2, min(req.depth, 4))
    result = friend_suggestions(_social_graph, req.user.strip(), depth)
    positions = circular_layout(_social_graph.nodes())
    return {
        "graph": _social_graph.to_dict(),
        "positions": positions,
        "result": result,
    }


# Mount static files LAST so /api routes take priority
app.mount("/static", StaticFiles(directory="static"), name="static")
