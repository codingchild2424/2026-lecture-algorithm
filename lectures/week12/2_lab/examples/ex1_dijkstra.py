# === Ex 1: 다익스트라 최단 경로 알고리즘 ===
# Week 12 그래프 알고리즘 2 - 음이 아닌 가중치 그래프에서 단일 출발점 최단 경로
# 알고리즘: 최소 힙(우선순위 큐)을 사용한 그리디 방식
# 시간 복잡도: O((V + E) log V) - 이진 힙 사용 시
# 공간 복잡도: O(V + E) - 거리 배열 + 우선순위 큐
"""Dijkstra's Algorithm using heapq."""
import heapq


def dijkstra(graph, start):
    """다익스트라 알고리즘으로 시작 노드에서 모든 노드까지의 최단 거리를 구한다.

    알고리즘:
    1. 시작 노드의 거리를 0, 나머지를 무한대로 초기화
    2. 최소 힙에서 가장 짧은 거리의 노드 u를 꺼낸다
    3. u의 모든 인접 노드 v에 대해 완화(relaxation) 수행:
       dist[u] + w(u,v) < dist[v]이면 dist[v]를 갱신
    4. 갱신된 노드를 힙에 추가
    5. 힙이 빌 때까지 반복

    핵심 조건: 모든 간선의 가중치가 0 이상이어야 함 (음수 가중치 불가)
    그리디 정당성: 최소 힙에서 꺼낸 노드의 거리는 이미 최단 거리가 확정됨

    Args:
        graph: 인접 리스트 {노드: [(이웃, 가중치), ...]}
        start: 시작 노드

    Returns:
        (dist, prev) - dist: 최단 거리 딕셔너리, prev: 경로 추적용 이전 노드 딕셔너리

    시간 복잡도: O((V + E) log V) - 각 노드/간선마다 힙 연산 O(log V)
    공간 복잡도: O(V) - dist, prev 딕셔너리 + 힙
    """
    # 모든 노드의 거리를 무한대로 초기화
    dist = {node: float('inf') for node in graph}
    dist[start] = 0  # 시작 노드의 거리는 0
    prev = {node: None for node in graph}  # 최단 경로 추적용 이전 노드
    pq = [(0, start)]  # 최소 힙: (거리, 노드) 쌍

    while pq:
        d, u = heapq.heappop(pq)  # 현재 최소 거리 노드를 꺼냄

        # 이미 더 짧은 경로로 처리된 노드는 건너뜀 (lazy deletion)
        if d > dist[u]:
            continue

        # 인접 노드에 대해 완화(relaxation) 수행
        for v, w in graph[u]:
            if dist[u] + w < dist[v]:  # 더 짧은 경로를 발견하면
                dist[v] = dist[u] + w  # 거리 갱신
                prev[v] = u            # 이전 노드 기록 (경로 추적용)
                heapq.heappush(pq, (dist[v], v))  # 힙에 추가

    return dist, prev


def get_path(prev, target):
    """prev 딕셔너리를 역추적하여 시작 노드에서 target까지의 경로를 구한다.

    알고리즘: target에서 시작하여 prev[node]를 따라가며 역추적 후 뒤집기
    시간 복잡도: O(V) - 최악의 경우 경로 길이가 V
    """
    path = []
    node = target
    while node is not None:
        path.append(node)
        node = prev[node]  # 이전 노드로 이동
    return list(reversed(path))  # 역순으로 뒤집어 시작->목표 순서로 반환


if __name__ == "__main__":
    # 무방향 가중 그래프 (인접 리스트)
    graph = {
        'A': [('B', 4), ('C', 2)],
        'B': [('A', 4), ('C', 1), ('D', 5)],
        'C': [('A', 2), ('B', 1), ('D', 8), ('E', 10)],
        'D': [('B', 5), ('C', 8), ('E', 2)],
        'E': [('C', 10), ('D', 2)]
    }
    dist, prev = dijkstra(graph, 'A')

    # 각 노드까지의 최단 거리와 경로 출력
    print("Shortest distances from A:")
    for node in sorted(dist):
        path = get_path(prev, node)
        print(f"  A -> {node}: dist={dist[node]}, path={' -> '.join(path)}")
