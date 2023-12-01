# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

      # base case -> once the root node is nonde
      if root == None:
        return root
      
      # interchange
      root.left, root.right = root.right, root.left

      # recursive call
      self.invertTree(root.left)
      self.invertTree(root.right)

      # return the root node
      return root
