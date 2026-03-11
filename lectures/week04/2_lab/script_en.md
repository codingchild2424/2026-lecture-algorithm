# Week 04 Lab -- Instructor Script (Advanced Divide and Conquer)

## Pre-class Preparation (5 minutes before class)

- [ ] Check classroom Wi-Fi
- [ ] Verify Python 3.x and `matplotlib` are installed on student machines
- [ ] Open `examples/a1_merge_sort_trace.py`, `examples/a2_kth_smallest.py`, and `examples/a3_closest_pair.py` on the projector
- [ ] Test the Flask app in `examples/b1_web_autocomplete/` runs correctly
- [ ] Prepare a whiteboard diagram showing recursive call tree for Merge Sort

---

## Introduction (3 min)

> "Last week we implemented sorting algorithms. Today we go deeper into divide and conquer. You will trace the recursive call tree of Merge Sort to understand how it splits and merges. Then you will implement the Randomized Select algorithm to find the k-th smallest element in expected O(n) time. After that, you will solve the Closest Pair of Points problem -- comparing brute force O(n^2) with divide and conquer O(n log n). Finally, we will see how divide and conquer powers autocomplete in a web application."

---

## Type A -- Algorithm Implementation

### A-1: Merge Sort Tracing (10 min)

#### How to Proceed

1. **Brief Intro (2 min):**
   > "Open `examples/a1_merge_sort_trace.py`. This is not about implementing Merge Sort -- you already did that last week. This time, the code prints the recursive call tree so you can see exactly how the array is split and how the halves are merged back together at each level. Run it and study the output."

2. **Student Practice (6 min):**
   - Students run the script with the provided sample array.
   - Observe the output: each recursive call shows the sub-array being processed.
   - Students trace the depth of recursion and count the number of merge operations.
   - Encourage students to try different input arrays (sorted, reverse-sorted, random) and see if the call tree structure changes.

3. **Checkpoint (2 min):**
   > "The call tree always has log n levels, regardless of the input. At each level, every element is involved in exactly one merge. That gives us n work per level times log n levels -- O(n log n) total. Seeing this structure makes the complexity analysis concrete."

---

### A-2: Finding the k-th Smallest Element (15 min)

#### How to Proceed

1. **Brief Intro (3 min):**
   > "Open `examples/a2_kth_smallest.py`. The problem: given an unsorted array, find the k-th smallest element. You could sort the array in O(n log n), but there is a better way. The Randomized Select algorithm uses the partition step from Quick Sort to narrow down the search to one side of the pivot. On average, this runs in O(n) time. Implement the algorithm."

2. **Student Practice (10 min):**
   - Students implement the partition function (reuse from Quick Sort if available).
   - Students implement Randomized Select: pick a random pivot, partition, then recurse on the appropriate side.
   - Key insight: unlike Quick Sort, we only recurse on ONE side -- this is why it is O(n) on average instead of O(n log n).
   - Test with examples: find the 1st smallest (minimum), the n-th smallest (maximum), and the median.

3. **Checkpoint (2 min):**
   > "The trick is that we only recurse on the side where the k-th element must be. If the pivot ends up at position p and k equals p, we are done. If k is less than p, recurse left. If k is greater than p, recurse right. This halving of the problem on average gives us O(n) expected time -- much faster than sorting."

---

### A-3: Closest Pair of Points (10 min)

#### How to Proceed

1. **Brief Intro (2 min):**
   > "Open `examples/a3_closest_pair.py`. Given n points in 2D space, find the pair with the smallest distance between them. The brute force approach checks all pairs -- that is O(n^2). The divide and conquer approach splits the points by x-coordinate, solves each half recursively, then handles the boundary strip. This achieves O(n log n). The code has both implementations -- run them and compare."

2. **Student Practice (6 min):**
   - Students run both the brute force and divide-and-conquer versions.
   - Compare execution times at various N values (100, 1,000, 10,000).
   - Study the boundary strip logic: only points within distance d of the dividing line need cross-half comparison.
   - This is the hardest part conceptually -- walk around and help students who are stuck.

3. **Checkpoint (2 min):**
   > "The brute force is straightforward but slow. The divide and conquer version is elegant: split, solve each half, then only check points near the boundary. The boundary strip is the key insight -- at most 6 points need to be checked for each point in the strip. Without this optimization, the combine step would be O(n^2) and we would gain nothing."

---

## Type B -- Web Code Analysis

### B-1: Autocomplete API (15 min)

#### How to Proceed

1. **Brief Intro (3 min):**
   > "Autocomplete is something you use every day -- type a few characters and get suggestions. Open the Flask app in `examples/b1_web_autocomplete/`. It has a dictionary of 100,000 words and two search strategies. The first scans every word sequentially. The second uses a sorted array with binary search to find the prefix range. Start the server and type characters to feel the difference."

   Show students how to start the server:
   ```
   cd examples/b1_web_autocomplete
   python app.py
   ```

2. **Student Practice (9 min):**
   - Students start the Flask server and query both endpoints:
     - `GET /autocomplete/linear?q=pre` -- Sequential search through all words
     - `GET /autocomplete/binary?q=pre` -- Sorted array + binary search for prefix range
   - Type progressively longer prefixes (e.g., "p", "pr", "pre", "pres") and compare response times.
   - Notice how the linear approach slows down while binary search stays consistently fast.
   - Discussion: Why does binary search work for prefix matching on a sorted array?

3. **Checkpoint (3 min):**
   > "In a sorted dictionary, all words starting with 'pre' are contiguous. Binary search finds the first and last position of that prefix range in O(log n) time. The linear approach must scan all 100,000 words every time -- O(n). For autocomplete, which fires on every keystroke, the difference is critical. This is divide and conquer in action: binary search repeatedly halves the search space."

---

## Wrap-up (2 min)

> "Today you traced Merge Sort's recursive structure, implemented Randomized Select for O(n) element finding, compared brute force versus divide and conquer for closest pair, and saw binary search powering autocomplete. The common thread: divide and conquer breaks problems into smaller pieces, solves them independently, and combines the results. It is one of the most powerful algorithmic paradigms you will use. Check ../3_assignment/README.md for this week's Baekjoon practice problems."

### Checklist
- Confirm students understand the recursive call tree structure of Merge Sort
- Ensure students have a working Randomized Select implementation
- Verify students observed the performance difference in the autocomplete demo
- Remind students to complete the Baekjoon homework before next week
