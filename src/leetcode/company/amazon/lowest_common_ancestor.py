"""
Key Insights:


Recursive Traversal:
- We can use a recursive approach to traverse the tree and identify the LCA.
- At each node, we check whether p or q exists in the left or right subtrees.


Base Cases:
- If the current node is `None`, we return `None`.
- If the current node is either p or q, we return the current node.


Pre-Order Traversal:
- If we find that the current node is one of the two nodes we are looking for,
  we do not need to explore it's children, because either this is the LCA or
  the parent node that called this node is.


Identifying the LCA:
- If both left and right recursive calls return non-`None` values, it means p and q are found in different subtrees, and the current node is the LCA.
- If only one side returns a non-`None` value, we propagate that value up the recursion stack.


Algorithm Steps:
    1. Define a Recursive Function:
        - The function will return the LCA if found, or `None`.
    2. Base Case:
        - If the current node is `None`, return `None`.
        - If the current node is p or q, return the current node.
    3. Recursive Calls:
        - Recurse on the left child.
        - Recurse on the right child.
    4. Process Returned Values:
        - If both left and right recursive calls return non-`None`, the current node is the LCA.
        - If only one side returns non-`None`, return that side's result.
        - If both sides return `None`, return `None`.
    5. Return the LCA:
        - The initial call to the recursive function will return the LCA of p and q.


Time and Space Complexity:
    - Time Complexity: O(N), where N is the number of nodes in the tree. We traverse each node once.
    - Space Complexity: O(H), where H is the height of the tree. This accounts for the recursion stack space.
"""


# Definition for a binary tree node.
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode | None':
        # Helper function for recursion
        def recurse_tree(current_node):
            if not current_node:
                return None
           
            # If the current node is p or q, return it
            if current_node == p or current_node == q:
                return current_node
           
            # Recurse on the left and right subtrees
            left = recurse_tree(current_node.left)
            right = recurse_tree(current_node.right)
           
            # If both left and right are non-None, current node is the LCA
            if left and right:
                return current_node
           
            # If one side is non-None: return that side, else return None
            return left or right
       
        # Start the recursion from the root
        return recurse_tree(root)


