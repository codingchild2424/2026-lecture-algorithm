import pytest, sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skeleton'))
import solution

def test_heap_sort_basic():
    assert solution.heap_sort([3, 1, 4, 1, 5, 9]) == [1, 1, 3, 4, 5, 9]

def test_heap_sort_empty():
    assert solution.heap_sort([]) == []

def test_counting_sort_basic():
    assert solution.counting_sort([4, 2, 2, 8, 3, 3, 1]) == [1, 2, 2, 3, 3, 4, 8]

def test_counting_sort_empty():
    assert solution.counting_sort([]) == []

def test_benchmark_returns_dict():
    result = solution.benchmark([100])
    assert isinstance(result, dict)
