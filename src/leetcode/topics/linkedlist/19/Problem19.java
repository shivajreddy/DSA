package leetcode.linkedlist;

public class Problem19 {
}

class Problem19Solution {
    public ListNode removeNthFromEnd(ListNode head, int n) {
        if (head == null) return null;

        int size = 0;
        ListNode curr = head;
        while (curr != null) {
            size++;
            curr = curr.next;
        }
        int target = size - n;

        // if the first item to be removed, then return 2nd item in list
        // technically head still is attached to 2nd element. but its ok.
        if (target == 0) return head.next;

        ListNode dummyHead = new ListNode(0);
        curr = head;
        dummyHead.next = curr;
        int i = 0;
        while (curr != null) {
            if (i == target - 1) {
                if (curr.next.next != null) {
                    curr.next = curr.next.next;
                } else {
                    curr.next = null;
                }
                return dummyHead.next;
            }
            i++;
            curr = curr.next;
        }
        return dummyHead.next;
    }
}