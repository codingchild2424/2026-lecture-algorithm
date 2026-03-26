---
theme: default
title: "Week 04 Assignment — Large Number Multiplication"
class: text-center
transition: slide-left
---

# Week 04 Assignment

Large Number Multiplication — Karatsuba Algorithm

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

Build a **large number multiplication** web app that compares the **naive method** with the **Karatsuba algorithm** to demonstrate how divide and conquer reduces computational complexity.

**Backend:** Python (FastAPI or Flask)
**Frontend:** HTML + CSS + JavaScript

::right::

<img src="https://images.unsplash.com/photo-1635070041078-e363dbe005cb?w=800&q=80" alt="Mathematics" style="border-radius: 12px; margin-top: 40px;" />

---

# Required Features

### 1. Multiplication Algorithms

Implement **two multiplication approaches** for arbitrarily large integers:

| Approach | Method | Complexity |
|----------|--------|-----------|
| Naive | Python's built-in `*` operator (grade-school multiplication) | O(n²) |
| Karatsuba | Divide and conquer — split digits, 3 recursive multiplications | O(n^1.585) |

**Karatsuba key idea:**

```
x = high_x · 10^m + low_x
y = high_y · 10^m + low_y

z0 = low_x × low_y
z2 = high_x × high_y
z1 = (low_x + high_x) × (low_y + high_y) − z0 − z2

result = z2 · 10^(2m) + z1 · 10^m + z0
```

Only **3 multiplications** instead of 4 → better asymptotic complexity.

---

# Required Features (cont.)

### 2. Web Interface

- User can **enter two large numbers** or click **"Generate Random"** to create numbers with a specified digit count
- Clicking **"Multiply"** runs both algorithms
- Display:
  - The **result** of the multiplication
  - **Execution time** for both naive and Karatsuba methods
  - **Speedup ratio** (naive time / Karatsuba time)

### 3. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `POST` | `/multiply` | Multiply two numbers using both methods, return results and timing |
| `POST` | `/generate` | Generate two random numbers with a given digit count |
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

- **Screenshot** of the web app multiplying two large numbers (1,000+ digits)
- **Performance table** comparing naive vs Karatsuba at digit counts 100, 1,000, 10,000
- **Analysis:** Explain the divide and conquer strategy behind Karatsuba. Why does reducing from 4 to 3 recursive multiplications improve the overall complexity?

---

# Grading Criteria

| Criteria | Weight |
|----------|--------|
| Web app runs and works correctly | 20% |
| Algorithm requirements fully implemented | 40% |
| Report (2 pages max, font size 11+) | 40% |

> **Notice:** Assignment content may appear on **written exams**. If there is a significant discrepancy between your assignment results and your exam performance, a **grade penalty** may apply.

**Submit to LMS before the deadline.**
