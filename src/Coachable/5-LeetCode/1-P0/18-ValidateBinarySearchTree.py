# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        sorted_list = [float('-inf')]

        def dfs(node: TreeNode) -> bool:
            if not node:
                return True

            if not dfs(node.left):
                return False

            # check if the previous item is small, before adding the current item
            if sorted_list[-1] >= node.val:
                return False
            sorted_list.append(node.val)

            if not dfs(node.right):
                return False
            return True

        return dfs(root)
