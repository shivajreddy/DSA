package leetcode.stack;

import java.util.ListIterator;
import java.util.Stack;

public class Problem232 {
    public static void main(String[] args) {
    }
}


class MyQueue {

    private Stack<Integer> stack = new Stack<>();

    public MyQueue() {
    }

    private Stack<Integer> makeReverse(Stack<Integer> stack) {
        Stack<Integer> reverseStack = new Stack<>();
        ListIterator<Integer> listIterator = stack.listIterator();
        while (listIterator.hasNext()) {
            listIterator.next();
        }
        while (listIterator.hasPrevious()) {
            reverseStack.push(listIterator.previous());
        }
        return reverseStack;
    }

    public void push(int x) {
        stack.push(x);
        // Stack<Integer> reverseStack = makeReverse(stack);
    }

    public int pop() {
        Stack<Integer> reverseStack = makeReverse(stack);
        int head = reverseStack.pop();
        stack = makeReverse(reverseStack);
        return head;
    }

    public int peek() {
        Stack<Integer> reverseStack = makeReverse(stack);
        return reverseStack.peek();
    }

    public boolean empty() {
        return stack.empty();
    }
}

/*
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */




/* Stack
 * Collection(I) -- List(I) -- Vector(I) --
 *  Stack<?> stack = new Stack<>();
 * stack.push(Object o) -> add o to the top of the stack.
 * stack.pop() -> remove and return the top. if no top -> EmptyStackException
 * stack.peek() -> return the top. if no top -> EmptyStackException
 * boolean b = stack.empty()
 * int offset = stack.search(Object o) -> returns the o offset, if no o -> -1
 */