# === TSP: 외판원 문제 - 브루트포스 vs MST 기반 근사 알고리즘 ===
# Week 13 NP-완전성 - TSP를 통해 NP-hard 문제의 난이도와 근사 알고리즘을 체험
# 브루트포스: 모든 순열 탐색, 시간 복잡도 O(n!) - n이 커지면 실행 불가능
# MST 2-근사: 최소 신장 트리 기반, 최적 해의 2배 이내 보장 (삼각 부등식 조건)
"""TSP - Brute force vs MST-based approximation."""
import itertools
import time
import math
import random


def tsp_bruteforce(dist_matrix):
    """브루트포스로 TSP의 최적 해를 구한다.

    알고리즘:
    1. 도시 0을 시작점으로 고정 (대칭성 이용)
    2. 나머지 도시들의 모든 순열(permutation)을 생성
    3. 각 순열에 대해 전체 경로 비용을 계산
    4. 최소 비용 경로를 반환

    왜 O(n!)인가?
    - n-1개의 도시에 대한 모든 순열 = (n-1)!
    - 각 순열마다 n개의 간선 비용을 합산 = O(n)
    - 전체: O(n * (n-1)!) = O(n!)

    실행 가능한 범위: n <= 12 정도 (12! = 479,001,600)

    Args:
        dist_matrix: n x n 거리 행렬, dist_matrix[i][j] = 도시 i에서 j까지 거리

    Returns:
        (최소 비용, 최적 경로 튜플)
    """
    n = len(dist_matrix)
    cities = list(range(1, n))  # 도시 0은 시작점으로 고정
    min_cost = float('inf')
    best_path = None

    # 나머지 도시들의 모든 순열을 탐색
    for perm in itertools.permutations(cities):
        # 시작 도시(0)에서 첫 번째 도시까지의 거리
        cost = dist_matrix[0][perm[0]]
        # 순열 내 연속된 도시들 간의 거리 합산
        for i in range(len(perm) - 1):
            cost += dist_matrix[perm[i]][perm[i + 1]]
        # 마지막 도시에서 시작 도시(0)로 돌아오는 거리
        cost += dist_matrix[perm[-1]][0]

        # 최소 비용 갱신
        if cost < min_cost:
            min_cost = cost
            best_path = (0,) + perm + (0,)  # 시작->순열->시작 경로
    return min_cost, best_path


def tsp_mst_approx(dist_matrix):
    """MST 기반 2-근사 알고리즘으로 TSP의 근사 해를 구한다.

    알고리즘:
    1. Prim 알고리즘으로 최소 신장 트리(MST)를 구축
    2. MST를 DFS 전위 순회하여 방문 순서를 결정
    3. 방문 순서대로 도시를 연결하여 해밀턴 경로를 생성

    근사 보장 (삼각 부등식 만족 시):
    - MST 비용 <= 최적 TSP 비용 (TSP에서 간선 하나를 빼면 신장 트리)
    - DFS 순회 비용 = 2 * MST 비용 (각 간선을 두 번 지남)
    - 삼각 부등식으로 지름길이 더 짧으므로, 근사 해 <= 2 * 최적 해

    시간 복잡도: O(n^2) - Prim의 단순 구현 (인접 행렬)
    공간 복잡도: O(n^2) - 인접 리스트 및 거리 행렬

    Args:
        dist_matrix: n x n 거리 행렬

    Returns:
        (근사 비용, 근사 경로 튜플)
    """
    n = len(dist_matrix)

    # --- 1단계: Prim 알고리즘으로 MST 구축 ---
    in_mst = [False] * n
    in_mst[0] = True  # 도시 0에서 시작
    adj = [[] for _ in range(n)]  # MST의 인접 리스트

    for _ in range(n - 1):  # MST에 n-1개의 간선을 추가
        min_edge = (float('inf'), -1, -1)
        # MST에 포함된 노드에서 포함되지 않은 노드로 가는 최소 가중치 간선 탐색
        for u in range(n):
            if not in_mst[u]:
                continue
            for v in range(n):
                if not in_mst[v] and dist_matrix[u][v] < min_edge[0]:
                    min_edge = (dist_matrix[u][v], u, v)
        _, u, v = min_edge
        in_mst[v] = True      # 새 노드를 MST에 추가
        adj[u].append(v)       # 양방향 인접 리스트에 간선 추가
        adj[v].append(u)

    # --- 2단계: MST의 DFS 전위 순회로 방문 순서 결정 ---
    visited = [False] * n
    tour = []

    def dfs(node):
        """MST에서 DFS 전위 순회를 수행한다.

        전위 순회 순서가 곧 도시 방문 순서가 된다.
        이미 방문한 도시는 건너뛰므로 해밀턴 경로가 만들어진다.
        """
        visited[node] = True
        tour.append(node)      # 전위(preorder)로 방문 순서 기록
        for neighbor in adj[node]:
            if not visited[neighbor]:
                dfs(neighbor)

    dfs(0)
    tour.append(0)  # 시작 도시로 돌아옴 (순환 경로)

    # 경로 비용 계산
    cost = sum(dist_matrix[tour[i]][tour[i+1]] for i in range(len(tour)-1))
    return cost, tuple(tour)


def generate_random_cities(n):
    """n개의 랜덤 도시를 생성하고 유클리드 거리 행렬을 반환한다.

    도시들은 100x100 평면에 무작위로 배치됨
    유클리드 거리는 삼각 부등식을 만족하므로 MST 2-근사 보장이 성립

    시간 복잡도: O(n^2) - 모든 도시 쌍의 거리 계산
    """
    cities = [(random.uniform(0, 100), random.uniform(0, 100)) for _ in range(n)]
    dist = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            # 유클리드 거리 계산
            dist[i][j] = math.sqrt((cities[i][0]-cities[j][0])**2 + (cities[i][1]-cities[j][1])**2)
    return dist


if __name__ == "__main__":
    # 도시 수를 늘려가며 브루트포스의 시간 폭발과 근사 알고리즘의 효율성을 비교
    print("=== TSP: Brute Force Execution Time ===")
    for n in [6, 8, 10, 11, 12]:
        dist = generate_random_cities(n)

        # 브루트포스: O(n!) - 정확한 최적 해
        start = time.perf_counter()
        bf_cost, bf_path = tsp_bruteforce(dist)
        bf_time = time.perf_counter() - start

        # MST 근사: O(n^2) - 최적 해의 2배 이내
        start = time.perf_counter()
        approx_cost, approx_path = tsp_mst_approx(dist)
        approx_time = time.perf_counter() - start

        # 근사 비율: 근사 해 / 최적 해 (2.0 이하가 보장됨)
        ratio = approx_cost / bf_cost
        print(f"N={n:2d}: BF={bf_time:8.3f}s (cost={bf_cost:.1f}), "
              f"Approx={approx_time:.4f}s (cost={approx_cost:.1f}), ratio={ratio:.2f}")

        if bf_time > 30:
            print("  (stopping — brute force too slow)")
            break
