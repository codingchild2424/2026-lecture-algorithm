"""Simple Flask app comparing linear vs binary search API endpoints."""
from flask import Flask, request, jsonify
import time
import bisect

app = Flask(__name__)

# Generate product data
products = [{"id": i, "name": f"Product-{i:06d}", "price": (i * 37) % 10000}
            for i in range(100000)]
products_sorted = sorted(products, key=lambda p: p["name"])
product_names_sorted = [p["name"] for p in products_sorted]


@app.route("/")
def index():
    return """
    <h1>Product Search API - Complexity Demo</h1>
    <p>Compare linear search vs binary search performance:</p>
    <ul>
        <li><code>GET /search/linear?q=Product-050000</code> — O(n) linear scan</li>
        <li><code>GET /search/binary?q=Product-050000</code> — O(log n) binary search</li>
        <li><code>GET /benchmark?q=Product-050000</code> — Run both and compare times</li>
    </ul>
    <p>Total products: {:,}</p>
    """.format(len(products))


@app.route("/search/linear")
def search_linear():
    q = request.args.get("q", "")
    start = time.perf_counter()
    result = None
    for p in products:
        if p["name"] == q:
            result = p
            break
    elapsed = time.perf_counter() - start
    return jsonify({"method": "linear", "time_ms": round(elapsed * 1000, 4),
                     "found": result is not None, "result": result})


@app.route("/search/binary")
def search_binary():
    q = request.args.get("q", "")
    start = time.perf_counter()
    idx = bisect.bisect_left(product_names_sorted, q)
    result = None
    if idx < len(product_names_sorted) and product_names_sorted[idx] == q:
        result = products_sorted[idx]
    elapsed = time.perf_counter() - start
    return jsonify({"method": "binary", "time_ms": round(elapsed * 1000, 4),
                     "found": result is not None, "result": result})


@app.route("/benchmark")
def benchmark():
    q = request.args.get("q", "Product-050000")
    # Linear
    start = time.perf_counter()
    for p in products:
        if p["name"] == q:
            break
    t_linear = time.perf_counter() - start
    # Binary
    start = time.perf_counter()
    idx = bisect.bisect_left(product_names_sorted, q)
    t_binary = time.perf_counter() - start

    return jsonify({
        "query": q,
        "linear_ms": round(t_linear * 1000, 4),
        "binary_ms": round(t_binary * 1000, 4),
        "speedup": round(t_linear / t_binary, 1) if t_binary > 0 else "inf",
        "total_products": len(products)
    })


if __name__ == "__main__":
    print(f"Loaded {len(products):,} products")
    app.run(debug=True, port=5000)
