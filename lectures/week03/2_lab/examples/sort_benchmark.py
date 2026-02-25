"""Benchmark all sorting algorithms."""
import time
import random
from basic_sorts import selection_sort, bubble_sort, insertion_sort
from advanced_sorts import merge_sort, quick_sort

try:
    import matplotlib.pyplot as plt
    HAS_MATPLOTLIB = True
except ImportError:
    HAS_MATPLOTLIB = False


def measure(func, data, repeat=1):
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        func(data)
        end = time.perf_counter()
        times.append(end - start)
    return sum(times) / len(times)


if __name__ == "__main__":
    sizes = [100, 500, 1000, 5000, 10000]
    algorithms = {
        "Selection": selection_sort,
        "Bubble": bubble_sort,
        "Insertion": insertion_sort,
        "Merge": merge_sort,
        "Quick": quick_sort,
        "Python sorted()": sorted,
    }
    results = {name: [] for name in algorithms}

    for n in sizes:
        data = [random.randint(1, 100000) for _ in range(n)]
        print(f"\nN = {n:,}")
        for name, func in algorithms.items():
            if n > 5000 and name in ("Selection", "Bubble"):
                results[name].append(None)
                print(f"  {name:>15}: skipped (too slow)")
                continue
            t = measure(func, data)
            results[name].append(t)
            print(f"  {name:>15}: {t:.6f} sec")

    if HAS_MATPLOTLIB:
        plt.figure(figsize=(10, 6))
        for name, times in results.items():
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
