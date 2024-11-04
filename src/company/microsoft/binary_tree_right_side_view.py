from collections import deque
from typing import Optional, List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # DFS
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []

        def dfs(node, lvl):
            if not node:
                return

            if len(result) - 1 < lvl:
                result.append(0)

            result[lvl] = node.val

            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)

        dfs(root, 0)

        return result

    # BFS
    def rightSideView_bfs(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        q = deque([(root, 1)])
        res = []
        curr_lvl = 0

        while q:
            node, lvl = q.popleft()

            # Only add the first node encountered at each level(right most)
            if lvl > curr_lvl:
                res.append(node.val)
                curr_lvl = lvl

            if node.right:
                q.append((node.right, lvl + 1))
            if node.left:
                q.append((node.left, lvl + 1))

        return res
