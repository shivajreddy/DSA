from stencil import *
from treeNode import TreeNode
from narytreenode import NaryTreeNode

root = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
root2 = TreeNode(1, TreeNode(2, TreeNode(4), TreeNode(5)), TreeNode(3, TreeNode(6), TreeNode(7)))
nary_root = NaryTreeNode("A", [
    NaryTreeNode("B", []),
    NaryTreeNode("C", []),
    NaryTreeNode("D", [
        NaryTreeNode("E", []),
        NaryTreeNode("F", [])
    ])
])
nary_root2 = NaryTreeNode("A", [
    NaryTreeNode("B", []),
    NaryTreeNode("C", []),
    NaryTreeNode("D", [
        NaryTreeNode("E", []),
        NaryTreeNode("F", [])
    ])
])


def test_question1_case1():
    assert question1(root) == [4, 2, 5, 1, 6, 3, 7]


def test_question1_case2():
    assert question1(root2) == [4, 2, 5, 1, 6, 3, 7]


def test_question2_case1():
    assert question2(root) == [1, 2, 4, 5, 3, 6, 7]


def test_question2_case2():
    assert question2(root2) == [1, 2, 4, 5, 3, 6, 7]


def test_question3_case1():
    assert question3(root) == [4, 5, 2, 6, 7, 3, 1]


def test_question3_case2():
    assert question3(root2) == [4, 5, 2, 6, 7, 3, 1]


def test_question4_case1():
    assert question4(root) == [1, 2, 3, 4, 5, 6, 7]


def test_question4_case2():
    assert question4(root2) == [1, 2, 3, 4, 5, 6, 7]


def test_question5_case1():
    assert question5(nary_root) == {"A": 6, "B": 1, "c": 1, "D": 3, "E": 1, "F": 1}


def test_question5_case2():
    assert question5(nary_root2) == {"A": 6, "B": 1, "c": 1, "D": 3, "E": 1, "F": 1}
