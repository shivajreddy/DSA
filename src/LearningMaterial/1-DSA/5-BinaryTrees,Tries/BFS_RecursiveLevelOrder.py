from TreeSamples import TreeNode, binary_tree_1
# from Queue import Queue
from collections import deque


def recursive_level_order(root: TreeNode) -> list[int]:
    q = deque()
    q.append(root)

    result = []
    level_order_traversal = []

    while q:
        curr_lvl = []
        for _ in range(len(q)):
            curr = q.popleft()
            curr_lvl.append(curr.val if curr else None)
            if curr is not None:
                result.append(curr.val)
                q.append(curr.left)
                q.append(curr.right)
        level_order_traversal.append(curr_lvl)
        print(curr_lvl)
    # print(result)
    print("final =")
    print(level_order_traversal[-2])
    return result


recursive_level_order(binary_tree_1)
