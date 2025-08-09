class TreeNode:
    def __init__(self,
                 val: int,
                 left: 'TreeNode | None' = None,
                 right: 'TreeNode | None' = None):
        self.val = val
        self.left = left
        self.right = right


'''
           5
         /   \
        3     7
       /     / \
      2     6   8
       
'''
tree = TreeNode(5, (TreeNode(3, TreeNode(2))), (TreeNode(7, (TreeNode(6)), (TreeNode(8)))))


# DFS Preorder
def preorder(root: TreeNode) -> list[int]:
    def dfs(node: TreeNode, arr: list[int]):
        if not node:
            return
        arr.append(node.val)
        dfs(node.left, arr)
        dfs(node.right, arr)

    result = []
    dfs(root, result)
    return result


# DFS Inorder
def inorder(root: TreeNode) -> list[int] | None:
    def dfs(node: TreeNode, arr: list[int]):
        if not node:
            return
        dfs(node.left, arr)
        result.append(node.val)
        dfs(node.right, arr)

    result = []
    dfs(root, result)
    return result


# DFS postorder
def postorder(root: TreeNode) -> list[int] | None:
    def dfs(node: TreeNode, arr: list[int]):
        if not node:
            return
        dfs(node.left, arr)
        dfs(node.right, arr)
        result.append(node.val)

    result = []
    dfs(root, result)
    return result


print(preorder(tree))
print(inorder(tree))
print(postorder(tree))
