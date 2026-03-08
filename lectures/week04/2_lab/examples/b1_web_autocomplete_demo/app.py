"""
자동완성 API — 선형 탐색 vs 이진 탐색 비교 데모
Flask 서버: http://localhost:5004
"""

import time
import bisect
import random
import string
from flask import Flask, request, jsonify, render_template

app = Flask(__name__)


def generate_words(n=100_000):
    """
    n개의 랜덤 영단어를 생성합니다.
    길이 3~8의 소문자 알파벳 조합으로 생성하며, 중복을 제거합니다.
    """
    words = set()
    while len(words) < n:
        length = random.randint(3, 8)
        word = "".join(random.choices(string.ascii_lowercase, k=length))
        words.add(word)
    return sorted(words)


# 서버 시작 시 단어 사전 생성
print("Generating 100,000 words...")
word_list = generate_words(100_000)
print(f"Done. {len(word_list)} unique words generated.")


def linear_search_prefix(words, prefix):
    """
    선형 탐색: 모든 단어를 순회하며 prefix로 시작하는 단어를 찾습니다.
    시간복잡도: O(n * m) — n: 단어 수, m: prefix 길이
    """
    return [w for w in words if w.startswith(prefix)]


def binary_search_prefix(words, prefix):
    """
    이진 탐색: 정렬된 사전에서 bisect를 사용하여 prefix 범위를 찾습니다.
    시간복잡도: O(log n + k) — k: 매칭되는 단어 수
    """
    if not prefix:
        return words[:]

    # prefix 이상인 첫 위치
    lo = bisect.bisect_left(words, prefix)

    # prefix의 다음 접두사 (예: "abc" -> "abd")
    # prefix의 마지막 문자를 1 증가시킨 문자열
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
