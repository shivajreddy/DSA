class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right

def has_path(root, sum):

  if root == None:
    return False

  if root.left == None and root.right == None and root.val == sum:
    return True

  leftResult = has_path(root.left, sum-root.val)
  rightResult = has_path(root.right, sum-root.val)
  if leftResult or rightResult:
    return True
  return False

def check_path(node , target):

  # base case check if the node is a leaf node, AND val is the remaining sum
  if not node.left and not node.right and node.val == target:
    return True
  
  new_target = target - node.val
  if new_target < -1:
    return False

  if node.left:
    return check_path(node.left, new_target)
  if node.right:
    return check_path(node.right, new_target)
  
  return False

def reached(root, val):
  if not root.left and not root.right and root.val == val:
    return True


def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree has path: " + str(has_path(root, 23)))
  print("Tree has path: " + str(has_path(root, 16)))

main()