# === A-3: Execution Time Visualization by Complexity Class ===
# Measures and plots execution times for four complexity classes
# — O(1), O(n), O(n log n), O(n^2) — as input size (N) varies.
#
# This experiment shows how theoretical complexity translates to actual execution time.
"""Plot execution times for different complexity classes."""
import time
import random
import math

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False
    print("matplotlib not installed. Install with: pip install matplotlib")


def o_1(arr):
    """
    O(1) — constant time: accesses the first element of the array.
    Takes the same amount of time regardless of input size.
    """
    return arr[0] if arr else None


def o_n(arr):
    """
    O(n) — linear time: iterates through all elements to compute the sum.
    Time increases proportionally to input size.
    """
    total = 0
    for x in arr:  # visit each element once
        total += x
    return total


def o_n_log_n(arr):
    """
    O(n log n) — linearithmic time: sorts the array.
    Python's Timsort guarantees O(n log n).
    """
    return sorted(arr)


def o_n_squared(arr):
    """
    O(n^2) — quadratic time: nested loops performing n*n operations.
    When input size doubles, time increases ~4x.
    """
    n = len(arr)
    count = 0
    for i in range(n):  # outer loop: n times
        for j in range(n):  # inner loop: n times — total n^2 iterations
            count += 1
    return count


def measure(func, arr, repeat=3):
    """
    Repeatedly measures a function's execution time and returns the average.

    Time complexity: O(repeat * T(func))
    """
    times = []
    for _ in range(repeat):
        start = time.perf_counter()  # high-resolution start time
        func(arr)
        end = time.perf_counter()  # high-resolution end time
        times.append(end - start)
    return sum(times) / len(times)  # return average execution time


if __name__ == "__main__":
    sizes = [100, 500, 1000, 2000, 5000, 10000]  # input sizes to test
    results = {"O(1)": [], "O(n)": [], "O(n log n)": [], "O(n²)": []}  # dictionary to store results

    # Measure execution time for all four complexity classes at each input size
    for n in sizes:
        data = [random.randint(1, 1000) for _ in range(n)]  # generate random test data
        results["O(1)"].append(measure(o_1, data))  # measure constant time
        results["O(n)"].append(measure(o_n, data))  # measure linear time
        results["O(n log n)"].append(measure(o_n_log_n, data))  # measure linearithmic time
        results["O(n²)"].append(measure(o_n_squared, data))  # measure quadratic time
        print(f"N={n:>6}: O(1)={results['O(1)'][-1]:.6f}, O(n)={results['O(n)'][-1]:.6f}, "
              f"O(n log n)={results['O(n log n)'][-1]:.6f}, O(n²)={results['O(n²)'][-1]:.6f}")

    # Generate graph if matplotlib is installed
    if HAS_MATPLOTLIB:
        plt.figure(figsize=(10, 6))
        for label, times in results.items():  # plot a line for each complexity class
            plt.plot(sizes, times, marker='o', label=label)
        plt.xlabel("Input Size (N)")  # x-axis: input size
        plt.ylabel("Time (seconds)")  # y-axis: execution time
        plt.title("Execution Time by Complexity Class")  # graph title
        plt.legend()  # show legend
        plt.grid(True)  # show grid
        plt.savefig("complexity_plot.png", dpi=150)  # save graph as image
        plt.show()
        print("Graph saved as complexity_plot.png")
