"""
Approach  
    We need to check three conditions:  
        - Rows: No duplicate numbers in any row.  
        - Columns: No duplicate numbers in any column.  
        - Sub-boxes (3x3 grids): No duplicate numbers in any of the nine sub-boxes.  

    We can use sets to keep track of seen numbers for rows, columns, and sub-boxes.  

Algorithm Steps  
    1. Initialize Data Structures:  
        - Use a list of sets for rows (`rows[9]`), columns (`cols[9]`), and sub-boxes (`boxes[9]`).  
    2. Iterate Over the Board:  
        - For each cell `(i, j)`:
            - If the cell contains a digit (not `'.'`):
                - Check if the digit is already in the corresponding row, column, or box set:
                    - Row: `rows[i]`
                    - Column: `cols[j]`
                    - Box: `boxes[(i // 3) * 3 + (j // 3)]`
                - If it is, return False.
                - Otherwise, add the digit to the respective sets.  
    3. Return True:  
        - If no duplicates are found after iterating through all cells, return True.  

"""


from typing import List
import math


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        n = 9
        m = int(math.sqrt(n))

        # Initialize lists of sets for rows, columns, and boxes
        cols = [set() for _ in range(n)]
        rows = [set() for _ in range(n)]
        boxes = [set() for _ in range(n)]

        # Iterate over each cell in the board
        for r in range(n):
            for c in range(n):
                num = board[r][c]
                if num != '.':
                    # Calculate box index
                    b = (r // m) * m + (c // m)

                    # Check for duplicates
                    if (num in rows[r] or
                        num in cols[c] or
                        num in boxes[b]):
                        return False

                    # Add the number to the sets
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[b].add(num)

        return True

