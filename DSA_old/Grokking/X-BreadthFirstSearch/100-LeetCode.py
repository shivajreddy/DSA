from collections import deque
# Definition for a binary tree node.
class TreeNode(object):
  def __init__(self, val=0, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

  def Solution(p, q):

    if not p and not q:
      return True

    if not p or not q:
      return False

    if p.val != q.val:
      return False

    return self.Solution(p.left, q.left) and self.Solution(p.right, q.right)