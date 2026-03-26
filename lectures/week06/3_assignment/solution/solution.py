"""Homework 5: Reference Solution — Plagiarism Checker (LCS)"""


def lcs(text_a, text_b):
    """
    Longest Common Subsequence using dynamic programming.
    Returns: (lcs_length, dp_table)
    """
    m, n = len(text_a), len(text_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if text_a[i - 1] == text_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
    return dp[m][n], dp


def backtrack_lcs(dp, text_a, text_b):
    """Backtrack through the DP table to recover the actual LCS string."""
    i, j = len(text_a), len(text_b)
    result = []
    while i > 0 and j > 0:
        if text_a[i - 1] == text_b[j - 1]:
            result.append(text_a[i - 1])
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    return "".join(reversed(result))


def similarity_score(text_a, text_b):
    """Calculate similarity as LCS length / max(len(A), len(B)) * 100."""
    if not text_a and not text_b:
        return 100.0
    if not text_a or not text_b:
        return 0.0
    length, _ = lcs(text_a, text_b)
    return length / max(len(text_a), len(text_b)) * 100


def generate_diff(dp, text_a, text_b):
    """
    Generate a diff view from the DP table.
    Returns list of (char, status) where status is 'match', 'removed', or 'added'.
    """
    i, j = len(text_a), len(text_b)
    diff = []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and text_a[i - 1] == text_b[j - 1]:
            diff.append((text_a[i - 1], "match"))
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j - 1] >= dp[i - 1][j]):
            diff.append((text_b[j - 1], "added"))
            j -= 1
        else:
            diff.append((text_a[i - 1], "removed"))
            i -= 1
    return list(reversed(diff))
