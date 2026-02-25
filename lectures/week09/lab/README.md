# Week 09 Lab — Claude Code Tutorial + Project Kickoff

## Overview
- **Duration**: 50 minutes
- **Format**: Guided tutorial + team activity
- **Goal**: Learn to use Claude Code for building web applications, form project teams, and set up a project skeleton

---

## Part 1: Claude Code Tutorial (25 min)

### Task 1: Install Claude Code (5 min)
Install Claude Code and verify it runs:
```bash
npm install -g @anthropic-ai/claude-code
claude
```

If you encounter issues:
- Node.js not installed: `brew install node` (macOS) or download from https://nodejs.org
- npm permission errors: use `sudo npm install -g ...` or use nvm

### Task 2: Build a Flask App with Claude Code (20 min)
Use Claude Code to generate a simple web application step by step:

1. **Create a project directory and start Claude Code:**
   ```bash
   mkdir my-web-app && cd my-web-app
   claude
   ```

2. **Ask Claude Code to create a Flask starter app:**
   > "Create a simple Flask web app with a landing page, a page that sorts a list of numbers using different algorithms, and a page that searches for a number using binary search."

3. **Run and test the app:**
   ```bash
   pip install flask
   python app.py
   ```

4. **Iterate with Claude Code** — ask it to add features, fix bugs, or explain the code.

**Key Skills to Practice**:
- Giving clear, specific prompts
- Reviewing and understanding generated code (do not blindly accept)
- Asking "why?" to learn from the agent

---

## Part 2: Project Kickoff (25 min)

### Task 3: Team Formation + Topic Selection (10 min)
- Form teams of **3-4 members**
- Select a topic (or propose your own):

| Topic | Description | Example Algorithms |
|-------|-------------|-------------------|
| Mini Shopping Mall | Product listings, search, recommendations, cart | Sorting, Hash, Graph (recommendations), DP |
| Social Network | Profiles, friends, feed, recommendations | BST, Hash, BFS (friend suggestions), Dijkstra |
| Campus Map/Navigator | Building search, route finding | Hash, Graph, Dijkstra, Greedy |

### Task 4: Project Skeleton Setup (15 min)
Use Claude Code to create your team's project skeleton:
- Basic Flask app with routes for your topic
- Sample data (products, users, buildings, etc.)
- At least one working page

**Grading Criteria**:
- Algorithm application (40%): Minimum 4 algorithms
- Performance comparison (20%): Before/after measurements
- Completeness (20%): Working web app, code quality
- Presentation (20%): Slides, explanation, Q&A

**Project Schedule**:
| Week | Activity | Milestone |
|------|----------|-----------|
| 09 | CC tutorial + kickoff | Team formed, skeleton running |
| 10 | Hash table features | Hash-based feature integrated |
| 11 | Graph traversal features | Graph feature + midpoint check-in |
| 12 | Shortest path features | Path finding + presentation draft |
| 13 | Finalization + presentations | Code + slides complete |
