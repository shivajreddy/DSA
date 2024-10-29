from collections import deque
from typing import List

class Solution:
    """
    - Count all fresh oranges and queues the positions of initially rotten oranges
    - Edge Case: 
        - If there are no fresh oranges, return 0
        - If there are fresh oranges but no rotten ones, return -1
    - BFS Process:
        - rotting adjacent fresh oranges each minute and addthem to the queue
        - max_time increments each time a new level of oranges is processed
    - After BFS, if any fresh oranges remain, return -1. Else return max_time

    Time : O(R × C) for R x C grid, go over all coordinates
    Space: O(R × C) for R x C grid, due to the queue storing positions of rotten oranges.
    """
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
                # Found a fresh orange
                if grid[r][c] == 1:                
                    fresh += 1
                # Found a rotten orange
                elif grid[r][c] == 2:              
                    rotten.append((r,c))    

        # If there are no fresh oranges, no time is required to rot them
        if fresh == 0:
            return 0

        # If there are fresh oranges, but no rotten oranges, can't rot any
        if len(rotten) == 0:
            return -1

        # Count the maximum time take
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
            # Important: we only increase time, if we did rot anything. First level of queue
            # holds the given rotten oranges, further levels are the rotten oranges every minute
            if rotten:
                max_time += 1

        # Couldn’t rot all fresh oranges
        if fresh > 0:
            return -1

        # return the maximum time to rot all the oranges
        return max_time
