"""
463. Island Perimeter
https://leetcode.com/problems/island-perimeter/description/
"""

from typing import List


class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        def dfs(r: int, c: int) -> int:
            if r < 0 or c < 0 or r > len(grid) or c > len(grid[0]):
                return 1
            if (r, c) in visited:
                return 0

            visited.add((r, c))

            return dfs(r - 1, c) + dfs(r + 1, c) + dfs(r, c - 1) + dfs(r, c + 1)

        visited = set()

        for row_idx in range(len(grid)):
            for col_idx in range(len(grid[0])):
                if grid[row_idx][col_idx] == 1:
                    return dfs(row_idx, col_idx)
