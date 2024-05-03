"""
Design a HashMap
"""


class MyHashMap:
    M = 1001
    array = [0 for _ in range(M)]

    def __init__(self):
        pass

    def _hashing(self, key: int):
        hash_value = key % self.M
        return hash_value

    def put(self, key: int, value: int) -> None:
        # generate hash_value
        hash_value = self._hashing(key)
        new_node = Node(key, value)
        # collision: cell is occupied
        if self.array[hash_value]:
            self.insert_last(self.array[hash_value], new_node)
            return

        # empty cell
        self.array[hash_value] = new_node

    def get(self, key: int) -> int:
        hash_value = self._hashing(key)
        if self.array[hash_value]:
            curr = self.array[hash_value]
            while curr:
                if curr.key == key:
                    return curr.val
                curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        hash_value = self._hashing(key)
        if not self.array[hash_value]:
            print("ERROR: No key found")
            return

        head = self.array[hash_value]
        prev, curr = None, head
        if curr.key == key:
            nxt = head.next
            head.next = None
            self.array[hash_value] = nxt
            print(f"Deleted {curr.key} : {curr.val}")
            return
        while curr:
            if curr.key == key:
                self.array[hash_value] = self.remove_node(prev)
            prev = curr
            curr = curr.next

        pass

    def insert_last(self, head, new_node):
        prev, curr = None, head
        while curr:
            prev = curr
            curr = curr.next
        prev.next = new_node

    # removes the node next to 'prev_node'
    def remove_node(self, prev_node):
        nxt = prev_node.next
        prev_node.next = None
        return nxt

    def __str__(self):
        result = "{"
        for node in self.array:
            if node:
                curr = node
                while curr:
                    result += f"{curr.key}:{curr.val}, "
                    curr = curr.next
        result += "}"
        return result


class Node:
    def __init__(self, key: int, val: int, next=None) -> None:
        self.key = key
        self.val = val
        self.next = next


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(10, "shivaaaa")
obj.put(20, "reddy")
print(obj)
param_2 = obj.get(10)
print(param_2)
obj.remove(20)
print(obj)
