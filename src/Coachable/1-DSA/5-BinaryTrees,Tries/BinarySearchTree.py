"""
Binary Search Tree
"""
from typing import Optional

from TreeSamples import TreeNode, binary_search_tree_1, binary_search_tree_2
from PrintTree import print_tree


# print the in order traversal of the binary search tree
def in_order_traversal(root: TreeNode) -> list[int]:
    # recursive function
    def dfs(node: TreeNode, arr: list):
        # base condition
        if not node:
            return
        dfs(node.left, arr)
        arr.append(node.val)
        dfs(node.right, arr)
        return arr

    result = []
    dfs(root, result)
    print(result)
    return result


# assert in_order_traversal(binary_search_tree_1) == [10, 20, 25, 30, 35, 40, 50]
# assert in_order_traversal(binary_search_tree_2) == [1, 5, 6, 14, 16]

# Search for target key - using recursive function
def search_key(root: TreeNode, target_key: int):
    def dfs(node, key):
        while node:
            if node.val == key:
                return node
            if node.val < key:
                node = node.right
            else:
                node = node.left
        return -1

    return dfs(root, target_key)


# recursive function in another style
def search_key2(root: TreeNode, target_key: int):
    if not root:
        return None
    if root.val == target_key:
        return root
    if root.val > target_key:
        return search_key2(root.left, target_key)
    # if root.val < target_key:
    else:
        return search_key2(root.right, target_key)


# in_order_traversal(search_key(binary_search_tree_1, 10))
# in_order_traversal(search_key(binary_search_tree_1, 40))


# Add a new node to binary search tree.
def add_new_node(bst: TreeNode, key: int) -> Optional[TreeNode]:
    pass


# Add a new node to binary search tree.
def add_new_node2(root: TreeNode, key: int):
    if not root:
        root = TreeNode(key)
        return
    if root.val > key:
        if not root.left:
            root.left = TreeNode(key)
            return
        add_new_node2(root.left, key)
    if root.val < key:
        if not root.right:
            root.right = TreeNode(key)
            return
        add_new_node2(root.right, key)


add_new_node2(binary_search_tree_1, 13)
add_new_node2(binary_search_tree_1, 33)
add_new_node2(binary_search_tree_1, 31)
add_new_node2(binary_search_tree_1, -10)
add_new_node2(binary_search_tree_2, -10)
print_tree(binary_search_tree_1)
print_tree(binary_search_tree_2)
