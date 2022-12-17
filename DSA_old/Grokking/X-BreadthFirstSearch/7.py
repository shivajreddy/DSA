from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right, self.next = None, None, None

  # level order traversal using 'next' pointer
  def print_level_order(self):
    nextLevelRoot = self
    while nextLevelRoot:
      current = nextLevelRoot
      nextLevelRoot = None
      while current:
        print(str(current.val) + " ", end='')
        if not nextLevelRoot:
          if current.left:
            nextLevelRoot = current.left
          elif current.right:
            nextLevelRoot = current.right
        current = current.next
      print()


def connect_level_order_siblings(root):
  # TODO: Write your code here

  #* My own method -> not so clean
  # q = deque()
  # q.append(root)

  # while q:

  #   size = len(q)
  #   for i in range(size):
  #     curr = q.popleft()
  #     if curr.left:
  #       q.append(curr.left)
  #     if curr.right:
  #       q.append(curr.right)
  #     if i == size-1:
  #       curr.next = None
  #     else:
  #       curr.next = q[0]
  # return

  q = deque()
  q.append(root)

  while q:
    # depth level
    prevNode = None
    for _ in range(len(q)):
      curr = q.popleft()
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
      if prevNode:
        prevNode.next = curr
      prevNode = curr

def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  connect_level_order_siblings(root)

  print("Level order traversal using 'next' pointer: ")
  root.print_level_order()


main()