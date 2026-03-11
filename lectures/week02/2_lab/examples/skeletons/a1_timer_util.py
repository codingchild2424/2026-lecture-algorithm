# === A-1: Timer Utility ===
# A utility module for precisely measuring function execution time.
# Uses time.perf_counter() for high-resolution timing.
# Runs multiple iterations and computes the average to reduce measurement error.
"""Timer utility for measuring execution time."""
import time


def measure_time(func, *args, repeat=3):
    """
    Repeatedly measures a function's execution time and returns the average.

    Parameters:
      func   — the function to measure
      *args  — arguments to pass to func
      repeat — number of measurement iterations (default: 3)

    Returns: (average_time_in_seconds, last_execution_result) tuple

    Algorithm:
      1. Execute func(*args) `repeat` times
      2. Record the elapsed time for each execution
      3. Return the average time and the last result

    Time complexity: O(repeat * T(func)) — proportional to func's time complexity
    Space complexity: O(repeat) — list storing each execution time
    """
    # TODO: Create a list to store execution times for each iteration
    # TODO: Loop `repeat` times:
    #   - Record start time using time.perf_counter()
    #   - Execute func(*args) and save the result
    #   - Record end time using time.perf_counter()
    #   - Append (end - start) to the times list
    # TODO: Compute the average of all recorded times
    # TODO: Return (average_time, result) as a tuple
    pass  # TODO: implement


if __name__ == "__main__":
    import random

    # Test function: sum all elements in an array — O(n)
    def sum_list(arr):
        total = 0
        for x in arr:
            total += x
        return total

    # Increase input size (N) and observe how execution time changes
    # If time increases ~10x when N increases 10x, it confirms O(n)
    for n in [1000, 10000, 100000, 1000000]:
        data = [random.randint(1, 100) for _ in range(n)]  # generate random test data
        result = measure_time(sum_list, data)  # measure execution time
        if result is not None:
            elapsed, _ = result
            print(f"N={n:>10,}: {elapsed:.6f} sec")
        else:
            print(f"N={n:>10,}: measure_time not yet implemented")
