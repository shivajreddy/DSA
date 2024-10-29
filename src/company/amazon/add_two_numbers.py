"""
Constraints:
l1, l2 are non empty
1 <= n1 <=100
1 <= n2 <= 100
0 <= Node.val <= 9

Scope & Assumptions:
Linked list root being the first digit of the number
two numbers need not be of same length
No leading zeros
API: 
Input:  given inputs are mutable
Output: output of this function are also mutable
Node API is predefined

Observations:
start adding from right to left
there can be carry over after adding two nodes, could be a carry over after adding the the root nodes i.e., the leftmost digits
Reversing the given lists could be ideal, since we iterate from right most digit to left most digit.

Approach & Solution:
Reverse the linked lists
two pointers, each pointing to a node in the given lists, and traverse until the end of that list.
Carry-over: add two numbers, create a new node with units place digit, collect carry over if any
repeat addition of two digits, while both pointers point to valid nodes
if one or both pointers point to None, continue the process with leftover carry(if any) & left over list(if any).
Perform addition of two digits, while any of the pointers point to a valid node

Time & Space Complexity:
Time Complexity: O(max(m, n)), where m is the length of l1 and n is the length of l2. We                   iterate through both lists once.
Space Complexity: O(max(m, n)) for the result list, since we store the sum as a new linked list.
"""

from typing import Optional


class Node:
    def __init__(self, val: int, next: Optional['Node'] = None) -> None:
        self.val = val
        self.next = next

class Solution:
    def add_two_numbers(self, l1: Optional[Node], l2: Optional[Node]) -> Optional[Node]:

        # Create a dummy node as pseudo head
        dummy = Node(-1)

        # Pointer for the most recent node in the result list
        curr = dummy

        # Carry over the sum after adding two digits
        carry_over = 0

        # Go over both the lists
        '''
        - continue iterating while at least 1 pointer points to a valid node
        - or there is a carry over
        '''
        while l1 or l2 or carry_over != 0:
            l1_val = l1.val if l1 else 0
            l2_val = l2.val if l2 else 0

            # add the two digits and carry-over
            total = l1_val + l2_val + carry_over

            new_val = total % 10			# digit in units place

            carry_over = total // 10		# digit in one's place

            new_node = Node(new_val)		# curr 	|  new_node
            curr.next = new_node			# curr -> new_node

            # Move pointers
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            curr = curr.next

            # return the root of the final list
            return dummy.next

