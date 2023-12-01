from stencil import *


def test_max_leaf_height_diff():
    # test case 1
    """
            1
        2       3
    4     5         6
         7
    """
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.left.right.left = TreeNode(7)
    root.right.right = TreeNode(6)

    assert root.height() == 4
    assert root.lowest_leaf_height() == 3
    assert root.max_leaf_height_diff() == 1

    # test case 2
    '''
            1
        2       3
      4       5
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)

    assert root.height() == 3
    assert root.lowest_leaf_height() == 3
    assert root.max_leaf_height_diff() == 0

    # test case 3
    '''
            1
    '''
    root = TreeNode(1)

    assert root.height() == 1
    assert root.lowest_leaf_height() == 1
    assert root.max_leaf_height_diff() == 0

    # tet case 4
    '''
            1
        2       3
      4       5
     6
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.left.left = TreeNode(6)
    root.right.left = TreeNode(5)

    assert root.height() == 4
    assert root.lowest_leaf_height() == 3
    assert root.max_leaf_height_diff() == 1

    # test case 5
    '''
            1
        2       3
    4     5        6
  7     8        9
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    root.right.right = TreeNode(6)
    root.right.right.left = TreeNode(9)
    root.left.left.left = TreeNode(7)
    root.left.right.left = TreeNode(8)

    assert root.height() == 4
    assert root.lowest_leaf_height() == 4
    assert root.max_leaf_height_diff() == 0

    # test case 6
    '''
            1
        2
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)

    assert root.height() == 2
    assert root.lowest_leaf_height() == 2
    assert root.max_leaf_height_diff() == 0

    # test case 7
    '''
            1
              2
    '''
    root = TreeNode(1)
    root.right = TreeNode(2)

    assert root.height() == 2
    assert root.lowest_leaf_height() == 2
    assert root.max_leaf_height_diff() == 0

    # test case 8
    '''
            1
        2       3
             4     5
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.right.left = TreeNode(4)
    root.right.right = TreeNode(5)

    assert root.height() == 3
    assert root.lowest_leaf_height() == 2
    assert root.max_leaf_height_diff() == 1

    # test case 9
    '''
            1
        2       3
      4       5
            6
    '''
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.right.left = TreeNode(5)
    root.right.left.left = TreeNode(6)

    assert root.height() == 4
    # TODO: not sure below values
    # assert root.lowest_leaf_height() == 3
    # assert root.max_leaf_height_diff() == 1
