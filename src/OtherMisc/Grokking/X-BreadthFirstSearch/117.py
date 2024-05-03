"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
from collections import deque
class Solution:
    def connect(self, root: 'Node') -> 'Node':
      if root == None or root == []:
        return root
      
      q = deque()
      q.append(root)
      while q:
        prev = None
        for _ in range(len(q)):
          curr = q.popleft()
          if curr.left:
            q.append(curr.left)
          if curr.right:
            q.append(curr.right)
          if prev:
            prev.next = curr
          prev = curr
      return root
