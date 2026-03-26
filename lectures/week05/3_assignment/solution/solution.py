"""Homework 4: Reference Solution — Classroom Reservation (Activity Selection)"""
import random


def activity_selection(activities):
    """
    Greedy activity selection — sort by finish time, greedily pick non-overlapping.
    Input: list of dicts with 'name', 'start', 'end'
    Returns: (selected list, trace of selection steps)
    """
    sorted_acts = sorted(activities, key=lambda a: a["end"])
    selected = []
    trace = []
    last_end = -1

    for act in sorted_acts:
        if act["start"] >= last_end:
            selected.append(act)
            trace.append({
                "action": "select",
                "activity": act,
                "reason": f"start={act['start']} >= last_end={last_end}",
            })
            last_end = act["end"]
        else:
            trace.append({
                "action": "reject",
                "activity": act,
                "reason": f"start={act['start']} < last_end={last_end}",
            })

    return selected, trace


def generate_activities(n=15):
    """Generate n random activities with start/end times."""
    activities = []
    for i in range(n):
        start = random.randint(0, 20)
        end = start + random.randint(1, 5)
        activities.append({"name": f"Event_{i+1}", "start": start, "end": end})
    return activities
