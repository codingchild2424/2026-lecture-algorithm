"""
쇼핑몰 상품 정렬 비교 데모
Flask 서버: http://localhost:5003
"""

import time
import random
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

NUM_PRODUCTS = 10_000


def generate_products(n):
    """랜덤 가격의 상품 n개를 생성합니다."""
    return [
        {"id": i, "name": f"Product-{i:05d}", "price": random.randint(1000, 999999)}
        for i in range(n)
    ]


def bubble_sort_by_price(products):
    """버블 정렬: O(n^2)"""
    arr = products[:]
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j]["price"] > arr[j + 1]["price"]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def quick_sort_by_price(products):
    """퀵 정렬: O(n log n) 평균"""
    if len(products) <= 1:
        return products[:]
    pivot = products[len(products) // 2]["price"]
    left = [p for p in products if p["price"] < pivot]
    middle = [p for p in products if p["price"] == pivot]
    right = [p for p in products if p["price"] > pivot]
    return quick_sort_by_price(left) + middle + quick_sort_by_price(right)


def builtin_sort_by_price(products):
    """Python 내장 정렬 (Timsort): O(n log n)"""
    return sorted(products, key=lambda p: p["price"])


# 시작 시 상품 데이터 생성
products_data = generate_products(NUM_PRODUCTS)


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/products")
def api_products():
    sort_method = request.args.get("sort", "builtin")
    n = request.args.get("n", NUM_PRODUCTS, type=int)
    n = min(n, NUM_PRODUCTS)

    data = products_data[:n]

    sort_functions = {
        "bubble": bubble_sort_by_price,
        "quick": quick_sort_by_price,
        "builtin": builtin_sort_by_price,
    }

    sort_func = sort_functions.get(sort_method, builtin_sort_by_price)

    start = time.perf_counter()
    sorted_products = sort_func(data)
    elapsed_ms = (time.perf_counter() - start) * 1000

    return jsonify({
        "sort_method": sort_method,
        "sort_time_ms": round(elapsed_ms, 4),
        "count": len(sorted_products),
        "products": sorted_products[:100],  # 상위 100개만 반환
    })


@app.route("/api/regenerate")
def regenerate():
    """상품 데이터를 재생성합니다 (가격 셔플)."""
    global products_data
    n = request.args.get("n", NUM_PRODUCTS, type=int)
    n = min(n, 50_000)
    products_data = generate_products(n)
    return jsonify({"message": f"Regenerated {n} products", "count": n})


if __name__ == "__main__":
    print(f"Generated {NUM_PRODUCTS} products. Starting server on http://localhost:5003")
    app.run(debug=True, port=5003)
