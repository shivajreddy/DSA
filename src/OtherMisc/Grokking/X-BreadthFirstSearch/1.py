from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def traverse(root):
  
  #* Main Code here

  result = []

  q = deque()
  q.append(root)

  while q:  # if q length = 0, q is None

    currLevel = []

    for _ in range(len(q)):     # looping n times the no:of child nodes in the queue
      curr = q.popleft()
      currLevel.append(curr.val)
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
    
    result.append(currLevel)

  return result



def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level order traversal: " + str(traverse(root)))

main()