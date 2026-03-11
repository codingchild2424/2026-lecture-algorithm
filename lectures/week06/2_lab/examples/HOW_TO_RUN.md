# Week 06 Lab Examples - How to Run

## Directory Structure

```
examples/
  a1_fibonacci.py              # Skeleton - implement memoization & tabulation
  a1_fibonacci_comparison.py   # Complete demo - benchmark & call count analysis
  a2_lcs.py                    # Skeleton - implement LCS DP table & backtracking
  a3_knapsack.py               # Skeleton - implement 0-1 knapsack DP
  a3_knapsack_01.py            # Complete demo - DP table visualization & greedy comparison
  b1_web_diff/                 # Web demo (run separately)
  solutions/                   # Complete solutions for all skeleton files
```

## Running the Examples

All examples run as standalone Python scripts with no external dependencies.

```bash
# Fibonacci - skeleton (implement TODO sections first)
python a1_fibonacci.py

# Fibonacci - detailed benchmark demo (complete, runs as-is)
python a1_fibonacci_comparison.py

# LCS - skeleton (implement TODO sections first)
python a2_lcs.py

# Knapsack - skeleton (implement TODO sections first)
python a3_knapsack.py

# Knapsack - detailed visualization demo (complete, runs as-is)
python a3_knapsack_01.py
```

## Workflow

1. Open the skeleton file (e.g., `a1_fibonacci.py`)
2. Read the docstrings, comments, and TODO hints
3. Implement the function bodies where you see `# TODO`
4. Run the script to verify your implementation
5. If stuck, check the corresponding file in `solutions/`

## Skeleton Files (implement these)

| File | Functions to Implement |
|------|----------------------|
| `a1_fibonacci.py` | `fib_memo()`, `fib_tab()` |
| `a2_lcs.py` | `build_lcs_table()`, `backtrack_lcs()` |
| `a3_knapsack.py` | `knapsack_01()` (DP table fill + backtracking) |

## Complete Demos (run as-is for reference)

| File | Description |
|------|-------------|
| `a1_fibonacci_comparison.py` | Benchmark naive vs memo vs tabulation with call counts |
| `a3_knapsack_01.py` | DP table visualization, backtracking walkthrough, greedy vs DP |
