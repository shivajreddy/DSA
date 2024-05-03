package leetcode.linkedlist;

public class Problem234 {
    public static void main(String[] args) {
        Problem234Solution solution = new Problem234Solution();
        ListNode one = new ListNode(1);
        one.next = new ListNode(1);
        one.next.next = new ListNode(2);
        one.next.next.next = new ListNode(1);
        // one.next.next.next.next = new ListNode(1);
        // one.next.next.next.next.next = new ListNode(2);
        boolean result = solution.isPalindrome(one);
        System.out.println(result);
    }
}


/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode() {}
 * ListNode(int val) { this.val = val; }
 * ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */


class Problem234Solution {
    public boolean isPalindrome(ListNode head) {

        ListNode tail = null;
        ListNode curr = head;

        int count = 0;
        while (curr != null) {
            tail = head;
            curr = head.next;
            count++;
        }

        if (count < 2) return true;

        int p = 0;
        ListNode midNode = head;
        while (p < count / 2) {
            midNode = midNode.next;
            p++;
        }
        reverseLinkedList(midNode);

        ListNode left = head;
        while (left != null && tail != null) {
            if (left.val != tail.val) {
                return false;
            }
            left = left.next;
            tail = tail.next;
        }

        return true;

    }

    private ListNode reverseLinkedList(ListNode head) {

        ListNode temp = null;

        while (head != null) {

            ListNode nxt = head.next;
            head.next = temp;

            temp = head;
            head = nxt;
        }
        return temp;
    }
}
