"""
Deque Implementation
"""


class Node:
    def __init__(self, val: int, next=None, prev=None) -> None:
        self.val = val
        self.next = next
        self.prev = prev


class Deque:
    def __init__(self):
        self._size = 0
        self.head = Node(-1)
        self.tail = Node(-1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get_size(self) -> int:
        return self._size

    def is_empty(self) -> bool:
        return self._size == 0

    def add_first(self, item: int) -> Node:
        # def add_first(self, item: int) -> None:

        # base :    head <-> tail
        # add 1:    head <-> 1 <-> tail
        # add 2:    head <-> 2 <-> 1 <-> tail

        new_node = Node(item)  # create new node
        nxt = self.head.next  # safe save the curr self.head.next pointer, say nxt

        self.head.next = new_node  # head's next points to new_node:  head -> new   nxt
        new_node.prev = self.head  # new_node's prev points to head:  head <-> new  nxt

        new_node.next = nxt  # new_node's next points to nxt:   new -> nxt
        nxt.prev = new_node  # nxt's prev points to new:    new <-> nxt

        self._size += 1  # increase size of deque
        return new_node

    def add_last(self, item: int) -> None:
        # base :    head <-> tail
        # add 1:    head <-> 1 <-> tail
        # add 2:    head <-> 1 <-> 2 <-> tail

        new_node = Node(item)  # create a new node
        tail_prev = self.tail.prev  # safe save the tail's prev node, say tail_prev :  head <-> tail_prev <-> tail

        self.tail.prev = new_node  # tail's prev points to new node:    tail_prev  new_node <- tail
        new_node.next = self.tail  # new node's next points to tail:    tail_prev  new_node <-> tail

        new_node.prev = tail_prev  # new node's prev point to tail_prev:    tail_prev <- new_node <-> tail
        tail_prev.next = new_node  # tail_prev next point to new_node:      tail_prev <-> new_node <-> tail

        self._size += 1  # increase size of deque

    def remove_first(self) -> int:
        # base  :    head <-> 1 <-> 2 <-> tail
        # remove:    head <-> 2 <-> tail
        # remove:    head <-> tail

        # null check
        if self.get_size() == 0:
            print("ERROR, No items to remove")
            return -1

        # safe save head.next.next, since head.next is going to be removed
        target, target_next = self.head.next, self.head.next.next  # head <-> target <-> target_next

        target.prev = None  # head -> target <-> target_next
        target.next = None  # head -> target <- target_next

        self.head.next = target_next  # head  target <- target_next,    head -> target_next
        target_next.prev = self.head  # head <-> target_next

        self._size -= 1  # decrease size of deque
        return target.val  # return deleted node's value

    def remove_last(self) -> int:
        # base  :    head <-> 1 <-> 2 <-> tail
        # remove:    head <-> 1 <-> tail
        # remove:    head <-> tail

        # null check
        if self.get_size() == 0:
            print("ERROR, No items to remove")
            return -1

        # safe save target_prev
        target, target_prev = self.tail.prev, self.tail.prev.prev  # target_prev <-> target <-> tail

        target.next = None  # target_prev <-> target <- tail
        target.prev = None  # target_prev -> target <- tail

        self.tail.prev = target_prev  # target_prev -> target  tail,  target_prev <- tail
        target_prev.next = self.tail  # target_prev <-> tail

        self._size -= 1  # decrease size of deque
        return target.val  # return deleted node's value

    def as_list(self):
        lst = []
        curr = self.head.next
        while curr != self.tail:
            lst.append(curr.val)
            curr = curr.next
        return lst

    def sanity_check(self) -> bool:
        curr = self.head
        while curr.next:
            if curr.next.prev is not curr:
                return False
            curr = curr.next
        return True

    def __str__(self):
        result = "Head <-> "
        curr = self.head.next
        while curr != self.tail:
            result += f"{curr.val}"
            if curr.next:
                result += " <-> "
            curr = curr.next
        result += "Tail"
        return result


# test cases
'''
dq = Deque()
for i in range(1, 6):
    dq.add_first(i)
print(dq)
for i in range(6, 11):
    dq.add_last(i)

print(dq)  # 5,4,3,2,1,6,7,8,9,10
print(dq.as_list())  # 5,4,3,2,1,6,7,8,9,10
print(dq.remove_first())  # 5
print(dq.as_list())  # 4,3,2,1,6,7,8,9,10
print(dq.remove_last())  # 10
print(dq.as_list())  # 4,3,2,1,6,7,8,9

print(dq.sanity_check())
'''
