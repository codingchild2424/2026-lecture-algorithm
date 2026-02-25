# Week 10 Project -- Hash Table Explorer

## Setup

```bash
pip install fastapi uvicorn
```

## Run

```bash
cd lectures/week10/2_lab/project
uvicorn app:app --reload
```

Then open <http://127.0.0.1:8000> in your browser.

## Features

- **Hash Table Visualization** -- Initialize a hash table with configurable
  size and collision resolution method (separate chaining or linear probing).
  Insert, search, and delete keys interactively. See the hash function
  computation step by step, observe bucket states, collision chains, and
  probe sequences in real time.

- **Collision Resolution Comparison** -- Insert N random keys into both a
  chaining and a linear probing hash table of the same size. Compare
  collisions, load factor, average chain/probe length, and average search
  probes side by side with tables and bar charts.

- **Phone Book Application** -- A practical hash table use case: a phone
  book that stores name-to-phone mappings using a custom chaining hash
  table (not Python's built-in dict). Add, look up, and remove contacts
  while viewing the internal hash table structure and collision details.

- **Performance Comparison** -- Benchmark hash table O(1) average lookup
  against list O(n) linear search at different data sizes (N). Compares
  Python's built-in dict, a custom chaining hash table, and a plain list.
  Visualizes speedup growth as N increases.

## API Endpoints

| Method | Path                      | Description                              |
|--------|---------------------------|------------------------------------------|
| POST   | `/api/hashtable/init`     | Initialize a hash table for visualization |
| POST   | `/api/hashtable/op`       | Insert, search, or delete a key          |
| POST   | `/api/hashtable/compare`  | Compare chaining vs linear probing       |
| POST   | `/api/hashtable/hash`     | Show hash computation for a key          |
| POST   | `/api/phonebook/init`     | Initialize a new phone book              |
| POST   | `/api/phonebook/op`       | Add, look up, remove, or list contacts   |
| POST   | `/api/phonebook/preset`   | Load preset contacts                     |
| POST   | `/api/performance/compare`| Benchmark hash table vs list search      |

## Project Structure

```
project/
  app.py              # FastAPI backend (hash table implementations + API)
  static/
    index.html        # Main single-page HTML with four tabs
    style.css         # Stylesheet
    app.js            # Frontend logic (API calls, DOM rendering)
  README.md           # This file
```
