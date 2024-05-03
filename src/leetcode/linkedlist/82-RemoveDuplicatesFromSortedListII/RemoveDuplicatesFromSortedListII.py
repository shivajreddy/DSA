from typing import List, Optional


class ListNode:
    def __init__(self, val=0, next=None) -> None:
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        pass


s = Solution()

head = ListNode(1, ListNode(1, ListNode(1, ListNode(2, ListNode(3, None)))))
s.deleteDuplicates(head)

head = ListNode(1, ListNode(2, ListNode(3, ListNode(3, ListNode(3, ListNode(4, ListNode(4, ListNode(5, None))))))))
s.deleteDuplicates(head)

