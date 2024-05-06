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
    // Time : O(n), Space: O(1)
    public void reorderList(ListNode head) {
        if (head == null) return;

        ListNode first = head;
        ListNode middleNode = getMiddleNode(head); // O(n)
        ListNode second  = reverseList(middleNode); // O(n/2)

        mergeLists(first, second); // O(n/2)
    }
    private static ListNode getMiddleNode(ListNode head){
        ListNode slow = head, fast = head;
        while (fast != null && fast.next != null){
            slow = slow.next;
            fast = fast.next.next;
        }
        return slow;
    }
    private static ListNode reverseList(ListNode head){
        ListNode prev = null;
        while (head != null){
            ListNode nxt = head.next;
            head.next = prev;

            prev = head;
            head = nxt;
        }
        return prev;
    }
    private static void mergeLists(ListNode first, ListNode second){
        ListNode nxt, nxt2;
        while (second.next != null){
            nxt = first.next;
            first.next = second;
            first = nxt;

            nxt2 = second.next;
            second.next = first;
            second = nxt2;
        }
    }
}