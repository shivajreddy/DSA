# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
      if root == None:
        return None
      if root == []:
        return []
      
      q = deque()
      q.append(root)
      result = deque()
      
      while q:
        currLevel = []
        for _ in range(len(q)):
          curr = q.popleft()
          currLevel.append(curr.val)
          if curr.left:
            q.append(curr.left)
          if curr.right:
            q.append(curr.right)
        result.appendleft(currLevel)
      return list(result)