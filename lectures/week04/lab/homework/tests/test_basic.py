import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'skeleton'))
import solution

def test_karatsuba_small():
    assert solution.karatsuba(12, 34) == 408

def test_karatsuba_large():
    assert solution.karatsuba(1234, 5678) == 1234 * 5678

def test_karatsuba_zero():
    assert solution.karatsuba(0, 12345) == 0

def test_karatsuba_single_digit():
    assert solution.karatsuba(7, 8) == 56
