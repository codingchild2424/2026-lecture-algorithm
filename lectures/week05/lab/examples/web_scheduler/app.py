"""Meeting Room Scheduler - Activity Selection demo."""
from flask import Flask, request, jsonify
import random

app = Flask(__name__)


def activity_selection(meetings):
    """Greedy: select maximum non-overlapping meetings (sort by end time)."""
    sorted_meetings = sorted(meetings, key=lambda m: m["end"])
    selected = [sorted_meetings[0]]
    for m in sorted_meetings[1:]:
        if m["start"] >= selected[-1]["end"]:
            selected.append(m)
    return selected


def generate_meetings(n=20):
    meetings = []
    for i in range(n):
        start = random.randint(8, 17)
        duration = random.randint(1, 3)
        meetings.append({"id": i, "name": f"Meeting-{i}", "start": start, "end": start + duration})
    return meetings


@app.route("/")
def index():
    return """<!DOCTYPE html>
<html><head><title>Meeting Scheduler</title>
<style>
.timeline { position: relative; height: 30px; margin: 2px 0; }
.meeting { position: absolute; height: 28px; border-radius: 4px; font-size: 11px;
           display: flex; align-items: center; padding: 0 4px; color: white; }
.selected { background: #2196F3; }
.rejected { background: #ccc; color: #666; }
</style></head>
<body>
<h1>Meeting Room Scheduler</h1>
<p>Greedy Algorithm: select meetings sorted by end time.</p>
<button onclick="run()">Generate & Schedule</button>
<p id="info"></p>
<div id="timeline"></div>
<script>
async function run() {
    const res = await fetch('/api/schedule');
    const data = await res.json();
    document.getElementById('info').innerHTML =
        `Total requests: ${data.total}, Selected: ${data.selected_count} (Greedy - Activity Selection)`;
    const div = document.getElementById('timeline');
    const ids = new Set(data.selected.map(m => m.id));
    div.innerHTML = '<div style="position:relative;margin-left:60px">' +
        Array.from({length:13}, (_,i) =>
            `<span style="position:absolute;left:${i*60}px;top:-15px;font-size:11px">${i+8}:00</span>`
        ).join('') + '</div>' +
        data.all.map(m => {
            const cls = ids.has(m.id) ? 'selected' : 'rejected';
            return `<div class="timeline"><span style="width:55px;display:inline-block;font-size:12px">${m.name}</span>` +
                `<div class="meeting ${cls}" style="left:${(m.start-8)*60+60}px;width:${(m.end-m.start)*60}px">${m.start}~${m.end}</div></div>`;
        }).join('');
}
</script>
</body></html>"""


@app.route("/api/schedule")
def api_schedule():
    meetings = generate_meetings(15)
    selected = activity_selection(meetings)
    return jsonify({
        "all": sorted(meetings, key=lambda m: m["start"]),
        "selected": selected,
        "total": len(meetings),
        "selected_count": len(selected)
    })


if __name__ == "__main__":
    app.run(debug=True, port=5000)
