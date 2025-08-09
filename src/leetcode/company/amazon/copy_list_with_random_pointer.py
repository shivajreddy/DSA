"""
Key Insights  
Deep Copy Requirement:  
- A deep copy means creating entirely new nodes where both `next` and `random` 
  pointers replicate the original list's structure.  
- Simply copying the `val` and `next` pointers isn't sufficient because 
  the `random` pointers could create complex connections.  

Handling Random Pointers:  
- The challenge lies in correctly assigning the `random` pointers in the copied 
  list, especially when they point to nodes ahead or behind in the original list  

Avoiding Duplicates:  
- Without careful handling, nodes could be duplicated in the copied list, 
  leading to incorrect structures.  

Space Optimization:  
- While using additional space (like a HashMap) simplifies the problem, 
  optimizing space usage is beneficial, especially for larger lists.  


Approach 1: HashMap-Based Solution  
Overview:  
- Use a HashMap (Dictionary) to map each original node to its corresponding 
  copied node.
  - This allows us to easily assign `next` and `random` pointers in the 
    copied list by referencing the map.  

Steps:  
Edge Case Handling:  
- If the input `head` is `null`, return `null` as there's nothing to copy.  

First Pass - Create Copy Nodes:  
- Traverse the original list.  
- For each node, create a new node with the same `val`.  
- Store the mapping from the original node to the copied node in the HashMap.  

Second Pass - Assign `next` and `random` Pointers:  
- Traverse the original list again.  
- For each node:  
  - Assign the `next` pointer of the copied node to the copied version of the 
    original node's `next`.  
  - Assign the `random` pointer of the copied node to the copied version of 
    the original node's `random`.  

Return the Copied List:  
    - The `head` of the copied list is the copied node corresponding to the 
      original `head`.  

Time and Space Complexity:  
    Time Complexity: O(n)  
        - Two passes through the list, each taking linear time.  
    Space Complexity: O(n)  
        - Additional space for the HashMap storing n node mappings.
"""


from typing import Optional

# Definition for a Node.
class Node:
    def __init__(self, val: int, next: Optional['Node'] = None, random: Optional['Node'] = None):
        self.val = val
        self.next = next
        self.random = random

class Solution:
    def copyRandomList(self, head: Optional[Node]) -> Optional[Node]:
        if not head:
            return None

        # Step 1: Create a mapping from original nodes to copied nodes
        old_to_new = {}

        current = head
        while current:
            copy = Node(current.val)
            old_to_new[current] = copy
            current = current.next

        # Step 2: Assign next and random pointers
        current = head
        while current:
            copy = old_to_new[current]
            copy.next = old_to_new.get(current.next)
            copy.random = old_to_new.get(current.random)

            current = current.next
        # Step 3: Return the head of the copied list
        return old_to_new[head]


