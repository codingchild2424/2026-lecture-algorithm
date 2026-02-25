# Week 11 Project -- Graph Traversal Explorer

## Setup

```bash
pip install fastapi uvicorn
```

## Run

```bash
cd lectures/week11/2_lab/project
uvicorn app:app --reload
```

Then open <http://127.0.0.1:8000> in your browser.

## Features

- **Graph Traversal Visualization** -- Define an undirected or directed graph
  by entering nodes and edges (or load a preset). Run BFS or DFS and watch the
  traversal order highlighted step by step on an SVG graph. Use the Prev/Next
  buttons or Play to animate. Visit-order badges show the sequence in which
  nodes are discovered.

- **BFS Shortest Path** -- Find the shortest path between two nodes in an
  unweighted graph using BFS. The path is highlighted in green on the graph
  alongside the distance (edge count).

- **DFS Applications: Topological Sort & Cycle Detection** -- Input a directed
  graph (or load a preset DAG / cyclic graph). Run Kahn's algorithm for
  topological sort and see the ordering step by step. Run DFS-based cycle
  detection to find back edges; if a cycle exists, the cycle path is
  highlighted in red.

- **Social Network Demo** -- A preset social network of 10 users. Select any
  user to get friend-of-friend suggestions via BFS. The BFS tree is overlaid
  on the graph, with direct friends and suggestions styled differently.

## API Endpoints

| Method | Path                       | Description                                 |
|--------|----------------------------|---------------------------------------------|
| POST   | `/api/graph/init`          | Initialize a graph for traversal            |
| POST   | `/api/graph/preset`        | Load preset undirected graph                |
| POST   | `/api/graph/traverse`      | Run BFS or DFS on the graph                 |
| POST   | `/api/graph/shortest-path` | BFS shortest path between two nodes         |
| POST   | `/api/dag/init`            | Initialize a directed graph                 |
| POST   | `/api/dag/preset-dag`      | Load preset DAG (course prerequisites)      |
| POST   | `/api/dag/preset-cycle`    | Load preset graph with a cycle              |
| POST   | `/api/dag/toposort`        | Run topological sort (Kahn's algorithm)     |
| POST   | `/api/dag/cycle`           | Run DFS-based cycle detection               |
| POST   | `/api/social/init`         | Load preset social network                  |
| POST   | `/api/social/suggest`      | Get BFS friend suggestions for a user       |

## Project Structure

```
project/
  app.py              # FastAPI backend (graph algorithms + API)
  static/
    index.html        # Main single-page HTML with four tabs
    style.css         # Stylesheet
    app.js            # Frontend logic (SVG rendering, API calls, step animation)
  README.md           # This file
```
