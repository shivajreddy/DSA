from typing import List

class Solution:
    """
    - Iterate through each cell in the grid
    - If a cell contains a '1' (land), start a DFS from that cell
    - In the DFS, mark the current cell as visited and recursively explore adjacent land cells
    - After each complete DFS, increment the island count

    Time Complexity: O(M * N), in M x N grid
    Space Complexity: O(M * N) in M x N grid 
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        # Grid size
        R = len(grid)
        C = len(grid[0])

        # Allowed directions to explore
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # Base Case: out of bounds (or) no land
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == "0":
                return
            
            grid[r][c] = "0"  # Mark as visited
            
            # Explore in all four directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1
        
        return islands


class Solution2:
    """
    - Initialize a visited array to track explored cells
    - Iterate through each cell in the grid
    - If a cell contains '1' (land) and is not visited, start a DFS from that cell
    - In the DFS, mark the current cell as visited and recursively explore adjacent unvisited land cells
    - Increment island count after each complete DFS and return the total

    Time Complexity: O(M * N), in M x N grid
    Space Complexity: O(M * N) in M x N grid 

    This version uses additional space for the visited array but avoids modifying the original grid.
    """
    def numIslands(self, grid: List[List[str]]) -> int:
        # Null case
        if not grid:
            return 0

        # Grid size
        R = len(grid)
        C = len(grid[0])

        # Track all visited coordinates on grid
        visited = [[False] * C for _ in range(R)]

        # Allowed directions to explore
        directions = [(1,0), (-1, 0), (0, 1), (0, -1)]

        def dfs(r, c):
            # Base Case: out of bounds
            if r < 0 or r >= R or c < 0 or c >= C:
                return
            # Base Case: no land, (or) already visited
            if grid[r][c] == '0' or visited[r][c]:
                return

            visited[r][c] = True    # Mark as visited

            # Explore in all four directions
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        islands = 0
        for r in range(R):
            for c in range(C):
                if grid[r][c] == "1" and not visited[r][c]:
                    dfs(r, c)
                    islands += 1

        return islands

