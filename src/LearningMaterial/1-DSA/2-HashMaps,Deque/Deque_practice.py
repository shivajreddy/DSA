class Node:
    def __init__(self, val: int, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev


class Deque:
    HEAD, TAIL = None, None
    SIZE = 0

    def is_empty(self) -> bool:
        return self.SIZE == 0

    def get_size(self) -> int:
        return self.SIZE

    def add_first(self, val: int) -> None:
        new_node = Node(val)
        if self.SIZE == 0:
            self.HEAD = new_node
            self.TAIL = new_node
            self.SIZE += 1
            return
        self.HEAD.prev = new_node
        new_node.next = self.HEAD
        self.HEAD = new_node
        self.SIZE += 1

    def add_last(self, val: int) -> None:
        new_node = Node(val)
        if self.SIZE == 0:
            self.HEAD = new_node
            self.TAIL = new_node
            self.SIZE += 1
            return
        self.TAIL.next = new_node
        new_node.prev = self.TAIL
        self.TAIL = new_node
        self.SIZE += 1

    def remove_first(self) -> int:
        if not self.HEAD:
            print("NO head to remove")
            return -1
        curr_head = self.HEAD
        nxt = curr_head.next
        curr_head.next = None
        nxt.prev = None
        self.HEAD = nxt
        self.SIZE -= 1
        return curr_head.val

    def remove_last(self) -> int:
        if not self.TAIL:
            print("NO tail to remove")
            return -1
        curr_tail = self.TAIL
        tail_prev = curr_tail.prev
        tail_prev.next = None
        curr_tail.prev = None
        self.TAIL = tail_prev
        self.SIZE -= 1
        return curr_tail.val

    def as_list(self) -> list[int]:
        lst = []
        curr = self.HEAD
        while curr:
            lst.append(curr.val)
            curr = curr.next
        return lst

    def __str__(self):
        # pass
        result = "None <- "
        curr = self.HEAD
        while curr:
            result += f"{curr.val}"
            if curr.next:
                result += " <-> "
            curr = curr.next
        result += " -> None"
        return result


"""
# test cases
dq = Deque()
for i in range(1, 6):
    dq.add_first(i)
for i in range(6, 11):
    dq.add_last(i)

print(dq)
# 5,4,3,2,1,6,7,8,9,10
print(dq.as_list())
print(dq.remove_first())
print(dq.as_list())
# 4,3,2,1,6,7,8,9,10
print(dq.remove_last())
print(dq.as_list())
# 4,3,2,1,6,7,8,9
"""
