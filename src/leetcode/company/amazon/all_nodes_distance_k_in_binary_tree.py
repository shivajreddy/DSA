"""
Key Insights:
    - Parent Mapping: To traverse upwards from the target, map each node to 
      its parent.
    - BFS Traversal: Perform BFS starting from the target node to explore 
      nodes at increasing distances.
    - Visited Tracking: Keep track of visited nodes to avoid cycles.

Algorithm Design:
    1. Map Parents:
        - Use DFS to traverse the tree and map each node to its parent.
    2. Initialize BFS:
        - Start BFS from the target node.
        - Use a queue to manage nodes to visit and a set to track visited nodes.
    3. BFS Traversal:
        - For each level (distance from target), dequeue nodes and enqueue 
          their unvisited neighbors (left child, right child, and parent).
        - Increment distance after each level.
        - Stop when distance reaches K.
    4. Collect Results:
        - Once distance K is reached, collect all node values in the current queue.

Time Complexity: O(N)
    - Each node is visited twice: once during parent mapping and once during BFS.
Space Complexity: O(N)
    - Parent map, queue, and visited set may store up to N nodes.

"""
from typing import List, Optional
from collections import deque, defaultdict

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val:int=0, left:'TreeNode | None'=None, right:'TreeNode | None'=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def distanceK(self, root: Optional[TreeNode], target: TreeNode, k: int) -> List[int]:
        # Null checks
        if not root:
            return []
        if k == 0:
            return [target.val]
        
        # Map each node to its parent
        node_to_parent_map = {}
        def map_parents(node: Optional[TreeNode], parent: Optional[TreeNode]):
            if not node:
                return
            node_to_parent_map[node] = parent
            map_parents(node.left, node)
            map_parents(node.right, node)
        map_parents(root, None)

        # """
        ''' 
        Approach 1: BFS - using a queue 
        Time : O(N)
        Space: O(N)
        '''
        queue = deque([target])
        visited = {target}
        current_distance = 0
        
        while queue:
            if current_distance == k:
                return [node.val for node in queue]
            
            for _ in range(len(queue)):
                node = queue.popleft()
                # Explore the neighbors: left child, right child, and parent
                for neighbor in (node.left, node.right, node_to_parent_map.get(node)):
                    if neighbor and neighbor not in visited:
                        visited.add(neighbor)
                        queue.append(neighbor)
            current_distance += 1

        return []
        # """

        """
        '''
        Appraoch 2: BFS - use a hasmap to store all nodes at given dist from target
        Time : O(N)
        Space: O(N)
        '''
        visited = set()
        hm = defaultdict(list)      # { dist : [ nodes at this dist from target ] }
        hm[0].append(target)

        dist = 0
        while dist < k:     # Explore distances that are <= k
            if not hm[dist]:
                return []
            for node in hm[dist]:
                if not node or node in visited:
                    continue
                visited.add(node)

                hm[dist + 1].append(node.left)
                hm[dist + 1].append(node.right)
                hm[dist + 1].append(node_to_parent_map.get(node))
            dist += 1
        
        return [node.val for node in hm[k] if node is not None and node not in visited]
        # """

        """
        '''
        Appraoch 2 improvement: only valid nodes that are not yet visited, are added to hashamp 
        Time : O(N)
        Space: O(N)
        '''
        visited = set()
        hm = defaultdict(list)      # { dist : [ nodes at this dist from target ] }
        hm[0].append(target)

        dist = 0
        while dist < k:     # Explore distances that are <= k
            if not hm[dist]:
                return []
            for node in hm[dist]:
                if not node or node in visited:
                    continue
                visited.add(node)

                neighbors = [node.left, node.right, node_to_parent_map.get(node)]
                for node in neighbors:
                    if not node or node in visited:
                        continue
                    hm[dist + 1].append(node)
            dist += 1
        
        return [node.val for node in hm[k] if node is not None and node not in visited]
        # """

