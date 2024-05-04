'''
Workflow Timestamps
1. Understand the Problem: 0-5:10  (5 mins)
2. Design&Verify Solution: 5:10-10:54 (6 mins)
3. Code & Pass Test Cases: 11:00-28:44 (17 mins)


     S       E
IN : 1 2-3-4 5  
       -----    l=2, r=4
OUT: 1 4 3 2 5

IN : 1 2 3 4 5
     ---------  l=1, r=5
OUT: 5 4 3 2 1

IN : 1 1 1 1
       -----  l=2,r=4
OUT: 1 1 1 1

IN : 5
OUT: 5

TIME : O(N)
SPACE: O(1)

'''

from typing import Optional

class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:

        if not head:
            return

        target_node = None

        dummy = ListNode(-1, head)
        S, E = dummy, None

        curr, idx = head, 1

        while curr:
            if idx == left:
                S.next = None
                target_node = curr
                while idx < right:
                    curr = curr.next
                    idx += 1
                E = curr.next
                curr.next = None
                break

            idx += 1
            S = curr
            curr = curr.next
        
        def reverseList(node: ListNode):
            dummy = ListNode(-1, node)
            prev, curr = None, node

            while curr:
                nxt = curr.next 

                curr.next = prev
                prev = curr

                curr = nxt
            
            return (prev, dummy.next)
        
        s, e = reverseList(target_node)

        S.next = s
        e.next = E

        return dummy.next


        
