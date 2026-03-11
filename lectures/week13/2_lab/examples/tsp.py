# === TSP: Traveling Salesman Problem - Brute Force vs MST-based Approximation ===
# Week 13 NP-Completeness - Experience the difficulty of NP-hard problems and approximation algorithms through TSP
# Brute force: Explore all permutations, time complexity O(n!) - infeasible for large n
# MST 2-approximation: Based on minimum spanning tree, guaranteed within 2x of optimal (triangle inequality condition)
"""TSP - Brute force vs MST-based approximation."""
import itertools
import time
import math
import random


def tsp_bruteforce(dist_matrix):
    """Find the optimal TSP solution using brute force.

    Algorithm:
    1. Fix city 0 as the starting point (exploiting symmetry)
    2. Generate all permutations of the remaining cities
    3. Compute the total path cost for each permutation
    4. Return the minimum cost path

    Why O(n!)?
    - All permutations of n-1 cities = (n-1)!
    - Summing n edge costs per permutation = O(n)
    - Total: O(n * (n-1)!) = O(n!)

    Feasible range: approximately n <= 12 (12! = 479,001,600)

    Args:
        dist_matrix: n x n distance matrix, dist_matrix[i][j] = distance from city i to j

    Returns:
        (minimum cost, optimal path tuple)
    """
    n = len(dist_matrix)
    cities = list(range(1, n))  # Fix city 0 as the starting point
    min_cost = float('inf')
    best_path = None

    # Explore all permutations of the remaining cities
    for perm in itertools.permutations(cities):
        # Distance from start city (0) to the first city
        cost = dist_matrix[0][perm[0]]
        # Sum distances between consecutive cities in the permutation
        for i in range(len(perm) - 1):
            cost += dist_matrix[perm[i]][perm[i + 1]]
        # Distance from the last city back to start city (0)
        cost += dist_matrix[perm[-1]][0]

        # Update minimum cost
        if cost < min_cost:
            min_cost = cost
            best_path = (0,) + perm + (0,)  # Path: start -> permutation -> start
    return min_cost, best_path


def tsp_mst_approx(dist_matrix):
    """Find an approximate TSP solution using the MST-based 2-approximation algorithm.

    Algorithm:
    1. Build a Minimum Spanning Tree (MST) using Prim's algorithm
    2. Determine visit order via DFS preorder traversal of the MST
    3. Connect cities in visit order to form a Hamiltonian path

    Approximation guarantee (when triangle inequality holds):
    - MST cost <= optimal TSP cost (removing one edge from TSP yields a spanning tree)
    - DFS traversal cost = 2 * MST cost (each edge is traversed twice)
    - Triangle inequality ensures shortcuts are shorter, so approximate solution <= 2 * optimal

    Time complexity: O(n^2) - simple Prim's implementation (adjacency matrix)
    Space complexity: O(n^2) - adjacency list and distance matrix

    Args:
        dist_matrix: n x n distance matrix

    Returns:
        (approximate cost, approximate path tuple)
    """
    n = len(dist_matrix)

    # --- Step 1: Build MST using Prim's algorithm ---
    in_mst = [False] * n
    in_mst[0] = True  # Start from city 0
    adj = [[] for _ in range(n)]  # MST adjacency list

    for _ in range(n - 1):  # Add n-1 edges to the MST
        min_edge = (float('inf'), -1, -1)
        # Find the minimum weight edge from MST nodes to non-MST nodes
        for u in range(n):
            if not in_mst[u]:
                continue
            for v in range(n):
                if not in_mst[v] and dist_matrix[u][v] < min_edge[0]:
                    min_edge = (dist_matrix[u][v], u, v)
        _, u, v = min_edge
        in_mst[v] = True      # Add new node to MST
        adj[u].append(v)       # Add edge to bidirectional adjacency list
        adj[v].append(u)

    # --- Step 2: Determine visit order via DFS preorder traversal of MST ---
    visited = [False] * n
    tour = []

    def dfs(node):
        """Perform DFS preorder traversal on the MST.

        The preorder traversal order becomes the city visit order.
        Already visited cities are skipped, forming a Hamiltonian path.
        """
        visited[node] = True
        tour.append(node)      # Record visit order in preorder
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(0)
    tour.append(0)  # Return to the starting city (circular tour)

    # Compute path cost
    cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return cost, tuple(tour)


def generate_random_cities(n):
    """Generate n random cities and return the Euclidean distance matrix.

    Cities are randomly placed on a 100x100 plane
    Euclidean distance satisfies the triangle inequality, so the MST 2-approximation guarantee holds

    Time complexity: O(n^2) - computing distances for all city pairs
    """
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # Compute Euclidean distance
            dist[i][j] = math.sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2)
    return dist


if __name__ == "__main__":
    # Increase the number of cities to compare brute force time explosion vs approximation algorithm efficiency
    print("=== TSP: Brute Force Execution Time ===")
    for n in [6, 8, 10, 11, 12]:
        dist = generate_random_cities(n)

        # Brute force: O(n!) - exact optimal solution
        start = time.perf_counter()
        bf_cost, bf_path = tsp_bruteforce(dist)
        bf_time = time.perf_counter() - start

        # MST approximation: O(n^2) - within 2x of the optimal solution
        start = time.perf_counter()
        approx_cost, approx_path = tsp_mst_approx(dist)
        approx_time = time.perf_counter() - start

        # Approximation ratio: approximate solution / optimal solution (guaranteed <= 2.0)
        ratio = approx_cost / bf_cost
        print(f"N={n:2d}: BF={bf_time:8.3f}s (cost={bf_cost:.1f}), "
              f"Approx={approx_time:.4f}s (cost={approx_cost:.1f}), ratio={ratio:.2f}")

        if bf_time > 30:
            print("  (stopping — brute force too slow)")
            break
