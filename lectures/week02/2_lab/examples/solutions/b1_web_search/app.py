"""
Product Search API — Linear Search vs Binary Search comparison demo
Flask server: http://localhost:5002
"""

import time
import bisect
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# Product data (generated at server startup)
products = []
products_sorted = []  # list sorted by name
MAX_PRODUCTS = 100_000


def generate_products(n):
    """Generates product data."""
    global products, products_sorted
    products = [f"Product_{i:05d}" for i in range(n)]
    products_sorted = sorted(products)


def linear_search(data, target):
    """Linear search: O(n)"""
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


def binary_search(data, target):
    """Binary search: O(log n) — data must be sorted."""
    left, right = 0, len(data) - 1
    while left <= right:
        mid = (left + right) // 2
        if data[mid] == target:
            return mid
        elif data[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/search/linear")
def search_linear():
    q = request.args.get("q", "")
    n = request.args.get("n", len(products), type=int)
    n = min(n, len(products))

    data = products[:n]

    start = time.perf_counter()
    idx = linear_search(data, q)
    elapsed = (time.perf_counter() - start) * 1000  # ms

    return jsonify({
        "method": "linear",
        "query": q,
        "found": idx >= 0,
        "index": idx,
        "dataset_size": n,
        "elapsed_ms": round(elapsed, 4),
    })


@app.route("/api/search/binary")
def search_binary():
    q = request.args.get("q", "")
    n = request.args.get("n", len(products_sorted), type=int)
    n = min(n, len(products_sorted))

    data = products_sorted[:n]

    start = time.perf_counter()
    idx = binary_search(data, q)
    elapsed = (time.perf_counter() - start) * 1000  # ms

    return jsonify({
        "method": "binary",
        "query": q,
        "found": idx >= 0,
        "index": idx,
        "dataset_size": n,
        "elapsed_ms": round(elapsed, 4),
    })


@app.route("/api/resize")
def resize_dataset():
    n = request.args.get("n", MAX_PRODUCTS, type=int)
    n = max(100, min(n, MAX_PRODUCTS))
    generate_products(n)
    return jsonify({"dataset_size": n, "message": f"Dataset resized to {n} products"})


if __name__ == "__main__":
    print(f"Generating {MAX_PRODUCTS} products...")
    generate_products(MAX_PRODUCTS)
    print(f"Done. Starting server on http://localhost:5002")
    app.run(debug=True, port=5002)
