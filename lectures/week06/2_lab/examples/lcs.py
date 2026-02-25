"""
LCS (Longest Common Subsequence) -- DP 테이블 시각화 + 역추적

두 문자열 X, Y의 최장 공통 부분 수열을 구한다.
DP 테이블을 시각적으로 출력하고, 역추적으로 실제 LCS를 복원한다.

재귀식:
  X[i] == Y[j]일 때: dp[i][j] = dp[i-1][j-1] + 1
  X[i] != Y[j]일 때: dp[i][j] = max(dp[i-1][j], dp[i][j-1])
"""


def build_lcs_table(x, y):
    """LCS DP 테이블을 구성한다.

    Args:
        x: 첫 번째 문자열
        y: 두 번째 문자열

    Returns:
        2D DP 테이블 (크기: (len(x)+1) x (len(y)+1))
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
    """DP 테이블에서 역추적하여 실제 LCS를 복원한다.

    Args:
        dp: LCS DP 테이블
        x: 첫 번째 문자열
        y: 두 번째 문자열

    Returns:
        (LCS 문자열, 역추적 경로 리스트)
        경로: [(i, j, action), ...] action = 'match'|'up'|'left'
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
    """DP 테이블을 시각적으로 출력한다.

    Args:
        dp: LCS DP 테이블
        x: 첫 번째 문자열
        y: 두 번째 문자열
        path: 역추적 경로 (하이라이트용)
    """
    m, n = len(x), len(y)

    # 역추적 경로를 set으로 변환
    match_cells = set()
    path_cells = set()
    if path:
        for i, j, action in path:
            path_cells.add((i, j))
            if action == "match":
                match_cells.add((i, j))

    cell_width = 4

    # Y 문자 헤더
    print(f"    {'':>{cell_width}}    ", end="")
    for j in range(n + 1):
        if j == 0:
            print(f"{'':>{cell_width}}", end=" ")
        else:
            print(f"{y[j-1]:>{cell_width}}", end=" ")
    print()

    # 인덱스 헤더
    print(f"    {'':>{cell_width}}    ", end="")
    for j in range(n + 1):
        print(f"{j:>{cell_width}}", end=" ")
    print()

    print(f"    {'':>{cell_width}}   {'---' * (n + 1) * 2}")

    # 테이블 본체
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
    """LCS 분석을 수행하고 결과를 출력한다."""
    if label:
        print(f"\n{'='*60}")
        print(f"[{label}]")
        print(f"{'='*60}")

    print(f"\n  X = \"{x}\"")
    print(f"  Y = \"{y}\"")

    # DP 테이블 구성
    dp = build_lcs_table(x, y)

    # 역추적
    lcs_str, path = backtrack_lcs(dp, x, y)

    # DP 테이블 출력
    print(f"\n  --- DP 테이블 ---")
    print(f"  [n] = 매칭 (LCS에 포함), (n) = 역추적 경로")
    print_dp_table(dp, x, y, path)

    # 결과 출력
    lcs_length = dp[len(x)][len(y)]
    print(f"  LCS 길이: {lcs_length}")
    print(f"  LCS: \"{lcs_str}\"")

    # 역추적 경로 시각화
    print(f"\n  --- 역추적 경로 ---")
    for i, j, action in path:
        if action == "match":
            print(f"    ({i},{j}): X[{i}]=Y[{j}]='{x[i-1]}' -> 대각선 (매치!)")
        elif action == "up":
            print(f"    ({i},{j}): X[{i}]='{x[i-1]}' != Y[{j}]='{y[j-1]}' -> 위로 이동")
        else:
            print(f"    ({i},{j}): X[{i}]='{x[i-1]}' != Y[{j}]='{y[j-1]}' -> 왼쪽 이동")

    # LCS 위치 표시
    print(f"\n  --- LCS 위치 표시 ---")
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
    print(" LCS (Longest Common Subsequence) -- DP 테이블 시각화")
    print("=" * 60)

    # 예제 1: 교과서 예제
    lcs_analysis("ABCBDAB", "BDCAB", "예제 1: ABCBDAB vs BDCAB")

    # 예제 2: 간단한 예제
    lcs_analysis("AGGTAB", "GXTXAYB", "예제 2: AGGTAB vs GXTXAYB")

    # 예제 3: 완전히 같은 문자열
    lcs_analysis("ABC", "ABC", "예제 3: 동일 문자열 ABC vs ABC")

    # 예제 4: 공통 부분 없음
    lcs_analysis("ABC", "XYZ", "예제 4: 공통 없음 ABC vs XYZ")

    # 요약
    print("\n" + "=" * 60)
    print(" 요약")
    print("=" * 60)
    print("""
  LCS 알고리즘:
  - 시간 복잡도: O(m * n) (m, n = 두 문자열의 길이)
  - 공간 복잡도: O(m * n) (DP 테이블)

  재귀식:
  - X[i] == Y[j]: dp[i][j] = dp[i-1][j-1] + 1
  - X[i] != Y[j]: dp[i][j] = max(dp[i-1][j], dp[i][j-1])

  역추적:
  - dp[m][n]에서 시작하여 dp[0][0]까지 이동
  - 문자가 같으면 대각선으로 이동 (LCS에 포함)
  - 다르면 dp 값이 큰 쪽으로 이동

  응용:
  - 텍스트 diff (git diff)
  - DNA 서열 비교
  - 편집 거리 (Edit Distance)
""")
