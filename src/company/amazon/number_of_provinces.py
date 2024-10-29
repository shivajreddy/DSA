"""
Key Insights


Graph Traversal Techniques:
    1. Depth-First Search (DFS):
        - Traverse each node (city) and mark connected nodes as visited.
        - This will help in identifying a connected component.

    2. Breadth-First Search (BFS):
        - Similar to DFS but uses a queue to traverse nodes level by level.

Symmetry in `isConnected`:
    - The matrix is symmetric, meaning `isConnected[i][j] == isConnected[j][i]`,
      which represents an undirected graph.

Self-loop Handling:
- Each city is connected to itself (`isConnected[i][i] == 1`), which means 
  every city is a component by itself at least.

---

Algorithm Design:

Depth-First Search (DFS) Approach

Idea:
    - Use DFS to traverse the graph and count the number of connected components.
    - Start from each unvisited city and perform DFS to mark all connected cities as visited.

Steps:
    1. Initialize a `visited` list to track visited cities.
    2. Initialize a counter `province_count` to 0.
    3. For each city `i` from `0` to `n-1`:
        - If city `i` is not visited:
            - Increment `province_count`.
            - Perform DFS starting from city `i` to mark all connected cities as visited.
    4. Return `province_count`.

---

Time and Space Complexity

### DFS Approach:
- Time Complexity: O(n²)
  - We may need to traverse all edges in the worst case.
  
- Space Complexity: O(n)
  - Due to the `visited` array and the recursive call stack.

"""
from typing import List

class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        n = len(isConnected)

        visited = [False] * n

        province_count = 0

        def visit_neighbor_cities(city_idx: int):
            visited[city_idx] = True
            for neighbor_idx in range(n):
                if isConnected[city_idx][neighbor_idx] == 1 and not visited[neighbor_idx]:
                    visit_neighbor_cities(neighbor_idx)

        for idx in range(n):
            if not visited[idx]:
                visit_neighbor_cities(idx)
                province_count += 1

        return province_count

