from typing import Optional


# Definition for singly-linked list.
class ListNode:
	def __init__(self, val=0, next=None):
		self.val = val
		self.next = next


class Solution:
	def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
		return ListNode()

	@staticmethod
	def reverse_linked_list(root: ListNode) -> ListNode:
		curr: ListNode = root
		prev = None

		while curr:
			nxt: ListNode = curr.next
			curr.next = prev

			prev = curr
			curr = nxt

		return prev


two = ListNode(2)
four = ListNode(4)
three = ListNode(3)
two.next = four
four.next = three

Solution.reverse_linked_list(three)

print(two)
