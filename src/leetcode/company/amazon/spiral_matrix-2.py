from typing import List

class Solution:
    """
    - Uses directions to guide movement and checks if the next position is valid
    - Have a set to store the visited locations
    - If the next move is invalid, the direction is updated.
    - The process continues until all matrix elements are visited.

    Time : O(R * C). R = No.of Rows, C = No.of Columns
    Space: O(R * C) for storing the output list and the visited set.
    """
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # Directions: right, down, left, up
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]

        rows = len(matrix)
        cols = len(matrix[0])

        spiral_order = []
        visited_positions = set()

        current_row = current_col = current_direction = 0
        for _ in range(rows * cols):
            # Add current element to the spiral order & mark as visited
            spiral_order.append(matrix[current_row][current_col])
            visited_positions.add((current_row, current_col))

            # Calculate the next position in the current direction
            next_row, next_col = (current_row + directions[current_direction][0], 
                                  current_col + directions[current_direction][1])
            
            # Check if the next position is valid and unvisited
            if 0 <= next_row < rows and 0 <= next_col < cols and (next_row, next_col) not in visited_positions:
                current_row, current_col = next_row, next_col
            else:
                # Change direction if the next position is invalid
                current_direction = (current_direction + 1) % 4
                current_row += directions[current_direction][0]
                current_col += directions[current_direction][1]
        
        return spiral_order

