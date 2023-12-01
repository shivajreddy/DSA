"""
Trees for testing
"""


class TreeNode:

    def __init__(self, val=None, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def __str__(self):
        return str(self.val)


'''
Binary_Tree_1
          d
        /   \
       b     f
     /  \   / \
    a    c e   g
'''
binary_tree_1 = TreeNode('d')
binary_tree_1.left = TreeNode('b')
binary_tree_1.right = TreeNode('f')
binary_tree_1.left.left = TreeNode('a')
binary_tree_1.left.right = TreeNode('c')
binary_tree_1.right.left = TreeNode('e')
binary_tree_1.right.right = TreeNode('g')

'''
Binary_Tree_2
          10
        /    \
       6      15
     /  \    /  \
    2    7  12   20
     \
      4
      /\
     3  5
'''
binary_tree_2 = TreeNode(10)
binary_tree_2.left = TreeNode(6)
binary_tree_2.left.left = TreeNode(2)
binary_tree_2.left.right = TreeNode(7)
binary_tree_2.left.left.right = TreeNode(4)
binary_tree_2.left.left.right.left = TreeNode(3)
binary_tree_2.left.left.right.right = TreeNode(5)
binary_tree_2.right = TreeNode(15)
binary_tree_2.right.left = TreeNode(12)
binary_tree_2.right.right = TreeNode(20)

'''
Binary_Search_Tree_1
          30
        /    \
       20     40
     /  \    /  \
    10   25 35   50
'''


def create_binary_search_tree_1():
    binary_search_tree_1 = TreeNode(30)
    binary_search_tree_1.left = TreeNode(20)
    binary_search_tree_1.right = TreeNode(40)
    binary_search_tree_1.left.left = TreeNode(10)
    binary_search_tree_1.left.right = TreeNode(25)
    binary_search_tree_1.right.left = TreeNode(35)
    binary_search_tree_1.right.right = TreeNode(50)
    return binary_search_tree_1


binary_search_tree_1 = create_binary_search_tree_1()

'''
binary_search_tree_2
          5
        /    \
       1      14
             /  \
            6    16
'''


def create_binary_search_tree_2():
    binary_search_tree_2 = TreeNode(5)
    binary_search_tree_2.left = TreeNode(1)
    binary_search_tree_2.right = TreeNode(14)
    binary_search_tree_2.right.left = TreeNode(6)
    binary_search_tree_2.right.right = TreeNode(16)
    return binary_search_tree_2


binary_search_tree_2 = create_binary_search_tree_2()
