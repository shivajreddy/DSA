# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:

    def dfs(self, root: Optional[TreeNode]) -> tuple[bool, int]:
        if not root:
            return True, 0

        left, right = self.dfs(root.left), self.dfs(root.right)

        balanced = left[0] and right[0] and abs(left[1] - right[1]) <= 1

        height = 1 + max(left[1], right[1])

        return balanced, height

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        return self.dfs(root)[0]
