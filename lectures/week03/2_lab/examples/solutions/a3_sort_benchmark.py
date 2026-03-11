# === A-3: Sorting Algorithm Benchmark ===
# Compare execution times of basic sorts (O(n^2)) and advanced sorts (O(n log n))
# Visually observe performance differences by input size
"""Benchmark all sorting algorithms."""
import time
import random
from a1_basic_sorts import selection_sort, bubble_sort, insertion_sort
from a2_advanced_sorts import merge_sort, quick_sort

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


def measure(func, data, repeat=1):
    """
    Measure the execution time of a sorting function.
    - func: sorting function to measure
    - data: input data
    - repeat: number of repetitions (for computing the average)
    - Returns: average execution time (seconds)
    - Uses perf_counter() for high-precision time measurement
    """
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)  # Return average execution time


if __name__ == "__main__":
    # List of input sizes to test
    sizes = [100, 500, 1000, 5000, 10000]
    algorithms = {
        "Selection": selection_sort,
        "Bubble": bubble_sort,
        "Insertion": insertion_sort,
        "Merge": merge_sort,
        "Quick": quick_sort,
        "Python sorted()": sorted,  # Python built-in sort (Timsort, O(n log n))
    }
    results = {name: [] for name in algorithms}

    for n in sizes:
        # Compare all algorithms using the same random data
        data = [random.randint(1, 100000) for _ in range(n)]
        print(f"\nN = {n:,}")
        for name, func in algorithms.items():
            # Skip O(n^2) algorithms for large inputs as they are too slow
            if n > 5000 and name in ("Selection", "Bubble"):
                results[name].append(None)
                print(f"  {name:>15}: skipped (too slow)")
                continue
            t = measure(func, data)
            results[name].append(t)
            print(f"  {name:>15}: {t:.6f} sec")

    # If matplotlib is installed, visualize the results as a graph
    if HAS_MATPLOTLIB:
        plt.figure(figsize=(10, 6))
        for name, times in results.items():
            # Plot only valid data, excluding None (skipped results)
            valid = [(s, t) for s, t in zip(sizes, times) if t is not None]
            if valid:
                ss, ts = zip(*valid)
                plt.plot(ss, ts, marker='o', label=name)
        plt.xlabel("Input Size (N)")
        plt.ylabel("Time (seconds)")
        plt.title("Sorting Algorithm Benchmark")
        plt.legend()
        plt.grid(True)
        plt.savefig("sort_benchmark.png", dpi=150)
        plt.show()
