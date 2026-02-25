"""
Week 13 Project -- Algorithm Finale
FastAPI backend with TSP visualization, Knapsack solver,
algorithm complexity dashboard, and interactive quiz.
"""

from __future__ import annotations

import itertools
import math
import random
import time
from typing import Optional

from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI(title="Algorithm Finale")


# ---------------------------------------------------------------------------
# TSP -- Travelling Salesman Problem
# ---------------------------------------------------------------------------

def tsp_distance(cities: list[dict], order: list[int]) -> float:
    """Compute total round-trip tour distance for a given ordering."""
    total = 0.0
    n = len(order)
    for i in range(n):
        a = cities[order[i]]
        b = cities[order[(i + 1) % n]]
        total += math.hypot(b["x"] - a["x"], b["y"] - a["y"])
    return total


def tsp_brute_force(cities: list[dict]) -> dict:
    """Exact solution by trying all permutations. Feasible for N <= 10."""
    n = len(cities)
    if n <= 1:
        return {"order": list(range(n)), "distance": 0.0}

    # Fix city 0 and permute the rest to reduce from N! to (N-1)!
    rest = list(range(1, n))
    best_order = None
    best_dist = float("inf")
    perms_checked = 0

    for perm in itertools.permutations(rest):
        order = [0] + list(perm)
        d = tsp_distance(cities, order)
        perms_checked += 1
        if d < best_dist:
            best_dist = d
            best_order = order

    return {
        "order": best_order,
        "distance": round(best_dist, 2),
        "permutations_checked": perms_checked,
    }


def tsp_nearest_neighbor(cities: list[dict], start: int = 0) -> dict:
    """Greedy nearest-neighbor heuristic."""
    n = len(cities)
    if n <= 1:
        return {"order": list(range(n)), "distance": 0.0}

    visited = [False] * n
    order = [start]
    visited[start] = True
    current = start

    for _ in range(n - 1):
        best_next = -1
        best_d = float("inf")
        for j in range(n):
            if visited[j]:
                continue
            d = math.hypot(
                cities[j]["x"] - cities[current]["x"],
                cities[j]["y"] - cities[current]["y"],
            )
            if d < best_d:
                best_d = d
                best_next = j
        visited[best_next] = True
        order.append(best_next)
        current = best_next

    dist = tsp_distance(cities, order)
    return {
        "order": order,
        "distance": round(dist, 2),
    }


# TSP presets

TSP_PRESETS = {
    "pentagon": {
        "cities": [
            {"x": 300, "y": 60, "name": "A"},
            {"x": 490, "y": 200, "name": "B"},
            {"x": 420, "y": 420, "name": "C"},
            {"x": 180, "y": 420, "name": "D"},
            {"x": 110, "y": 200, "name": "E"},
        ]
    },
    "random_7": {
        "cities": [
            {"x": 80, "y": 120, "name": "C0"},
            {"x": 400, "y": 80, "name": "C1"},
            {"x": 520, "y": 250, "name": "C2"},
            {"x": 450, "y": 430, "name": "C3"},
            {"x": 200, "y": 400, "name": "C4"},
            {"x": 100, "y": 300, "name": "C5"},
            {"x": 300, "y": 220, "name": "C6"},
        ]
    },
    "cluster_8": {
        "cities": [
            {"x": 100, "y": 100, "name": "A1"},
            {"x": 150, "y": 140, "name": "A2"},
            {"x": 120, "y": 180, "name": "A3"},
            {"x": 400, "y": 100, "name": "B1"},
            {"x": 450, "y": 150, "name": "B2"},
            {"x": 250, "y": 400, "name": "C1"},
            {"x": 300, "y": 430, "name": "C2"},
            {"x": 500, "y": 380, "name": "D1"},
        ]
    },
}


# ---------------------------------------------------------------------------
# 0-1 Knapsack
# ---------------------------------------------------------------------------

def knapsack_dp(items: list[dict], capacity: int) -> dict:
    """0-1 Knapsack via dynamic programming. Returns DP table and selected items."""
    n = len(items)
    # dp[i][w] = max value using items 0..i-1 with capacity w
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        wi = items[i - 1]["weight"]
        vi = items[i - 1]["value"]
        for w in range(capacity + 1):
            dp[i][w] = dp[i - 1][w]
            if wi <= w and dp[i - 1][w - wi] + vi > dp[i][w]:
                dp[i][w] = dp[i - 1][w - wi] + vi

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append(i - 1)  # 0-indexed
            w -= items[i - 1]["weight"]
    selected.reverse()

    return {
        "max_value": dp[n][capacity],
        "selected": selected,
        "dp_table": dp,
    }


def knapsack_brute_force(items: list[dict], capacity: int) -> dict:
    """0-1 Knapsack by brute force (enumerate all 2^N subsets)."""
    n = len(items)
    best_value = 0
    best_selected = []
    subsets_checked = 0

    for mask in range(1 << n):
        total_w = 0
        total_v = 0
        chosen = []
        for i in range(n):
            if mask & (1 << i):
                total_w += items[i]["weight"]
                total_v += items[i]["value"]
                chosen.append(i)
        subsets_checked += 1
        if total_w <= capacity and total_v > best_value:
            best_value = total_v
            best_selected = chosen

    return {
        "max_value": best_value,
        "selected": best_selected,
        "subsets_checked": subsets_checked,
    }


# Knapsack presets

KNAPSACK_PRESETS = {
    "small": {
        "items": [
            {"name": "Laptop", "weight": 3, "value": 40},
            {"name": "Phone", "weight": 1, "value": 20},
            {"name": "Camera", "weight": 2, "value": 30},
            {"name": "Book", "weight": 2, "value": 10},
            {"name": "Tablet", "weight": 3, "value": 35},
        ],
        "capacity": 7,
    },
    "medium": {
        "items": [
            {"name": "Item A", "weight": 2, "value": 12},
            {"name": "Item B", "weight": 1, "value": 10},
            {"name": "Item C", "weight": 3, "value": 20},
            {"name": "Item D", "weight": 2, "value": 15},
            {"name": "Item E", "weight": 4, "value": 25},
            {"name": "Item F", "weight": 5, "value": 30},
            {"name": "Item G", "weight": 1, "value": 8},
            {"name": "Item H", "weight": 3, "value": 18},
        ],
        "capacity": 12,
    },
    "large": {
        "items": [
            {"name": f"Item {i+1}", "weight": random.randint(1, 8),
             "value": random.randint(5, 40)}
            for i in range(12)
        ],
        "capacity": 20,
    },
}

# Fix the random seed for reproducibility in the large preset
random.seed(42)
KNAPSACK_PRESETS["large"] = {
    "items": [
        {"name": f"Item {i+1}", "weight": random.randint(1, 8),
         "value": random.randint(5, 40)}
        for i in range(12)
    ],
    "capacity": 20,
}


# ---------------------------------------------------------------------------
# Algorithm Complexity Dashboard data
# ---------------------------------------------------------------------------

ALGORITHM_DASHBOARD = [
    {
        "category": "Sorting",
        "algorithms": [
            {
                "name": "Bubble Sort",
                "best": "O(n)",
                "average": "O(n^2)",
                "worst": "O(n^2)",
                "space": "O(1)",
                "stable": True,
                "paradigm": "Brute Force",
                "week": 2,
            },
            {
                "name": "Selection Sort",
                "best": "O(n^2)",
                "average": "O(n^2)",
                "worst": "O(n^2)",
                "space": "O(1)",
                "stable": False,
                "paradigm": "Brute Force",
                "week": 2,
            },
            {
                "name": "Insertion Sort",
                "best": "O(n)",
                "average": "O(n^2)",
                "worst": "O(n^2)",
                "space": "O(1)",
                "stable": True,
                "paradigm": "Incremental",
                "week": 2,
            },
            {
                "name": "Merge Sort",
                "best": "O(n log n)",
                "average": "O(n log n)",
                "worst": "O(n log n)",
                "space": "O(n)",
                "stable": True,
                "paradigm": "Divide & Conquer",
                "week": 4,
            },
            {
                "name": "Quick Sort",
                "best": "O(n log n)",
                "average": "O(n log n)",
                "worst": "O(n^2)",
                "space": "O(log n)",
                "stable": False,
                "paradigm": "Divide & Conquer",
                "week": 5,
            },
            {
                "name": "Heap Sort",
                "best": "O(n log n)",
                "average": "O(n log n)",
                "worst": "O(n log n)",
                "space": "O(1)",
                "stable": False,
                "paradigm": "Selection (Heap)",
                "week": 6,
            },
            {
                "name": "Counting Sort",
                "best": "O(n + k)",
                "average": "O(n + k)",
                "worst": "O(n + k)",
                "space": "O(k)",
                "stable": True,
                "paradigm": "Non-comparison",
                "week": 7,
            },
            {
                "name": "Radix Sort",
                "best": "O(d(n + k))",
                "average": "O(d(n + k))",
                "worst": "O(d(n + k))",
                "space": "O(n + k)",
                "stable": True,
                "paradigm": "Non-comparison",
                "week": 7,
            },
        ],
    },
    {
        "category": "Searching",
        "algorithms": [
            {
                "name": "Linear Search",
                "best": "O(1)",
                "average": "O(n)",
                "worst": "O(n)",
                "space": "O(1)",
                "paradigm": "Brute Force",
                "week": 1,
            },
            {
                "name": "Binary Search",
                "best": "O(1)",
                "average": "O(log n)",
                "worst": "O(log n)",
                "space": "O(1)",
                "paradigm": "Divide & Conquer",
                "week": 3,
            },
            {
                "name": "Hash Table Lookup",
                "best": "O(1)",
                "average": "O(1)",
                "worst": "O(n)",
                "space": "O(n)",
                "paradigm": "Hashing",
                "week": 9,
            },
        ],
    },
    {
        "category": "Graph Algorithms",
        "algorithms": [
            {
                "name": "BFS",
                "best": "O(V + E)",
                "average": "O(V + E)",
                "worst": "O(V + E)",
                "space": "O(V)",
                "paradigm": "Exploration",
                "week": 10,
            },
            {
                "name": "DFS",
                "best": "O(V + E)",
                "average": "O(V + E)",
                "worst": "O(V + E)",
                "space": "O(V)",
                "paradigm": "Exploration",
                "week": 10,
            },
            {
                "name": "Dijkstra's",
                "best": "O((V+E) log V)",
                "average": "O((V+E) log V)",
                "worst": "O((V+E) log V)",
                "space": "O(V)",
                "paradigm": "Greedy",
                "week": 12,
            },
            {
                "name": "Bellman-Ford",
                "best": "O(V * E)",
                "average": "O(V * E)",
                "worst": "O(V * E)",
                "space": "O(V)",
                "paradigm": "Dynamic Programming",
                "week": 12,
            },
            {
                "name": "Kruskal's (MST)",
                "best": "O(E log E)",
                "average": "O(E log E)",
                "worst": "O(E log E)",
                "space": "O(V)",
                "paradigm": "Greedy",
                "week": 11,
            },
            {
                "name": "Prim's (MST)",
                "best": "O(E log V)",
                "average": "O(E log V)",
                "worst": "O(E log V)",
                "space": "O(V)",
                "paradigm": "Greedy",
                "week": 11,
            },
            {
                "name": "Topological Sort",
                "best": "O(V + E)",
                "average": "O(V + E)",
                "worst": "O(V + E)",
                "space": "O(V)",
                "paradigm": "DFS-based",
                "week": 10,
            },
        ],
    },
    {
        "category": "Dynamic Programming",
        "algorithms": [
            {
                "name": "0-1 Knapsack",
                "best": "O(nW)",
                "average": "O(nW)",
                "worst": "O(nW)",
                "space": "O(nW)",
                "paradigm": "Dynamic Programming",
                "week": 13,
            },
            {
                "name": "LCS",
                "best": "O(mn)",
                "average": "O(mn)",
                "worst": "O(mn)",
                "space": "O(mn)",
                "paradigm": "Dynamic Programming",
                "week": 8,
            },
            {
                "name": "Matrix Chain",
                "best": "O(n^3)",
                "average": "O(n^3)",
                "worst": "O(n^3)",
                "space": "O(n^2)",
                "paradigm": "Dynamic Programming",
                "week": 8,
            },
        ],
    },
    {
        "category": "NP-Complete Problems",
        "algorithms": [
            {
                "name": "TSP (Brute Force)",
                "best": "O(n!)",
                "average": "O(n!)",
                "worst": "O(n!)",
                "space": "O(n)",
                "paradigm": "Exhaustive Search",
                "week": 13,
            },
            {
                "name": "TSP (Nearest Neighbor)",
                "best": "O(n^2)",
                "average": "O(n^2)",
                "worst": "O(n^2)",
                "space": "O(n)",
                "paradigm": "Greedy Heuristic",
                "week": 13,
            },
        ],
    },
]


# ---------------------------------------------------------------------------
# Quiz questions
# ---------------------------------------------------------------------------

QUIZ_QUESTIONS = [
    {
        "id": 1,
        "question": "Which sorting algorithm has the best worst-case time complexity?",
        "options": ["Quick Sort", "Merge Sort", "Bubble Sort", "Selection Sort"],
        "answer": 1,
        "explanation": "Merge Sort guarantees O(n log n) in the worst case, while Quick Sort degrades to O(n^2).",
    },
    {
        "id": 2,
        "question": "What is the time complexity of binary search on a sorted array of size n?",
        "options": ["O(n)", "O(n log n)", "O(log n)", "O(1)"],
        "answer": 2,
        "explanation": "Binary search halves the search space each step, giving O(log n).",
    },
    {
        "id": 3,
        "question": "Which algorithm paradigm does Dijkstra's shortest path algorithm use?",
        "options": ["Divide and Conquer", "Dynamic Programming", "Greedy", "Backtracking"],
        "answer": 2,
        "explanation": "Dijkstra always picks the unvisited node with the smallest known distance -- a greedy choice.",
    },
    {
        "id": 4,
        "question": "The Travelling Salesman Problem (TSP) is in which complexity class?",
        "options": ["P", "NP-complete", "O(n log n)", "Linear"],
        "answer": 1,
        "explanation": "TSP is a classic NP-complete problem. No polynomial-time exact algorithm is known.",
    },
    {
        "id": 5,
        "question": "What is the space complexity of the 0-1 Knapsack DP solution with n items and capacity W?",
        "options": ["O(n)", "O(W)", "O(nW)", "O(2^n)"],
        "answer": 2,
        "explanation": "The DP table has (n+1) rows and (W+1) columns, so it uses O(nW) space.",
    },
    {
        "id": 6,
        "question": "Which data structure does BFS use to track the frontier?",
        "options": ["Stack", "Queue", "Priority Queue", "Hash Set"],
        "answer": 1,
        "explanation": "BFS explores nodes level by level using a FIFO queue.",
    },
    {
        "id": 7,
        "question": "Which of these algorithms can handle negative edge weights?",
        "options": ["Dijkstra", "Bellman-Ford", "BFS", "Prim's"],
        "answer": 1,
        "explanation": "Bellman-Ford can handle negative edges and even detect negative cycles. Dijkstra cannot.",
    },
    {
        "id": 8,
        "question": "What does it mean for a problem to be NP-complete?",
        "options": [
            "It cannot be solved at all",
            "It is in NP and every NP problem reduces to it in polynomial time",
            "It can always be solved in polynomial time",
            "It requires exponential space"
        ],
        "answer": 1,
        "explanation": "NP-complete problems are the hardest in NP: every NP problem can be reduced to them in polynomial time.",
    },
    {
        "id": 9,
        "question": "If P = NP, which of the following would be true?",
        "options": [
            "All problems become unsolvable",
            "Every problem verifiable in polynomial time is also solvable in polynomial time",
            "Sorting becomes O(1)",
            "Hash tables become obsolete"
        ],
        "answer": 1,
        "explanation": "P = NP would mean that every problem whose solution can be verified quickly can also be solved quickly.",
    },
    {
        "id": 10,
        "question": "Which algorithm builds a minimum spanning tree by always picking the cheapest edge that does not form a cycle?",
        "options": ["Dijkstra's", "Prim's", "Kruskal's", "Bellman-Ford"],
        "answer": 2,
        "explanation": "Kruskal's algorithm sorts edges by weight and adds them if they don't form a cycle, using Union-Find.",
    },
]


# ---------------------------------------------------------------------------
# Pydantic request models
# ---------------------------------------------------------------------------

class TSPRequest(BaseModel):
    cities: list[dict]  # [{x, y, name}, ...]


class TSPPresetRequest(BaseModel):
    preset: str = "pentagon"


class KnapsackRequest(BaseModel):
    items: list[dict]  # [{name, weight, value}, ...]
    capacity: int


class KnapsackPresetRequest(BaseModel):
    preset: str = "small"


class QuizSubmission(BaseModel):
    answers: list[int]  # list of selected option indices, one per question


# ---------------------------------------------------------------------------
# API Endpoints
# ---------------------------------------------------------------------------

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")


# --- TSP ---

@app.post("/api/tsp/solve")
async def api_tsp_solve(req: TSPRequest):
    """Solve TSP with both brute-force (if N <= 10) and nearest-neighbor."""
    cities = req.cities
    n = len(cities)

    result: dict = {"n": n, "cities": cities}

    # Nearest-neighbor heuristic (always)
    t0 = time.perf_counter()
    nn = tsp_nearest_neighbor(cities)
    t1 = time.perf_counter()
    nn["time_ms"] = round((t1 - t0) * 1000, 4)
    result["nearest_neighbor"] = nn

    # Brute-force (only for small N)
    if n <= 10:
        t0 = time.perf_counter()
        bf = tsp_brute_force(cities)
        t1 = time.perf_counter()
        bf["time_ms"] = round((t1 - t0) * 1000, 4)
        result["brute_force"] = bf
    else:
        result["brute_force"] = None
        result["brute_force_skipped"] = (
            f"Brute force skipped: N={n} is too large (limit 10). "
            f"Would require checking {math.factorial(n - 1):,} permutations."
        )

    # Comparison
    if result["brute_force"]:
        bf_dist = result["brute_force"]["distance"]
        nn_dist = result["nearest_neighbor"]["distance"]
        if bf_dist > 0:
            ratio = round(nn_dist / bf_dist, 3)
        else:
            ratio = 1.0
        result["comparison"] = {
            "optimal_distance": bf_dist,
            "heuristic_distance": nn_dist,
            "ratio": ratio,
            "quality_percent": round(100.0 / ratio, 1) if ratio > 0 else 100.0,
        }

    return result


@app.post("/api/tsp/preset")
async def api_tsp_preset(req: TSPPresetRequest):
    """Return a TSP preset."""
    preset = TSP_PRESETS.get(req.preset)
    if not preset:
        return {"error": f"Unknown preset '{req.preset}'. Available: {list(TSP_PRESETS.keys())}"}
    return {"preset": req.preset, "cities": preset["cities"]}


@app.get("/api/tsp/presets")
async def api_tsp_presets():
    """List available TSP presets."""
    return {
        "presets": {k: {"n": len(v["cities"])} for k, v in TSP_PRESETS.items()}
    }


# --- Knapsack ---

@app.post("/api/knapsack/solve")
async def api_knapsack_solve(req: KnapsackRequest):
    """Solve 0-1 Knapsack with both DP and brute force."""
    items = req.items
    capacity = req.capacity
    n = len(items)

    result: dict = {"n": n, "capacity": capacity, "items": items}

    # DP solution
    t0 = time.perf_counter()
    dp_result = knapsack_dp(items, capacity)
    t1 = time.perf_counter()
    dp_result["time_ms"] = round((t1 - t0) * 1000, 4)
    result["dp"] = {
        "max_value": dp_result["max_value"],
        "selected": dp_result["selected"],
        "dp_table": dp_result["dp_table"],
        "time_ms": dp_result["time_ms"],
    }

    # Brute-force solution (only for N <= 20)
    if n <= 20:
        t0 = time.perf_counter()
        bf_result = knapsack_brute_force(items, capacity)
        t1 = time.perf_counter()
        bf_result["time_ms"] = round((t1 - t0) * 1000, 4)
        result["brute_force"] = bf_result
    else:
        result["brute_force"] = None
        result["brute_force_skipped"] = (
            f"Brute force skipped: N={n} would require checking {2**n:,} subsets."
        )

    # Comparison
    result["comparison"] = {
        "dp_time_ms": result["dp"]["time_ms"],
        "bf_time_ms": result["brute_force"]["time_ms"] if result.get("brute_force") else None,
        "dp_subproblems": (n + 1) * (capacity + 1),
        "bf_subsets": 2 ** n if n <= 20 else None,
    }

    return result


@app.post("/api/knapsack/preset")
async def api_knapsack_preset(req: KnapsackPresetRequest):
    """Return a Knapsack preset."""
    preset = KNAPSACK_PRESETS.get(req.preset)
    if not preset:
        return {"error": f"Unknown preset '{req.preset}'. Available: {list(KNAPSACK_PRESETS.keys())}"}
    return {"preset": req.preset, **preset}


@app.get("/api/knapsack/presets")
async def api_knapsack_presets():
    """List available Knapsack presets."""
    return {
        "presets": {
            k: {"n": len(v["items"]), "capacity": v["capacity"]}
            for k, v in KNAPSACK_PRESETS.items()
        }
    }


# --- Algorithm Dashboard ---

@app.get("/api/dashboard")
async def api_dashboard():
    """Return the algorithm complexity dashboard data."""
    return {"categories": ALGORITHM_DASHBOARD}


# --- Quiz ---

@app.get("/api/quiz")
async def api_quiz():
    """Return quiz questions (without answers)."""
    questions = []
    for q in QUIZ_QUESTIONS:
        questions.append({
            "id": q["id"],
            "question": q["question"],
            "options": q["options"],
        })
    return {"questions": questions, "total": len(questions)}


@app.post("/api/quiz/submit")
async def api_quiz_submit(req: QuizSubmission):
    """Grade quiz answers and return results."""
    answers = req.answers
    results = []
    correct_count = 0

    for i, q in enumerate(QUIZ_QUESTIONS):
        user_answer = answers[i] if i < len(answers) else -1
        is_correct = user_answer == q["answer"]
        if is_correct:
            correct_count += 1
        results.append({
            "id": q["id"],
            "question": q["question"],
            "options": q["options"],
            "user_answer": user_answer,
            "correct_answer": q["answer"],
            "is_correct": is_correct,
            "explanation": q["explanation"],
        })

    total = len(QUIZ_QUESTIONS)
    percentage = round(correct_count / total * 100, 1) if total > 0 else 0

    return {
        "score": correct_count,
        "total": total,
        "percentage": percentage,
        "results": results,
    }


# Mount static files LAST so /api routes take priority
app.mount("/static", StaticFiles(directory="static"), name="static")
