package Coachable.DS.StackAndQueue;

import edu.princeton.cs.algs4.StdIn;
import edu.princeton.cs.algs4.StdOut;

import java.util.Stack;


public class Reverse {

	Stack<Character> stack = new Stack<>();

	public static void main(String[] args) {
		while (!StdIn.isEmpty()) {
			String item = StdIn.readString();
			StdOut.print(item);
		}
	}
}

