"""
상품 검색 API — 선형 탐색 vs 이진 탐색 비교 데모
Flask 서버: http://localhost:5002
"""

import time
import bisect
from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# 상품 데이터 (서버 시작 시 생성)
products = []
products_sorted = []  # 이름순 정렬된 리스트
MAX_PRODUCTS = 100_000


def generate_products(n):
    """상품 데이터를 생성합니다."""
    global products, products_sorted
    products = [f"Product_{i:05d}" for i in range(n)]
    products_sorted = sorted(products)


def linear_search(data, target):
    """선형 탐색: O(n)"""
    for i, item in enumerate(data):
        if item == target:
            return i
    return -1


def binary_search(data, target):
    """이진 탐색: O(log n) — data는 정렬되어 있어야 합니다."""
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
