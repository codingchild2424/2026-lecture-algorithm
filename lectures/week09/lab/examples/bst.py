"""Binary Search Tree implementation."""


class BSTNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left = self._insert(node.left, key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None or node.key == key:
            return node
        if key < node.key:
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            return None
        if key < node.key:
            node.left = self._delete(node.left, key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            if node.left is None:
                return node.right
            if node.right is None:
                return node.left
            successor = self._min_node(node.right)
            node.key = successor.key
            node.right = self._delete(node.right, successor.key)
        return node

    def _min_node(self, node):
        while node.left:
            node = node.left
        return node

    def height(self):
        return self._height(self.root)

    def _height(self, node):
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def inorder(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)


if __name__ == "__main__":
    import random

    # Basic test
    bst = BST()
    for key in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(key)
    print(f"Inorder: {bst.inorder()}")
    print(f"Height: {bst.height()}")
    print(f"Search 40: {bst.search(40) is not None}")
    bst.delete(30)
    print(f"After delete 30: {bst.inorder()}")

    # Degenerate case: sorted insertion
    bst_sorted = BST()
    for i in range(1, 101):
        bst_sorted.insert(i)
    print(f"\nSorted insertion (1-100): height = {bst_sorted.height()}")

    # Random insertion
    bst_random = BST()
    data = list(range(1, 101))
    random.shuffle(data)
    for i in data:
        bst_random.insert(i)
    print(f"Random insertion (1-100): height = {bst_random.height()}")
