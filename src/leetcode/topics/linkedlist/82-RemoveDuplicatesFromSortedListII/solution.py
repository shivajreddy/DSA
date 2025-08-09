'''
Workflow Timestamps
1. Understand the Problem:
2. Design&Verify Solution:
3. Code & Pass Test Cases:


IN : 1 1 1 2 3
OUT: 2 3

IN : 1 1
OUT: _

IN : _
OUT: _

'''

from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next




class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:


        dummy = ListNode(-1, head)

        curr = head
        unique = dummy

        while curr:
            if curr.next and curr.next.val == curr.val:
                while curr.next and curr.next.val == curr.val:
                    curr = curr.next
                unique.next = curr.next
            else:
                unique = curr

            curr = curr.next


        return dummy.next


s = Solution()
head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, None)))))
s.deleteDuplicates(head)
head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, None))))))))
s.deleteDuplicates(head)
