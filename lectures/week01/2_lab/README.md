# Week 01 Lab — Environment Setup & Coding Agents

## Objectives
- Set up the development environment and learn how to leverage coding agents for algorithm study.

## Prerequisites
- Python 3.10+ installed
- Text editor or IDE (VS Code recommended)

---

## Task 1: Install a Coding Agent (10 min)

Install one of the following:
- **Claude Code**: `npm install -g @anthropic-ai/claude-code`
- **Gemini CLI**: `npm install -g @anthropic-ai/gemini-cli` (or refer to the official docs)
- **OpenCode**: `go install github.com/opencode-ai/opencode@latest`

After installation, run the tool in your terminal and verify it works correctly.

## Task 2: Verify Dev Environment & Online Judge Account (10 min)

1. Check your Python version:
   ```bash
   python3 --version
   ```

2. Install the required packages:
   ```bash
   pip install matplotlib
   ```

3. Create an account on [Baekjoon Online Judge](https://www.acmicpc.net/)

## Task 3: Implement Binary Search with an Agent (15 min)

Use the RALPH technique to ask a coding agent to implement binary search.

**What is the RALPH technique?**
- **R**ole: Assign a role ("You are an algorithm tutor")
- **A**sk: Make a request ("Implement binary search in Python")
- **L**imit: Set constraints ("Both recursive and iterative versions")
- **P**rovide: Supply input ("Find 7 in the sorted list [1,3,5,7,9,11]")
- **H**int: Give a hint ("Also explain why the time complexity is O(log n)")

**Exercise**: Refer to `examples/binary_search.py`, implement it yourself, and compare your code with the agent's output.

## Task 4: Create an Algorithm Visualization Script (10 min)

Ask the agent to create a script that visually demonstrates the binary search process.

Example prompt:
> "Create a Python script that prints the binary search process step by step. At each step, show the current search range and the mid value."

## Task 5: Solve Your First Baekjoon Problem (5 min)

- [BOJ 1920 — Finding Numbers](https://www.acmicpc.net/problem/1920)
- Use the agent to develop a solving strategy, then submit your solution.

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

**Suggested Topics**: Mini Shopping Mall, Social Network, Campus Map/Navigator, or your own idea

**Grading Criteria**:
- Algorithm application (40%): Apply at least 4 different algorithms
- Performance comparison (20%): Before/after measurement results
- Completeness (20%): Working web app, code quality
- Presentation (20%): Slides, explanation, Q&A
