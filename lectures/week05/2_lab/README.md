# Week 05 Lab — Greedy Algorithms

## Objectives
- Experimentally verify the success and failure conditions of greedy algorithms.
- Experience how greedy strategies are applied to real scheduling problems.

---

## Type A — Algorithm Implementation

### A-1: Coin Change (10 min)

Run `examples/skeletons/a1_coin_change.py` to observe cases where the greedy algorithm succeeds and fails.

- Success case: coins = [500, 100, 50, 10]
- Failure case: coins = [1, 3, 4], amount = 6

### A-2: Fractional Knapsack (10 min)

Solve the fractional knapsack problem using a greedy approach in `examples/skeletons/a2_fractional_knapsack.py`.

- Sort by unit value (value/weight) and make greedy selections

### A-3: Huffman Coding (15 min)

Implement Huffman coding in `examples/skeletons/a3_huffman.py`.

- Build a tree based on character frequencies
- Verify encoding and decoding

---

## Type B — Web Code Analysis

### B-1: Meeting Room Reservation System (15 min)

Run the Flask app in `examples/b1_web_scheduler/`:

```bash
cd examples/b1_web_scheduler
python app.py
```

Analyze the scheduler that uses the Activity Selection algorithm.
- Determine the maximum number of meetings that can be scheduled from a list of meeting requests
- Think about why the greedy strategy (sorting by end time) is optimal
