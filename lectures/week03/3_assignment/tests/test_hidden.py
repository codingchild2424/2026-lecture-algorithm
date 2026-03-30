import pytest, sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))
import solution


def test_selection_sort_random():
    for _ in range(10):
        data = [random.randint(-1000, 1000) for _ in range(100)]
        result, comps, swaps = solution.selection_sort(data)
        assert result == sorted(data)
        assert comps > 0


def test_insertion_sort_random():
    for _ in range(10):
        data = [random.randint(-1000, 1000) for _ in range(100)]
        result, comps, swaps = solution.insertion_sort(data)
        assert result == sorted(data)


def test_merge_sort_random():
    for _ in range(10):
        data = [random.randint(-1000, 1000) for _ in range(100)]
        result, comps, swaps = solution.merge_sort(data)
        assert result == sorted(data)


def test_sorts_with_key():
    songs = [{"title": "C"}, {"title": "A"}, {"title": "B"}]
    key = lambda x: x["title"]
    r1, _, _ = solution.selection_sort(songs, key=key)
    r2, _, _ = solution.insertion_sort(songs, key=key)
    r3, _, _ = solution.merge_sort(songs, key=key)
    expected = [{"title": "A"}, {"title": "B"}, {"title": "C"}]
    assert r1 == expected
    assert r2 == expected
    assert r3 == expected


def test_does_not_modify_input():
    data = [5, 3, 1, 4, 2]
    original = data[:]
    solution.selection_sort(data)
    assert data == original
    solution.insertion_sort(data)
    assert data == original
    solution.merge_sort(data)
    assert data == original
