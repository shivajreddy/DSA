from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

def traverse(root):

  #* Summary
  #? 1. Same as problem 2, but, changing the direction of values being added to the currentLevel array.
  #? 2. To do that, need a bool to toggle direction. Also, need a deque to add values in a level instead of array.
  #? 3. After the for loop (iterate through all the nodes in the level) toggle the direction.
  #? 4. Inside the for loop, add values to the right or left, based on the direction.

  result = []
  q = deque()
  q.append(root)    #? 1.
  leftToRight = True

  while q:
    currLevel = deque()   #? 2. ability to append left, based on the boolean

    for _ in range(len(q)):
      curr = q.popleft()
      
      if leftToRight:     #? 4. Add to the current deque, based on direction
        currLevel.append(curr.val)
      else:
        currLevel.appendleft(curr.val)
      
      # add child nodes   #? 1.
      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)

    result.append(list(currLevel))
    leftToRight = not leftToRight   #? 3. toggle direction, after adding all nodes in a level

  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.right.left.left = TreeNode(20)
  root.right.left.right = TreeNode(17)
  print("Zigzag traversal: " + str(traverse(root)))


main()