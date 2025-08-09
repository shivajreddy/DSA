from __future__ import annotations
from typing import *

'''
Implement collision handling for this hashmap
which accepts integers as keys and strings as values

we recommend using separate chaining with a python list
'''


class Node:
    def __init__(self, key: int, val: str, next: 'Node | None' = None):
        self.key = key
        self.val = val
        self.next = next


class Hashmap:
    # initialize hashmap with
    def __init__(self, capacity: int):
        self._capacity = capacity

        # add the rest of your implementation below
        self.nodes: list[Node | None] = [None] * capacity

    # do not change this function
    def _hash_int(self, key: int) -> int:
        return key % self._capacity

    def insert(self, key: int, val: str) -> None:
        new_node = Node(key, val)
        hash_idx = self._hash_int(key)
        main_list = self.nodes

        if not main_list[hash_idx]:
            main_list[hash_idx] = new_node
            return

        # collision resolution
        curr = main_list[hash_idx]
        while curr.next:
            if curr.key == key:  # duplicate key found
                curr.val = val
                return
            curr = curr.next
        curr.next = new_node

    # return None if the key is not found
    def get(self, key: int) -> str | None:
        main_list = self.nodes
        hash_idx = self._hash_int(key)

        # no node for given key
        if not main_list[hash_idx]:
            return

        # node at idx is the target
        if main_list[hash_idx].key == key:
            return main_list[hash_idx].val

        # traverse nodes in the chain
        curr = main_list[hash_idx]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next

    # should be the same as the .items() method for python dictionaries
    # return a list of tuples in the form [(key, val), ...]
    def items(self) -> list:
        result = []

        nodes = self.nodes

        for idx, node in enumerate(nodes):
            while node:
                # add the main node
                pair = (node.key, node.val)
                result.append(pair)
                node = node.next  # move to child
        return result
