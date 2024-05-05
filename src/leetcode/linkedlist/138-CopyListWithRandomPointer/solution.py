'''
Workflow Timestamps
1. Understand the Problem: 00:00 - 04:14 (4  Mins)
2. Design&Verify Solution: 04:14 - 10:30 (7  Mins)
3. Code & Pass Test Cases: 10:30 - 19:51 (10 Mins)


Assumptions: no cycles in the given linked list
Approach: create a hm 
    Map:  { <id_of_old_node> : <new_node> }
    - 2 traversals, 1st - create new nodes, 2nd- add random ppty

TIME : O(N)
SPACE: O(N)     Due to HashMap

in python:
id(node) -> memory_address of that variable

{ <memory_address_of_old_node> : <pointer_to_new_node_that_is_a_deepcopy_of_this_mem-address>}

'''


from typing import Optional

class Node:
    def __init__(self, x: int, next: 'Node | None' = None, random: 'Node | None' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':

        if not head:
            return None

        hm = {}

        curr = head

        # TIME: O(N)
        # Traverse through linked-list
        #   - add curr-node to map, with value as 'pointer to new node'
        while curr:

            new_node = Node(curr.val, None, None)   # create new-node

            hm[id(curr)] = new_node                 # add to mapper

            curr = curr.next                        # move pointer

        curr = head

        # TIME: O(N)
        # Traverse through linked-list
        #   - assign 'next' and 'random' properties to the deep-copied nodes
        while curr:

            # assign 'next' and 'random' ppty, using the new-nodes
            nxt = curr.next
            rdm = curr.random

            # Assign 'next' property
            if nxt:
                new_node = hm[id(curr)]
                new_node.next = hm[id(nxt)]

            # Assign 'random' property
            if rdm:
                new_node = hm[id(curr)]
                new_node.random = hm[id(rdm)]

            curr = curr.next                        # move pointer

        return hm[id(head)]

