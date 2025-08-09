""" 
Description:

- Use bfs to go level by level. for every new level, the time taken to rot the oranges in queue was
  increased by 1. So starting at the first level, where we hold the oranges that were already rotten
  we say time taken to rot these oranges is 0.
- We iterate over all rotten oranges in this level, and find the next set of oranges that can be
  rotted (why couldn’t they describe the problem the other way round, feel bad for wasting some
  fresh oranges here lol). For an orange that can be rotted with the current orange, this child
  should be with in bounds and be a fresh orange. Before adding these to the queue, we rot them
  decrease fresh orange count
- Mark the value at this location as rotted, so that we don’t re-visit this location.
- Before moving to the next level, we check if there are any oranges in the queue to begin with,
  if there are then we increase the time, because the next level would take the current_time + 1.

Time & Space:
    Time:
    - We visite all nodes 1 time. Though we are exploring all 4 possible childs, leading to
      total time of (4n) but more formally its O(N).
    Space: 
    - Our queue in the worst case can hold all the cells, meaning if we were given all 
      rotten oranges. so a space of O(N)


        c1      c2      c3      <- time=0 for rotting these oranges
      c5 c6   c7 c8    c9       <- time=1 for rotting these oranges
             .....              <- time=2 for rotting these



### Explanation

This problem involves determining the minimum time required to rot all fresh oranges in a grid.
Rotten oranges can cause adjacent fresh oranges to rot in **4 directions**: up, down, left, and right. 
The task can be solved using **Breadth-First Search (BFS)** because at each minute (or level in BFS), 
the rotten oranges from the previous minute infect adjacent fresh oranges.

---

### Steps

1. **Identify fresh and rotten oranges:**
   - Traverse through the grid to count the fresh oranges and locate the initial rotten oranges. 
   - Rotten oranges are stored in a queue to process their neighbors later.
   
2. **Edge Cases:**
   - If there are no fresh oranges, the result is `0` since no oranges need rotting.
   - If there are fresh oranges but no rotten ones, return `-1` since the fresh oranges cannot be 
     rotted without an initial rotten orange.

3. **Breadth-First Search (BFS):**
   - Process each rotten orange and infect the neighboring fresh oranges.
   - For each level in the BFS, increment the time (minutes).
   - Continue until all possible oranges are infected or there are no more oranges to infect.

4. **Final Check:**
   - If any fresh oranges remain uninfected, return `-1`.
   - Otherwise, return the total time taken to rot all the oranges.

---

### Time Complexity

- **O(R * C)**: where `R` is the number of rows and `C` is the number of columns in the grid.
  - We traverse each cell of the grid at most once during the BFS process.

### Space Complexity

- **O(R * C)**: Space used by the queue to store the rotten oranges, which could contain all cells 
  in the worst case.k

"""


from typing import List
from collections import deque


class Solution:

    def orangesRotting(self, grid: List[List[int]]) -> int:

        # Size of grid
        R = len(grid)
        C = len(grid[0])

        # Track fresh and rotten oranges in the grid
        fresh = 0
        rotten = deque([])

        # Go over all cells in the grid, count rotten & fresh oranges
        for r in range(R):
            for c in range(C):
                if grid[r][c] == 1:                # Found a fresh orange
                    fresh += 1
                elif grid[r][c] == 2:              # Found a rotten orange
                    rotten.append((r,c))    # (row, column)

        # No fresh oranges
        if fresh == 0:
            return 0

        # No rot oranges
        if len(rotten) == 0:
            return 0

        # Count the maximum time take (lowest level in bfs)
        max_time = 0

        # All directions that a rotten orange can look at
        directions = [ (1,0), (-1, 0), (0, 1), (0, -1) ]

        # Go over all the rotten oranges, and rot fresh oranges next to them
        while rotten:
            for _ in range(len(rotten)):
                r,c = rotten.popleft()
                for dr, dc in directions:
                    new_r, new_c = r + dr, c + dc
                    # Look at possible fresh oranges that this rot orange can rot
                    if 0 <= new_r < R and 0 <= new_c < C and grid[new_r][new_c] == 1:
                        grid[new_r][new_c] = 2
                        fresh -= 1
                        rotten.append((new_r, new_c))
            # There is a new level of rotten oranges to go over
            if rotten:
                max_time += 1

        # Couldn't rot all fresh oranges
        if fresh > 0:
            return -1

        # return the maximum time to rot all the oranges
        return max_time

