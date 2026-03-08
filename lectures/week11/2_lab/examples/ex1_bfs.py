# === Ex 1: BFS 너비 우선 탐색 ===
# Week 11 그래프 알고리즘 1 - BFS를 이용한 그래프 탐색 및 최단 거리 계산
# 알고리즘: 큐(FIFO)를 사용하여 시작 노드에서 가까운 노드부터 순서대로 방문
# 시간 복잡도: O(V + E) - V는 정점 수, E는 간선 수
# 공간 복잡도: O(V) - visited 집합, 큐, distance 딕셔너리
"""BFS - Breadth First Search with shortest distance."""
from collections import deque


def bfs(graph, start):
    """너비 우선 탐색(BFS)을 수행하고 방문 순서와 최단 거리를 반환한다.

    알고리즘:
    1. 시작 노드를 방문 처리하고 큐에 넣는다
    2. 큐에서 노드를 꺼내고(popleft), 인접 노드 중 미방문 노드를 방문 처리 후 큐에 추가
    3. 큐가 빌 때까지 반복

    BFS의 핵심 특성:
    - 가중치가 없는 그래프에서 최단 경로를 보장한다
    - 같은 레벨(거리)의 노드를 모두 방문한 후 다음 레벨로 진행

    Args:
        graph: 인접 리스트로 표현된 그래프 (딕셔너리)
        start: 탐색 시작 노드

    Returns:
        (방문 순서 리스트, 시작 노드로부터의 최단 거리 딕셔너리)

    시간 복잡도: O(V + E) - 모든 정점과 간선을 정확히 한 번씩 처리
    공간 복잡도: O(V) - 큐와 visited에 최대 V개의 노드 저장
    """
    visited = {start}           # 방문한 노드 집합 (중복 방문 방지)
    queue = deque([start])      # BFS 탐색 큐 (FIFO)
    distance = {start: 0}       # 시작 노드로부터의 최단 거리
    order = []                  # 방문 순서 기록

    while queue:
        node = queue.popleft()  # 큐의 맨 앞에서 노드 꺼내기 (FIFO) - O(1)
        order.append(node)      # 방문 순서 기록

        # 현재 노드의 모든 인접 노드를 확인
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                visited.add(neighbor)       # 방문 표시 (큐에 넣을 때 표시해야 중복 방지)
                queue.append(neighbor)      # 큐에 추가
                distance[neighbor] = distance[node] + 1  # 거리 = 부모 거리 + 1

    return order, distance


if __name__ == "__main__":
    # 무방향 그래프 예시 (인접 리스트)
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    order, dist = bfs(graph, 'A')
    print(f"BFS order: {order}")         # A에서 시작하여 레벨 순으로 방문
    print(f"Distances from A: {dist}")   # 각 노드까지의 최단 거리 (간선 수)
