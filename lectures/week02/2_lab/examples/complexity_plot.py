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
    """O(1): Access first element."""
    return arr[0] if arr else None


def o_n(arr):
    """O(n): Sum all elements."""
    total = 0
    for x in arr:
        total += x
    return total


def o_n_log_n(arr):
    """O(n log n): Sort the array."""
    return sorted(arr)


def o_n_squared(arr):
    """O(n^2): Nested loop."""
    n = len(arr)
    count = 0
    for i in range(n):
        for j in range(n):
            count += 1
    return count


def measure(func, arr, repeat=3):
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(arr)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


if __name__ == "__main__":
    sizes = [100, 500, 1000, 2000, 5000, 10000]
    results = {"O(1)": [], "O(n)": [], "O(n log n)": [], "O(n²)": []}

    for n in sizes:
        data = [random.randint(1, 1000) for _ in range(n)]
        results["O(1)"].append(measure(o_1, data))
        results["O(n)"].append(measure(o_n, data))
        results["O(n log n)"].append(measure(o_n_log_n, data))
        results["O(n²)"].append(measure(o_n_squared, data))
        print(f"N={n:>6}: O(1)={results['O(1)'][-1]:.6f}, O(n)={results['O(n)'][-1]:.6f}, "
              f"O(n log n)={results['O(n log n)'][-1]:.6f}, O(n²)={results['O(n²)'][-1]:.6f}")

    if HAS_MATPLOTLIB:
        plt.figure(figsize=(10, 6))
        for label, times in results.items():
            plt.plot(sizes, times, marker='o', label=label)
        plt.xlabel("Input Size (N)")
        plt.ylabel("Time (seconds)")
        plt.title("Execution Time by Complexity Class")
        plt.legend()
        plt.grid(True)
        plt.savefig("complexity_plot.png", dpi=150)
        plt.show()
        print("Graph saved as complexity_plot.png")
