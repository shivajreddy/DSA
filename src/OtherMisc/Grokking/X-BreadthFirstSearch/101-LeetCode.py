from collections import deque

def isMirror(node1, node2):

  # base condition
  if not node1 and not node2:
    return True
  
  if node1 and node2 and node1.val == node2.val:
    # recursive call
    return isMirror(node1.left, node2.right) and isMirror(node1.right, node2.left)
  
  return False

def symmetric(root):
  return isMirror(root, root)


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

one = TreeNode(1) 
two = TreeNode(2)
three = TreeNode(2)
one.left = two
one.right = three

print(symmetric(one))