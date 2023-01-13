package leetcode.linkedlist;

public class Problem143 {
    public static void main(String[] args) {

        Problem143Solution solution = new Problem143Solution();

        ListNode head = LinkedList.usingArray(new int[]{1, 2, 3, 4});

        LinkedList.printLinkedList(head);
        LinkedList.printLinkedList(LinkedList.reverseLinkedList(head));
    }
}

class Problem143Solution {
    public void reorderList(ListNode head) {

        ListNode reverseHead = head;

    }
}
