# Week 09 Project -- Algorithm Review Web App

A single-page web application that demonstrates fundamental algorithms
covered in weeks 01-07: sorting, binary search, greedy, and dynamic
programming.  Built with **FastAPI** (backend) and vanilla **HTML / CSS /
JavaScript** (frontend).

## Setup

```bash
pip install fastapi uvicorn
```

## Run

```bash
cd lectures/week09/2_lab/project
uvicorn app:app --reload
```

Then open <http://127.0.0.1:8000> in your browser.

## Features

- **Sorting** -- Enter (or randomly generate) a list of numbers and sort
  with Bubble, Selection, Insertion, Merge, or Quick Sort.  View
  step-by-step traces, comparison/swap counts, and a side-by-side
  performance comparison of all five algorithms with bar charts.

- **Binary Search** -- Search for a target in a sorted array.  The app
  shows each low/mid/high step and explains the decision at every
  iteration.  Includes O(log n) complexity annotation.

- **Greedy (Coin Change)** -- Enter an amount and coin denominations.
  The greedy algorithm picks the largest coins first and shows each
  step.  Includes a note about when greedy fails to find the optimal
  solution.

- **Dynamic Programming**
  - *Fibonacci*: Compare naive recursion vs. bottom-up DP.  See function
    call counts, execution times, speedup ratio, and the DP table.
  - *0/1 Knapsack*: Enter items (name, weight, value) and a capacity.
    The DP solver finds the optimal selection and highlights chosen
    items.

## API Endpoints

| Method | Path                  | Description                        |
|--------|-----------------------|------------------------------------|
| POST   | `/api/sort`           | Sort with a single algorithm       |
| POST   | `/api/sort/compare`   | Compare all sorting algorithms     |
| POST   | `/api/search/binary`  | Binary search with step trace      |
| POST   | `/api/greedy/coins`   | Greedy coin change                 |
| POST   | `/api/dp/fibonacci`   | Fibonacci: naive vs DP             |
| POST   | `/api/dp/knapsack`    | 0/1 Knapsack problem               |

## Project Structure

```
project/
  app.py              # FastAPI backend (algorithms + API routes)
  static/
    index.html        # Main single-page HTML
    style.css         # Stylesheet
    app.js            # Frontend logic (fetch calls, DOM updates)
  README.md           # This file
```
