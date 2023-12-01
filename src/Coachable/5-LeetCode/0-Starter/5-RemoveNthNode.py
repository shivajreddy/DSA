# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        size = 0

        curr = head
        while curr:
            size += 1
            curr = curr.next

        safe = ListNode()
        safe.next = head

        size = size - n

        curr = safe
        while size > 0:
            size -= 1
            curr = curr.next

        curr.next = curr.next.next
        return safe.next
