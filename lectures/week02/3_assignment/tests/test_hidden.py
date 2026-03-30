import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))
import solution


def test_search_by_id_found():
    products = [{"id": i, "name": f"Item{i}", "category": "A", "price": 10.0} for i in range(100)]
    result = solution.search_by_id(products, 42)
    assert result is not None
    assert result["id"] == 42


def test_search_by_id_not_found():
    products = [{"id": i, "name": f"Item{i}", "category": "A", "price": 10.0} for i in range(10)]
    result = solution.search_by_id(products, 999)
    assert result is None


def test_search_by_name():
    products = [
        {"id": 0, "name": "Laptop Pro", "category": "Electronics", "price": 999},
        {"id": 1, "name": "Laptop Air", "category": "Electronics", "price": 799},
        {"id": 2, "name": "Mouse Pad", "category": "Accessories", "price": 15},
    ]
    results = solution.search_by_name(products, "laptop")
    assert len(results) == 2


def test_find_duplicates():
    products = [
        {"id": 0, "name": "Widget", "category": "A", "price": 10},
        {"id": 1, "name": "Gadget", "category": "B", "price": 20},
        {"id": 2, "name": "Widget", "category": "C", "price": 30},
    ]
    dupes = solution.find_duplicates(products)
    assert len(dupes) == 1
    assert dupes[0][0]["name"] == "Widget"


def test_find_duplicates_none():
    products = [
        {"id": 0, "name": "A", "category": "X", "price": 1},
        {"id": 1, "name": "B", "category": "X", "price": 2},
    ]
    dupes = solution.find_duplicates(products)
    assert len(dupes) == 0
