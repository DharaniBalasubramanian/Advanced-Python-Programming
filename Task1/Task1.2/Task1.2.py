#  1.2 Implement a Binary Search Tree (BST)
# - Objective: Gain hands-on experience with tree-based data structures and algorithms.
# - Instructions:
#   - Step 1: Create a `Node` class to represent a node in the tree.
#   - Step 2: Implement a `BinarySearchTree` class with methods like `insert`, `delete`, `find`, `inorder_traversal`, `preorder_traversal`, and `postorder_traversal`.
#   - Step 3: Implement a method to find the height of the tree and check if the tree is balanced.
#   - Step 4: Add a method to print all nodes at a given depth.
# - Expected Output: A fully functional BST with methods to perform common operations, traversal, and analysis.
# - Complexity Analysis: 
#   - Analyze the time complexity for insertion, deletion, and search operations in both balanced and unbalanced scenarios.


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, key):
        if self.root is None:
            self.root = Node(key)
        else:
            self._insert_recursive(self.root, key)

    def _insert_recursive(self, node, key):
        if key < node.val:
            if node.left is None:
                node.left = Node(key)
            else:
                self._insert_recursive(node.left, key)
        else:
            if node.right is None:
                node.right = Node(key)
            else:
                self._insert_recursive(node.right, key)  # Corrected: pass `key`

    def delete(self, key):
        self.root = self._delete_recursive(self.root, key)

    def _delete_recursive(self, node, key):
        if node is None:
            return node
        if key < node.val:
            node.left = self._delete_recursive(node.left, key)
        elif key > node.val:
            node.right = self._delete_recursive(node.right, key)
        else:
            if node.left is None:
                return node.right
            elif node.right is None:
                return node.left
            min_larger_node = self._min_value_node(node.right)
            node.val = min_larger_node.val
            node.right = self._delete_recursive(node.right, min_larger_node.val)
        return node

    def _min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def find(self, key):
        return self._find_recursive(self.root, key)

    def _find_recursive(self, node, key):
        if node is None or node.val == key:
            return node
        if key < node.val:
            return self._find_recursive(node.left, key)
        return self._find_recursive(node.right)

    def inorder_traversal(self):
        return self._inorder_recursive(self.root)

    def _inorder_recursive(self, node):
        return (self._inorder_recursive(node.left) if node.left else []) + \
               [node.val] + \
               (self._inorder_recursive(node.right) if node.right else [])

    def preorder_traversal(self):
        return self._preorder_recursive(self.root)

    def _preorder_recursive(self, node):
        return [node.val] + \
               (self._preorder_recursive(node.left) if node.left else []) + \
               (self._preorder_recursive(node.right) if node.right else [])

    def postorder_traversal(self):
        return self._postorder_recursive(self.root)

    def _postorder_recursive(self, node):
        return (self._postorder_recursive(node.left) if node.left else []) + \
               (self._postorder_recursive(node.right) if node.right else []) + \
               [node.val]

    def height(self):
        return self._height_recursive(self.root)

    def _height_recursive(self, node):
        if node is None:
            return -1
        return 1 + max(self._height_recursive(node.left), self._height_recursive(node.right))

    def is_balanced(self):
        def check_balance(node):
            if node is None:
                return 0
            left_height = check_balance(node.left)
            right_height = check_balance(node.right)
            if left_height == -1 or right_height == -1 or abs(left_height - right_height) > 1:
                return -1
            return max(left_height, right_height) + 1
        
        return check_balance(self.root) != -1

    def nodes_at_depth(self, depth):
        nodes = []
        self._nodes_at_depth_recursive(self.root, depth, 0, nodes)
        return nodes

    def _nodes_at_depth_recursive(self, node, depth, current_depth, nodes):
        if node is None:
            return
        if current_depth == depth:
            nodes.append(node.val)
        else:
            self._nodes_at_depth_recursive(node.left, depth, current_depth + 1, nodes)
            self._nodes_at_depth_recursive(node.right, depth, current_depth + 1, nodes)

    def print_tree(self, node=None, level=0):
        if node is not None:
            self.print_tree(node.right, level + 1)
            print('     ' * level + str(node.val))
            self.print_tree(node.left, level + 1)


# Example usage
if __name__ == "__main__":
    # Balanced tree insertions
    print("--- Balanced Tree ---")
    bst = BinarySearchTree()
    balanced_values = [10, 5, 15, 3, 7, 12, 18]
    for val in balanced_values:
        bst.insert(val)
    
    bst.print_tree(bst.root)  # Print tree after all insertions

    print("\nInorder Traversal:", bst.inorder_traversal())
    print("Preorder Traversal:", bst.preorder_traversal())
    print("Postorder Traversal:", bst.postorder_traversal())
    print("Height of tree:", bst.height())
    print("Is the tree balanced?", bst.is_balanced())
    print("Nodes at depth 2:", bst.nodes_at_depth(2))

    # Deleting a node
    bst.delete(5)
    print("\nInorder Traversal after deleting 5:", bst.inorder_traversal())
    print("Is the tree balanced after deletion?", bst.is_balanced())

    # Imbalanced tree insertions
    print("\n--- Imbalanced Tree ---")
    bst2 = BinarySearchTree()
    imbalanced_values = [10, 20, 30, 40, 50]  # Creates a right-heavy tree
    for val in imbalanced_values:
        bst2.insert(val)
    
    bst2.print_tree(bst2.root)  # Print tree after all insertions

    print("\nInorder Traversal:", bst2.inorder_traversal())
    print("Preorder Traversal:", bst2.preorder_traversal())
    print("Postorder Traversal:", bst2.postorder_traversal())
    print("Height of tree:", bst2.height())
    print("Is the tree balanced?", bst2.is_balanced())
    print("Nodes at depth 2:", bst2.nodes_at_depth(2))
