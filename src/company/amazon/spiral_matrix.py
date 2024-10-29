"""
### Spiral Matrix Traversal

This solution aims to traverse a matrix in a "spiral order," starting from the top-left corner,
moving right, down, left, and up, repeating this pattern until all elements have been visited.

### Approach:
1. **Edge Case Handling**: 
   - If the matrix is empty or has no columns, return an empty list immediately.
   
2. **Initialization**:
   - Use a **deque** to store the four possible directions: right, down, left, and up.
   - Keep track of the number of rows and columns, and the total number of elements in the matrix.
   - Initialize a list to hold the result and a set to track visited cells.
   - Start at the top-left corner of the matrix.

3. **Traversal**:
   - In each iteration, add the current cell value to the result and mark the cell as visited.
   - Calculate the next cell based on the current direction.
   - If the next cell is within the matrix bounds and hasn't been visited, move to the next cell.
   - If the next cell is invalid (out of bounds or already visited), rotate the direction deque
     to change direction and update the current cell.

4. **Termination**:
   - Continue this process until all matrix elements have been added to the result list.


Time Complexity: O(m * n)
    - Where m is the number of rows and n is the number of columns. Each element
      of the matrix is visited exactly once.

Space Complexity: O(m * n)
    - We store the result list which contains m * n elements, and the visited set that 
      tracks the state of every matrix cell.
    - The directions deque always contains four items, so its space complexity is O(1).

### Code Explanation:
"""


from typing import List
from collections import deque

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix or not matrix[0]:
            return []

        # Define the four possible movement directions
        directions = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])  # Right, Down, Left, Up
        rows = len(matrix)
        cols = len(matrix[0])
        total_elements = rows * cols

        result = []
        visited = set()

        # Starting position
        curr_row, curr_col = 0, 0

        while len(result) < total_elements:
            result.append(matrix[curr_row][curr_col])
            visited.add((curr_row, curr_col))

            # Calculate next position in the current direction
            dir_row, dir_col = directions[0]
            next_row, next_col = curr_row + dir_row, curr_col + dir_col

            # Check if the next position is valid and not visited
            if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in visited:
                curr_row, curr_col = next_row, next_col
            else:
                # Change direction if the next position is invalid
                directions.rotate(-1)  # Rotate the direction deque to the left
                dir_row, dir_col = directions[0]  # Update the direction
                curr_row, curr_col = curr_row + dir_row, curr_col + dir_col

        return result

