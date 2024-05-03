package leetcode.linkedlist;

public class ListNode {

    int val;
    ListNode next;

    ListNode() {
    }

    ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class LinkedList {

    public static ListNode usingArray(int[] array) {

        ListNode dummyHead = new ListNode(0);

        ListNode curr = dummyHead;
        for (int num : array) {
            curr.next = new ListNode(num);
            curr = curr.next;
        }
        curr.next = null;
        return dummyHead.next;
    }

    public static void printLinkedList(ListNode head) {
        StringBuilder sb = new StringBuilder();
        while (head != null) {
            sb.append(head.val).append(" -> ");
            head = head.next;
        }
        sb.append("null");
        System.out.println(sb.toString());
    }

    public static ListNode reverseLinkedList(ListNode head) {

        ListNode prev = null;

        ListNode curr = head;
        while (curr != null) {

            ListNode nxt = curr.next;

            curr.next = prev;

            // move pointers
            prev = curr;
            curr = nxt;
        }
        return prev;
    }

}
