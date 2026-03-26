---
theme: default
title: "Week 04 Assignment — Closest Pair of Points Visualizer"
class: text-center
transition: slide-left
---

# Week 04 Assignment

Closest Pair of Points — Divide and Conquer Visualizer

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

Build a **closest pair of points** web app that compares the **brute force** approach with the **divide and conquer** algorithm, and visualizes the result on a 2D canvas.

**Backend:** Python (FastAPI or Flask)
**Frontend:** HTML + CSS + JavaScript (Canvas)

::right::

<img src="https://images.unsplash.com/photo-1509228468518-180dd4864904?w=800&q=80" alt="Points" style="border-radius: 12px; margin-top: 40px;" />

---

# Required Features

### 1. Closest Pair Algorithms

Implement **two approaches** to find the closest pair among n points in a 2D plane:

| Approach | Method | Complexity |
|----------|--------|-----------|
| Brute Force | Check all n(n−1)/2 pairs | O(n²) |
| Divide & Conquer | Split by x-coordinate, recurse, check strip | O(n log² n) |

**D&C strategy:**

```
1. Sort points by x-coordinate
2. Split into LEFT and RIGHT halves
3. Recursively find closest pair in each half → d
4. Check the "strip" (points within distance d of the dividing line)
5. Return the overall closest pair
```

---

# Required Features (cont.)

### 2. Web Interface

- **"Generate Random"** button to scatter n random points (user chooses n)
- Clicking **"Find Closest Pair"** runs both algorithms
- Display on a **2D canvas**:
  - All points plotted as dots
  - The **closest pair** highlighted and connected with a line
- Show **execution time** for both brute force and D&C, plus the **speedup ratio**

### 3. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/closest-pair` | Find closest pair using both methods, return results and timing |
| `POST` | `/generate` | Generate n random 2D points |
| `GET` | `/` | Serve the frontend page |

---

# Deliverables

### 1. Source Code (`.zip`)

```
week04_assignment/
├── app.py              # Backend
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── requirements.txt
```

### 2. Report (`.pdf` only, max 2 pages, font size 11pt+)

- **Screenshot** of the web app showing the closest pair highlighted on the canvas
- **Performance table** comparing brute force vs D&C at point counts 100, 1,000, 5,000
- **Analysis:** Explain how the divide and conquer approach reduces the problem from O(n²) to O(n log² n). Why is checking only the strip sufficient?

---

# Grading Criteria

| Criteria | Weight |
|----------|--------|
| Web app runs and works correctly | 20% |
| Algorithm requirements fully implemented | 40% |
| Report (2 pages max, font size 11+) | 40% |

> **Notice:** Assignment content may appear on **written exams**. If there is a significant discrepancy between your assignment results and your exam performance, a **grade penalty** may apply.

**Submit to LMS before the deadline.**
