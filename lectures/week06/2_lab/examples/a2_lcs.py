# === A-2: Longest Common Subsequence (LCS) ===
# LCS computation using DP, table visualization, and backtracking
#
# Key concepts:
# - Compute the LCS of two strings using DP
# - Recurrence:
#     When X[i] == Y[j]: dp[i][j] = dp[i-1][j-1] + 1 (diagonal +1)
#     When X[i] != Y[j]: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
# - Backtracking: trace back from dp[m][n] to dp[0][0] to reconstruct the LCS
# - Time complexity: O(m * n) (m, n = lengths of the two strings)
# - Space complexity: O(m * n) (DP table)
# - Applications: git diff, DNA sequence comparison, edit distance
"""
LCS (Longest Common Subsequence) -- DP table visualization + backtracking

Find the longest common subsequence of two strings X and Y.
Visually print the DP table and reconstruct the actual LCS via backtracking.

Recurrence:
  When X[i] == Y[j]: dp[i][j] = dp[i-1][j-1] + 1
  When X[i] != Y[j]: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""


def build_lcs_table(x, y):
    """Build the LCS DP table.

    Args:
        x: first string
        y: second string

    Returns:
        2D DP table (size: (len(x)+1) x (len(y)+1))
    """
    m, n = len(x), len(y)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if x[i - 1] == y[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def backtrack_lcs(dp, x, y):
    """Backtrack through the DP table to reconstruct the actual LCS.

    Args:
        dp: LCS DP table
        x: first string
        y: second string

    Returns:
        (LCS string, backtracking path list)
        Path: [(i, j, action), ...] action = 'match'|'up'|'left'
    """
    lcs = []
    path = []
    i, j = len(x), len(y)

    while i > 0 and j > 0:
        if x[i - 1] == y[j - 1]:
            lcs.append(x[i - 1])
            path.append((i, j, "match"))
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            path.append((i, j, "up"))
            i -= 1
        else:
            path.append((i, j, "left"))
            j -= 1

    lcs.reverse()
    path.reverse()

    return "".join(lcs), path


def print_dp_table(dp, x, y, path=None):
    """Visually print the DP table.

    Args:
        dp: LCS DP table
        x: first string
        y: second string
        path: backtracking path (for highlighting)
    """
    m, n = len(x), len(y)

    # Convert backtracking path to sets
    match_cells = set()
    path_cells = set()
    if path:
        for i, j, action in path:
            path_cells.add((i, j))
            if action == "match":
                match_cells.add((i, j))

    cell_width = 4

    # Y character header
    print(f"    {'':>{cell_width}}    ", end="")
    for j in range(n + 1):
        if j == 0:
            print(f"{'':>{cell_width}}", end=" ")
        else:
            print(f"{y[j-1]:>{cell_width}}", end=" ")
    print()

    # Index header
    print(f"    {'':>{cell_width}}    ", end="")
    for j in range(n + 1):
        print(f"{j:>{cell_width}}", end=" ")
    print()

    print(f"    {'':>{cell_width}}   {'---' * (n + 1) * 2}")

    # Table body
    for i in range(m + 1):
        if i == 0:
            row_label = " "
        else:
            row_label = x[i - 1]

        print(f"    {row_label:>{cell_width}} {i} |", end="")

        for j in range(n + 1):
            val = dp[i][j]
            if (i, j) in match_cells:
                print(f"[{val:>{cell_width - 2}}]", end=" ")
            elif (i, j) in path_cells:
                print(f"({val:>{cell_width - 2}})", end=" ")
            else:
                print(f"{val:>{cell_width}}", end=" ")
        print()

    print()


def lcs_analysis(x, y, label=""):
    """Perform LCS analysis and print the results."""
    if label:
        print(f"\n{'='*60}")
        print(f"[{label}]")
        print(f"{'='*60}")

    print(f"\n  X = \"{x}\"")
    print(f"  Y = \"{y}\"")

    # Build DP table
    dp = build_lcs_table(x, y)

    # Backtrack
    lcs_str, path = backtrack_lcs(dp, x, y)

    # Print DP table
    print(f"\n  --- DP Table ---")
    print(f"  [n] = match (included in LCS), (n) = backtracking path")
    print_dp_table(dp, x, y, path)

    # Print results
    lcs_length = dp[len(x)][len(y)]
    print(f"  LCS length: {lcs_length}")
    print(f"  LCS: \"{lcs_str}\"")

    # Backtracking path visualization
    print(f"\n  --- Backtracking Path ---")
    for i, j, action in path:
        if action == "match":
            print(f"    ({i},{j}): X[{i}]=Y[{j}]='{x[i-1]}' -> diagonal (match!)")
        elif action == "up":
            print(f"    ({i},{j}): X[{i}]='{x[i-1]}' != Y[{j}]='{y[j-1]}' -> move up")
        else:
            print(f"    ({i},{j}): X[{i}]='{x[i-1]}' != Y[{j}]='{y[j-1]}' -> move left")

    # LCS position display
    print(f"\n  --- LCS Position Display ---")
    x_display = list(x)
    y_display = list(y)
    x_marks = [" "] * len(x)
    y_marks = [" "] * len(y)

    for i, j, action in path:
        if action == "match":
            x_marks[i - 1] = "^"
            y_marks[j - 1] = "^"

    print(f"  X: {' '.join(x_display)}")
    print(f"     {' '.join(x_marks)}")
    print(f"  Y: {' '.join(y_display)}")
    print(f"     {' '.join(y_marks)}")

    return lcs_str, lcs_length


if __name__ == "__main__":
    print("=" * 60)
    print(" LCS (Longest Common Subsequence) -- DP Table Visualization")
    print("=" * 60)

    # Example 1: Textbook example
    lcs_analysis("ABCBDAB", "BDCAB", "Example 1: ABCBDAB vs BDCAB")

    # Example 2: Simple example
    lcs_analysis("AGGTAB", "GXTXAYB", "Example 2: AGGTAB vs GXTXAYB")

    # Example 3: Identical strings
    lcs_analysis("ABC", "ABC", "Example 3: Identical strings ABC vs ABC")

    # Example 4: No common subsequence
    lcs_analysis("ABC", "XYZ", "Example 4: No common subsequence ABC vs XYZ")

    # Summary
    print("\n" + "=" * 60)
    print(" Summary")
    print("=" * 60)
    print("""
  LCS Algorithm:
  - Time complexity: O(m * n) (m, n = lengths of the two strings)
  - Space complexity: O(m * n) (DP table)

  Recurrence:
  - X[i] == Y[j]: dp[i][j] = dp[i-1][j-1] + 1
  - X[i] != Y[j]: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  Backtracking:
  - Start from dp[m][n] and move to dp[0][0]
  - If characters match, move diagonally (included in LCS)
  - If different, move toward the larger dp value

  Applications:
  - Text diff (git diff)
  - DNA sequence comparison
  - Edit Distance
""")
