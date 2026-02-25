"""Timer utility for measuring execution time."""
import time


def measure_time(func, *args, repeat=3):
    """Run func(*args) multiple times and return average time in seconds."""
    times = []
    for _ in range(repeat):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        times.append(end - start)
    avg = sum(times) / len(times)
    return avg, result


if __name__ == "__main__":
    import random

    def sum_list(arr):
        total = 0
        for x in arr:
            total += x
        return total

    for n in [1000, 10000, 100000, 1000000]:
        data = [random.randint(1, 100) for _ in range(n)]
        elapsed, _ = measure_time(sum_list, data)
        print(f"N={n:>10,}: {elapsed:.6f} sec")
