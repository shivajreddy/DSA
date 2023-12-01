# https://leetcode.com/problems/balanced-binary-tree/
from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # using que
        q = deque()
        q.append(root)

        while q:
            curr = q.popleft()
