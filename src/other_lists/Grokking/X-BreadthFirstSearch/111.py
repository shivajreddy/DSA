# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
      if root == None:
        return 0 
      if root == []:
        return 0
      
      q = deque()
      q.append(root)
      n = 0
      while q:
        n += 1
        for _ in range(len(q)):
          curr = q.popleft()
          if not curr.left and not curr.right:
            return n
          if curr.left:
            q.append(curr.left)
          if curr.right:
            q.append(curr.right)
