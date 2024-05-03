from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:

        prev, curr = head, head

        while curr:

            if prev.val == curr.val:
                prev.next = None
            else:
                prev.next = curr
                prev = curr

            curr = curr.next

        return head


s = Solution()
