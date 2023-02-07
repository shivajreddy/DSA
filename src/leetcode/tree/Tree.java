package leetcode.tree;


class Node {
	private int val;
	private Node next = null;
	private Node left = null;
	private Node right = null;

	public Node() {
	}

	public Node(int val) {
		this.val = val;
	}

	public Node(int val, Node next) {
		this.val = val;
		this.next = next;
	}

	public int getVal() {
		return val;
	}

	public void setVal(int val) {
		this.val = val;
	}

	public Node getNext() {
		return next;
	}

	public void setNext(Node next) {
		this.next = next;
	}

	public Node getLeft() {
		return left;
	}

	public void setLeft(Node left) {
		this.left = left;
	}

	public Node getRight() {
		return right;
	}

	public void setRight(Node right) {
		this.right = right;
	}
}


/*******************************
 * create a node based from a given array of items
 * assumes these items are given level by level
 * if a node is not present, give -1, else give value
 *******************************/

public class Tree {

	// Can't instantiate this class
	private Tree() {
	}

	public static Node create(int[] arr) {
		Node dummy = new Node();
		Node curr = dummy;

		int i = 0;
		int N = arr.length;
		while (i < N) {
			Node node = new Node(arr[i]);
			if (i * 2 < N) node.setLeft(new Node());

		}

		for (int num : arr) {
			if (num == -1) continue;
			curr.setNext(new Node(num));
			curr = curr.getNext();
		}
		return dummy.getNext();
	}
}

