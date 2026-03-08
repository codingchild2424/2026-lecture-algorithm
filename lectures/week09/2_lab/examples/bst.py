# === 이진 탐색 트리 (Binary Search Tree) 구현 ===
# Week 09 탐색 트리 - BST의 삽입, 검색, 삭제, 순회 연산 구현
# 시간 복잡도: 평균 O(log n), 최악 O(n) (편향 트리)
# 공간 복잡도: O(n) - n개의 노드 저장
"""Binary Search Tree implementation."""


class BSTNode:
    """BST의 개별 노드를 나타내는 클래스.

    각 노드는 키(key)와 왼쪽/오른쪽 자식 포인터를 가진다.
    BST 속성: 왼쪽 서브트리의 모든 키 < 현재 키 < 오른쪽 서브트리의 모든 키
    """
    def __init__(self, key):
        self.key = key
        self.left = None   # 왼쪽 자식 (현재 키보다 작은 값)
        self.right = None  # 오른쪽 자식 (현재 키보다 큰 값)


class BST:
    """이진 탐색 트리 클래스.

    주요 연산의 시간 복잡도:
    - 삽입(insert): 평균 O(log n), 최악 O(n)
    - 검색(search): 평균 O(log n), 최악 O(n)
    - 삭제(delete): 평균 O(log n), 최악 O(n)
    - 순회(inorder): O(n)

    최악의 경우는 트리가 한쪽으로 편향될 때 발생 (정렬된 순서로 삽입 시)
    """
    def __init__(self):
        self.root = None  # 루트 노드

    def insert(self, key):
        """키를 BST에 삽입한다. 공개 인터페이스."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """재귀적으로 올바른 위치를 찾아 새 노드를 삽입한다.

        알고리즘:
        1. 빈 위치를 찾으면 새 노드 생성
        2. key가 현재 노드보다 작으면 왼쪽으로 이동
        3. key가 현재 노드보다 크면 오른쪽으로 이동
        4. 중복 키는 무시한다 (key == node.key일 때 아무 작업 안 함)

        시간 복잡도: O(h) - h는 트리 높이
        """
        if node is None:
            return BSTNode(key)  # 빈 위치에 새 노드 삽입
        if key < node.key:
            node.left = self._insert(node.left, key)    # 왼쪽 서브트리로 재귀
        elif key > node.key:
            node.right = self._insert(node.right, key)  # 오른쪽 서브트리로 재귀
        return node  # 중복 키는 무시하고 현재 노드 반환

    def search(self, key):
        """키를 BST에서 검색한다. 공개 인터페이스."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """재귀적으로 키를 검색한다.

        알고리즘: BST 속성을 이용하여 매 단계마다 탐색 범위를 절반으로 축소
        반환: 키를 가진 노드 (없으면 None)
        시간 복잡도: O(h) - h는 트리 높이
        """
        if node is None or node.key == key:
            return node  # 키를 찾았거나 트리 끝에 도달
        if key < node.key:
            return self._search(node.left, key)   # 왼쪽 서브트리 탐색
        return self._search(node.right, key)      # 오른쪽 서브트리 탐색

    def delete(self, key):
        """키를 BST에서 삭제한다. 공개 인터페이스."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """재귀적으로 키를 찾아 삭제한다.

        삭제 시 3가지 경우:
        1. 리프 노드: 단순히 제거
        2. 자식이 하나: 자식으로 교체
        3. 자식이 둘: 오른쪽 서브트리의 최소값(후계자)으로 교체 후
                     후계자를 오른쪽 서브트리에서 삭제

        시간 복잡도: O(h) - h는 트리 높이
        """
        if node is None:
            return None  # 삭제할 키가 트리에 없음
        if key < node.key:
            node.left = self._delete(node.left, key)    # 왼쪽에서 삭제
        elif key > node.key:
            node.right = self._delete(node.right, key)  # 오른쪽에서 삭제
        else:
            # 삭제할 노드를 찾음
            if node.left is None:
                return node.right  # 경우 1, 2: 왼쪽 자식 없음 -> 오른쪽 자식으로 교체
            if node.right is None:
                return node.left   # 경우 2: 오른쪽 자식 없음 -> 왼쪽 자식으로 교체
            # 경우 3: 자식이 둘 -> 후계자(inorder successor) 사용
            successor = self._min_node(node.right)  # 오른쪽 서브트리의 최소 노드
            node.key = successor.key                 # 후계자의 키로 교체
            node.right = self._delete(node.right, successor.key)  # 후계자 삭제
        return node

    def _min_node(self, node):
        """서브트리에서 최소 키를 가진 노드를 찾는다.

        BST에서 최소값은 항상 가장 왼쪽 노드에 위치한다.
        시간 복잡도: O(h)
        """
        while node.left:
            node = node.left  # 왼쪽으로 계속 이동
        return node

    def height(self):
        """트리의 높이를 반환한다. 공개 인터페이스."""
        return self._height(self.root)

    def _height(self, node):
        """재귀적으로 트리 높이를 계산한다.

        높이 = 루트에서 가장 깊은 리프까지의 간선 수 + 1
        빈 트리의 높이는 0
        시간 복잡도: O(n) - 모든 노드를 방문
        """
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def inorder(self):
        """중위 순회 결과를 리스트로 반환한다. 공개 인터페이스."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """중위 순회(Inorder Traversal): 왼쪽 -> 루트 -> 오른쪽 순서로 방문.

        BST를 중위 순회하면 키가 오름차순으로 정렬된 결과를 얻는다.
        시간 복잡도: O(n) - 모든 노드를 한 번씩 방문
        """
        if node:
            self._inorder(node.left, result)   # 왼쪽 서브트리 방문
            result.append(node.key)            # 현재 노드 처리
            self._inorder(node.right, result)  # 오른쪽 서브트리 방문


if __name__ == "__main__":
    import random

    # 기본 테스트: 균형 잡힌 삽입 순서
    bst = BST()
    for key in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(key)
    print(f"Inorder: {bst.inorder()}")          # 오름차순 정렬 결과 확인
    print(f"Height: {bst.height()}")            # 균형 트리: 높이 약 log(n)
    print(f"Search 40: {bst.search(40) is not None}")  # 검색 테스트
    bst.delete(30)                              # 자식이 둘인 노드 삭제
    print(f"After delete 30: {bst.inorder()}")

    # 편향 트리 테스트: 정렬된 순서로 삽입 -> 높이가 n이 됨
    bst_sorted = BST()
    for i in range(1, 101):
        bst_sorted.insert(i)
    print(f"\nSorted insertion (1-100): height = {bst_sorted.height()}")  # 높이 100 (최악)

    # 랜덤 삽입: 평균적으로 높이가 O(log n)에 가까움
    bst_random = BST()
    data = list(range(1, 101))
    random.shuffle(data)
    for i in data:
        bst_random.insert(i)
    print(f"Random insertion (1-100): height = {bst_random.height()}")  # 높이 약 12~20
