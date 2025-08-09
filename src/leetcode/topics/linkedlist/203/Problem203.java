package leetcode.linkedlist;

public class Problem203 {
    public static void main(String[] args) {
        Problem203Solution solution = new Problem203Solution();
    }
}

class Problem203Solution {

    public ListNode removeElements(ListNode head, int val) {


        ListNode temp = new ListNode(0, head);

        ListNode prev = temp;
        ListNode curr = head;

        while (curr != null) {

            // curr node is the target
            if (curr.val == val) {
                prev.next = curr.next;
                ListNode nxt = curr.next;
                curr.next = null;
                curr = nxt;
            } else {
                // curr node is not the target
                prev = curr;
                curr = curr.next;
            }
        }
        // if (head != null && head.val == val) return null;
        return temp.next;


    }
}
