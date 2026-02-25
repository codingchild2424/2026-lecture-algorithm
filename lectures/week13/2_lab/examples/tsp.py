"""TSP - Brute force vs MST-based approximation."""
import itertools
import time
import math
import random


def tsp_bruteforce(dist_matrix):
    n = len(dist_matrix)
    cities = list(range(1, n))
    min_cost = float('inf')
    best_path = None
    for perm in itertools.permutations(cities):
        cost = dist_matrix[0][perm[0]]
        for i in range(len(perm) - 1):
            cost += dist_matrix[perm[i]][perm[i + 1]]
        cost += dist_matrix[perm[-1]][0]
        if cost < min_cost:
            min_cost = cost
            best_path = (0,) + perm + (0,)
    return min_cost, best_path


def tsp_mst_approx(dist_matrix):
    """MST-based 2-approximation for metric TSP."""
    n = len(dist_matrix)
    # Prim's MST
    in_mst = [False] * n
    in_mst[0] = True
    mst_edges = []
    adj = [[] for _ in range(n)]

    for _ in range(n - 1):
        min_edge = (float('inf'), -1, -1)
        for u in range(n):
            if not in_mst[u]:
                continue
            for v in range(n):
                if not in_mst[v] and dist_matrix[u][v] < min_edge[0]:
                    min_edge = (dist_matrix[u][v], u, v)
        _, u, v = min_edge
        in_mst[v] = True
        adj[u].append(v)
        adj[v].append(u)

    # DFS preorder traversal of MST
    visited = [False] * n
    tour = []
    def dfs(node):
        visited[node] = True
        tour.append(node)
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)
    dfs(0)
    tour.append(0)

    cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return cost, tuple(tour)


def generate_random_cities(n):
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            dist[i][j] = math.sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2)
    return dist


if __name__ == "__main__":
    # Show explosion of brute force
    print("=== TSP: Brute Force Execution Time ===")
    for n in [6, 8, 10, 11, 12]:
        dist = generate_random_cities(n)
        start = time.perf_counter()
        bf_cost, bf_path = tsp_bruteforce(dist)
        bf_time = time.perf_counter() - start

        start = time.perf_counter()
        approx_cost, approx_path = tsp_mst_approx(dist)
        approx_time = time.perf_counter() - start

        ratio = approx_cost / bf_cost
        print(f"N={n:2d}: BF={bf_time:8.3f}s (cost={bf_cost:.1f}), "
              f"Approx={approx_time:.4f}s (cost={approx_cost:.1f}), ratio={ratio:.2f}")

        if bf_time > 30:
            print("  (stopping — brute force too slow)")
            break
