'''
Design LRU

1. Create a Node type
2. Create a DoubleLinkedList
    Node1 <-> Node2 <-> Node3 -> None
3. Design LRU Cache
    A node can atmost have 1 node as its next
    A node can atmost have 1 node as its prev
    This ensures there is no branching or circular linked lists
'''

from typing import Dict

class Node: 
    def __init__(self, 
                key: int,
                val: int,
                next: 'Node | None' = None,
                prev: 'Node | None' = None
                ) -> None:
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:
    def __init__(self):
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head   # head <-> tail

    def push(self, node: Node): # O(1)
        head, nxt = self.head, self.head.next   # head <-> nxt <-> ... <-> tail
        head.next, nxt.prev = node, node        # head  -> node <-  nxt     #type: ignore
        node.prev, node.next = head, nxt        # head <-> node <-> nxt
        self.size += 1

    def remove(self, node: Node) -> None: # O(1)
        # head <-> ... <-> node <-> ... <-> tail
        prev, nxt = node.prev, node.next        # prev <-> node <-> nxt
        node.prev, node.next = None, None       # prev  -> node <-  nxt
        prev.next, nxt.prev = nxt, prev         # prev <-> nxt   |  node    #type: ignore
        self.size -= 1

    def pop(self) -> Node: # O(1)
        node = self.tail.prev                   # head <-> ... <-> node <-> tail
        self.remove(node)       # type: ignore
        return node             # type: ignore


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = DoublyLinkedList()
        self.mapper: Dict[int, int] = {}

    def get(self, key: int) -> int: #O(1)
        if key not in self.mapper:
            return -1
        node = self.mapper[key]
        self.cache.remove(node)     # O(1)  # type: ignore
        self.cache.push(node)       # O(1)  # type: ignore
        return node.val     # type: ignore

    def put(self, key: int, value: int) -> None:
        # node exists with key already
        if key in self.mapper:
            node = self.mapper[key]
            node.val = value            # type: ignore
            self.cache.remove(node)     # type: ignore
            self.cache.push(node)       # type: ignore
            return

        if self.capacity == self.cache.size:
            node = self.cache.pop()
            del self.mapper[node.key]

        new_node = Node(key, value)
        self.cache.push(new_node)
        self.mapper[key] = new_node     # type: ignore


