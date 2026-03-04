---
theme: default
title: "Week 02 Assignment — Mini Shopping Mall Search"
class: text-center
transition: slide-left
---

# Week 02 Assignment

Mini Shopping Mall — Product Search

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

Build a **mini shopping mall** web app where users can search for products. Implement three different search approaches and compare their performance — then use **Locust** to see how algorithm choice affects the service under real user load.

**Backend:** Python (FastAPI or Flask)
**Frontend:** HTML + CSS + JavaScript
**Load Testing:** Locust

::right::

<img src="https://images.unsplash.com/photo-1563013544-824ae1b704d3?w=800&q=80" alt="Online Shopping" style="border-radius: 12px; margin-top: 40px;" />

---

# Required Features

### 1. Product Data & Search Algorithms

Load a product list (1,000+ items with id, name, category, price) and implement **3 search methods**:

| Search Method | How It Works | Complexity |
|---------------|-------------|-----------|
| ID Lookup | `dict[product_id]` | O(1) |
| Name Search | Scan all products sequentially | O(n) |
| Duplicate Detection | Find products with the same name (nested loops) | O(n²) |

---

# Required Features (cont.)

### 2. Web Interface

- A **search bar** to search products by name or ID
- A **"Find Duplicates"** button to detect duplicate product names
- Results displayed as a **product card list** with name, price, category
- Each search shows **execution time** (ms)

### 3. API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/search/id?id=123` | O(1) lookup by product ID |
| `GET` | `/search/name?q=keyword` | O(n) linear name search |
| `GET` | `/search/duplicates` | O(n²) duplicate detection |
| `GET` | `/` | Serve the frontend page |

---

# Required Features (cont.)

### 4. Load Testing with Locust

Write a `locustfile.py` that simulates concurrent users calling each search endpoint.

```python
from locust import HttpUser, task

class ShopUser(HttpUser):
    @task
    def search_by_id(self):
        self.client.get("/search/id?id=42")

    @task
    def search_by_name(self):
        self.client.get("/search/name?q=laptop")

    @task
    def find_duplicates(self):
        self.client.get("/search/duplicates")
```

Run: `locust -f locustfile.py --host=http://localhost:8000`

---

# Load Test — What to Observe

Open the Locust web UI at `http://localhost:8089`:

- Start with **10 users**, ramp up to **50 users**
- Observe **response time** and **throughput** per endpoint

As concurrent users increase:

- O(1) ID lookup → stays fast and stable
- O(n) name search → slows slightly
- **O(n²) duplicate detection → response times spike, requests queue up**

> This is why algorithm choice matters in real web services.

---

# Deliverables

### 1. Source Code (`.zip`)

```
week02_assignment/
├── app.py              # Backend (FastAPI or Flask)
├── locustfile.py       # Locust load test
├── static/
│   ├── index.html
│   ├── style.css
│   └── app.js
└── requirements.txt    # Include locust
```

### 2. Report (`.pdf` only, max 2 pages, font size 11pt+)

- **Screenshot** of the shopping mall search results
- **Locust results**: response time chart for 10, 30, 50 concurrent users
- **Analysis:** Why does O(n²) degrade under load? Relate to Big-O and real-world impact

---

# Grading Criteria

| Criteria | Weight |
|----------|--------|
| Web app runs and works correctly | 20% |
| Algorithm requirements fully implemented | 40% |
| Report (2 pages max, font size 11+) | 40% |

> **Notice:** Assignment content may appear on **written exams**. If there is a significant discrepancy between your assignment results and your exam performance, a **grade penalty** may apply.

**Submit to LMS before the deadline.**
