# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:

      q = deque()
      q.append(root)
      result = []

      while q:
        currLevel = []
        for _ in range(len(q)):
          curr = q.popleft()
          currLevel.append(curr.val)
          if curr.left:
            q.append(curr.left)
          if curr.right:
            q.append(curr.right)
        result.append(currLevel)
      
      result[-1][-1]