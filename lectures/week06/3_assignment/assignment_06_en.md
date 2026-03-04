---
theme: default
title: "Week 06 Assignment — Plagiarism Checker"
class: text-center
transition: slide-left
---

# Week 06 Assignment

Plagiarism Checker

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

Build a **plagiarism checker** web app that compares two documents and calculates their similarity using the **Longest Common Subsequence (LCS)** algorithm (dynamic programming).

**Backend:** Python (FastAPI or Flask)
**Frontend:** HTML + CSS + JavaScript

::right::

<img src="https://images.unsplash.com/photo-1450101499163-c8848c66ca85?w=800&q=80" alt="Documents" style="border-radius: 12px; margin-top: 40px;" />

---

# Required Features

### 1. LCS-Based Similarity Analysis

Implement the **LCS algorithm** using dynamic programming:

- Build the **DP table** for two input texts
- **Backtrack** to find the LCS
- Calculate **similarity score**: `LCS length / max(len(A), len(B)) * 100%`
- Generate a **diff view**: mark parts as matched, added, or removed

---

# Required Features (cont.)

### 2. Web Interface

- Two **text areas** for inputting Document A and Document B
- A **"Check"** button to run the plagiarism analysis
- Display:
  - **Similarity score** (percentage)
  - **LCS length** and the actual LCS string
  - A **colored diff view**: matched (gray) / removed (red) / added (green)

### 3. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/check` | Compare two texts, return similarity score + diff |
| `GET` | `/` | Serve the frontend page |

---

# Deliverables

### 1. Source Code (`.zip`)

```
week06_assignment/
├── app.py              # Backend
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── requirements.txt
```

### 2. Report (`.pdf` only, max 2 pages, font size 11pt+)

- **Screenshot** of the plagiarism checker comparing two sample texts
- **DP table** for a short example (e.g., "ALGORITHM" vs "ALTRUISTIC")
- **Analysis:** Explain the time and space complexity of LCS. How does this relate to tools like `git diff` or Turnitin?

---

# Grading Criteria

| Criteria | Weight |
|----------|--------|
| Web app runs and works correctly | 20% |
| Algorithm requirements fully implemented | 40% |
| Report (2 pages max, font size 11+) | 40% |

> **Notice:** Assignment content may appear on **written exams**. If there is a significant discrepancy between your assignment results and your exam performance, a **grade penalty** may apply.

**Submit to LMS before the deadline.**
