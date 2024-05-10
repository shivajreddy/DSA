"""
# 430 -  Flatten a Multilevel Doubly Linked List
[LeetCode](https://leetcode.com/problems/flatten-a-multilevel-doubly-linked-list/)


TimeStamps:
1. Understand the Problem: 00:00 - 00:00 (00 MIN)
2. Design&Verify Solution: 00:00 - 00:00 (00 MIN)
3. Code & Pass Test Cases: 00:00 - 00:00 (00 MIN)
"""


"""
# Definition for a Node.
class Node:
    def __init__(self, val, prev, next, child):
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child



 1  2  3  4  5  6
       
       3 <-> 7...10 <->4 
       |
       s      e
       7 8 9 10
         c n
         |
         11 12
         s  e

         8 <-> 11 ... 12 <-> 9 


Edge Cases:

IN : 1
     |
     2
     |
     3
OUT: 1 <-> 2 <-> 3

IN : []
OUT: []

IN : 1
OUT: 1


fn rec(node) -> s=node, e=?

- traverse through the list
- if there is a child, recursively call rec()
- if no child, move to the next node
- return the first and last nodes

rec(head)
return head

"""

from typing import Optional

class Node:
    def __init__(self, val, prev=None, next=None, child=None) -> None:
        self.val = val
        self.prev = prev
        self.next = next
        self.child = child


class Solution:
    def flatten(self, head: 'Optional[Node]') -> 'Optional[Node]':


        def recursively_get_first_and_last(node):

            prev = None
            curr = node

            while curr:
                # curr has children
                if curr.child:
                    # flatten it
                    S, E = recursively_get_first_and_last(curr.child)

                    nxt = curr.next

                    curr.next = S
                    S.prev = curr
                    curr.child = None

                    E.next = nxt
                    if nxt: nxt.prev = E

                    prev = E
                    curr = nxt

                else:
                    prev = curr
                    curr = curr.next

            return (node, prev)

        recursively_get_first_and_last(head)
        return head

