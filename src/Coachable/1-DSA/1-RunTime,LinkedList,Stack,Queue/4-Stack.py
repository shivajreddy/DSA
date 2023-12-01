# ! Valid parentheses
from typing import Any


class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        hm = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for char in s:
            if char in hm:
                stack.append(char)
            else:
                if not stack or hm[stack.pop()] != char:
                    return False

        if stack:
            return False

        return True


class Node:
    def __init__(self, val: Any = None, next: Any = None):
        self.val = val
        self.next = next


# ! Stack implementation
class Stack:

    def __init__(self):
        self._size = 0
        self._first_item = None

    def __str__(self) -> str:
        curr = self._first_item
        result = ""
        while curr:
            result += f"{curr.val}->"
            curr = curr.next
        result += "None"
        return result

    def peek(self) -> Any:
        return self._first_item.val

    def push(self, element: Any) -> None:
        # existing 3 -> 10  new item is 5. So 5->3->10
        new_element = Node(element)
        new_element.next = self._first_item
        self._first_item = new_element
        self._size += 1

    def pop(self) -> Any:
        if self.is_empty():
            return
        curr_top = self._first_item
        self._first_item = self._first_item.next
        curr_top.next = None
        self._size -= 1
        return curr_top.val

    def is_empty(self) -> bool:
        return self._size == 0

    def size(self) -> int:
        return self._size


# ! Queue implementation

class Queue:
    def __init__(self) -> None:
        self._size = 0
        self._front = None
        self._end = None

    # adds an item to the queue
    def enqueue(self, element: Any) -> Any:
        new_element = Node(element)
        if self._size == 0:
            self._front = new_element
            self._end = new_element
        else:
            self._end.next = new_element
            self._end = new_element
        self._size += 1
        return new_element.val

    # removes and returns the most recently added item
    def dequeue(self) -> Any:
        if self._size == 0:
            return
        curr_first = self._front
        self._front = self._front.next
        curr_first.next = None
        self._size -= 1
        return curr_first.val

    def is_empty(self) -> bool:
        return self._size == 0

    def get_size(self) -> int:
        return self._size

    # returns a list of items in the queue
    def items(self) -> list[Any]:
        result = []
        curr = self._front
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result

    def __str__(self) -> str:
        result = ""
        curr = self._front
        while curr:
            result += f"{curr.val}->"
            curr = curr.next
        result += "None"
        return result
