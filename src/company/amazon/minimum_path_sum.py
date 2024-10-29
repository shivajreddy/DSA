"""
### Key Insights:
- Dynamic Programming (DP) is ideal for this problem, as the minimum path sum 
  at each cell depends on the minimum path sums of the previous cells (top and 
  left).
- We can either:
  - Use a 2D DP array, where each cell represents the minimum sum to reach that 
    cell.
  - Optimize space by reusing the input grid itself, or even just a single 
    row/column of space.

### Plan:
- **Base Case**: The minimum path sum for the top-left cell is the value of 
  that cell itself.
  
- **Recurrence Relation**: For each cell `(i, j)`, the minimum path sum to 
  reach that cell is:
  
  `dp[i][j] = grid[i][j] + min(dp[i−1][j], dp[i][j−1])`
  
  This means the value at each cell is the sum of the current cell's value and 
  the minimum of the values from the top or left cells (if they exist).
  
- **Edge Case Handling**: For the first row, we can only move right, and for 
  the first column, we can only move down.

### Time Complexity:
- `O(m * n)`, where `m` is the number of rows and `n` is the number of 
  columns. We need to process each cell exactly once.

### Space Complexity:
- `O(1)` if we modify the grid in-place, since no additional storage is 
  required.
- Alternatively, we can use `O(n)` if we want to avoid modifying the input and 
  only use a single row or column to store intermediate results.

### Optimized Python Solution (In-Place DP):

#### Explanation:

- **First Row and First Column Initialization**:
  - We update the first row by adding values from left to right. This accounts 
    for the only valid direction for cells in the first row (from the left).
  - Similarly, we update the first column by adding values from top to bottom, 
    as cells in the first column can only be reached from the top.

- **Filling the Rest of the Grid**:
  - For each remaining cell `(i, j)`, the minimum path sum to reach that cell 
    is the minimum of the cell directly above `(i-1, j)` and the cell directly 
    to the left `(i, j-1)`. We add the current cell’s value to the minimum of 
    these two values.

- **Return the Result**:
  - The bottom-right corner `(grid[rows - 1][cols - 1])` now contains the 
    minimum path sum from the top-left to the bottom-right of the grid.
"""
from typing import List

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        
        # Update the first row by accumulating values from left to right
        for j in range(1, cols):
            grid[0][j] += grid[0][j - 1]
        
        # Update the first column by accumulating values from top to bottom
        for i in range(1, rows):
            grid[i][0] += grid[i - 1][0]
        
        # Update the rest of the grid
        for i in range(1, rows):
            for j in range(1, cols):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])
        
        # The bottom-right corner contains the result
        return grid[rows - 1][cols - 1]

"""
### Explanation:

#### dp Array:
- We initialize the `dp` array to hold the minimum path sums for each column. 
  At the start, `dp[0]` holds the value of the top-left cell, and we initialize 
  the rest of the first row in `dp`.

#### Row-wise Processing:
- We process each row, starting from the second. For each row, we first update 
  the first column by adding the current grid cell to the existing value in 
  `dp[0]`.
- For the rest of the row, we update the `dp[j]` for each column using the 
  minimum of the top cell (already in `dp[j]`) and the left cell (`dp[j - 1]`), 
  and add the current grid cell value.

#### Result:
- The last element in `dp` contains the minimum path sum to reach the 
  bottom-right corner of the grid.

"""
class Solution2:
    def minPathSum(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        dp = [0] * cols
        
        dp[0] = grid[0][0]  # Initialize the first cell
        
        # Initialize the first row
        for j in range(1, cols):
            dp[j] = dp[j - 1] + grid[0][j]
        
        # Process the grid row by row
        for i in range(1, rows):
            dp[0] += grid[i][0]  # Update the first column value
            for j in range(1, cols):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]
        
        return dp[-1]

