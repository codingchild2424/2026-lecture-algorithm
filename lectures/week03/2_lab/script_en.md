# Week 03 Lab -- Instructor Script (Sorting Algorithm Implementation & Benchmark)

## Pre-class Preparation (5 minutes before class)

- [ ] Check classroom Wi-Fi
- [ ] Verify Python 3.x and `matplotlib` are installed on student machines
- [ ] Open `examples/a1_basic_sorts.py`, `examples/a2_advanced_sorts.py`, and `examples/a3_sort_benchmark.py` on the projector
- [ ] Test the Flask app in `examples/b1_web_sort/` runs correctly
- [ ] Prepare a whiteboard summary of O(n^2) sorts vs. O(n log n) sorts

---

## Introduction (3 min)

> "Last week we measured complexity. Today we implement sorting algorithms ourselves and see the performance differences firsthand. You will code Selection Sort, Bubble Sort, and Insertion Sort -- all O(n^2) -- then Merge Sort and Quick Sort -- both O(n log n). After that, we will benchmark them all side by side and see the crossover point where O(n^2) becomes unacceptable. Finally, you will experience this in a web application where sorting speed directly affects the user."

---

## Type A -- Algorithm Implementation

### A-1: Basic Sorting Implementation (10 min)

#### How to Proceed

1. **Brief Intro (2 min):**
   > "Open `examples/a1_basic_sorts.py`. There are three functions with TODOs: Selection Sort, Bubble Sort, and Insertion Sort. Each takes a list and returns a new sorted list. These are all O(n^2) algorithms -- simple to implement but slow on large inputs. Fill in the missing code and run the tests."

2. **Student Practice (6 min):**
   - Students implement Selection Sort: find the minimum, swap it to the front, repeat.
   - Students implement Bubble Sort: repeatedly compare adjacent elements and swap.
   - Students implement Insertion Sort: insert each element into its correct position in the sorted prefix.
   - Run `python examples/a1_basic_sorts.py` to verify correctness.

3. **Checkpoint (2 min):**
   > "All three algorithms should produce correct sorted output. If your tests pass, notice that they all have nested loops -- that is where the O(n^2) comes from. Among these three, Insertion Sort is typically fastest in practice on nearly-sorted data. Keep that in mind."

---

### A-2: Advanced Sorting Implementation (15 min)

#### How to Proceed

1. **Brief Intro (3 min):**
   > "Now open `examples/a2_advanced_sorts.py`. Here you will implement Merge Sort and Quick Sort. Both are O(n log n) on average, but they work very differently. Merge Sort divides the array in half, recursively sorts each half, then merges. Quick Sort picks a pivot, partitions around it, then recursively sorts each partition. Fill in the TODOs."

2. **Student Practice (10 min):**
   - Students implement Merge Sort: split, recurse, merge two sorted halves.
   - Students implement Quick Sort: choose pivot, partition, recurse on both sides.
   - Common stumbling point: the merge step in Merge Sort and the partition logic in Quick Sort.
   - Encourage students to trace through a small example (e.g., [3, 1, 4, 1, 5]) on paper.

3. **Checkpoint (2 min):**
   > "Merge Sort and Quick Sort should both produce correct sorted output. The key difference: Merge Sort always divides evenly so it is guaranteed O(n log n). Quick Sort depends on pivot choice -- worst case is O(n^2) but average case is O(n log n). In practice, Quick Sort is often faster due to better cache behavior."

---

### A-3: Benchmark (10 min)

#### How to Proceed

1. **Brief Intro (2 min):**
   > "Now we race them all. Run `examples/a3_sort_benchmark.py`. This script times every sorting algorithm you implemented at N=100, 1,000, 10,000, and 100,000, then generates comparison graphs."

2. **Student Practice (6 min):**
   - Students run `python examples/a3_sort_benchmark.py` and observe the output.
   - At N=100, all algorithms are fast. At N=10,000, the O(n^2) algorithms start struggling.
   - At N=100,000, Selection Sort and Bubble Sort may take tens of seconds while Merge Sort and Quick Sort finish in under a second.
   - Ask students: "At what N does the difference become noticeable?"

3. **Checkpoint (2 min):**
   > "The crossover point is usually around N=1,000 to N=10,000. Below that, the overhead of recursion in Merge Sort and Quick Sort can make them comparable to the simple sorts. Above that, O(n^2) becomes painfully slow. This is why choosing the right algorithm matters for real applications."

---

## Type B -- Web Code Analysis

### B-1: Mini Shopping Mall Sort Comparison (15 min)

#### How to Proceed

1. **Brief Intro (3 min):**
   > "Imagine you are building an online shopping mall and need to sort products by price. Open the Flask app in `examples/b1_web_sort/`. It has a web page with two buttons -- one sorts products using Bubble Sort, the other uses Quick Sort. Start the server and try both."

   Show students how to start the server:
   ```
   cd examples/b1_web_sort
   pip install flask
   python app.py
   ```

2. **Student Practice (9 min):**
   - Students open `http://localhost:5000` in the browser.
   - Click "Sort with Bubble Sort" and note the loading time.
   - Click "Sort with Quick Sort" and note the loading time.
   - Change the product count from 1,000 to 10,000 to 50,000 and feel the difference.
   - Discussion question: What would happen if a real online shopping mall used an O(n^2) sorting algorithm?

3. **Checkpoint (3 min):**
   > "At 1,000 products, both buttons respond quickly. At 50,000 products, Bubble Sort makes the page hang for several seconds while Quick Sort stays responsive. In a real shopping mall with millions of products, an O(n^2) sort would make the site unusable. This is why every major language and framework uses O(n log n) sorting algorithms internally."

---

## Wrap-up (2 min)

> "Today you implemented five sorting algorithms from scratch, benchmarked them, and saw the real-world impact in a web application. The key lesson: O(n^2) sorts are fine for small data but become a bottleneck as data grows. Always reach for O(n log n) sorts in production code. Check ../3_assignment/README.md for this week's Baekjoon practice problems."

### Checklist
- Confirm all students have working implementations of at least Merge Sort or Quick Sort
- Ensure students observed the performance crossover in the benchmark
- Ensure students experienced the web demo and understand the practical implications
- Remind students to complete the Baekjoon homework before next week
