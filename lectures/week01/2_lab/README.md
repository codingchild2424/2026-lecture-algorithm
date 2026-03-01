# Week 01 Lab — Coding Agents

## Objectives
- Install and use an AI-powered coding agent for real development tasks.
- Learn effective prompting techniques (RALPH) to iteratively improve agent output.

## Prerequisites
- Node.js (for `npm install`)
- Python 3.10+ installed
- Text editor or IDE (VS Code recommended)

---

## Task 1: Install a Coding Agent (10 min)

Install one of the following:
- **Gemini CLI** (free): `npm install -g @google/gemini-cli`
- **Claude Code** (paid): `npm install -g @anthropic-ai/claude-code`

Verify installation and try a simple prompt.

## Task 2: Organize Files (10 min)

Use the agent to organize files in a messy directory (e.g., `~/Downloads`).

Observe how the agent plans, asks for confirmation, and handles edge cases.

## Task 3: Document a GitHub Repo (10 min)

Use the agent to generate a `README.md` for an existing codebase.

Evaluate: accuracy, completeness, setup instructions.

## Task 4: RALPH Technique (10 min)

**R**equest → **A**nalyze → **L**ist issues → **P**rompt again → **H**armonize

Use the RALPH loop to iteratively improve the README from Task 3 using a rubric.

## Task 5: Build a Sorting Benchmark (10 min)

Use the agent to build a multi-file Python sorting benchmark (bubble sort, merge sort, built-in sort).

Observe how the agent breaks a complex problem into multiple files and handles follow-up requests.

---

## Semester Project Preview

Starting in **Week 09**, you will work in teams of 3-4 to build a **web application that incorporates algorithms** learned throughout the course.

| Phase | Week | Activity |
|-------|------|----------|
| Kickoff | 09 | Claude Code tutorial + team formation + topic selection |
| Sprint 1 | 10 | Hash table features + performance comparison |
| Sprint 2 | 11 | Graph traversal features + mid-project check-in |
| Sprint 3 | 12 | Shortest path features + presentation prep |
| Final | 13 | Code finalization + team presentations |

**Grading Criteria**:
- Algorithm application (40%): Apply at least 4 different algorithms
- Performance comparison (20%): Before/after measurement results
- Completeness (20%): Working web app, code quality
- Presentation (20%): Slides, explanation, Q&A
