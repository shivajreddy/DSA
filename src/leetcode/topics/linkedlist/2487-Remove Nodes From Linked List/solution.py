"""
# 2487 -Remove Nodes From Linked List
[LeetCode](https://leetcode.com/problems/remove-nodes-from-linked-list/description/)


TimeStamps:
1. Understand the Problem: 00:00 - 00:00 (00 MIN)
2. Design&Verify Solution: 00:00 - 00:00 (00 MIN)
3. Code & Pass Test Cases: 00:00 - 00:00 (00 MIN)
"""

'''

Assumptions:
    - do not remove node, for having a right side node that is == curr-node

Observations:
    - tail node always get's added, cuz no nodes on the right side of tail.
    - at every node during traversal
            - must look at all nodes on it's right side

Test Case:

IN : 5
OUT: 5

IN : 1 1 1
OUT: 1 1 1

IN : 10 8 7 5
OUT: 10 8 7 5

IN : 1 2 3 4 5
OUT: 5

IN : 5 2 13 3 8
OUT: 13 8

'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:


        # helper functio to reverse the given list
        # O(N)
        def reverse(node):
            prev = None
            curr = node
            while curr:
                nxt = curr.next

                # p  c -> n
                # p <- c   n
                #      p   c
                curr.next = prev

                prev = curr
                curr = nxt
            
            return prev
        
        head_of_reveresed = reverse(head)

        prev = head_of_reveresed
        curr = head_of_reveresed.next

        while curr:
            if curr.val >= prev.val:
                prev.next = curr
                prev = curr
                curr = curr.next
            else:
                nxt = curr.next 

                prev.next = None
                curr.next = None
                del(curr)

                curr = nxt

        return reverse(head_of_reveresed)

