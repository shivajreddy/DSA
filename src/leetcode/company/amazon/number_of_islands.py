""" Solution if given input is IMMUTABLE:
### Approach:
The algorithm uses Depth-First Search (DFS) to explore and mark all cells
belonging to a particular island. The DFS begins when an unvisited land cell
('1') is encountered. From there, it recursively explores all adjacent land
cells and marks them as visited. This process is repeated for each unvisited
land cell found in the grid.


### Steps:
- **Track Visited Cells**: A `visited` set is used to keep track of all visited
  cells to prevent reprocessing.
- **DFS**: A helper function `explore_island` uses DFS to recursively mark all
  the connected land cells of an island as visited.
- **Main Loop**: The algorithm iterates over all the cells in the grid. If an
  unvisited land cell is found, it triggers the DFS to explore the entire
  island and increments the island count.
- **Explore Directions**: The four possible directions to explore from any cell
  are right, down, left, and up.


### Time Complexity:
- **`O(R * C)`**: where `R` is the number of rows and `C` is the number of
  columns in the grid. Each cell is visited once.


### Space Complexity:
- **`O(R * C)`**: due to the recursion stack and the `visited` set to track
  explored cells.


"""


from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Size of grid
        R = len(grid)
        C = len(grid[0])


        # Track already visited coordinates, with O(1) lookup
        visited = set()


        # Allowed directions: Right, Down, Left, Up
        dirs = [(0,1), (1,0), (0,-1), (-1,0)]


        # Cover/Explore entire island using DFS
        def explore_island(r, c):
            visited.add((r, c))
            for dr, dc in dirs:
                new_r, new_c = r + dr, c + dc  # Keep original r, c intact
                if 0 <= new_r < R and 0 <= new_c < C and (new_r, new_c) not in visited and grid[new_r][new_c] == '1':
                    explore_island(new_r, new_c)


        total_islands = 0

        # Go over all coordinates
        for r in range(R):
            for c in range(C):
                if (r, c) not in visited and grid[r][c] == '1':
                    total_islands += 1
                    explore_island(r, c)


        return total_islands




""" Solution if given input is mutable:

### Problem Breakdown:
We are given a 2D grid of `'1's` (land) and `'0's` (water). We need to count
the number of islands, where an island is defined as a group of adjacent `'1's`
(horizontally or vertically), surrounded by `'0's`.


This is a classic graph traversal problem, where the grid can be viewed as a
graph, and the goal is to count the connected components of `'1's`. We can use
either Depth First Search (DFS) or Breadth First Search (BFS) to explore and
mark the connected land cells.


### Plan:
1. **Traverse the grid**: For each cell, if it is `'1'`, initiate a DFS or BFS
   to mark all the connected cells (land) and count it as one island.
2. **Mark visited cells**: Once a cell is visited, mark it as `'0'` (or a
   different marker) to prevent revisiting.
3. **Boundaries**: Ensure the traversal does not go out of bounds of the grid.


### Time Complexity:
- **Time**: `O(M * N)` where `M` is the number of rows and `N` is the number of
  columns. Every cell is visited at most once.
- **Space**: `O(min(M, N))` due to the stack space in the recursive DFS (or BFS
  queue size).
"""


class Solution2:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Null case
        if not grid:
            return 0

        rows, cols = len(grid), len(grid[0])
        num_islands = 0

        # Allowed directions: up, down, left, right
        directions = ((-1, 0), (1, 0), (0, -1), (0, 1))


        def dfs(r, c):
            # Base case: return if out of bounds or water ('0')
            if r < 0 or c < 0 or r >= rows or c >= cols or grid[r][c] == '0':
                return

            # Mark the cell as visited by setting it to '0'
            grid[r][c] = '0'


            # Explore neighbors: up, down, left, right
            for direction in directions:
                dfs(r + direction[0], c + direction[1])


        # Traverse the grid
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == '1':
                    # Start DFS from the current cell
                    num_islands += 1
                    dfs(r, c)


        return num_islands

