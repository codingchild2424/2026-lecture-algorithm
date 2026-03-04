---
theme: default
title: "Week 03 Assignment — Music Playlist Manager"
class: text-center
transition: slide-left
---

# Week 03 Assignment

Music Playlist Manager

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

Build a **music playlist manager** web app that sorts songs by various criteria using different sorting algorithms. Compare sorting performance as the playlist grows.

**Backend:** Python (FastAPI or Flask)
**Frontend:** HTML + CSS + JavaScript

::right::

<img src="https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=800&q=80" alt="Music" style="border-radius: 12px; margin-top: 40px;" />

---

# Required Features

### 1. Sorting Algorithms

Implement at least **3 sorting algorithms**:

| Algorithm | Worst Case |
|-----------|-----------|
| Selection Sort | O(n²) |
| Insertion Sort | O(n²) |
| Merge Sort | O(n log n) |

Each must sort a playlist by a user-chosen criterion: **title**, **artist**, **duration**, or **play count**.

---

# Required Features (cont.)

### 2. Web Interface

- Display a **playlist table** (title, artist, duration, play count)
- **"Generate Random"** button to create a playlist of N songs
- **Dropdown** to select sort criterion and sort algorithm
- **"Sort"** button shows: sorted result, comparisons, swaps, execution time
- **"Compare All"** button runs all algorithms and shows a comparison table

### 3. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/sort` | Sort playlist with chosen algorithm + criterion |
| `POST` | `/compare` | Run all algorithms, return comparison data |
| `POST` | `/generate` | Generate random playlist of N songs |
| `GET` | `/` | Serve the frontend page |

---

# Deliverables

### 1. Source Code (`.zip`)

```
week03_assignment/
├── app.py              # Backend
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── requirements.txt
```

### 2. Report (`.pdf` only, max 2 pages, font size 11pt+)

- **Screenshot** of the playlist manager with sorting results
- **Comparison table** for N = 100, 1000, 5000 (comparisons, swaps, time per algorithm)
- **Analysis:** Which algorithm was fastest? Why? When would O(n²) algorithms still be acceptable?

---

# Grading Criteria

| Criteria | Weight |
|----------|--------|
| Web app runs and works correctly | 20% |
| Algorithm requirements fully implemented | 40% |
| Report (2 pages max, font size 11+) | 40% |

> **Notice:** Assignment content may appear on **written exams**. If there is a significant discrepancy between your assignment results and your exam performance, a **grade penalty** may apply.

**Submit to LMS before the deadline.**
