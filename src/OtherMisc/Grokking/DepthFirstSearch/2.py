class TreeNode:
  def __init__(self, val, left=None, right=None):
    self.val = val
    self.left = left
    self.right = right


def find_paths(root, sum):
  allPaths = []
  if root == None:
    return False

  if not root.left and not root.right and root.val == sum:
    return True
  
  new_sum = sum - root.val
  leftResult = find_paths(root.left, new_sum)
  rightResult = find_paths(root.right, new_sum)
  if leftResult or rightResult:
    allPaths.append(root.val)
    return True

  return False

def main():

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(4)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  sum = 23
  print("Tree paths with sum " + str(sum) +
        ": " + str(find_paths(root, sum)))


main()