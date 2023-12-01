# Node in a linked list
from typing import Optional


class ListNode:
    val = None
    next = None

    def __init__(self, val: int = None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{{ val:{self.val} next:{self.next} }}"


class LinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, element) -> None:
        if not self.head:
            self.head = ListNode(element)
            self.size += 1
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        self.size += 1
        curr.next = ListNode(element)

    def get_size(self) -> int:
        return self.size

    def peek(self) -> ListNode:
        return self.head.val if self.head else None

    def pop(self) -> Optional[ListNode]:
        if not self.head:
            return
        curr_head = self.head
        self.head = curr_head.next
        curr_head.next = None
        self.size -= 1
        return curr_head

    def __str__(self) -> str:
        result = "{"
        curr = self.head
        while curr:
            result += str(curr.val)
            if curr.next:
                result += "->"
            curr = curr.next
        result += "->None}"
        return result


ll = LinkedList()
ll.add(10)
ll.add(20)
ll.add(30)
ll.add(40)
print(ll, ll.size)
print(ll.peek())
print(ll.pop())
print(ll, ll.size)
print(ll.peek())
