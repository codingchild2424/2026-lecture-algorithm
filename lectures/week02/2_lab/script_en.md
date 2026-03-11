# Week 02 Lab -- Instructor Script (Complexity Analysis Practice)

## Pre-class Preparation (5 minutes before class)

- [ ] Check classroom Wi-Fi
- [ ] Verify Python 3.x and `matplotlib` are installed on student machines
- [ ] Open `examples/a1_timer_util.py`, `examples/a2_find_duplicate.py`, and `examples/a3_complexity_plot.py` on the projector
- [ ] Test the Flask app in `examples/b1_web_search/` runs correctly
- [ ] Prepare a whiteboard summary of O(1), O(n), O(n log n), O(n^2)

---

## Introduction (3 min)

> "Today we move from theory to practice. In the lecture, we learned about Big-O notation and analyzed complexities on paper. Now we will actually measure execution times and see how different complexities behave as input size grows. You will build a timing utility, optimize a duplicate-finding algorithm from O(n^2) to O(n), plot complexity curves, and finally see how algorithm choice affects real API response times."

---

## Type A -- Algorithm Implementation

### A-1: Write a Timing Utility (10 min)

#### How to Proceed

1. **Brief Intro (2 min):**
   > "Before we can compare algorithms, we need a way to measure them. Open `examples/a1_timer_util.py`. This file provides a skeleton for a utility that wraps any function call and reports how long it took. You will use Python's `time.perf_counter()` to capture start and end times."

2. **Student Practice (6 min):**
   - Students open `examples/a1_timer_util.py` and fill in the timing logic.
   - The utility should accept a function and its arguments, run it, and print the elapsed time.
   - Encourage students to test it with a simple function like summing a list.

3. **Checkpoint (2 min):**
   > "Your timer should print something like 'Elapsed: 0.00234s'. This utility is the foundation for everything we do today -- we will reuse it in the next two exercises. If yours is working, move on to A-2."

---

### A-2: Finding Duplicates -- O(n^2) to O(n) (15 min)

#### How to Proceed

1. **Brief Intro (3 min):**
   > "Open `examples/a2_find_duplicate.py`. The problem is simple: given an array of integers, determine whether it contains any duplicates. There are two approaches here. The first uses nested for loops to compare every pair -- that is O(n^2). The second uses a hash set to track what we have seen -- that is O(n). Implement both and measure them."

2. **Student Practice (9 min):**
   - Students implement the brute-force O(n^2) solution with nested loops.
   - Students implement the O(n) solution using a Python `set`.
   - Using the timer utility from A-1, students compare execution times at N=100, 1,000, 10,000, and 50,000.
   - Encourage students to record results in a table.

3. **Checkpoint (3 min):**
   > "At N=100, both approaches are fast. But at N=50,000, the O(n^2) version takes noticeably longer -- possibly several seconds -- while the set-based version finishes instantly. This is Big-O in action. The theoretical difference we discussed in lecture is now a real, measurable difference."

---

### A-3: Execution Time Graphs (10 min)

#### How to Proceed

1. **Brief Intro (2 min):**
   > "Now let us visualize complexity. Run `examples/a3_complexity_plot.py`. This script generates graphs for O(1), O(n), O(n log n), and O(n^2) by running dummy workloads at various input sizes and plotting the results with matplotlib."

2. **Student Practice (6 min):**
   - Students run the script and observe the generated plot.
   - Ask students to identify which curve is which from the shape alone.
   - Optionally, students modify the script to add an O(n^3) curve or adjust the range of N values.

3. **Checkpoint (2 min):**
   > "Notice how O(n^2) curves upward dramatically while O(n) and O(n log n) stay relatively flat at smaller scales. The visual makes it clear why algorithm choice matters -- and it only gets worse as N increases. Keep this image in mind whenever you analyze complexity."

---

## Type B -- Web Code Analysis

### B-1: Product Search API Comparison (15 min)

#### How to Proceed

1. **Brief Intro (3 min):**
   > "Now let us see how complexity affects a real web application. In `examples/b1_web_search/`, there is a Flask app with two search endpoints. One performs linear search -- scanning every product until it finds a match. The other uses binary search on a sorted list. Start the server and test both endpoints."

   Show students how to start the server:
   ```
   cd examples/b1_web_search
   pip install flask
   python app.py
   ```

2. **Student Practice (9 min):**
   - Students start the Flask server and query both endpoints:
     - `GET /search/linear?q=product_name` -- Linear search O(n)
     - `GET /search/binary?q=product_name` -- Binary search O(log n)
   - Students test with N=100, 10,000, and 1,000,000 products and record the response times.
   - Discuss: How does the response time gap change as N grows?

3. **Checkpoint (3 min):**
   > "With 100 products, both endpoints respond almost identically. With 1,000,000 products, the linear search endpoint becomes noticeably slower while binary search remains nearly instant. This is exactly the difference between O(n) and O(log n). In a production system, this could mean the difference between a responsive app and a frustrated user."

---

## Wrap-up (2 min)

> "Today you measured complexity with real code, not just formulas. You built a timer, optimized an algorithm from O(n^2) to O(n), visualized complexity curves, and saw how search algorithms affect API response times. The takeaway: algorithm choice is not academic -- it has real, measurable consequences. Check ../3_assignment/README.md for this week's assignment details."

### Coming up -- Week 3 Lab
**Sorting Algorithm Implementation & Benchmark**

### Checklist
- Confirm students can explain why the set-based duplicate check is faster
- Ensure students observed the performance gap in the web search API
- Remind students to complete Homework 1 before next week
