from typing import *

'''
Find the max diff. in height among all leaf nodes

            
            1
        2       3
    4     5     
  8
  
  This tree would have
  height() == 4 (Node 8)
  lowest_leaf_height() == 2 (Node 3)
  max_leaf_height_diff() == 2 (Difference b/w heights of  8 and 3 is 2)
'''


class TreeNode:
    def __init__(self, val: int, left: 'TreeNode' = None, right: 'TreeNode' = None):
        self.val = val
        self.left = left
        self.right = right

    # Returns the height of the binary tree
    def height(self) -> int:
        curr = self

        # base case
        if not curr:
            return 0

        left_tree = (curr.left.height()) if curr.left else 0
        right_tree = (curr.right.height()) if curr.right else 0

        return max(left_tree, right_tree) + 1

    # returns the lowest ht. of any leaf in the bt
    def lowest_leaf_height(self) -> int:
        curr = self

        # base case
        if not curr:
            return 0

        left_tree = (curr.left.height()) if curr.left else 0
        right_tree = (curr.right.height()) if curr.right else 0

        if left_tree and right_tree:
            return min(left_tree, right_tree) + 1
        if left_tree:
            return left_tree + 1
        if right_tree:
            return right_tree + 1
        return 1

    # r find hte the max diff in ht b/w 2 leaf nodes
    def max_leaf_height_diff(self) -> int:
        return self.height() - self.lowest_leaf_height()
