"""
Key Insights

Understanding the Problem:

- The task is to compute the minimum distance from each cell containing 1 to 
  the nearest cell containing 0.
- The distance is measured in terms of adjacent moves (up, down, left, right).
  
Potential Approaches:

1. Brute Force (DFS/BFS from Each Cell):
   - For each cell with 1, perform BFS or DFS to find the nearest 0.
   - Inefficient due to the high time complexity of O((m * n)²), as we would 
     perform a search for every cell.

2. Dynamic Programming (Two-Pass Approach):
   - Use dynamic programming by propagating distances in two passes:
     - First pass: from top-left to bottom-right.
     - Second pass: from bottom-right to top-left.
   - This approach works faster than brute force but may not handle certain 
     edge cases correctly.

3. Multi-source BFS (Optimal Solution):
   - Treat all cells with 0 as sources and perform BFS from all of them 
     simultaneously.
   - Update the distance for cells containing 1 as we expand the BFS frontier.
   - This is the most efficient and optimal approach, with a time complexity 
     of O(m * n).

Choosing the Optimal Approach:

- Multi-source BFS is the best choice because:
  - It efficiently propagates the distance layer by layer, starting 
    from all 0 cells simultaneously.
  - Time complexity is linear with respect to the number of cells.

---

Algorithm Design:

1. Initialize the Result Matrix:
   - Create a result matrix `dist` of the same size as `mat`.
   - Initialize all cells in `dist` to a large value (e.g., `inf`), except for 
     cells where `mat[i][j] == 0`. For these cells, set `dist[i][j] = 0`.

2. Initialize BFS Queue:
   - Create a queue and enqueue all positions (i, j) where `mat[i][j] == 0`.

3. Perform Multi-source BFS:
   - While the queue is not empty:
     - Dequeue a position `(i, j)`.
     - For each of the four directions (up, down, left, right):
       - Calculate the new position `(new_i, new_j)`.
       - If `(new_i, new_j)` is within bounds and 
         `dist[new_i][new_j] > dist[i][j] + 1`:
            - Update `dist[new_i][new_j] = dist[i][j] + 1`.
            - Enqueue `(new_i, new_j)`.

4. Return the Result:
   - After the BFS completes, `dist` contains the minimum distances to the 
     nearest 0 for all cells.
   - Return `dist` as the result.

---

Time and Space Complexity

- Time Complexity: O(m * n)
  - Each cell is processed at most once.
  - The BFS expands the frontier cell by cell, resulting in linear time with 
    respect to the number of cells.

- Space Complexity: O(m * n)
  - The `dist` matrix requires O(m * n) space.
  - The queue can hold up to O(m * n) elements in the worst case, such as when 
    all cells are filled with 1s except for a few 0s.
"""

from typing import List
from collections import deque

class Solution:
    # def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
    def updateMatrix(self, mat):

        # Null check
        if not mat or not mat[0]:
            return []

        R, C = len(mat), len(mat[0])

        result = [[float('inf')] * C for _ in range(R)]

        queue = deque()

        # Step 1: Initialize distances and queue
        for r in range(R):
            for c in range(C):
                if mat[r][c] == 0:
                    result[r][c] = 0
                    queue.append((r, c))  # Enqueue all zero cells

        # Directions for up, down, left, right
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

        # Step 2: Perform BFS
        while queue:
            r, c = queue.popleft()
            for dir_r, dir_c in directions:
                new_r, new_c = r + dir_r, c + dir_c
                # Check bounds and update distance if necessary
                if 0 <= new_r < R and 0 <= new_c < C:
                    # The neighbor could reach to 0 in fewer steps than 
                    # it's current steps needed to get to 0
                    if result[new_r][new_c] > result[r][c] + 1:
                        result[new_r][new_c] = result[r][c] + 1
                        queue.append((new_r, new_c))

        return result

