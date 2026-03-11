"""
Meeting Room Scheduler -- Activity Selection Problem

Greedy strategy: Selecting meetings with the earliest end time maximizes the number of meetings.
Brute force: Checks all subsets to find the optimal solution (only feasible for small N).

Run: python app.py
Access: http://localhost:5000
"""

from flask import Flask, render_template, request, jsonify
from itertools import combinations
import random

app = Flask(__name__)


def greedy_schedule(meetings):
    """Select the maximum number of meetings using greedy.

    Activity Selection: Sort by end time in ascending order,
    then select meetings that do not overlap with the previously selected one.

    Time complexity: O(n log n) -- sorting dominates

    Args:
        meetings: [{"id": int, "name": str, "start": float, "end": float}, ...]

    Returns:
        List of selected meeting ids
    """
    # Sort by end time
    sorted_meetings = sorted(meetings, key=lambda m: m["end"])

    selected = []
    last_end = -1

    for meeting in sorted_meetings:
        if meeting["start"] >= last_end:
            selected.append(meeting["id"])
            last_end = meeting["end"]

    return selected


def bruteforce_schedule(meetings):
    """Select the maximum number of meetings using brute force.

    Checks all subsets to find the maximum number of non-overlapping meetings.

    Time complexity: O(2^n * n) -- checks all subsets

    Args:
        meetings: [{"id": int, "name": str, "start": float, "end": float}, ...]

    Returns:
        List of selected meeting ids
    """
    n = len(meetings)

    # Prevent timeout for large N
    if n > 20:
        return None

    def is_compatible(subset):
        """Check if all meetings in the subset are non-overlapping."""
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
    """Generate random meeting data."""
    random.seed(42)
    names = [
        "Team Meeting", "Planning", "Code Review", "Design Discussion", "Sprint Planning",
        "Client Meeting", "1:1 Meeting", "Tech Seminar", "Project Report", "Brainstorming",
        "Strategy Meeting", "Budget Discussion", "Performance Review", "Workshop", "Training Session",
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
    """Return the optimal schedule using greedy."""
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
    """Return the optimal schedule using brute force."""
    data = request.get_json()
    meetings = data.get("meetings", [])

    if len(meetings) > 20:
        return jsonify({
            "error": "Brute force can only run with 20 or fewer meetings.",
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
    """Return sample meeting data."""
    count = request.args.get("count", 10, type=int)
    count = min(count, 20)
    meetings = generate_sample_meetings(count)
    return jsonify({"meetings": meetings})


if __name__ == "__main__":
    print("=" * 50)
    print(" Meeting Room Scheduler")
    print(" http://localhost:5000")
    print("=" * 50)
    app.run(debug=True, port=5000)
