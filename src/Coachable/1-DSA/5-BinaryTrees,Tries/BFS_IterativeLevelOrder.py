import collections

from TreeSamples import TreeNode, binary_tree_1
from collections import deque


def iterative_level_order(root: TreeNode):
    q = deque()
    q.append(root)
    result = []

    while q:
        curr_lvl = []
        for _ in range(len(q)):
            curr = q.popleft()
            curr_lvl.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        result.append(curr_lvl)
    return result


# print(iterative_level_order(binary_tree_1))

# iterative level order
def level_order_traversal(root):
    q = collections.deque([root])
    while q:
        x = q.popleft()
        if x is not None:
            print(x.val)
            q.append(x.left)
            q.append(x.right)


# iterative for inorder (much more complex than recursive):
def inorderTraversal(root):
    stack = []  # keep track of previously seen nodes
    node = root  # current node
    while (node):  # do pre processing to traverse down left side and record previously seen nodes
        stack.append(node)
        node = node.left

    while (stack):  # while there are nodes that we have seen and not processed
        cur = stack.pop()
        print(cur.val)  # if there are no more left children then we can print it
        if cur.right:  # now we have to add its right child to seen and go down its left subtree
            node = cur.right
            while (node):  # go down left subtree
                stack.append(node)
                node = node.left
