'''
Shape of Node:
    key         -> This is important, because
    val         ->
    next        -> Pointer to next node in list
    prev        -> Pointer to prev node in list

Shape of Mapper:
{ <key> : <pointer-to-node-in-Doubly_Linked_List> }

'''


class Node:

    def __init__(self, key: int, val: int, next=None, prev=None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev


class DoublyLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = Node(-1, -1), Node(-1, -1)
        self.head.next, self.tail.prev = self.tail, self.head  # head <-> tail

    def insert_front(self, new_node: Node):
        first = self.head.next  # head <-> first ... <-> tail
        self.head.next, new_node.prev = new_node, self.head  # head <-> new_node
        new_node.next, first.prev = first, new_node  # head <-> new_node <-> first
        self.size += 1  # increase the size by 1

    # Remove and return the last node of the linked list
    def remove_last(self) -> Node:
        # make sure list is not empty
        if self.size == 0: return

        # head <-> ....<-> target_prev <-> target <-> tail
        target, target_prev = self.tail.prev, self.tail.prev.prev

        target.prev, target.next = None, None  # target_prev -> target <- tail
        target_prev.next, self.tail.prev = self.tail, target_prev  # target_prev <-> tail

        self.size -= 1  # reduce the size by 1
        return target

    # only called when there is at-least 1 node
    def remove_node(self, target: Node) -> Node:
        # head <->.... <-> target <-> .... tail
        target_prev, target_next = target.prev, target.next
        target.prev, target.next = None, None  # target_prev -> target <- target_next
        target_prev.next, target_next.prev = target_next, target_prev

        self.size -= 1
        return target


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = DoublyLinkedList()
        self.mapper = {}

    def get(self, key: int) -> int:
        # check if its in mapper, if so, remove from list, add it to front
        if key not in self.mapper:
            return -1
        target_node = self.mapper[key]
        self.cache.remove_node(target_node)
        self.cache.insert_front(target_node)
        return target_node.val

    def put(self, key: int, value: int) -> None:
        # check if key already exists, if so update the value of the node
        if key in self.mapper:
            existing_node = self.mapper[key]
            existing_node.val = value
            self.cache.remove_node(existing_node)
            self.cache.insert_front(existing_node)
            return

        if self.cache.size == self.capacity:
            last_node = self.cache.remove_last()  # remove from doubly linked list
            del self.mapper[last_node.key]  # remove from mapper

        new_node = Node(key, value)
        self.cache.insert_front(new_node)
        self.mapper[key] = new_node
