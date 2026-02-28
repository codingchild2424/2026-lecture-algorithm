---
theme: default
title: "Week 09 Lab — Claude Code Tutorial + Project Kickoff"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 09 Lab
## Claude Code Tutorial + Project Kickoff

**Duration**: 50 min | **Format**: Guided tutorial + team activity

---
layout: section
---

# Part 1: Claude Code Tutorial
25 minutes

---

# Task 1: Install Claude Code

**Goal**: Install Claude Code and verify it runs

```bash
npm install -g @anthropic-ai/claude-code
claude
```

**Troubleshooting**:

| Problem | Solution |
|---------|----------|
| Node.js not installed | `brew install node` (macOS) or https://nodejs.org |
| npm permission errors | `sudo npm install -g ...` or use nvm |

<v-click>

**Time**: 5 minutes

</v-click>

---

# Task 2: Run the Reference Web App

**Goal**: Explore the algorithm review web app (Weeks 01-07)

```bash
cd project
pip install fastapi uvicorn
uvicorn app:app --reload
```

Open **http://127.0.0.1:8000** and explore:

| Feature | Algorithms |
|---------|-----------|
| Sorting | Bubble, merge, quick sort with step traces |
| Binary Search | Visualize search steps on a sorted array |
| Greedy | Coin change problem with greedy strategy |
| DP | Fibonacci (naive vs DP) and 0-1 Knapsack |

---

# Task 2: Study the Code

Read `project/app.py` and `project/static/app.js` to understand:

- How algorithms are implemented in Python
- How they connect to the web UI via FastAPI endpoints
- How step-by-step traces are generated and displayed

**Key question**: How does the frontend request algorithm results from the backend?

---

# Task 2: Build Your Own Version

Use Claude Code to generate a web app from scratch:

```bash
mkdir my-web-app && cd my-web-app
claude
```

> "Create a FastAPI web app that demonstrates sorting algorithms
> with step-by-step visualization."

**Key Skills to Practice**:
- Understanding how algorithms connect to web APIs
- Reviewing and understanding generated code (do **not** blindly accept)
- Asking "why?" to learn from the agent

**Time**: 20 minutes total for Task 2

---
layout: section
---

# Part 2: Project Kickoff
25 minutes

---

# Task 3: Team Formation + Topic Selection

**Form teams of 3-4 members**, then select a topic:

| Topic | Description | Example Algorithms |
|-------|-------------|-------------------|
| Mini Shopping Mall | Product listings, search, recommendations, cart | Sorting, Hash, Graph, DP |
| Social Network | Profiles, friends, feed, recommendations | BST, Hash, BFS, Dijkstra |
| Campus Map/Navigator | Building search, route finding | Hash, Graph, Dijkstra, Greedy |

You may also **propose your own topic** -- just ensure it uses at least 4 different algorithms.

**Time**: 10 minutes

---

# Task 4: Project Skeleton Setup

Use Claude Code to create your team's project skeleton:

```bash
mkdir team-project && cd team-project
claude
```

**Requirements**:
- FastAPI app with routes for your topic
- Sample data (products, users, buildings, etc.)
- At least one working page

**Time**: 15 minutes

---

# Grading Criteria

| Category | Weight | Details |
|----------|--------|---------|
| Algorithm Application | 40% | Minimum 4 algorithms |
| Performance Comparison | 20% | Before/after measurements |
| Completeness | 20% | Working web app, code quality |
| Presentation | 20% | Slides, explanation, Q&A |

---

# Project Schedule

| Week | Activity | Milestone |
|------|----------|-----------|
| **09** | CC tutorial + kickoff | Team formed, skeleton running |
| 10 | Hash table features | Hash-based feature integrated |
| 11 | Graph traversal features | Graph feature + midpoint check-in |
| 12 | Shortest path features | Path finding + presentation draft |
| 13 | Finalization + presentations | Code + slides complete |

---

# Today's Milestone

By the end of this lab:

- Claude Code is installed and working
- You have explored the reference web app
- Your team is formed (3-4 members)
- A topic is selected
- A project skeleton is running locally

**Next week**: Hash table features integration
