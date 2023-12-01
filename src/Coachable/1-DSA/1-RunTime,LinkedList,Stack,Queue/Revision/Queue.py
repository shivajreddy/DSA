class ListNode:
    val = None
    next = None

    def __init__(self, val: int = None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{{ val:{self.val} next:{self.next} }}"


'''
Queue :  FIFO, LILO
'''


class Queue:

    def __init__(self):
        self.size = 0
        self.head = None
        self.tail = None

    def push(self, element):
        self.size += 1
        new_node = ListNode(element)
        if not self.head:
            self.head, self.tail = new_node, new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if not self.head:
            return
        self.size -= 1
        if self.head == self.tail:
            self.head, self.tail = None, None
            return
        curr_top = self.head
        self.head = self.head.next
        curr_top.next = None

    def get_size(self) -> int:
        return self.size

    def peek(self):
        return self.head.val if self.head else None

    def clear(self):
        self.head = None
        self.size = 0

    def __str__(self) -> str:
        curr = self.head
        result = ""
        while curr:
            result += f"{curr.val}->"
            curr = curr.next
        result += "None"
        return result


q = Queue()

q.pop()
print(q, q.get_size())

q.push(1)
print(q, q.get_size())

q.pop()
print(q, q.get_size())
