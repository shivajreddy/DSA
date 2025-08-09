package Coachable.DS.tree;

import java.util.ArrayList;
import java.util.LinkedList;
import java.util.List;
import java.util.Queue;


public class Traversal {
	public static void main(String[] args) {

		int[] arr = new int[]{999, 10, 20, 30, -1, -1, -1, -1};
		TreeNode root = CreateTree.usingArray(arr);
		//System.out.println(root);
		recursive(root);
	}

	private static void iterativePreOrder(TreeNode root) {

	}

	private static List<Integer> recursive(TreeNode root) {
		List<Integer> result = new ArrayList<>();
		//dfsPre(root, result);
		dfsIn(root, result);
		//dfsPost(root, result);
		System.out.println(result);
		return result;
	}

	private static void dfsPre(TreeNode root, List<Integer> result) {
		if (root == null) return;
		result.add(root.val);
		dfsPre(root.leftChild, result);
		dfsPre(root.rightChild, result);
	}

	private static void dfsIn(TreeNode root, List<Integer> result) {
		if (root == null) return;
		result.add(root.val);
		dfsIn(root.leftChild, result);
		dfsIn(root.rightChild, result);
	}

	private static void dfsPost(TreeNode root, List<Integer> result) {
		if (root == null) return;
		result.add(root.val);
		dfsPost(root.leftChild, result);
		dfsPost(root.rightChild, result);
	}


}


class TreeNode {
	public TreeNode leftChild;
	public TreeNode rightChild;
	public int val;

	public TreeNode(int val) {
		this.val = val;
	}

	public TreeNode(TreeNode leftChild, int val, TreeNode rightChild) {
		this.leftChild = leftChild;
		this.val = val;
		this.rightChild = rightChild;
	}
}

class CreateTree {
	private CreateTree() {
	}

	public static TreeNode usingArray(int[] arr) {

		Queue<TreeNode> q = new LinkedList<>();
		TreeNode root = new TreeNode(null, arr[1], null);
		q.add(root);

		int i = 1, N = arr.length;
		while (!q.isEmpty() && i < N) {
			TreeNode p = q.remove();
			int leftIdx = i * 2, rightIdx = leftIdx + 1;
			System.out.println("leftIdx: " + leftIdx);
			if (leftIdx < N && arr[leftIdx] != -1) {
				p.leftChild = new TreeNode(arr[leftIdx]);
				q.add(p.leftChild);
			}
			if (rightIdx < N && arr[rightIdx] != -1) {
				p.rightChild = new TreeNode(arr[rightIdx]);
				q.add(p.rightChild);
				i++;
			}
		}
		return root;
	}
}