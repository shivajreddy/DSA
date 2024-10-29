"""
Key Insights:

Breadth-First Search (BFS):
    - A typical level order traversal uses BFS with a queue to traverse the tree level by level.
    - Alternating Traversal Direction:
    - To achieve the zigzag pattern, we need to alternate the order in which we add node values at each level.
    - We can maintain a flag or use data structures that allow us to reverse the order when needed.

Data Structure Choice:
    - Using a double-ended queue (deque) allows efficient appending and popping from both ends, which can be
      helpful if we choose to manipulate the order of node values or children insertion.

Plan:
    Initialize:
    - Use a queue (collections.deque) to perform BFS.
    - Initialize a result list to store the traversal levels.

Traversal:
    - While the queue is not empty, process nodes level by level.

For each level, determine the traversal direction:
    - If it's a left-to-right level, process nodes in the normal order.
    - If it's a right-to-left level, process nodes in reverse order.

Collect Node Values:
    - For each level, collect the node values in a list.
    - Reverse the list if the level is right-to-left before adding it to the result.

Alternate Direction:
    - Use a boolean flag (left_to_right) that flips after each level to alternate traversal direction.

Time and Space Complexity:
    Time Complexity: O(N), where N is the number of nodes in the tree. We visit each node exactly once.
    Space Complexity: O(N), to hold the nodes in the queue and the result list.


Testing the Implementation:
    - To ensure the solution works correctly, let's test it with a sample tree.

Example Tree:
        3
       / \
      9  20
        /  \
       15   7

Expected Output:
    [
    [3],
    [20, 9],
    [15, 7]
    ]
"""


from collections import deque
from typing import List, Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        result = []
        queue = deque()
        queue.append(root)
        left_to_right = True  # Flag to indicate the traversal direction

        while queue:
            level_size = len(queue)
            level_nodes = deque()  # Use deque to efficiently append nodes in both directions

            for _ in range(level_size):
                node = queue.popleft()

                # Add the node's value to the level list based on the traversal direction
                if left_to_right:
                    level_nodes.append(node.val)
                else:
                    level_nodes.appendleft(node.val)

                # Add the children to the queue for the next level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            # Add the current level's nodes to the result
            result.append(list(level_nodes))

            # Flip the traversal direction
            left_to_right = not left_to_right

        return result


"""
Explanation:

Edge Case Handling:
    - If the root is None, we return an empty list as there are no nodes to
      traverse.

Initialization:
    - We initialize queue with the root node.
    - The left_to_right flag starts as True to indicate the initial traversal
      direction.

Level Order Traversal:
    - While the queue is not empty, we process nodes level by level.
    - level_size keeps track of the number of nodes at the current level.

Processing Nodes at Each Level:
    - We initialize a level_nodes deque to store the node values at the
      current level.
    - For each node in the current level:

        - We pop the node from the left of the queue.
        - Based on the left_to_right flag, we append the node's value to
        - level_nodes:
            If left_to_right is True, we append to the right.
            If left_to_right is False, we append to the left
            (effectively reversing the order).
        - We enqueue the node's children for the next level traversal.

Updating Result and Traversal Direction:
    - After processing all nodes at the current level, we convert level_nodes
      to a list and append it to result.
    - We flip the left_to_right flag to change the traversal direction for
      the next level.

Return Result:
    Once all levels are processed, we return the result list.

Edge Cases and Considerations:
    Empty Tree:
        The code handles the case where the input tree is empty by returning an
        empty list.

    Single Node Tree:
        The traversal will simply return a list containing a single-element list with
        the root node's value.

    Large Trees:
        The solution scales well for large trees due to its linear time complexity.

    Traversal Direction Logic:
        By using a deque (level_nodes) and appending to either end based on the
        traversal direction, we avoid the need to reverse lists, which can be
        inefficient for large levels.

    Time and Space Complexity:
        Time Complexity: O(N), where N is the number of nodes in the tree. We visit
        each node exactly once.
        Space Complexity: O(N), to hold the nodes in the queue and the result list.
"""


