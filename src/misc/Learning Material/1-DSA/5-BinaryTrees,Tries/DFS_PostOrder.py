from TreeSamples import TreeNode, binary_tree_1, binary_tree_2


def post_order(root: TreeNode) -> list[int]:
    def dfs(node: TreeNode, arr: list[int]):
        if not node:
            return
        dfs(node.left, arr)
        dfs(node.right, arr)
        arr.append(node.val)

    result = []
    dfs(root, result)
    return result


print(post_order(binary_tree_2))
