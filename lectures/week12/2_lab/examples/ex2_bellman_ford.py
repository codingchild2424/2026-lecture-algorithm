# === Ex 2: 벨만-포드 최단 경로 알고리즘 ===
# Week 12 그래프 알고리즘 2 - 음수 가중치를 허용하는 단일 출발점 최단 경로
# 알고리즘: 모든 간선에 대해 V-1번 완화(relaxation)를 반복
# 시간 복잡도: O(V * E) - 다익스트라보다 느리지만 음수 가중치 처리 가능
# 공간 복잡도: O(V) - 거리 배열과 이전 노드 배열
"""Bellman-Ford Algorithm - handles negative weights."""


def bellman_ford(vertices, edges, start):
    """벨만-포드 알고리즘으로 최단 거리를 구한다.

    알고리즘:
    1. 시작 노드의 거리를 0, 나머지를 무한대로 초기화
    2. V-1번 반복하며 모든 간선에 대해 완화(relaxation) 수행:
       dist[u] + w < dist[v]이면 dist[v] = dist[u] + w로 갱신
    3. V번째 반복에서 추가 완화가 발생하면 음수 사이클이 존재

    다익스트라와의 차이:
    - 벨만-포드는 음수 가중치 간선을 처리할 수 있음
    - 음수 사이클을 감지할 수 있음
    - O(VE)로 다익스트라의 O((V+E)log V)보다 느림

    왜 V-1번 반복인가?
    - 최단 경로는 최대 V-1개의 간선을 포함 (사이클이 없을 때)
    - i번째 반복 후, 최대 i개의 간선을 사용하는 최단 경로가 확정됨

    Args:
        vertices: 정점 리스트
        edges: 간선 리스트 [(출발, 도착, 가중치), ...]
        start: 시작 정점

    Returns:
        (dist, prev) - dist: 최단 거리 딕셔너리, prev: 경로 추적용 딕셔너리

    Raises:
        ValueError: 음수 사이클이 존재할 경우

    시간 복잡도: O(V * E)
    공간 복잡도: O(V)
    """
    # 모든 정점의 거리를 무한대로 초기화
    dist = {v: float('inf') for v in vertices}
    dist[start] = 0  # 시작 노드 거리 0
    prev = {v: None for v in vertices}  # 경로 추적용

    # V-1번 반복: 매 반복마다 모든 간선에 대해 완화 수행
    for _ in range(len(vertices) - 1):
        for u, v, w in edges:
            # 완화(relaxation): 더 짧은 경로가 발견되면 갱신
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                prev[v] = u

    # 음수 사이클 검출: V번째 반복에서 추가 완화가 가능하면 음수 사이클 존재
    for u, v, w in edges:
        if dist[u] + w < dist[v]:
            raise ValueError("Graph contains a negative cycle")

    return dist, prev


if __name__ == "__main__":
    vertices = ['A', 'B', 'C', 'D', 'E']
    # 방향 가중 그래프 - B->C 간선에 음수 가중치(-1)가 포함됨
    edges = [
        ('A', 'B', 4), ('A', 'C', 2),
        ('B', 'C', -1), ('B', 'D', 5),   # B->C: 음수 가중치
        ('C', 'D', 8), ('C', 'E', 10),
        ('D', 'E', 2)
    ]

    dist, prev = bellman_ford(vertices, edges, 'A')
    print("Bellman-Ford from A (handles negative weights):")
    for v in sorted(dist):
        print(f"  A -> {v}: dist={dist[v]}")
