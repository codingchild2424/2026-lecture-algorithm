"""
회의실 예약 스케줄러 -- Activity Selection 문제 적용

그리디 전략: 종료 시간이 빠른 회의부터 선택하면 최대 개수의 회의를 배치할 수 있다.
브루트포스: 모든 부분집합을 검사하여 최적해를 구한다 (소규모 N에서만 사용).

실행: python app.py
접속: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
from itertools import combinations
import random

app = Flask(__name__)


def greedy_schedule(meetings):
    """그리디로 최대 회의 수를 선택한다.

    Activity Selection: 종료 시간 기준 오름차순 정렬 후,
    이전에 선택한 회의와 겹치지 않는 회의를 순서대로 선택한다.

    시간 복잡도: O(n log n) -- 정렬이 지배적

    Args:
        meetings: [{"id": int, "name": str, "start": float, "end": float}, ...]

    Returns:
        선택된 회의의 id 리스트
    """
    # 종료 시간 기준 정렬
    sorted_meetings = sorted(meetings, key=lambda m: m["end"])

    selected = []
    last_end = -1

    for meeting in sorted_meetings:
        if meeting["start"] >= last_end:
            selected.append(meeting["id"])
            last_end = meeting["end"]

    return selected


def bruteforce_schedule(meetings):
    """브루트포스로 최대 회의 수를 선택한다.

    모든 부분집합을 검사하여 겹치지 않는 회의의 최대 개수를 구한다.

    시간 복잡도: O(2^n * n) -- 모든 부분집합 검사

    Args:
        meetings: [{"id": int, "name": str, "start": float, "end": float}, ...]

    Returns:
        선택된 회의의 id 리스트
    """
    n = len(meetings)

    # N이 너무 크면 시간 초과 방지
    if n > 20:
        return None

    def is_compatible(subset):
        """부분집합의 회의들이 모두 겹치지 않는지 확인."""
        sorted_sub = sorted(subset, key=lambda m: m["start"])
        for i in range(1, len(sorted_sub)):
            if sorted_sub[i]["start"] < sorted_sub[i - 1]["end"]:
                return False
        return True

    best_selection = []

    for size in range(n, 0, -1):
        for combo in combinations(meetings, size):
            if is_compatible(combo):
                best_selection = [m["id"] for m in combo]
                return best_selection

    return best_selection


def generate_sample_meetings(count=10):
    """랜덤 회의 데이터를 생성한다."""
    random.seed(42)
    names = [
        "팀 회의", "기획 미팅", "코드 리뷰", "디자인 논의", "스프린트 계획",
        "고객 미팅", "1:1 미팅", "기술 세미나", "프로젝트 보고", "브레인스토밍",
        "전략 회의", "예산 논의", "성과 리뷰", "워크샵", "교육 세션",
    ]
    meetings = []
    for i in range(count):
        start = random.randint(9, 16)
        duration = random.choice([0.5, 1, 1.5, 2])
        end = min(start + duration, 18)
        meetings.append({
            "id": i,
            "name": names[i % len(names)],
            "start": start,
            "end": end,
        })
    return meetings


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/schedule", methods=["POST"])
def schedule_greedy():
    """그리디로 최적 스케줄을 반환한다."""
    data = request.get_json()
    meetings = data.get("meetings", [])

    selected_ids = greedy_schedule(meetings)

    return jsonify({
        "selected_ids": selected_ids,
        "count": len(selected_ids),
        "total": len(meetings),
        "algorithm": "greedy",
    })


@app.route("/api/schedule/bruteforce", methods=["POST"])
def schedule_bruteforce():
    """브루트포스로 최적 스케줄을 반환한다."""
    data = request.get_json()
    meetings = data.get("meetings", [])

    if len(meetings) > 20:
        return jsonify({
            "error": "브루트포스는 20개 이하의 회의에서만 실행 가능합니다.",
        }), 400

    selected_ids = bruteforce_schedule(meetings)

    return jsonify({
        "selected_ids": selected_ids if selected_ids is not None else [],
        "count": len(selected_ids) if selected_ids is not None else 0,
        "total": len(meetings),
        "algorithm": "bruteforce",
    })


@app.route("/api/sample")
def sample_data():
    """샘플 회의 데이터를 반환한다."""
    count = request.args.get("count", 10, type=int)
    count = min(count, 20)
    meetings = generate_sample_meetings(count)
    return jsonify({"meetings": meetings})


if __name__ == "__main__":
    print("=" * 50)
    print(" 회의실 예약 스케줄러")
    print(" http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
