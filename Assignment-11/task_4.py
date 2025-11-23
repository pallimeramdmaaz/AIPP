# Node class for BST
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# BST class
class BST:
    def __init__(self):
        self.root = None

    # Insert a value into BST
    def insert(self, data):
        self.root = self._insert_recursive(self.root, data)

    def _insert_recursive(self, node, data):
        if node is None:
            return Node(data)
        if data < node.data:
            node.left = self._insert_recursive(node.left, data)
        else:
            node.right = self._insert_recursive(node.right, data)
        return node

    # Inorder traversal (Left, Root, Right)
    def inorder_traversal(self):
        result = []
        self._inorder_recursive(self.root, result)
        return result

    def _inorder_recursive(self, node, result):
        if node:
            self._inorder_recursive(node.left, result)
            result.append(node.data)
            self._inorder_recursive(node.right, result)


# -----------------------
# Test the BST
# -----------------------
bst = BST()

# Sample input values
values = [50, 30, 70, 20, 40, 60, 80]

for val in values:
    bst.insert(val)

# Inorder traversal
print("Inorder Traversal:", bst.inorder_traversal())
