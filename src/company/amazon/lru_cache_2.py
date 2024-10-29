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

    def append_left(self, node) -> None:
        head, first = self.head, self.head.next
        head.next, first.prev = node, node
        node.prev, node.next = head, first
        self.size += 1

    def remove(self, target: Node) -> None:
        prev, nxt = target.prev, target.next
        prev.next, nxt.prev = nxt, prev
        target.next, target.prev = None, None
        self.size -= 1

    def pop_right(self) -> Node:
        target = self.tail.prev
        self.remove(target)
        return target


class LRUCache:
    def __init__(self, capacity) -> None:
        self.capacity = capacity
        self.cache = DLL()
        self.key_node_map = {}

    def get(self, key) -> int:
        if key not in self.key_node_map:
            return -1
        node = self.key_node_map[key]
        self.cache.remove(node)
        self.cache.append_left(node)
        return node.val

    def put(self, key, val) -> None:
        if key in self.key_node_map:
            node = self.key_node_map[key]
            self.cache.remove(node)
        if self.cache.size == self.capacity:
            node = self.cache.pop_right()
            del self.key_node_map[node.key]
        node = Node(key, val)
        self.cache.append_left(node)
        self.key_node_map[key] = node

