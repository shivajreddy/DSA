package leetcode.tree;

import java.util.ArrayList;
import java.util.Stack;


public class Test {
	/*
	input array -> [10, 20, 30, 40, -1, 50, 60, -1, -1, -1, -1, 70, -1, -1, -1]
	 */
	public static void main(String[] args) {

		int[] arr = new int[]{10, 20, 30, 40, -1, 50, 60, -1, -1, -1, -1, 70, -1, -1, -1};
		Node root = Tree.create(arr);


	}
}

class BinaryTree {
	private static ArrayList<Integer> result = new ArrayList<>();
	private BinaryTree() {
	}

	public void bfs(Node root) {

		Stack<Integer> stack = new Stack<>();
		while (root != null && !stack.isEmpty()) {
			System.out.println(root.getVal());
			bfs(root.getLeft());
			bfs(root.getRight());
			result.stream().toList();
		}
	}
}

