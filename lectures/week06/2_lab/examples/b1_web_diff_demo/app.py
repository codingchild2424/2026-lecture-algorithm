"""
텍스트 Diff 뷰어 -- LCS 기반 변경 감지

LCS(Longest Common Subsequence)를 이용하여 두 텍스트의 차이를 감지하고,
추가/삭제/유지된 줄을 색상으로 구분하여 표시한다.

실행: python app.py
접속: http://localhost:5001
"""

from flask import Flask, render_template, request, jsonify

app = Flask(__name__)


def compute_lcs_table(lines_a, lines_b):
    """두 줄 목록 사이의 LCS DP 테이블을 구성한다.

    Args:
        lines_a: 원본 텍스트의 줄 리스트
        lines_b: 수정된 텍스트의 줄 리스트

    Returns:
        2D DP 테이블
    """
    m, n = len(lines_a), len(lines_b)
    dp = [[0] * (n + 1) for _ in range(m + 1)]

    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if lines_a[i - 1] == lines_b[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + 1
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

    return dp


def compute_diff(lines_a, lines_b):
    """LCS 역추적으로 diff를 생성한다.

    Returns:
        diff 항목 리스트: [{"type": "keep"|"add"|"remove", "text": str}, ...]
    """
    dp = compute_lcs_table(lines_a, lines_b)
    diff = []

    i, j = len(lines_a), len(lines_b)

    # 역추적
    while i > 0 or j > 0:
        if i > 0 and j > 0 and lines_a[i - 1] == lines_b[j - 1]:
            diff.append({
                "type": "keep",
                "text": lines_a[i - 1],
                "line_a": i,
                "line_b": j,
            })
            i -= 1
            j -= 1
        elif j > 0 and (i == 0 or dp[i][j - 1] >= dp[i - 1][j]):
            diff.append({
                "type": "add",
                "text": lines_b[j - 1],
                "line_b": j,
            })
            j -= 1
        else:
            diff.append({
                "type": "remove",
                "text": lines_a[i - 1],
                "line_a": i,
            })
            i -= 1

    diff.reverse()
    return diff


def compute_similarity(lines_a, lines_b):
    """두 텍스트의 유사도를 계산한다.

    LCS 길이 / max(len(a), len(b)) * 100

    Returns:
        (LCS 길이, 유사도 백분율)
    """
    dp = compute_lcs_table(lines_a, lines_b)
    lcs_length = dp[len(lines_a)][len(lines_b)]
    max_len = max(len(lines_a), len(lines_b))
    similarity = (lcs_length / max_len * 100) if max_len > 0 else 100.0
    return lcs_length, similarity


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/diff", methods=["POST"])
def diff():
    """두 텍스트의 diff를 계산하여 반환한다."""
    data = request.get_json()
    text_a = data.get("text_a", "")
    text_b = data.get("text_b", "")

    lines_a = text_a.splitlines() if text_a else []
    lines_b = text_b.splitlines() if text_b else []

    diff_result = compute_diff(lines_a, lines_b)
    lcs_length, similarity = compute_similarity(lines_a, lines_b)

    stats = {
        "lines_a": len(lines_a),
        "lines_b": len(lines_b),
        "lcs_length": lcs_length,
        "similarity": round(similarity, 1),
        "added": sum(1 for d in diff_result if d["type"] == "add"),
        "removed": sum(1 for d in diff_result if d["type"] == "remove"),
        "kept": sum(1 for d in diff_result if d["type"] == "keep"),
    }

    return jsonify({
        "diff": diff_result,
        "stats": stats,
    })


SAMPLE_ORIGINAL = """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr

def main():
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", data)
    result = bubble_sort(data)
    print("Sorted:", result)

if __name__ == "__main__":
    main()"""

SAMPLE_MODIFIED = """def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        swapped = False
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr

def main():
    data = [64, 34, 25, 12, 22, 11, 90]
    print("Original:", data)
    result = bubble_sort(data)
    print("Sorted:", result)
    print("Length:", len(result))

if __name__ == "__main__":
    main()"""


@app.route("/api/sample")
def sample():
    """샘플 텍스트를 반환한다."""
    return jsonify({
        "text_a": SAMPLE_ORIGINAL,
        "text_b": SAMPLE_MODIFIED,
    })


if __name__ == "__main__":
    print("=" * 50)
    print(" 텍스트 Diff 뷰어 (LCS 기반)")
    print(" http://localhost:5001")
    print("=" * 50)
    app.run(debug=True, port=5001)
