# Week 12 Project -- Shortest Path Explorer

## Setup

```bash
pip install fastapi uvicorn
```

## Run

```bash
cd lectures/week12/2_lab/project
uvicorn app:app --reload
```

Then open <http://127.0.0.1:8000> in your browser.

## Features

- **Dijkstra Visualization** -- Define a weighted graph (nodes and weighted
  edges) or load a preset. Run Dijkstra from a source node and watch step by
  step as the algorithm extracts the minimum-distance node from the priority
  queue and relaxes neighboring edges. Distance badges update on each node,
  and the shortest path tree is highlighted as it builds. Use Prev/Next or
  Play to animate.

- **Bellman-Ford Visualization** -- Run Bellman-Ford on the same graph (or
  load special presets with negative weights). Watch iteration-by-iteration as
  every edge is checked for relaxation. The algorithm detects negative-weight
  cycles and displays an alert if one is found. Includes presets for both
  negative-weight graphs and graphs with negative cycles.

- **Algorithm Comparison** -- Run both Dijkstra and Bellman-Ford on the same
  graph from the same source node. A side-by-side comparison table shows the
  number of relaxations, execution time, and key properties (negative weight
  handling, time complexity). Both shortest path trees are rendered for visual
  comparison.

- **Campus Map Demo** -- A preset weighted graph representing a campus with
  10 buildings as nodes and walking distances (in minutes) as edge weights.
  Select two buildings to find the shortest walking route using Dijkstra's
  algorithm. The path is highlighted on the map along with a step-by-step
  route breakdown showing the walking time for each segment.

## API Endpoints

| Method | Path                        | Description                                   |
|--------|-----------------------------|-----------------------------------------------|
| POST   | `/api/graph/init`           | Initialize a weighted graph                   |
| POST   | `/api/graph/preset`         | Load preset undirected weighted graph          |
| POST   | `/api/graph/preset-negative`| Load preset directed graph with negative edges |
| POST   | `/api/graph/preset-negcycle`| Load preset graph with a negative cycle        |
| POST   | `/api/dijkstra`             | Run Dijkstra's algorithm                      |
| POST   | `/api/dijkstra/path`        | Run Dijkstra and return a specific path        |
| POST   | `/api/bellman-ford`         | Run Bellman-Ford algorithm                    |
| POST   | `/api/compare`              | Run both algorithms and compare                |
| POST   | `/api/campus/init`          | Load campus map preset                        |
| POST   | `/api/campus/path`          | Find shortest path between campus buildings   |

## Project Structure

```
project/
  app.py              # FastAPI backend (Dijkstra, Bellman-Ford, comparison, campus map)
  static/
    index.html        # Main single-page HTML with four tabs
    style.css         # Stylesheet
    app.js            # Frontend logic (SVG rendering, API calls, step animation)
  README.md           # This file
```
