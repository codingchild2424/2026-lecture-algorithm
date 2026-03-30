"""Homework 2: Reference Solution — Mini Shopping Mall Search"""
import time
import random
import string


def generate_products(n=1000):
    """Generate n products with id, name, category, price."""
    categories = ["Electronics", "Clothing", "Books", "Food", "Sports"]
    products = []
    for i in range(n):
        name = "Product_" + "".join(random.choices(string.ascii_lowercase, k=5))
        products.append({
            "id": i,
            "name": name,
            "category": random.choice(categories),
            "price": round(random.uniform(1, 500), 2),
        })
    return products


def search_by_id(products, product_id):
    """O(1) lookup using a dict keyed by product id."""
    lookup = {p["id"]: p for p in products}
    return lookup.get(product_id)


def search_by_name(products, keyword):
    """O(n) linear scan for name substring match."""
    results = []
    for p in products:
        if keyword.lower() in p["name"].lower():
            results.append(p)
    return results


def find_duplicates(products):
    """O(n^2) nested loop to find products with the same name."""
    duplicates = []
    n = len(products)
    for i in range(n):
        for j in range(i + 1, n):
            if products[i]["name"] == products[j]["name"]:
                duplicates.append((products[i], products[j]))
    return duplicates


def benchmark(sizes=None):
    if sizes is None:
        sizes = [100, 1000, 5000]
    results = {"search_by_id": {}, "search_by_name": {}, "find_duplicates": {}}
    for n in sizes:
        products = generate_products(n)
        target_id = n // 2

        start = time.perf_counter()
        search_by_id(products, target_id)
        results["search_by_id"][n] = time.perf_counter() - start

        start = time.perf_counter()
        search_by_name(products, "prod")
        results["search_by_name"][n] = time.perf_counter() - start

        start = time.perf_counter()
        find_duplicates(products)
        results["find_duplicates"][n] = time.perf_counter() - start
    return results
