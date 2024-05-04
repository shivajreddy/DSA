from typing import Optional

class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        d1 = ListNode(-1, None)
        d2 = ListNode(-1, None)

        small, big = d1, d2

        curr = head

        while curr:

            if curr.val < x:

                nxt = curr.next

                small.next = curr
                curr.next = None

                small = small.next
                curr = nxt
            
            else:
                nxt = curr.next

                big.next = curr
                curr.next = None

                big = big.next
                curr = nxt
        
        small.next = d2.next

        return d1.next

