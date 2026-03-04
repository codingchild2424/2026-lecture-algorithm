---
theme: default
title: "Week 05 Assignment — Classroom Reservation System"
class: text-center
transition: slide-left
---

# Week 05 Assignment

Classroom Reservation System

Korea University Sejong Campus, Dept. of Computer Science & Software

---

# Assignment Overview

- **Weight:** 1% of total grade
- **Deadline:** Monday before the next theory class, **11:59 PM**
- **Submission:** LMS (source code `.zip` + report `.pdf`)

> **Important:** LMS may experience issues near the deadline. Submit by **Sunday** at the latest to avoid problems. Late submissions due to system errors **will not be excused** — meeting the deadline is the student's responsibility.

---
layout: two-cols
layoutClass: gap-8
---

# Problem

Build a **classroom reservation system** web app that uses the **greedy activity selection** algorithm to schedule the maximum number of non-overlapping events in a room.

**Backend:** Python (FastAPI or Flask)
**Frontend:** HTML + CSS + JavaScript

::right::

<img src="https://images.unsplash.com/photo-1506784983877-45594efa4cbe?w=800&q=80" alt="Schedule" style="border-radius: 12px; margin-top: 40px;" />

---

# Required Features

### 1. Greedy Activity Selection

Implement the **activity selection algorithm**:

- Input: a list of reservation requests, each with **start time** and **end time**
- Sort by **finish time**
- Greedily select non-overlapping events
- Output: the **maximum set** of reservations that can be accommodated

---

# Required Features (cont.)

### 2. Web Interface

- User can **add reservations** by entering event name, start/end time
- **"Generate Random"** button for sample data (e.g., 15 random events)
- Clicking **"Schedule"** runs the greedy algorithm
- Display:
  - A **timeline visualization** — all requests (gray) and selected events (highlighted)
  - **Number of selected** vs total requests
  - **Step-by-step trace** of the greedy selection order

### 3. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/schedule` | Run activity selection, return selected events |
| `POST` | `/generate` | Generate random reservation requests |
| `GET` | `/` | Serve the frontend page |

---

# Deliverables

### 1. Source Code (`.zip`)

```
week05_assignment/
├── app.py              # Backend
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── requirements.txt
```

### 2. Report (`.pdf` only, max 2 pages, font size 11pt+)

- **Screenshot** of the reservation system with a sample input (10+ events)
- **Step-by-step trace** of the greedy selection on your sample input
- **Analysis:** Why does sorting by finish time guarantee the optimal solution? Could sorting by start time or duration work instead?

---

# Grading Criteria

| Criteria | Weight |
|----------|--------|
| Web app runs and works correctly | 20% |
| Algorithm requirements fully implemented | 40% |
| Report (2 pages max, font size 11+) | 40% |

> **Notice:** Assignment content may appear on **written exams**. If there is a significant discrepancy between your assignment results and your exam performance, a **grade penalty** may apply.

**Submit to LMS before the deadline.**
