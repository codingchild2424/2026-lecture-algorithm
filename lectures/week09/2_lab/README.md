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

### Task 2: Run the Algorithm Review Web App (20 min)
Explore the reference project that demonstrates algorithms from Weeks 01-07:

1. **Install dependencies and run the app:**
   ```bash
   cd project
   pip install fastapi uvicorn
   uvicorn app:app --reload
   ```

2. **Open `http://127.0.0.1:8000`** and explore:
   - **Sorting**: Compare bubble, merge, and quick sort with step traces
   - **Binary Search**: Visualize search steps on a sorted array
   - **Greedy**: Coin change problem with greedy strategy
   - **DP**: Fibonacci (naive vs DP) and 0-1 Knapsack

3. **Study the code** — read `project/app.py` and `project/static/app.js` to understand how the algorithms are implemented and connected to the web UI.

4. **Use Claude Code to build your own version:**
   ```bash
   mkdir my-web-app && cd my-web-app
   claude
   ```
   > "Create a FastAPI web app that demonstrates sorting algorithms with step-by-step visualization."

**Key Skills to Practice**:
- Understanding how algorithms connect to web APIs
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
- FastAPI app with routes for your topic
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
