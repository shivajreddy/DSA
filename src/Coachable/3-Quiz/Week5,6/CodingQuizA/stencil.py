from treeNode import TreeNode
from narytreenode import NaryTreeNode
import collections


# In-order
def question1(node: TreeNode) -> list[int]:
    if not node:
        return []
    return question1(node.left) + [node.val] + question1(node.right)
    # visited = []
    #
    # def dfs(root: TreeNode, arr: list[int]):
    #     if not root:
    #         return
    #     dfs(root.left, arr)
    #     arr.append(root.val)
    #     dfs(root.right, arr)
    #
    # dfs(node, visited)
    # return visited


# Pre-order
def question2(node: TreeNode) -> list[int]:
    if not node:
        return []
    return [node.val] + question2(node.left) + question2(node.right)
    # visited = []
    #
    # def dfs(root: TreeNode, arr: list[int]):
    #     if not root:
    #         return
    #     arr.append(root.val)
    #     dfs(root.left, arr)
    #     dfs(root.right, arr)
    #
    # dfs(node, visited)
    # return visited


# Post-order
def question3(node: TreeNode) -> list[int]:
    if not node:
        return []
    return question3(node.left) + question3(node.right) + [node.val]
    # visited = []
    #
    # def dfs(root: TreeNode, arr: list[int]):
    #     if not root:
    #         return
    #     dfs(root.left, arr)
    #     dfs(root.right, arr)
    #     arr.append(root.val)
    #
    # dfs(node, visited)
    # return visited


# BFS
def question4(node: TreeNode) -> list[int]:
    """
    # Using Level Order Traversal
    visited = []
    q = collections.deque([node])
    while q:
        curr = q.popleft()
        if curr is not None:
            visited.append(curr.val)
            q.append(curr.left)
            q.append(curr.right)

    return visited
    """
    # Using Iterative level order
    q = collections.deque([node])
    visited = []
    visited_by_lvl = []
    while q:
        lvl = []
        for _ in range(len(q)):
            curr = q.popleft()
            lvl.append(curr.val)
            visited.append(curr.val)
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        visited_by_lvl.append(lvl)

    return visited


# return the size of each subtree
def question5(node: NaryTreeNode) -> dict[str, int]:
    q = collections.deque([node])
    result = {}

    def count_nodes(root: NaryTreeNode) -> int:
        count = 1
        if not root:
            return count
        for child_node in root.children:
            count += count_nodes(child_node)
        return count

    while q:
        for _ in range(len(q)):
            curr = q.popleft()
            for child in curr.children:
                q.append(child)
            result[curr.val] = count_nodes(curr)
    return result
