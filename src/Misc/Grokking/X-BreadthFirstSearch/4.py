from collections import deque

class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None

#1. while Queue is not empty
  #2. create an array to add all the averages in a level
  #3. Loop n times, where n is the no.of items in Queue
    # in each iteration, pop the first item in the q -> add the value of this node, to the currentLevel array
    # add child nodes of this popped item to the Queue, if present
  #4. currLevel is filled, find average of values in this array, add it to result array

def find_level_averages(root):
  result = []

  q = deque()
  q.append(root)

  while q:

    currLevel = 0
    n = len(q)

    for i in range(n):
      curr = q.popleft()
      currLevel += curr.val

      if curr.left:
        q.append(curr.left)
      if curr.right:
        q.append(curr.right)
    
    avg = currLevel/n
    result.append(avg)
  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.left.right = TreeNode(2)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  print("Level averages are: " + str(find_level_averages(root)))


main()