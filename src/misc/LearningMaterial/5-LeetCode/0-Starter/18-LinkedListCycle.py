from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # approach is two pointers: slow, fast
        # intuition: start two pointers at a dummy node. First move the slow to dummy.next
        # and fast to dummy.next.next, then check if they point to same node, else shift.
        # repeat this until fast reaches end, or slow meets fast

        # create a dummy node that points to given head, both pointers start at dummy.
        # if fast and slow meet then there is a cycle.
        # if fast reaches end, then there is NO cycle.

        # Edge Case 1: if there is single node, and it's next is itself.
        # Null case: there are 0 nodes in the linkedlist

        if not head:
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False
