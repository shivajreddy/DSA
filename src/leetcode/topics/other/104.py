# 104 Maximum Depth of Binary Tree

# BFS


root = [3,9,20,0,0,15,7]
print('this is pop', root.pop())
print(root)
stack = [root]
result = []
while len(stack)>0:
    current = stack.pop()
    result.append(current.val)
    if current.right:
        stack.append(current.right)
    if current.left:
        stack.append(current.left)




while len(stack) != 0:
    if root.left :
        stack.append(root.left)
    if root.right:
        stack.append(root.right)
