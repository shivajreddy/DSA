"""
### Handle Base Cases:
- If the linked list is empty (`head is None`), has only one node 
  (`head.next is None`), or no rotation is needed (`k == 0`), it immediately 
  returns the head without making any changes.

### Find the Length of the List:
- The length (`n`) of the list is calculated by iterating through the entire 
  list using a pointer `curr`. During this traversal, the last node (`curr`) is 
  also located.

### Handle Cases Where k >= n:
- If `k` is greater than or equal to the length of the list, the rotation count 
  is reduced to `k % n` (as rotating a list by its length results in the same 
  list).

### Form a Circular List:
- The list is made circular by linking the last node back to the head. This 
  step simplifies finding the new head.

### Find the New Head:
- The new head is determined by moving `n - k` steps from the current head. The 
  `curr` pointer is moved along the list to find the new head, and the circular 
  link is broken by setting `curr.next` to `None`.

### Return the New Head:
- The new head of the rotated list is returned as the result.

### Time and Space Complexity:

#### Time Complexity: 
- `O(n)`, where `n` is the length of the linked list. We traverse the list 
  twice: once to calculate the length and once to find the new head.

#### Space Complexity: 
- `O(1)`, as the function only uses a few pointers and does not require any 
  extra space proportional to the input size.

"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

from typing import Optional

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Base cases: Empty list or no rotation needed
        if not head or not head.next or k == 0:
            return head

        # Step 1: Find the length of the list and the last node
        n = 1
        curr = head
        while curr.next:
            curr = curr.next
            n += 1

        # Step 2: Handle cases where k >= n
        k %= n
        if k == 0:
            return head  # No rotation needed

        # Step 3: Make the list circular by linking the last node to the head
        curr.next = head

        # Step 4: Find the new head after (n - k) steps from the original head
        steps_to_new_head = n - k
        curr = head
        for _ in range(steps_to_new_head - 1):
            curr = curr.next

        # Step 5: Break the circle and set the new head
        new_head = curr.next
        curr.next = None

        return new_head

