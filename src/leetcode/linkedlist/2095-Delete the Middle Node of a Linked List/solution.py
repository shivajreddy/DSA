"""
# 2095 - Delete the Middle Node of a Linked List
[LeetCode](https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/description/)


TimeStamps:
1. Understand the Problem: 00:00 - 00:00 (00 MIN)
2. Design&Verify Solution: 00:00 - 00:00 (00 MIN)
3. Code & Pass Test Cases: 00:00 - 00:00 (00 MIN)
"""


'''
Test Case

n  = 1 2 3 4 5
mid= 0 1 1 2 2

mid = int(n/2) or n // 2


         0
dummy -> 1
p        mid

         0    1
dummy -> 1 -> 2   None
         p   mid  nxt

         1 -> None
         p -> nxt



         0    1    2
dummy -> 1 -> 2 -> 3
         p   mid

         n = 3, mid = 3//2 = 1
         count = 0
         curr = dummy


O(N)
1. find, by going through the list
O(N)
2. find the mid's-previous, so start count=0, and curr pointing to dummy.
    stop once count == mid.
    curr is not pointing to mid's previous
    so delete mid node
3. return dummy.next which is the head


given a node delete it

  prev -> target -> nxt

  prev -> nxt    target  
  target.next = None
  prev.next = nxt


'''

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # 1. find length
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        # 2. find mid
        mid = n // 2 # or int(n/2)

        # 3. Traverse from dummy, with count as 0
        dummy = ListNode(-1, head)
        count = 0
        curr = dummy

        while curr:
            if count == mid:
                break
            count += 1
            curr = curr.next
        
        # curr is now pointing to target's previous node
        # delete target

        # curr -> target -> nxt
    
        target = curr.next
        nxt = target.next
    
        # curr -> nxt    target  
        target.next = None
        curr.next = nxt
        del(target)

        return dummy.next
