class ListNode:
    val = None
    next = None

    def __init__(self, val: int = None, next=None):
        self.val = val
        self.next = next

    def __str__(self):
        return f"{{ val:{self.val} next:{self.next} }}"


'''
Stack: LIFO, FILO


'''


class Stack:

    def __init__(self):
        self.size = 0
        self.top = None

    def get_size(self):
        return self.size

    def is_empty(self) -> bool:
        return self.size == 0

    def push(self, element) -> None:
        new_node = ListNode(element)
        self.size += 1
        if not self.top:
            self.top = new_node
            return
        curr_top = self.top
        new_node.next = curr_top
        self.top = new_node

    def pop(self):
        if not self.top:
            return None
        self.size -= 1
        curr_top = self.top
        self.top = self.top.next
        curr_top.next = None
        return curr_top.val

    def peek(self):
        if not self.top:
            return None
        return self.top.val

    def __str__(self) -> str:
        curr = self.top
        result = ""
        while curr:
            result += f"{curr.val}->"
            curr = curr.next
        result += "None"
        return result


s = Stack()
s.push(10)
s.push(20)
s.push(30)

print(s, s.get_size())
print(s.peek())

print(s.pop())
print(s, s.get_size())
