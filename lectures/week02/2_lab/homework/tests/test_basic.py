"""Basic tests for Homework 1."""
import pytest
import sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skeleton'))
import solution


def test_analyze_returns_dict():
    result = solution.analyze()
    assert isinstance(result, dict)
    assert len(result) == 5


def test_analyze_keys():
    result = solution.analyze()
    expected_keys = {"func_a", "func_b", "func_c", "func_d", "func_e"}
    assert set(result.keys()) == expected_keys


def test_analyze_values_not_empty():
    result = solution.analyze()
    for key, value in result.items():
        assert value != "", f"{key} complexity should not be empty"


def test_func_a_correct():
    assert solution.func_a(10) == 45
    assert solution.func_a(100) == 4950


def test_func_c_correct():
    assert solution.func_c(1) == 1
    assert solution.func_c(8) == 4


def test_benchmark_returns_dict():
    result = solution.benchmark([100])
    assert isinstance(result, dict)
    assert len(result) == 5
