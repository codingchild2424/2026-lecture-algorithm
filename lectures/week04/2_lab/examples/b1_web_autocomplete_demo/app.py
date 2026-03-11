"""
Autocomplete API -- Linear Search vs Binary Search Comparison Demo
Flask server: http://localhost:5004
"""

import time
import bisect
import random
import string
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def generate_words(n=100_000):
    """
    Generates n random English words.
    Creates combinations of lowercase letters with length 3-8, removing duplicates.
    """
    words = set()
    while len(words) < n:
        length = random.randint(3, 8)
        word = "".join(random.choices(string.ascii_lowercase, k=length))
        words.add(word)
    return sorted(words)


# Generate word dictionary at server startup
print("Generating 100,000 words...")
word_list = generate_words(100_000)
print(f"Done. {len(word_list)} unique words generated.")


def linear_search_prefix(words, prefix):
    """
    Linear search: iterates through all words to find those starting with the prefix.
    Time complexity: O(n * m) -- n: number of words, m: prefix length
    """
    return [w for w in words if w.startswith(prefix)]


def binary_search_prefix(words, prefix):
    """
    Binary search: uses bisect on a sorted dictionary to find the prefix range.
    Time complexity: O(log n + k) -- k: number of matching words
    """
    if not prefix:
        return words[:]

    # First position >= prefix
    lo = bisect.bisect_left(words, prefix)

    # Next prefix after the given one (e.g., "abc" -> "abd")
    # Increment the last character of the prefix by 1
    next_prefix = prefix[:-1] + chr(ord(prefix[-1]) + 1)
    hi = bisect.bisect_left(words, next_prefix)

    return words[lo:hi]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/autocomplete/linear")
def autocomplete_linear():
    prefix = request.args.get("prefix", "").lower().strip()
    if not prefix:
        return jsonify({"method": "linear", "prefix": "", "matches": [], "count": 0, "elapsed_ms": 0})

    start = time.perf_counter()
    matches = linear_search_prefix(word_list, prefix)
    elapsed_ms = (time.perf_counter() - start) * 1000

    return jsonify({
        "method": "linear",
        "prefix": prefix,
        "matches": matches[:20],
        "count": len(matches),
        "elapsed_ms": round(elapsed_ms, 4),
        "total_words": len(word_list),
    })


@app.route("/api/autocomplete/binary")
def autocomplete_binary():
    prefix = request.args.get("prefix", "").lower().strip()
    if not prefix:
        return jsonify({"method": "binary", "prefix": "", "matches": [], "count": 0, "elapsed_ms": 0})

    start = time.perf_counter()
    matches = binary_search_prefix(word_list, prefix)
    elapsed_ms = (time.perf_counter() - start) * 1000

    return jsonify({
        "method": "binary",
        "prefix": prefix,
        "matches": matches[:20],
        "count": len(matches),
        "elapsed_ms": round(elapsed_ms, 4),
        "total_words": len(word_list),
    })


if __name__ == "__main__":
    print("Starting server on http://localhost:5004")
    app.run(debug=True, port=5004)
