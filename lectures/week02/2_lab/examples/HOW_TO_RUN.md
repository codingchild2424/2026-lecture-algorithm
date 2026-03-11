# Week 02 Lab Examples

## Exercises

### A-1: Timer Utility (`a1_timer_util.py`)
A utility module that measures function execution time using `time.perf_counter()`.
Implement the `measure_time()` function that runs a function multiple times and returns the average elapsed time.

```bash
python3 a1_timer_util.py
```

**Expected output:** A table showing execution times for summing arrays of increasing size (N=1,000 to 1,000,000). Times should increase roughly linearly with N.

---

### A-2: Duplicate Detection (`a2_find_duplicate.py`)
Implement two algorithms to check whether an array contains any duplicate element:
- `has_duplicate_bruteforce()` — O(n^2) nested loop approach
- `has_duplicate_hashset()` — O(n) hash set approach

```bash
python3 a2_find_duplicate.py
```

**Expected output:** A benchmark table comparing O(n^2) vs O(n) execution times. The speedup column shows how much faster the hash set approach is.

> **Note:** The n=50,000 brute-force case may take several minutes.

---

### A-2: Find All Duplicates (`a2_find_duplicates.py`)
Similar to above, but returns the *set of all duplicate elements* instead of just True/False:
- `find_duplicates_bruteforce()` — O(n^2) nested loop approach
- `find_duplicates_hashset()` — O(n) two-set approach

```bash
python3 a2_find_duplicates.py
```

**Expected output:** First a correctness check (both methods should find `{1, 2}` in the test array), then a benchmark table.

---

### A-3: Complexity Plot (`a3_complexity_plot.py`)
Demo script (no implementation needed). Measures and plots execution times for O(1), O(n), O(n log n), and O(n^2) as input size varies.

```bash
python3 a3_complexity_plot.py
```

**Expected output:** A table of execution times per complexity class, plus a saved `complexity_plot.png` graph (requires `matplotlib`: `pip install matplotlib`).

---

### B-1: Web Search Demo (`solutions/b1_web_search/`)
A web application demo. See the README inside the directory for instructions.

---

## Solutions

Complete solution code is available in the `solutions/` subdirectory.
