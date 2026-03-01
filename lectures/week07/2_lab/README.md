# Week 07 Lab — Midterm Exam Preparation

## Learning Objectives

- Prepare for the midterm by solving past exam-style problems hands-on
- Develop the ability to identify the appropriate algorithm paradigm for a given problem
- Review the key algorithms from Weeks 02 through 06

## Lab Structure (50 min)

| Order | Exercise | Time | File |
|-------|----------|------|------|
| Ex 1 | Solving past exam-style problems with an AI agent | 20 min | (using an agent) |
| Ex 2 | Algorithm paradigm identification practice | 15 min | `examples/paradigm_practice.py` |
| Ex 3 | First-half algorithm review & code review | 15 min | `examples/review_problems.py` |

---

## Ex 1: Solving Past Exam-Style Problems with an AI Agent (20 min)

### Objective
Work with an AI agent (e.g., Claude) to solve problems of the type that may appear on the midterm.

### How to Proceed
1. Ask the agent something like:
   - "Give me a midterm-style algorithm problem"
   - Scope: complexity analysis, sorting, divide and conquer, greedy, DP
2. When you receive a problem, try solving it on your own first (5 min)
3. Have the agent check your solution
4. If incorrect, get a hint and try again
5. Repeat for 2-3 problems

### Recommended Prompt Example
```
"Give me an algorithm problem from the Week 02-06 scope that could appear on the midterm.
Please cover a mix of: complexity analysis, sorting, divide and conquer, greedy, and DP.
After giving the problem, please grade my solution when I submit it."
```

---

## Ex 2: Algorithm Paradigm Identification Practice (15 min)

### Objective
Develop the ability to read a problem and determine which algorithm paradigm
(divide and conquer / greedy / DP / brute force) should be applied.

### How to Proceed
1. Open `examples/paradigm_practice.py` and read the 10 problems
2. For each problem, think about which paradigm to use
3. Briefly note your reasoning
4. Compare with the answers and explanations at the bottom of the file

### Key Identification Criteria
| Paradigm | Key Characteristics |
|----------|---------------------|
| Brute Force | Explores all possibilities; suitable when constraints are small |
| Divide and Conquer | Splits the problem into independent subproblems to solve |
| Greedy | Makes the best choice at each step; greedy choice property |
| DP | Optimal substructure + overlapping subproblems |

---

## Ex 3: First-Half Algorithm Review & Code Review (15 min)

### Objective
Review the key algorithms from Weeks 02-06 through 5 mini problems.

### How to Proceed
1. Open `examples/review_problems.py` and check the 5 problems
2. Implement each skeleton function yourself
3. Compare your solution with the provided solution after completing it
4. If short on time, simply reading and understanding the solutions is still an effective review

### Problem Breakdown
| # | Topic | Related Week |
|---|-------|--------------|
| 1 | Complexity Analysis | Week 02 |
| 2 | Sorting Applications | Week 03 |
| 3 | Divide and Conquer | Week 04 |
| 4 | Greedy | Week 05 |
| 5 | DP | Week 06 |

---

## How to Run

```bash
python examples/paradigm_practice.py
python examples/review_problems.py
```
