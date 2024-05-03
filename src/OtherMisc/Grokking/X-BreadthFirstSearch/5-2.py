from collections import deque

from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

#* Maximum depth in a Binary Tree
def find_minimum_depth(root):
  if root == None:
    return None

  q = deque()
  q.append(root)
  n = 0

  while q:
    n += 1

    for _ in range(len(q)):
      curr = q.popleft()

      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)

  return n


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))
  root.left.left = TreeNode(9)
  root.right.left.left = TreeNode(11)
  print("Tree Minimum Depth: " + str(find_minimum_depth(root)))


main()