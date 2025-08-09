'''
TimeStamps:
1. Understand the Problem: 00:00 - 00:53 (1 MIN)
2. Design&Verify Solution: 00:53 - 08:12 (8 MIN)
3. Code & Pass Test Cases: 08:12 - 10:00 (2 MIN)

TIME : O(N)
SPACE: O(1)

   None    1 -> 2
    p      c    n

   None <- 1    2
    p      c    n

   None <- 1    2 -> 3
           p    c    n

   None <- 1 <- 2    3
           p    c    n

   None <- 1 <- 2    3 -> 4
                p    c    n

   None <- 1 <- 2 <- 3   4
                p    c   n

'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev = None

        curr = head


        while curr:

            nxt = curr.next          # safe-keeping

            curr.next = prev         # reverse connection

            # moving prev, curr pointers
            prev = curr
            curr = nxt

        return prev

