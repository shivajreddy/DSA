from typing import Optional


class Node:
    """Create a new doubly linked list node"""

    def __init__(self, key: int, val: int) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None


class DLL:
    """Create an empty doubly linked with head & tail handles"""

    def __init__(self) -> None:
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head  # h <-> t

    """ Add a new given to the front of the list """

    def append_left(self, node: Node) -> None:
        head, first = self.head, self.head.next  # h <-> f
        head.next, first.prev = node, node  # h -> n <- f
        node.prev, node.next = head, first  # h <-> n <-> f
        self.size += 1

    """ Remove a given target node """

    def remove(self, target: Node) -> None:
        prev, nxt = target.prev, target.next  # p <-> t <-> n
        prev.next, nxt.prev = nxt, prev  # p <-> n
        target.prev, target.next = None, None
        self.size -= 1

    """ Remove and return the last node """

    def pop_right(self) -> Node:
        target = self.tail.prev  # h <-> ... target <-> t
        self.remove(target)  # h <-> ...<-> t
        return target


class LRUCache:
    """Create a new LRU cache of fixed size. Space: O(n)"""

    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = DLL()
        self.key_node_map = {}

    """ Get the value for a valid key. Time: O(1) """

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1

        node = self.key_node_map[key]

        # Move node to front
        self.cache.remove(node)
        self.cache.append_left(node)
        return node.val

    """ Put key,value into LRU, update if key already exists. Time: O(1) """

    def put(self, key: int, val: int) -> None:
        # key already exists
        if key in self.key_node_map:
            node = self.key_node_map[key]
            self.cache.remove(node)

        # LRU cache is full
        if self.cache.size == self.capacity:
            last_node = self.cache.pop_right()
            del self.key_node_map[last_node.key]

        # Add new key-value to cache & add to key-node map
        node = Node(key, val)
        self.cache.append_left(node)
        self.key_node_map[key] = node
