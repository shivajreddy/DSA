# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # using bfs
        '''
        if not root:
            return 0

        q = deque([root])
        bfs = []

        while q:
            lvl = []
            for _ in range(len(q)):
                curr = q.popleft()
                lvl.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            bfs.append(lvl)

        print('bfs = ', bfs)
        return len(bfs)
        '''

        # using dfs
        def dfs(node):
            if not node:
                return 0
            return max(1 + dfs(node.left), 1 + dfs(node.right))

        return dfs(root)


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        stack = [[root, 1]]
        result = 0

        while stack:
            curr, depth = stack.pop()
            if curr:
                result = max(result, depth)
                stack.append([curr.right, depth + 1])
                stack.append([curr.left, depth + 1])

        return result
