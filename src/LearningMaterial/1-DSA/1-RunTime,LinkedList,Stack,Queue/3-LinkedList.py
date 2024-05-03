"""
LinkedList
"""
from __future__ import annotations

from typing import Optional

'''
Benefits:

There is no fixed size.
Adding an element to the front takes O(1) runtime.
Removing an element from the front takes O(1) runtime

'''


# ! Implement a Linked List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:

        # approach is two pointers: slow, fast
        # intuition: start two pointers at a dummy node. First move the slow to dummy.next
        # and fast to dummy.next.next, then check if they point to same node, else shift.
        # repeat this until fast reaches end, or slow meets fast

        # create a dummy node that points to given head, both pointers start at dummy.
        # if fast and slow meet then there is a cycle.
        # if fast reaches end, then there is NO cycle.

        # Edge Case 1: if there is single node, and it's next is itself.
        # Null case: there are 0 nodes in the linkedlist

        if not head:
            return head

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                return True
        return False


# ! Implement a Linked List
class Node:
    def __init__(self, val: int = None, next: Node = None):
        self.val = val
        self.next = next


class LinkedList:

    def __init__(self, head: Node):
        self._size = 1
        self.head = head

    def get_size(self) -> int:
        return self._size

    def insert_front(self, node: Node) -> Node:
        node.next = self.head
        self.head = node
        self._size += 1
        return node

    def insert_last(self, node: Node) -> Node:
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = node
        self._size += 1
        return node

    def remove_front(self) -> Node:
        curr_head = self.head
        nxt = curr_head.next
        curr_head.next = None
        self.head = nxt
        self._size -= 1
        return curr_head

    def __str__(self):
        curr = self.head
        result = ""
        while curr:
            result += f"{curr.val}->"
            curr = curr.next
        result += f"None"
        return result


ll = LinkedList(Node(99))
ll.insert_last(Node(88))
ll.insert_front(Node(33))
ll.insert_last(Node(12))
ll.insert_last(Node(83))
ll.insert_front(Node(44))
print(ll)  # 44->33->99->88->12->83->None


# ! Reverse a linked list
class ReverseLinkedListSolution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        if not head:
            return None

        prev = None
        while head:
            nxt = head.next
            head.next = prev

            prev = head
            head = nxt
        return prev
