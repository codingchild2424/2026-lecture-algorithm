# === Ex 2: DFS 깊이 우선 탐색 & 위상 정렬 ===
# Week 11 그래프 알고리즘 1 - DFS 재귀 구현 및 DAG 위상 정렬
# DFS 시간 복잡도: O(V + E), 공간 복잡도: O(V) (재귀 스택 포함)
# 위상 정렬 시간 복잡도: O(V + E)
"""DFS and Topological Sort."""


def dfs(graph, start, visited=None):
    """깊이 우선 탐색(DFS)을 재귀적으로 수행한다.

    알고리즘:
    1. 현재 노드를 방문 처리
    2. 인접 노드 중 미방문 노드에 대해 재귀적으로 DFS 수행
    3. 더 이상 방문할 노드가 없으면 되돌아감 (백트래킹)

    DFS의 특성:
    - 한 경로를 끝까지 탐색한 후 다른 경로로 이동
    - 스택(여기서는 재귀 호출 스택)을 사용

    Args:
        graph: 인접 리스트로 표현된 그래프 (딕셔너리)
        start: 탐색 시작 노드
        visited: 방문한 노드 집합 (재귀 호출 간 공유)

    Returns:
        방문 순서 리스트

    시간 복잡도: O(V + E) - 모든 정점과 간선을 한 번씩 처리
    공간 복잡도: O(V) - 재귀 스택 깊이 최대 V, visited 집합
    """
    if visited is None:
        visited = set()  # 최초 호출 시 빈 집합 생성
    visited.add(start)      # 현재 노드 방문 처리
    order = [start]         # 현재 노드를 방문 순서에 추가

    # 인접 노드를 순회하며 미방문 노드에 대해 재귀 탐색
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            order.extend(dfs(graph, neighbor, visited))  # 재귀 결과를 이어붙임
    return order


def topological_sort(graph):
    """DAG(방향 비순환 그래프)의 위상 정렬을 수행한다.

    알고리즘 (DFS 기반):
    1. 모든 노드에 대해 DFS를 수행
    2. DFS에서 한 노드의 모든 후계 노드를 방문한 후 (즉, DFS 종료 시)
       해당 노드를 스택에 추가
    3. 스택을 뒤집으면 위상 순서가 됨

    핵심 아이디어:
    - DFS에서 노드 u의 탐색이 완전히 끝난 후 스택에 추가하면,
      u에 의존하는 모든 노드들이 u 뒤에 위치하게 됨
    - 스택을 뒤집으면 의존성 순서가 올바르게 됨

    Args:
        graph: 방향 그래프의 인접 리스트 (딕셔너리)

    Returns:
        위상 정렬된 노드 리스트

    시간 복잡도: O(V + E)
    공간 복잡도: O(V) - visited 집합 + 재귀 스택
    """
    visited = set()
    stack = []  # DFS 완료 순서를 저장할 스택

    def _dfs(node):
        """내부 DFS 함수: 노드 탐색 완료 후 스택에 추가한다."""
        visited.add(node)
        # 모든 후속 노드를 먼저 방문 (재귀)
        for neighbor in graph.get(node, []):
            if neighbor not in visited:
                _dfs(neighbor)
        # 모든 후속 노드 방문 완료 후 스택에 추가 (후위 처리)
        stack.append(node)

    # 모든 노드에 대해 DFS 수행 (연결되지 않은 컴포넌트도 처리)
    for node in graph:
        if node not in visited:
            _dfs(node)

    # 스택을 뒤집으면 위상 순서가 됨
    return list(reversed(stack))


if __name__ == "__main__":
    # 무방향 그래프에서 DFS 테스트
    graph = {'A': ['B', 'C'], 'B': ['A', 'D'], 'C': ['A', 'E'], 'D': ['B'], 'E': ['C']}
    print(f"DFS from A: {dfs(graph, 'A')}")

    # DAG(방향 비순환 그래프)에서 위상 정렬 테스트
    # 과목 선수과목 관계: CS101 -> CS201, CS202 -> CS301 -> CS401
    dag = {
        'CS101': ['CS201', 'CS202'],
        'CS201': ['CS301'],
        'CS202': ['CS301'],
        'CS301': ['CS401'],
        'MATH101': ['CS201'],
        'CS401': []
    }
    print(f"\nCourse prerequisites (DAG):")
    for course, prereqs_for in dag.items():
        if prereqs_for:
            print(f"  {course} -> {prereqs_for}")
    print(f"Topological order: {topological_sort(dag)}")  # 선수과목이 먼저 나옴
