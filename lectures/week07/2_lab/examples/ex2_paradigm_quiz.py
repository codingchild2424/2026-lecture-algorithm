# === Ex 2: Algorithm Paradigm Identification Quiz ===
# Week 07 Midterm Review - Interactive quiz format for paradigm identification practice
# A quiz selecting one of 4 paradigms (BF, D&C, Greedy, DP) for each of 10 problems
"""Algorithm Paradigm Quiz - identify the best approach for each problem."""

# PROBLEMS list: 10 quiz problems
# Each problem contains question (problem description), answer (correct paradigm), and explanation
PROBLEMS = [
    {
        # Binary search - divide and conquer since we split a sorted array in half to search
        "question": "Find the position of a specific value in a sorted array.",
        "answer": "Divide & Conquer",
        "explanation": "Binary search -- split the array in half to search. O(log n)"
    },
    {
        # Change making - greedy is optimal for Korean/US currency since denominations are multiples
        "question": "Given coin denominations [1, 5, 10, 50, 100, 500], find the minimum number of coins for change.",
        "answer": "Greedy",
        "explanation": "Use the largest coins first -- greedy is optimal when denominations are multiples (as in Korean/US currency)."
    },
    {
        # LCS - overlapping subproblems + optimal substructure -> DP
        "question": "Find the length of the longest common subsequence (LCS) of two strings.",
        "answer": "Dynamic Programming",
        "explanation": "Subproblems overlap and optimal substructure exists -- solve with a DP table in O(mn)."
    },
    {
        # Closest pair of points - divide by x-coordinate then handle boundary -> divide and conquer
        "question": "Find the distance between the closest pair among n points.",
        "answer": "Divide & Conquer",
        "explanation": "Divide points by x-coordinate, find closest pair in each half, and check the boundary. O(n log n)"
    },
    {
        # Activity Selection - sort by end time then greedily select
        "question": "Select the maximum number of non-overlapping activities from n activities.",
        "answer": "Greedy",
        "explanation": "Sort by end time, then greedily select -- Activity Selection Problem."
    },
    {
        # 0-1 Knapsack - items cannot be split, so DP (fractional would be greedy)
        "question": "Given n items (each with weight and value), maximize value within knapsack capacity W. (Items cannot be split.)",
        "answer": "Dynamic Programming",
        "explanation": "0-1 Knapsack -- the choice to include or exclude each item creates overlapping subproblems."
    },
    {
        # Subset enumeration - must generate all 2^n subsets, so brute force
        "question": "Print all subsets of an array.",
        "answer": "Brute Force",
        "explanation": "Must generate all 2^n subsets -- no room for optimization."
    },
    {
        # Matrix multiplication - Strassen algorithm divides into quadrants for divide and conquer
        "question": "Multiply two n*n matrices. (n is very large.)",
        "answer": "Divide & Conquer",
        "explanation": "Strassen algorithm -- divide matrices into quadrants and solve with 7 multiplications. O(n^2.81)"
    },
    {
        # Huffman coding - greedy by merging lowest-frequency characters first
        "question": "Compress a string using Huffman codes.",
        "answer": "Greedy",
        "explanation": "The greedy choice of merging lowest-frequency characters first is optimal."
    },
    {
        # Fibonacci - fib(n) = fib(n-1) + fib(n-2), a classic example of overlapping subproblems
        "question": "Find the n-th term of the Fibonacci sequence.",
        "answer": "Dynamic Programming",
        "explanation": "fib(n) = fib(n-1) + fib(n-2) -- a classic example of overlapping subproblems."
    },
]


def run_quiz():
    """Run the interactive quiz.

    How it works:
    1. Display each problem in order and show 4 choices
    2. Accept user input (1-4) and compare with the correct answer
    3. If correct, increase the score; if wrong, show the correct answer and explanation
    4. After all problems, display the final score

    Time complexity: O(n) - n is the number of problems (fixed at 10)
    """
    score = 0
    options = ["Brute Force", "Divide & Conquer", "Greedy", "Dynamic Programming"]

    for i, problem in enumerate(PROBLEMS, 1):
        print(f"\n{'='*60}")
        print(f"Problem {i}: {problem['question']}")
        print()
        # Display 4 paradigm choices with numbers
        for j, opt in enumerate(options, 1):
            print(f"  {j}. {opt}")

        try:
            choice = int(input("\nAnswer (1-4): "))
            chosen = options[choice - 1]  # Convert 1-based index to 0-based
        except (ValueError, IndexError):
            chosen = ""  # Handle invalid input

        # Compare answer and display result
        if chosen == problem["answer"]:
            print(f"  Correct! -- {problem['explanation']}")
            score += 1
        else:
            print(f"  Wrong. Answer: {problem['answer']}")
            print(f"    {problem['explanation']}")

    # Display final score
    print(f"\n{'='*60}")
    print(f"Result: {score}/{len(PROBLEMS)}")


if __name__ == "__main__":
    print("=== Algorithm Paradigm Identification Quiz ===")
    print("Choose the most appropriate algorithm paradigm for each problem.\n")
    run_quiz()
