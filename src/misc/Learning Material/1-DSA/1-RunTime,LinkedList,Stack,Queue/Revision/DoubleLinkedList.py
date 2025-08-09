class ListNode:
    val = None
    next = None
    prev = None

    def __init__(self, val: int = None, next=None, prev=None):
        self.val = val
        self.next = next
        self.prev = prev

    def __str__(self):
        return f" {self.prev}<->{self.val}<->{self.next}"


class DoubleLinkedList:

    def __init__(self):
        self.size = 0
        self.head, self.tail = ListNode(-1), ListNode(-1)  # None <- head -> None, None <- tail -> None
        self.head.next, self.tail.prev = self.tail, self.head  # None <- head <-> tail -> None

    def insert_front(self, element):
        self.size += 1
        self._insert_between(self.head, self.head.next, element)

    def insert_back(self, element):
        self.size += 1
        self._insert_between(self.tail.prev, self.tail, element)

    def remove_front(self):
        if not self.size:
            return
        self.size -= 1
        removed_node = self._remove_between(self.head, self.head.next.next)
        return removed_node.val

    def remove_last(self):
        if not self.size:
            return
        self.size -= 1
        removed_node = self._remove_between(self.tail.prev.prev, self.tail)
        return removed_node.val

    # inserts an element between two given non-equal nodes. prv <-> nxt => prv <-> insert_here <-> nxt
    @staticmethod
    def _insert_between(prv: ListNode, nxt: ListNode, element) -> None:
        new_node = ListNode(element)
        prv.next, nxt.prev = new_node, new_node  # prv -> new_node <- nxt
        new_node.prev, new_node.next = prv, nxt  # prv <-> new_node <-> nxt

    # removes the node between the two separate nodes. prv <-> target <-> nxt
    @staticmethod
    def _remove_between(prv: ListNode, nxt: ListNode) -> ListNode:
        target_node = prv.next
        target_node.prev, target_node.next = None, None  # prv -> target <- nxt
        prv.next, nxt.prev = nxt, prv  # prv  target  nxt, prv <-> nxt
        return target_node

    def peek_head(self):
        return self.head.next.val

    def peek_tail(self):
        return self.tail.prev.val

    def __str__(self):
        result = ""
        curr = self.head
        while curr:
            result += str(curr.val)
            if curr.next:
                result += " <-> "
            curr = curr.next
        return result


# Test
dll = DoubleLinkedList()
dll.insert_back(20)
dll.insert_front(10)
dll.insert_front(30)
dll.insert_front(40)
dll.insert_back(70)

print(dll)

print(dll.remove_front())
print(dll)
