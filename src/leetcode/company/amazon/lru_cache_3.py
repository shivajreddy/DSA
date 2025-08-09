class Node:
    def __init__(self, key, val) -> None:
        self.key = key
        self.val = val
        self.next = None
        self.prev = None

class DLL:
    def __init__(self) -> None:
        self.size = 0
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head

    def append_left(self, node: Node) -> None:
        head, first = self.head, self.head.next # h <-> f <-> ... <-> t
        head.next, first.prev = node, node      # h -> n <- f
        node.next, node.prev = first, head
        self.size += 1

    def remove(self, node: Node) -> None:
        prev, nxt = node.prev, node.next    # h <-> prev <-> node <-> nxt <-> ... <-> t
        prev.next, nxt.prev = nxt, prev     # prev <-> nxt
        node.prev, node.next = None, None
        self.size -= 1

    def pop_right(self) -> Node:
        target = self.tail.prev
        self.remove(target)
        return target


class LRUCache:
    def __init__(self, capacity: int) -> None:
        self.capacity = capacity
        self.cache = DLL()
        self.key_node_map = {}

    def get(self, key: int) -> int:
        if key not in self.key_node_map:
            return -1
        
        node = self.key_node_map[key]
        self.cache.remove(node)
        self.cache.append_left(node)
        return node.val

    def put(self, key: int, val: int) -> None:
        if key in self.key_node_map:
            self.cache.remove(self.key_node_map[key])
            del self.key_node_map[key]
        if self.cache.size == self.capacity:
            node = self.cache.pop_right()
            del self.key_node_map[node.key]
        node = Node(key, val)
        self.cache.append_left(node)
        self.key_node_map[key] = node

