"""
# 143. Reorder List
https://leetcode.com/problems/reorder-list/

TimeStamps:
1. Understand the Problem: 00:00 - 00:00 (00 MIN)
2. Design&Verify Solution: 00:00 - 00:00 (00 MIN)
3. Code & Pass Test Cases: 00:00 - 00:00 (00 MIN)
"""

'''
IN : 1 2 3 4 5
OUT: 1 5 2 4 3


IN : 1 2 3 4 5 6
OUT: 1 6 2 5 3 4


IN : 1
OUT: 1

'''

from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:

        # split list in half
        def get_middle(node):
            slow, fast = node, node
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        # reverese list
        def reverse_list(node):
            prev, curr = None, node
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        # merge lists
        def merge_lists(left, right):
            while right.next:
                # mark next nodes that curr nodes move to
                l_nxt = left.next
                r_nxt = right.next

                # change connections
                left.next = right
                right.next = l_nxt

                # move pointers
                left = l_nxt
                right = r_nxt

        middle = get_middle(head)
        right = reverse_list(middle)
        left = head

        merge_lists(left, right)


