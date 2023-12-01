from __future__ import annotations
from typing import *

'''
Complete this implementation of a Queue using a linked list.
All operations should run in O(1) runtime
'''


# complete the node class
class Node:
    def __init__(self, val: int, next: 'Node | None' = None):
        self.val = val
        self.next = next


class Queue:
    def __init__(self):
        self.count = 0
        self.head = None
        self.tail = None

    # add vals to the queue
    def enqueue(self, val: int) -> None:
        curr = self.head
        new_node = Node(val)
        if not curr:
            self.head = new_node
            self.tail = new_node
        prev_tail = self.tail
        prev_tail.next = new_node
        self.tail = new_node
        self.count += 1

    # return None if queue is empty
    def peek(self) -> int | None:
        if not self.head:
            return
        return self.head.val

    # return None if queue is empty
    def dequeue(self) -> int | None:
        if not self.head:
            return
        prev_head, nxt = self.head, self.head.next
        prev_head.next = None
        self.head = nxt
        self.count -= 1
        return prev_head.val

    # returns the number of elements in the queue
    def size(self) -> int:
        return self.count

    def get_items(self) -> list:
        result = []
        curr = self.head
        while curr:
            result.append(curr.val)
            curr = curr.next
        return result
