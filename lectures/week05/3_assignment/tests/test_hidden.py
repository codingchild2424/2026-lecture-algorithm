import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))
import solution


def test_basic_selection():
    activities = [
        {"name": "A", "start": 0, "end": 6},
        {"name": "B", "start": 1, "end": 4},
        {"name": "C", "start": 3, "end": 5},
        {"name": "D", "start": 5, "end": 7},
        {"name": "E", "start": 3, "end": 9},
        {"name": "F", "start": 5, "end": 9},
        {"name": "G", "start": 6, "end": 10},
        {"name": "H", "start": 8, "end": 11},
    ]
    selected, trace = solution.activity_selection(activities)
    assert len(selected) == 3  # B(1-4), D(5-7), H(8-11)


def test_no_overlap():
    activities = [
        {"name": "A", "start": 0, "end": 2},
        {"name": "B", "start": 3, "end": 5},
        {"name": "C", "start": 6, "end": 8},
    ]
    selected, trace = solution.activity_selection(activities)
    assert len(selected) == 3


def test_all_overlap():
    activities = [
        {"name": "A", "start": 0, "end": 10},
        {"name": "B", "start": 1, "end": 11},
        {"name": "C", "start": 2, "end": 12},
    ]
    selected, trace = solution.activity_selection(activities)
    assert len(selected) == 1


def test_selected_are_non_overlapping():
    activities = solution.generate_activities(30)
    selected, _ = solution.activity_selection(activities)
    for i in range(len(selected) - 1):
        assert selected[i]["end"] <= selected[i + 1]["start"]


def test_trace_has_all_activities():
    activities = [
        {"name": "A", "start": 0, "end": 3},
        {"name": "B", "start": 2, "end": 5},
    ]
    selected, trace = solution.activity_selection(activities)
    assert len(trace) == 2
    actions = [t["action"] for t in trace]
    assert "select" in actions
