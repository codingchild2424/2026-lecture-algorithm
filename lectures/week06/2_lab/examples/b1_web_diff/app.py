"""Text Diff Viewer - LCS-based diff visualization."""
from flask import Flask, request, jsonify

app = Flask(__name__)


def compute_lcs_table(s1, s2):
    m, n = len(s1), len(s2)
    dp = [[0] * (n + 1) for _ in range(m + 1)]
    for i in range(1, m + 1):
        for j in range(1, n + 1):
            if s1[i-1] == s2[j-1]:
                dp[i][j] = dp[i-1][j-1] + 1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    return dp


def compute_diff(lines1, lines2):
    dp = compute_lcs_table(lines1, lines2)
    diff = []
    i, j = len(lines1), len(lines2)
    while i > 0 or j > 0:
        if i > 0 and j > 0 and lines1[i-1] == lines2[j-1]:
            diff.append({"type": "same", "line": lines1[i-1]})
            i -= 1; j -= 1
        elif j > 0 and (i == 0 or dp[i][j-1] >= dp[i-1][j]):
            diff.append({"type": "add", "line": lines2[j-1]})
            j -= 1
        else:
            diff.append({"type": "remove", "line": lines1[i-1]})
            i -= 1
    return list(reversed(diff))


@app.route("/")
def index():
    return """<!DOCTYPE html>
<html><head><title>Text Diff Viewer</title>
<style>
body { font-family: monospace; max-width: 800px; margin: 40px auto; }
textarea { width: 100%; height: 120px; }
.same { color: #333; }
.add { background: #d4edda; color: #155724; }
.remove { background: #f8d7da; color: #721c24; }
.diff-line { padding: 2px 8px; white-space: pre; }
</style></head>
<body>
<h1>Text Diff Viewer (LCS-based)</h1>
<table width="100%"><tr>
<td><b>Original</b><br><textarea id="t1">Hello World
This is a test
Foo bar baz
Keep this line</textarea></td>
<td><b>Modified</b><br><textarea id="t2">Hello World
This is an example
Foo bar baz
Added new line
Keep this line</textarea></td>
</tr></table>
<button onclick="diff()">Compute Diff</button>
<div id="result"></div>
<script>
async function diff() {
    const t1 = document.getElementById('t1').value;
    const t2 = document.getElementById('t2').value;
    const res = await fetch('/api/diff', {
        method: 'POST', headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({text1: t1, text2: t2})
    });
    const data = await res.json();
    document.getElementById('result').innerHTML =
        `<p>LCS length: ${data.lcs_length}, Diff computed in ${data.time_ms}ms</p>` +
        data.diff.map(d => {
            const prefix = d.type === 'add' ? '+' : d.type === 'remove' ? '-' : ' ';
            return `<div class="diff-line ${d.type}">${prefix} ${d.line}</div>`;
        }).join('');
}
</script>
</body></html>"""


@app.route("/api/diff", methods=["POST"])
def api_diff():
    import time
    data = request.json
    lines1 = data["text1"].splitlines()
    lines2 = data["text2"].splitlines()
    start = time.perf_counter()
    diff = compute_diff(lines1, lines2)
    lcs_len = sum(1 for d in diff if d["type"] == "same")
    elapsed = (time.perf_counter() - start) * 1000
    return jsonify({"diff": diff, "lcs_length": lcs_len, "time_ms": round(elapsed, 3)})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
