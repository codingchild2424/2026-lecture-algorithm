import pytest, sys, os
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', 'solution'))
import solution


def test_lcs_basic():
    length, dp = solution.lcs("ABCBDAB", "BDCAB")
    assert length == 4  # BCAB


def test_lcs_identical():
    length, _ = solution.lcs("HELLO", "HELLO")
    assert length == 5


def test_lcs_no_common():
    length, _ = solution.lcs("ABC", "XYZ")
    assert length == 0


def test_lcs_empty():
    length, _ = solution.lcs("", "ABC")
    assert length == 0
    length, _ = solution.lcs("ABC", "")
    assert length == 0


def test_backtrack_lcs():
    _, dp = solution.lcs("ALGORITHM", "ALTRUISTIC")
    result = solution.backtrack_lcs(dp, "ALGORITHM", "ALTRUISTIC")
    assert len(result) == 5  # ALRIT or similar


def test_similarity_score():
    score = solution.similarity_score("HELLO", "HELLO")
    assert score == 100.0
    score = solution.similarity_score("ABC", "XYZ")
    assert score == 0.0


def test_similarity_score_partial():
    score = solution.similarity_score("ABCDE", "ABFGH")
    assert 0 < score < 100


def test_generate_diff():
    _, dp = solution.lcs("ABC", "AXC")
    diff = solution.generate_diff(dp, "ABC", "AXC")
    statuses = [s for _, s in diff]
    assert "match" in statuses
    assert "removed" in statuses or "added" in statuses
