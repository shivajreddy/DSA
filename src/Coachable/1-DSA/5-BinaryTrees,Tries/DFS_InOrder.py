from TreeSamples import TreeNode, binary_tree_1, binary_tree_2


def inorder(root: TreeNode) -> list[int]:
    def dfs(node: TreeNode, arr: list):
        if not node:
            return
        dfs(node.left, arr)
        arr.append(node.val)
        dfs(node.right, arr)

    result = []
    dfs(root, result)
    return result


print(inorder(binary_tree_2))
