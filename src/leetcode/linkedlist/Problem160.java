package leetcode.linkedlist;


public class Problem160 {
    public static void main(String[] args) {
        Problem160Solution solution = new Problem160Solution();

        ListNode head1 = CreateListNode.usingArray(new int[]{4, 1, 8, 4, 5});
        ListNode head2 = CreateListNode.usingArray(new int[]{5, 6, 1, 8, 4, 5});
        // 3rd item of list2, 2nd item of list1 is the common node
        head2.next.next = head1.next;

        ListNode result = solution.getIntersectionNode(head1, head2);
        System.out.println(result.val);

    }
}

/**
 * Definition for singly-linked list.
 * public class ListNode {
 * int val;
 * ListNode next;
 * ListNode(int x) {
 * val = x;
 * next = null;
 * }
 * }
 */
class Problem160Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode l1 = headA, l2 = headB;

        while (l1 != l2) {
            l1 = (l1 != null) ? l1.next : headB;
            l2 = (l2 != null) ? l2.next : headA;
        }
        return l1;
    }
}
