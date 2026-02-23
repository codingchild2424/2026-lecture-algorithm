"""Autocomplete API - linear vs binary search comparison."""
from flask import Flask, request, jsonify
import time
import bisect
import random
import string

app = Flask(__name__)

# Generate dictionary of ~100,000 words
def generate_words(n=100000):
    words = set()
    for length in range(3, 10):
        while len(words) < n:
            word = ''.join(random.choices(string.ascii_lowercase, k=length))
            words.add(word)
            if len(words) >= n:
                break
    return sorted(list(words)[:n])

words = generate_words()
print(f"Dictionary loaded: {len(words)} words")


@app.route("/")
def index():
    return """<!DOCTYPE html>
<html><head><title>Autocomplete Demo</title></head>
<body>
<h1>Autocomplete - Search Algorithm Comparison</h1>
<p>Type a prefix and see response times for linear vs binary search:</p>
<input type="text" id="q" placeholder="Type a prefix..." oninput="search()">
<div id="results"></div>
<script>
let timeout;
async function search() {
    clearTimeout(timeout);
    timeout = setTimeout(async () => {
        const q = document.getElementById('q').value;
        if (q.length < 1) return;
        const [r1, r2] = await Promise.all([
            fetch(`/autocomplete/linear?q=${q}`).then(r => r.json()),
            fetch(`/autocomplete/binary?q=${q}`).then(r => r.json())
        ]);
        document.getElementById('results').innerHTML = `
            <p><b>Linear:</b> ${r1.time_ms.toFixed(3)}ms, ${r1.count} matches</p>
            <p><b>Binary:</b> ${r2.time_ms.toFixed(3)}ms, ${r2.count} matches</p>
            <p>Speedup: ${(r1.time_ms / Math.max(r2.time_ms, 0.001)).toFixed(1)}x</p>
            <p>Matches: ${r2.matches.slice(0, 10).join(', ')}${r2.count > 10 ? '...' : ''}</p>`;
    }, 100);
}
</script>
</body></html>"""


@app.route("/autocomplete/linear")
def autocomplete_linear():
    q = request.args.get("q", "")
    start = time.perf_counter()
    matches = [w for w in words if w.startswith(q)]
    elapsed = (time.perf_counter() - start) * 1000
    return jsonify({"method": "linear", "time_ms": round(elapsed, 4),
                     "count": len(matches), "matches": matches[:20]})


@app.route("/autocomplete/binary")
def autocomplete_binary():
    q = request.args.get("q", "")
    start = time.perf_counter()
    lo = bisect.bisect_left(words, q)
    hi = bisect.bisect_left(words, q[:-1] + chr(ord(q[-1]) + 1)) if q else len(words)
    matches = words[lo:hi]
    elapsed = (time.perf_counter() - start) * 1000
    return jsonify({"method": "binary", "time_ms": round(elapsed, 4),
                     "count": len(matches), "matches": matches[:20]})


if __name__ == "__main__":
    app.run(debug=True, port=5000)
