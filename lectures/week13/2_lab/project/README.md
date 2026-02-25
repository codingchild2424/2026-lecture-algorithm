# Week 13 Project -- Algorithm Finale

## Setup

```bash
pip install fastapi uvicorn
```

## Run

```bash
cd lectures/week13/2_lab/project
uvicorn app:app --reload
```

Then open <http://127.0.0.1:8000> in your browser.

## Features

- **TSP Visualization** -- Place cities on an SVG canvas by clicking, or load
  one of three presets (Pentagon, Random 7, Clusters 8). The brute-force
  algorithm finds the exact optimal tour for small N (up to 10) by checking all
  (N-1)! permutations, while the nearest-neighbor heuristic provides a fast
  O(N^2) approximate solution. Both tours are rendered side by side with
  distance, computation time, and quality ratio compared.

- **0-1 Knapsack Problem** -- Define items with weights and values (or load a
  preset), set a knapsack capacity, and solve using dynamic programming and
  brute force. The full DP table is rendered with the backtrack path
  highlighted. Selected items and their total weight/value are shown.
  Performance comparison shows DP's O(nW) vs brute force's O(2^n) with actual
  execution times.

- **Algorithm Complexity Dashboard** -- A comprehensive card-based summary of
  all algorithms covered during the semester, organized by category (Sorting,
  Searching, Graph Algorithms, Dynamic Programming, NP-Complete). Each card
  shows best/average/worst time complexity, space complexity, paradigm, and
  stability. Filter by category using the toolbar buttons.

- **Interactive Quiz** -- A 10-question multiple-choice quiz testing knowledge
  of algorithm paradigms, complexities, NP-completeness, and when to use which
  algorithm. Answers are graded server-side with explanations for each question.
  Score is displayed with a visual indicator.

## API Endpoints

| Method | Path                    | Description                                |
|--------|-------------------------|--------------------------------------------|
| POST   | `/api/tsp/solve`        | Solve TSP with brute force and heuristic   |
| POST   | `/api/tsp/preset`       | Load a TSP city preset                     |
| GET    | `/api/tsp/presets`      | List available TSP presets                 |
| POST   | `/api/knapsack/solve`   | Solve 0-1 Knapsack with DP and brute force |
| POST   | `/api/knapsack/preset`  | Load a Knapsack item preset                |
| GET    | `/api/knapsack/presets` | List available Knapsack presets             |
| GET    | `/api/dashboard`        | Get algorithm complexity dashboard data    |
| GET    | `/api/quiz`             | Get quiz questions (without answers)       |
| POST   | `/api/quiz/submit`      | Submit quiz answers and get graded results |

## Project Structure

```
project/
  app.py              # FastAPI backend (TSP, Knapsack, Dashboard, Quiz)
  static/
    index.html        # Main single-page HTML with four tabs
    style.css         # Stylesheet
    app.js            # Frontend logic (SVG rendering, API calls, DP table)
  README.md           # This file
```
