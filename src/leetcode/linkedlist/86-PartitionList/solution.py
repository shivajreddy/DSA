from typing import Optional

class ListNode:
    def __init__(self, val, next=None) -> None:
        self.val = val
        self.next = next

'''
Workflow Timestamps
1. Understand the Problem:
2. Design&Verify Solution:
3. Code & Pass Test Cases:

Test Cases:
IN : x=3    1-1  
OUT: 1-1

IN : x=3    4-5
OUT: 4-5

IN: x=3  1-2-1-5-4
OUT: 1-2-1-5-4


Lesson Learnt:
Test Cases: Didn't add any new test cases. TestCases for this question should be
1. waht if all are smaller than x. 2. what if all are >= than x
3. what already partitioned

Approach: Not simple. all over the place.
- not sure where to start 'prev' pointer

'''

class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:

        d1 = ListNode(-1, None)
        d2 = ListNode(-1, None)

        small, big = d1, d2

        curr = head

        while curr:

            # found a node < x
            if curr.val < x:

                nxt = curr.next     # safe-keeping

                # add curr node to small linked list
                small.next = curr
                curr.next = None

                # move pointers
                small = small.next
                curr = nxt
            
            # found a node >= x
            else:
                nxt = curr.next     # safe-keeping

                # add curr node to big linked list
                big.next = curr
                curr.next = None

                # move pointers
                big = big.next 
                curr = nxt
        
        # point big list to the end of small linked list
        small.next = d2.next

        return d1.next
