'''
237. Delete Node in a Linked List
https://leetcode.com/problems/delete-node-in-a-linked-list/description/
'''

'''
TimeStamps:
1. Understand the Problem: 00:00 - 00:00 (00 MIN)
2. Design&Verify Solution: 00:00 - 00:00 (00 MIN)
3. Code & Pass Test Cases: 00:00 - 00:00 (00 MIN)

- head is not given
- all nodes are unique
- node can be head
- node is NOT last node in linked list

4 - 5 - 1 - 9
    c   n

4   1   1   9 
        c   n 

4   1   9   9
            c   n

4   1   9   None 
                  c


1 2 3
-
c n
2 2 3
  c n
2 3 2
    c n
2 3 None 
         c


1 2
  -  
  c n
1 x 
    c

'''

from typing import Optional

class ListNode:
    def __init__(self, val, next = None) -> None:
        self.val = val
        self.next = None

class Solution:
    def deleteNode(self, node):

        # ''' Using single pointer
        # start curr pointer at the node that is to be removed
        curr = node

        while curr.next:
            nxt = curr.next     # mark the nxt node of curr pointer

            # remove curr-node value, by replacing with next pointer's value(if any)
            curr.val = nxt.val

            # if curr is pointing to the n-1th node, then curr's next should be removed
            if not nxt.next:
                curr.next = None

            # prev = curr
            curr = nxt      # move the curr pointer
        # '''


        ''' Using two pointers
        curr = node
        prev = None

        while curr.next:
            nxt = curr.next

            curr.val = nxt.val

            prev = curr
            curr = nxt
        
        # curr is now pointing to the last node, which is to be removed
        # so prev is pointing to the n-1th node
        prev.next = None

        # '''
