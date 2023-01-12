package leetcode.linkedlist;

public class ListNode {
    int val;
    ListNode next;

    public ListNode() {
    }

    public ListNode(int val) {
        this.val = val;
    }

    ListNode(int val, ListNode next) {
        this.val = val;
        this.next = next;
    }
}

class CreateListNode {

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


}
