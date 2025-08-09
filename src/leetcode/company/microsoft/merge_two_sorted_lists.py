# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(m + n), m nodes in List1, n nodes in List2
    Space: O(1)
    """

    def mergeTwoLists(self, list1, list2):

        p1, p2 = list1, list2

        dummy = ListNode(-1, None)

        curr = dummy

        while p1 and p2:
            if p1.val < p2.val:
                curr.next = p1
                p1 = p1.next
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next

        if p1:
            curr.next = p1
        if p2:
            curr.next = p2

        return dummy.next
