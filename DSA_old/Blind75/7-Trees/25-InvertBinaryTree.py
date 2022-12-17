# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


from collections import deque


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return root

        # bfs approach
        q = deque()
        q.append(root)

        while q:
            curr = q.pop()
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
            # swap the child
            curr.left, curr.right = curr.right, curr.left

        return root


# using recursive call
class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        if root == None:
            return None

        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)




"""Notes:

both approaches take same time.
Think of reverse as mirror, consider the base case, if you reverse childs of a give node, then thats it.
Reverse like this for all the nodes. done.

"""