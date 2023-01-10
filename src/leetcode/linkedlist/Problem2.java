package leetcode.linkedlist;

public class Problem2 {
    public static void main(String[] args) {

        ListNode head1 = new ListNode(2);
        head1.next = new ListNode(4);
        head1.next.next = new ListNode(7);

        ListNode head2 = new ListNode(5);
        head2.next = new ListNode(6);
        head2.next.next = new ListNode(4);
        head2.next.next.next = new ListNode(9);

        Problem2Solution solution = new Problem2Solution();
        solution.addTwoNumbers(head1, head2);
    }
}

class Problem2Solution {


    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        ListNode dummyHead = new ListNode(0);
        ListNode curr = dummyHead;

        int carry = 0;

        // as long as l1 or l2 are in bounds or carry exists
        while (l1 != null || l2 != null || carry != 0) {
            // x, y represents the curr val of node. 0 if no node.
            // easy to assume 0 if no need, when two lists are diff. sizes
            int x = (l1 != null) ? l1.val : 0;
            int y = (l2 != null) ? l2.val : 0;

            int sum = x + y + carry;
            // carried over value => given / 10 = val to carry over
            // 12 / 10 = 1, 7 / 10 = 0, 10 / 10 = 1
            carry = sum / 10;

            // reminder => given % 10 = val to add as next node
            // 12 % 10 = 2, 7 % 10 = 7, 10 % 10 = 0
            curr.next = new ListNode(sum % 10);
            curr = curr.next;

            // move nodes of lists if not at end
            if (l1 != null) l1 = l1.next;
            if (l2 != null) l2 = l2.next;

        }
        return dummyHead.next;

    }

}

class MyProblem2Solution {

    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {

        String str1 = convertToString(l1);
        String str2 = convertToString(l2);

        // int num1 = Integer.parseInt(str1);
        // int num2 = Integer.parseInt(str2);

        // String strResult = String.valueOf(num1 + num2);

        String strResult = addTwoStrings(str1, str2);

        System.out.println("str1 =" + str1);
        System.out.println("str2 =" + str2);
        System.out.println("strresult = " + strResult);

        ListNode resultNode = createReverseLinkedList(strResult);

        return resultNode;
    }

    private static String convertToString(ListNode head) {
        StringBuilder sb = new StringBuilder();
        while (head != null) {
            sb.append(head.val);
            head = head.next;
        }
        return sb.reverse().toString();
    }

    private static ListNode createReverseLinkedList(String input) {

        String reverseString = new StringBuilder(input).reverse().toString();

        int firstValue = Integer.parseInt(String.valueOf(reverseString.charAt(0)));
        ListNode head = new ListNode(firstValue);

        ListNode curr = head;
        for (int i = 1; i < input.length(); i++) {
            int num = Integer.parseInt(String.valueOf(reverseString.charAt(i)));
            curr.next = new ListNode(num);
            curr = curr.next;
        }
        return head;
    }

    private static String addTwoStrings(String str1, String str2) {

        StringBuilder sb = new StringBuilder();

        int i = str1.length() - 1, j = str2.length() - 1;

        int bal = 0;
        while (i >= 0 && j >= 0) {

            int num1 = Integer.parseInt(String.valueOf(str1.charAt(i)));
            int num2 = Integer.parseInt(String.valueOf(str2.charAt(j)));

            int sum = bal + num1 + num2;
            if (sum >= 10) {
                sb.append(sum - 10);
                bal = 1;
            } else {
                sb.append(sum);
                bal = 0;
            }
            i--;
            j--;
        }
        while (i >= 0) {
            int num1 = Integer.parseInt(String.valueOf(str1.charAt(i)));
            int sum = bal + num1;
            if (sum >= 10) {
                sb.append(sum - 10);
                bal = 1;
            } else {
                sb.append(sum);
                bal = 0;
            }
            i--;
        }
        while (j >= 0) {
            int num2 = Integer.parseInt(String.valueOf(str2.charAt(j)));
            int sum = bal + num2;
            if (sum >= 10) {
                sb.append(sum - 10);
                bal = 1;
            } else {
                sb.append(sum);
                bal = 0;
            }
            j--;
        }
        if (bal > 0) sb.append(bal);
        return sb.reverse().toString();
    }
}
