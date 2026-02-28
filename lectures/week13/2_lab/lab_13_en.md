---
theme: default
title: "Week 13 Lab — Project Finalization + Presentations"
info: "Algorithms Lab"
class: text-center
drawings:
  persist: false
transition: slide-left
---

# Week 13 Lab
## Project Finalization + Presentations

**Duration**: 50 min | **Format**: Final polish (15 min) + Presentations (35 min)

---
layout: section
---

# Reference Demo: Algorithm Finale
5 minutes

---

# Semester Review Demo

Run the reference project one last time for a comprehensive review:

```bash
cd project
pip install fastapi uvicorn
uvicorn app:app --reload
```

**Features**:
- TSP visualization (brute force vs. heuristic)
- Knapsack DP
- Algorithm complexity dashboard
- Interactive quiz

Take inspiration for your own presentation!

---
layout: section
---

# Part 1: Final Code Polish
10 minutes

---

# Final Code Checklist

Use the first 10 minutes to finalize your project:

- [ ] Fix any remaining bugs
- [ ] Ensure all algorithm features are working
- [ ] Verify **minimum 4 algorithms** are applied
- [ ] Prepare your demo scenario
- [ ] Test the full user flow end-to-end

**Algorithms checklist** (need at least 4):

| Algorithm | Integrated? |
|-----------|:-----------:|
| Sorting (bubble/merge/quick) | |
| Binary Search / BST | |
| Hash Table | |
| Graph Traversal (BFS/DFS) | |
| Shortest Path (Dijkstra/Bellman-Ford) | |
| Greedy | |
| Dynamic Programming | |

---
layout: section
---

# Part 2: Team Presentations
35 minutes

---

# Presentation Format

- **7 minutes** per team: 5 min presentation + 2 min Q&A
- **All team members** must participate in the presentation

```
[5 min] Present    ->    [2 min] Q&A    ->    Next team
```

---

# Required Presentation Content

| # | Section | What to cover |
|---|---------|---------------|
| 1 | **Project Introduction** | Web app topic and feature description |
| 2 | **Algorithms Applied** | At least 4 algorithms with brief explanation of each |
| 3 | **Performance Comparison** | Before/after measurement results |
| 4 | **Live Demo** | Walk through the running web app |
| 5 | **Lessons Learned** | Challenges faced and key takeaways |

---

# Grading Criteria

| Category | Weight | What is evaluated |
|----------|--------|-------------------|
| Algorithm Application | 40% | Minimum 4 algorithms correctly applied |
| Performance Comparison | 20% | Meaningful before/after measurements |
| Completeness | 20% | Working web app, code quality, documentation |
| Presentation | 20% | Slides, explanation clarity, Q&A responses |

**Total: 100%**

---

# Deliverables

Each team must submit:

1. **GitHub repository link**
   - Complete source code
   - README with setup instructions
   - Description of algorithms used

2. **Presentation materials**
   - PDF or slide deck
   - Include performance comparison charts

---

# Semester Project Journey

| Week | What you built | Algorithm focus |
|------|----------------|-----------------|
| 09 | Team formed, skeleton app | Setup + Claude Code |
| 10 | Hash-based features | Chaining, open addressing |
| 11 | Graph features + midpoint check-in | BFS, DFS, topological sort |
| 12 | Shortest path features + slides draft | Dijkstra, Bellman-Ford |
| **13** | **Final polish + presentation** | **All algorithms together** |

---

# Presentation Tips

**Do**:
- Start with a quick demo to grab attention
- Explain **why** you chose each algorithm, not just **what** it does
- Show real performance numbers (tables, charts)
- Prepare for common Q&A questions

**Don't**:
- Read slides word-for-word
- Skip the live demo
- Forget to mention challenges and lessons learned
- Go over time (5 min is strict)

---

# Good luck!

Present your work with confidence.

You have built a complete web application integrating multiple algorithms -- that is a real achievement.

**Submission deadline**: End of today's lab session
