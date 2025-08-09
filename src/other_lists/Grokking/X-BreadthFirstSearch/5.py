from collections import deque
class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_minimum_depth(root):
  if root == None:
    return None

  q = deque()   # deque to bfs the binary tree
  q.append(root)    # start with queue having the root
  n = 0

  while q:
    n += 1    # current level index -> root node level's idx is 1

    # start the loop of removing all nodes from the beginning of current level
    for _ in range(len(q)):
      curr = q.popleft()    # remove the first node in the queue

      if not curr.left and not curr.right:    # check if the curr node is a leaf node
        return n

      # not a leaf node, so check for child, add them to queue
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
  
  return -1


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