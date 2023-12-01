# https://leetcode.com/problems/reverse-linked-list/
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # create two pointers to track the current and previous,
        # before entering the loop
        c = head
        p = None

        while c:
            # Toggle them
            n = c.next
            c.next = p

            # move both pointers
            p = c
            c = n

        return p
