package leetcode.linkedlist;

import java.util.Stack;

public class Problem1265 {
}

/**
 * // This is the ImmutableListNode's API interface.
 * // You should not implement it, or speculate about its implementation.
 * interface ImmutableListNode {
 *      public void printValue(); // print the value of this node.
 *      public ImmutableListNode getNext(); // return the next node.
 * };
 */
interface ImmutableListNode {
    public void printValue(); // print the value of this node.

    public ImmutableListNode getNext(); // return the next node.
}


class Problem1265Solution {
    public void printLinkedListInReverse(ImmutableListNode head) {

        Stack<ImmutableListNode> stack = new Stack<>();
        while (head != null) {
            stack.push(head);
            head = head.getNext();
        }

        while (!stack.isEmpty()) stack.pop().printValue();

        // # using recursion
        // if (head == null) return;
        // printLinkedListInReverse(head.getNext());
        // head.printValue();
    }
}

