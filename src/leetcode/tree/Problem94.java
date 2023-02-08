package leetcode.tree;

import java.util.ArrayList;
import java.util.List;
import java.util.Stack;


public class Problem94 {
	public static void main(String[] args) {

	}
}

/****************************
 * TreeNode
 ***************************/
class TreeNode {
	int val;
	TreeNode left;
	TreeNode right;

	TreeNode() {
	}

	TreeNode(int val) {
		this.val = val;
	}

	TreeNode(int val, TreeNode left, TreeNode right) {
		this.val = val;
		this.left = left;
		this.right = right;
	}
}


/****************************
 * Recursive solution
 ***************************/
class Solution {
	public List<Integer> inorderTraversal(TreeNode root) {
		List<Integer> result = new ArrayList<>();
		dfs(root, result);
		return result;
	}

	private void dfs(TreeNode root, List<Integer> result) {
		if (root == null) return;
		dfs(root.left, result);
		result.add(root.val);
		dfs(root.right, result);
	}
}

/****************************
 * Iterative Solution
 ***************************/
class Solution2 {
	public List<Integer> inorderTraversal(TreeNode root) {
		List<Integer> res = new ArrayList<>();
		if (root == null) return res;

		Stack<TreeNode> stack = new Stack<>();
		stack.add(root);
		TreeNode curr = root;
		while (!stack.isEmpty() && curr != null) {
			res.add(curr.val);
			curr = curr.left;
			stack.push(curr.left);
			curr = curr.right;
			stack.push(curr.right);
		}
		return res;
	}
}
