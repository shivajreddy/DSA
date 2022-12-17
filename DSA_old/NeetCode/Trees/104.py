# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
      if root == None or root == []:
        return 0 
      
      q = deque()
      q.append(root)
      count = 0
      
      while q:
        count += 1
        for _ in range(len(q)):
          curr = q.popleft()
          if curr.left:
            q.append(curr.left)
          if curr.right:
            q.append(curr.right)
            
      return count      
