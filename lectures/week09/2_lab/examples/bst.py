# === Binary Search Tree (BST) Implementation ===
# Week 09 Search Trees - Insert, search, delete, and traversal operations for BST
# Time complexity: Average O(log n), Worst O(n) (skewed tree)
# Space complexity: O(n) - storing n nodes
"""Binary Search Tree implementation."""


class BSTNode:
    """Class representing an individual node of a BST.

    Each node has a key and left/right child pointers.
    BST property: all keys in left subtree < current key < all keys in right subtree
    """
    def __init__(self, key):
        self.key = key
        self.left = None   # Left child (values less than current key)
        self.right = None  # Right child (values greater than current key)


class BST:
    """Binary Search Tree class.

    Time complexity of main operations:
    - Insert: Average O(log n), Worst O(n)
    - Search: Average O(log n), Worst O(n)
    - Delete: Average O(log n), Worst O(n)
    - Inorder traversal: O(n)

    Worst case occurs when the tree is skewed to one side (e.g., inserting in sorted order)
    """
    def __init__(self):
        self.root = None  # Root node

    def insert(self, key):
        """Insert a key into the BST. Public interface."""
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        """Recursively find the correct position and insert a new node.

        Algorithm:
        1. If an empty position is found, create a new node
        2. If key is less than the current node, move left
        3. If key is greater than the current node, move right
        4. Duplicate keys are ignored (no action when key == node.key)

        Time complexity: O(h) - h is the tree height
        """
        if node is None:
            return BSTNode(key)  # Insert new node at empty position
        if key < node.key:
            node.left = self._insert(node.left, key)    # Recurse into left subtree
        elif key > node.key:
            node.right = self._insert(node.right, key)  # Recurse into right subtree
        return node  # Ignore duplicate key and return current node

    def search(self, key):
        """Search for a key in the BST. Public interface."""
        return self._search(self.root, key)

    def _search(self, node, key):
        """Recursively search for a key.

        Algorithm: Uses BST property to halve the search space at each step
        Returns: The node containing the key (or None if not found)
        Time complexity: O(h) - h is the tree height
        """
        if node is None or node.key == key:
            return node  # Key found or reached the end of the tree
        if key < node.key:
            return self._search(node.left, key)   # Search left subtree
        return self._search(node.right, key)      # Search right subtree

    def delete(self, key):
        """Delete a key from the BST. Public interface."""
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        """Recursively find and delete a key.

        Three cases when deleting:
        1. Leaf node: Simply remove it
        2. One child: Replace with the child
        3. Two children: Replace with the minimum value of the right subtree (successor),
                        then delete the successor from the right subtree

        Time complexity: O(h) - h is the tree height
        """
        if node is None:
            return None  # Key to delete is not in the tree
        if key < node.key:
            node.left = self._delete(node.left, key)    # Delete from left
        elif key > node.key:
            node.right = self._delete(node.right, key)  # Delete from right
        else:
            # Found the node to delete
            if node.left is None:
                return node.right  # Case 1, 2: No left child -> replace with right child
            if node.right is None:
                return node.left   # Case 2: No right child -> replace with left child
            # Case 3: Two children -> use inorder successor
            successor = self._min_node(node.right)  # Minimum node in right subtree
            node.key = successor.key                 # Replace with successor's key
            node.right = self._delete(node.right, successor.key)  # Delete successor
        return node

    def _min_node(self, node):
        """Find the node with the minimum key in a subtree.

        In a BST, the minimum value is always at the leftmost node.
        Time complexity: O(h)
        """
        while node.left:
            node = node.left  # Keep moving left
        return node

    def height(self):
        """Return the height of the tree. Public interface."""
        return self._height(self.root)

    def _height(self, node):
        """Recursively compute the tree height.

        Height = number of edges from root to deepest leaf + 1
        Height of an empty tree is 0
        Time complexity: O(n) - visits all nodes
        """
        if node is None:
            return 0
        return 1 + max(self._height(node.left), self._height(node.right))

    def inorder(self):
        """Return inorder traversal result as a list. Public interface."""
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        """Inorder Traversal: visit in left -> root -> right order.

        Inorder traversal of a BST yields keys in ascending sorted order.
        Time complexity: O(n) - visits each node exactly once
        """
        if node:
            self._inorder(node.left, result)   # Visit left subtree
            result.append(node.key)            # Process current node
            self._inorder(node.right, result)  # Visit right subtree


if __name__ == "__main__":
    import random

    # Basic test: balanced insertion order
    bst = BST()
    for key in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(key)
    print(f"Inorder: {bst.inorder()}")          # Verify ascending sorted order
    print(f"Height: {bst.height()}")            # Balanced tree: height ~ log(n)
    print(f"Search 40: {bst.search(40) is not None}")  # Search test
    bst.delete(30)                              # Delete a node with two children
    print(f"After delete 30: {bst.inorder()}")

    # Skewed tree test: inserting in sorted order -> height becomes n
    bst_sorted = BST()
    for i in range(1, 101):
        bst_sorted.insert(i)
    print(f"\nSorted insertion (1-100): height = {bst_sorted.height()}")  # Height 100 (worst case)

    # Random insertion: on average, height is close to O(log n)
    bst_random = BST()
    data = list(range(1, 101))
    random.shuffle(data)
    for i in data:
        bst_random.insert(i)
    print(f"Random insertion (1-100): height = {bst_random.height()}")  # Height ~ 12-20
