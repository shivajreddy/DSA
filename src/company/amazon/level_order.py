from typing import Deque, List, Optional, Tuple
from collections import deque
from collections import defaultdict


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        q: Deque[Tuple[TreeNode | None, int]] = deque([(root, 0)])
        res = defaultdict(list)

        while q:
            node, lvl = q.popleft()

            if not node:
                continue

            res[lvl].append(node.val)

            q.append((node.left, lvl + 1))
            q.append((node.right, lvl + 1))

        return list(res.values())
