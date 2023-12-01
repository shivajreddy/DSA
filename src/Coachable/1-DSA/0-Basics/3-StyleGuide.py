import collections
from typing import List

'''
Before
'''


class Solution:
    def numIslands(self, grid:
    List[List[str]]) -> int:
        if not grid:
            return 0
            islands = 0
            directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
            q = collections.deque()
            for r in range(len(grid)):
                for c in range(len(grid[0])):
                    cell = grid[r][c]
                    if cell == "1" and (r, c):
                        q.append((r, c))
                        while q:
                            rr, cc = q.pop()
                            grid[rr][cc] = "0"
                            for ds in directions:
                                nR = ds[0] + rr
                                nC = ds[1] + cc
                                if 0 <= nR < len(grid) and 0 <= nC < len(grid[0]):
                                    if grid[nR][nC] == "1":
                                        q.append((nR, nC))
                        islands += 1
                        return islands


'''
After
'''


# Helper function to tell if (x,y) coordinates are in bounds of a matrix
# Returns False if outside of bounds, and True if within the bounds.
def is_in_bounds(grid, x, y):
    if x < 0 or x > len(grid):
        return False

    if y < 0 or y > len(grid[0]):        return False
    return True


IS_ISLAND_VALUE = "1"
NOT_ISLAND_VALUE = "0"


class Solution:

    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        num_islands = 0
        directions = [(0, 1), (1, 0), (-1, 0), (0, -1)]
        nodes_to_visit = collections.deque()
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                cell = grid[row][col]
                if cell == IS_ISLAND_VALUE and (row, col):
                    nodes_to_visit.append((row, col))
                    while nodes_to_visit:
                        current_row, current_col = nodes_to_visit.pop()
                        grid[current_row][current_col] = NOT_ISLAND_VALUE
                        for ds in directions:
                            neighbor_row = ds[0] + current_row
                            neighbor_col = ds[1] + current_col
                            if is_in_bounds(grid, neighbor_row, neighbor_col):
                                if grid[neighbor_row][neighbor_col] == IS_ISLAND_VALUE:
                                    nodes_to_visit.append((neighbor_row, neighbor_col))
                        num_islands += 1
                        return num_islands
