
# Level Order Successor

from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def find_successor(root, key):
  # TODO: Write your code here
  q = deque()
  q.append(root)

  while q:

    curr = q.popleft()

    if curr.left:
      q.append(curr.left)
    if curr.right:
      q.append(curr.right)

    # should check after adding all children.
    # cause if curr node is root node, or right node, queue needs the curr node children to return
    if curr.val == key and q:
      return q[0]

  # no match found
  return None


def main():
  root = TreeNode(1);
  root.left = TreeNode(2);
  root.right = TreeNode(3);
  root.left.left = TreeNode(4);
  root.left.right = TreeNode(5);
  
  result = find_successor(root, 3)
  if result:
    print(result.val)

  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  
  result = find_successor(root, 9)
  if result:
    print(result.val)
  
  result = find_successor(root, 12)
  if result:
    print(result.val)


main()