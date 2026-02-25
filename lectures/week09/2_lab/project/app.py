"""
Week 09 Project -- Algorithm Review Web App
FastAPI backend serving algorithm endpoints and static files.
"""

import time
import math
from typing import Optional
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import RedirectResponse
from pydantic import BaseModel

app = FastAPI(title="Algorithm Review Web App")


# ---------------------------------------------------------------------------
# Pydantic models for request bodies
# ---------------------------------------------------------------------------

class SortRequest(BaseModel):
    numbers: list[int | float]
    algorithm: str  # "bubble", "selection", "insertion", "merge", "quick"


class BinarySearchRequest(BaseModel):
    numbers: list[int | float]
    target: int | float


class GreedyCoinRequest(BaseModel):
    amount: int
    coins: list[int]


class DPFibRequest(BaseModel):
    n: int  # which Fibonacci number to compute


class DPKnapsackRequest(BaseModel):
    capacity: int
    weights: list[int]
    values: list[int]
    names: Optional[list[str]] = None


# ---------------------------------------------------------------------------
# Sorting algorithms -- each returns (sorted list, steps log, comparisons)
# ---------------------------------------------------------------------------

def bubble_sort(arr: list) -> dict:
    a = list(arr)
    steps = []
    comparisons = 0
    swaps = 0
    n = len(a)
    for i in range(n):
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                steps.append({
                    "action": "swap",
                    "indices": [j, j + 1],
                    "array": list(a),
                })
    return {"sorted": a, "steps": steps, "comparisons": comparisons, "swaps": swaps}


def selection_sort(arr: list) -> dict:
    a = list(arr)
    steps = []
    comparisons = 0
    swaps = 0
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1
            steps.append({
                "action": "swap",
                "indices": [i, min_idx],
                "array": list(a),
            })
    return {"sorted": a, "steps": steps, "comparisons": comparisons, "swaps": swaps}


def insertion_sort(arr: list) -> dict:
    a = list(arr)
    steps = []
    comparisons = 0
    shifts = 0
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        while j >= 0:
            comparisons += 1
            if a[j] > key:
                a[j + 1] = a[j]
                shifts += 1
                j -= 1
            else:
                break
        a[j + 1] = key
        steps.append({
            "action": "insert",
            "index": j + 1,
            "value": key,
            "array": list(a),
        })
    return {"sorted": a, "steps": steps, "comparisons": comparisons, "swaps": shifts}


def merge_sort(arr: list) -> dict:
    comparisons = [0]
    steps = []

    def _merge_sort(a: list) -> list:
        if len(a) <= 1:
            return a
        mid = len(a) // 2
        left = _merge_sort(a[:mid])
        right = _merge_sort(a[mid:])
        return _merge(left, right)

    def _merge(left, right):
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            comparisons[0] += 1
            if left[i] <= right[j]:
                result.append(left[i])
                i += 1
            else:
                result.append(right[j])
                j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        steps.append({
            "action": "merge",
            "left": left,
            "right": right,
            "merged": list(result),
        })
        return result

    sorted_arr = _merge_sort(list(arr))
    return {"sorted": sorted_arr, "steps": steps, "comparisons": comparisons[0], "swaps": 0}


def quick_sort(arr: list) -> dict:
    comparisons = [0]
    swaps = [0]
    steps = []

    def _quick_sort(a: list, low: int, high: int):
        if low < high:
            pi = _partition(a, low, high)
            _quick_sort(a, low, pi - 1)
            _quick_sort(a, pi + 1, high)

    def _partition(a: list, low: int, high: int) -> int:
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if a[j] <= pivot:
                i += 1
                a[i], a[j] = a[j], a[i]
                if i != j:
                    swaps[0] += 1
        a[i + 1], a[high] = a[high], a[i + 1]
        swaps[0] += 1
        steps.append({
            "action": "partition",
            "pivot": pivot,
            "pivot_index": i + 1,
            "array": list(a),
        })
        return i + 1

    a = list(arr)
    _quick_sort(a, 0, len(a) - 1)
    return {"sorted": a, "steps": steps, "comparisons": comparisons[0], "swaps": swaps[0]}


SORT_ALGORITHMS = {
    "bubble": bubble_sort,
    "selection": selection_sort,
    "insertion": insertion_sort,
    "merge": merge_sort,
    "quick": quick_sort,
}


# ---------------------------------------------------------------------------
# Binary search
# ---------------------------------------------------------------------------

def binary_search(sorted_arr: list, target) -> dict:
    steps = []
    low, high = 0, len(sorted_arr) - 1
    found = False
    found_index = -1

    while low <= high:
        mid = (low + high) // 2
        steps.append({
            "low": low,
            "high": high,
            "mid": mid,
            "mid_value": sorted_arr[mid],
            "action": (
                "found" if sorted_arr[mid] == target
                else "go_right" if sorted_arr[mid] < target
                else "go_left"
            ),
        })
        if sorted_arr[mid] == target:
            found = True
            found_index = mid
            break
        elif sorted_arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    if not found:
        steps.append({
            "low": low,
            "high": high,
            "mid": -1,
            "mid_value": None,
            "action": "not_found",
        })

    return {
        "found": found,
        "index": found_index,
        "steps": steps,
        "total_steps": len(steps),
        "max_possible_steps": math.ceil(math.log2(len(sorted_arr) + 1)) if sorted_arr else 0,
    }


# ---------------------------------------------------------------------------
# Greedy coin change
# ---------------------------------------------------------------------------

def greedy_coin_change(amount: int, coins: list[int]) -> dict:
    coins_sorted = sorted(coins, reverse=True)
    remaining = amount
    result = []
    steps = []

    for coin in coins_sorted:
        if remaining <= 0:
            break
        count = remaining // coin
        if count > 0:
            result.append({"coin": coin, "count": count})
            steps.append({
                "coin": coin,
                "count": count,
                "remaining_before": remaining,
                "remaining_after": remaining - coin * count,
            })
            remaining -= coin * count

    return {
        "success": remaining == 0,
        "remaining": remaining,
        "coins_used": result,
        "total_coins": sum(c["count"] for c in result),
        "steps": steps,
        "note": (
            "Greedy works optimally for standard coin systems (e.g. 1,5,10,25). "
            "For arbitrary denominations it may not find the minimum number of coins."
        ),
    }


# ---------------------------------------------------------------------------
# Dynamic Programming -- Fibonacci
# ---------------------------------------------------------------------------

def fib_naive(n: int) -> dict:
    """Naive recursive Fibonacci -- exponential time."""
    calls = [0]

    def _fib(k):
        calls[0] += 1
        if k <= 1:
            return k
        return _fib(k - 1) + _fib(k - 2)

    start = time.perf_counter()
    value = _fib(n)
    elapsed = time.perf_counter() - start

    return {
        "value": value,
        "calls": calls[0],
        "time_ms": round(elapsed * 1000, 4),
        "complexity": "O(2^n)",
    }


def fib_dp(n: int) -> dict:
    """Bottom-up DP Fibonacci -- linear time."""
    calls = [0]
    table = [0] * (n + 1) if n >= 0 else [0]
    steps = []

    start = time.perf_counter()
    if n >= 0:
        table[0] = 0
        calls[0] += 1
    if n >= 1:
        table[1] = 1
        calls[0] += 1
    steps.append({"index": 0, "value": 0})
    if n >= 1:
        steps.append({"index": 1, "value": 1})
    for i in range(2, n + 1):
        table[i] = table[i - 1] + table[i - 2]
        calls[0] += 1
        steps.append({"index": i, "value": table[i]})
    elapsed = time.perf_counter() - start

    return {
        "value": table[n] if n >= 0 else 0,
        "calls": calls[0],
        "time_ms": round(elapsed * 1000, 4),
        "complexity": "O(n)",
        "table": steps,
    }


# ---------------------------------------------------------------------------
# Dynamic Programming -- 0/1 Knapsack
# ---------------------------------------------------------------------------

def knapsack_dp(capacity: int, weights: list[int], values: list[int],
                names: list[str] | None = None) -> dict:
    n = len(weights)
    if names is None:
        names = [f"item{i+1}" for i in range(n)]

    # Build DP table
    dp = [[0] * (capacity + 1) for _ in range(n + 1)]
    steps = []

    for i in range(1, n + 1):
        for w in range(capacity + 1):
            if weights[i - 1] <= w:
                include = values[i - 1] + dp[i - 1][w - weights[i - 1]]
                exclude = dp[i - 1][w]
                if include > exclude:
                    dp[i][w] = include
                    steps.append({
                        "item": names[i - 1],
                        "capacity": w,
                        "decision": "include",
                        "value": include,
                    })
                else:
                    dp[i][w] = exclude
            else:
                dp[i][w] = dp[i - 1][w]

    # Backtrack to find selected items
    selected = []
    w = capacity
    for i in range(n, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            selected.append({
                "name": names[i - 1],
                "weight": weights[i - 1],
                "value": values[i - 1],
            })
            w -= weights[i - 1]

    selected.reverse()

    return {
        "max_value": dp[n][capacity],
        "selected_items": selected,
        "total_weight": sum(s["weight"] for s in selected),
        "steps_count": len(steps),
        "dp_table_size": f"{n+1} x {capacity+1}",
        "complexity": f"O(n*W) = O({n}*{capacity}) = O({n * capacity})",
    }


# ---------------------------------------------------------------------------
# API endpoints
# ---------------------------------------------------------------------------

@app.get("/")
async def root():
    return RedirectResponse(url="/static/index.html")


@app.post("/api/sort")
async def api_sort(req: SortRequest):
    algo = req.algorithm.lower()
    if algo not in SORT_ALGORITHMS:
        return {"error": f"Unknown algorithm: {algo}. Choose from {list(SORT_ALGORITHMS.keys())}"}

    start = time.perf_counter()
    result = SORT_ALGORITHMS[algo](req.numbers)
    elapsed = time.perf_counter() - start
    result["algorithm"] = algo
    result["time_ms"] = round(elapsed * 1000, 4)
    result["input_size"] = len(req.numbers)
    return result


@app.post("/api/sort/compare")
async def api_sort_compare(req: SortRequest):
    """Run ALL sorting algorithms on the same input and compare."""
    results = {}
    for name, func in SORT_ALGORITHMS.items():
        start = time.perf_counter()
        res = func(req.numbers)
        elapsed = time.perf_counter() - start
        results[name] = {
            "time_ms": round(elapsed * 1000, 4),
            "comparisons": res["comparisons"],
            "swaps": res["swaps"],
        }
    return {"input_size": len(req.numbers), "results": results}


@app.post("/api/search/binary")
async def api_binary_search(req: BinarySearchRequest):
    sorted_arr = sorted(req.numbers)
    start = time.perf_counter()
    result = binary_search(sorted_arr, req.target)
    elapsed = time.perf_counter() - start
    result["sorted_array"] = sorted_arr
    result["time_ms"] = round(elapsed * 1000, 4)
    return result


@app.post("/api/greedy/coins")
async def api_greedy_coins(req: GreedyCoinRequest):
    start = time.perf_counter()
    result = greedy_coin_change(req.amount, req.coins)
    elapsed = time.perf_counter() - start
    result["time_ms"] = round(elapsed * 1000, 4)
    return result


@app.post("/api/dp/fibonacci")
async def api_dp_fibonacci(req: DPFibRequest):
    n = min(req.n, 35)  # cap naive recursion to prevent hang
    dp_result = fib_dp(n)

    if n <= 35:
        naive_result = fib_naive(n)
    else:
        naive_result = {"value": "skipped (too slow)", "calls": "N/A", "time_ms": "N/A", "complexity": "O(2^n)"}

    return {
        "n": n,
        "naive": naive_result,
        "dp": dp_result,
        "speedup": (
            round(naive_result["time_ms"] / dp_result["time_ms"], 1)
            if isinstance(naive_result["time_ms"], (int, float)) and dp_result["time_ms"] > 0
            else "N/A"
        ),
    }


@app.post("/api/dp/knapsack")
async def api_dp_knapsack(req: DPKnapsackRequest):
    start = time.perf_counter()
    result = knapsack_dp(req.capacity, req.weights, req.values, req.names)
    elapsed = time.perf_counter() - start
    result["time_ms"] = round(elapsed * 1000, 4)
    return result


# Mount static files LAST so /api routes take priority
app.mount("/static", StaticFiles(directory="static"), name="static")
