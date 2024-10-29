from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        R = len(grid)
        C = len(grid[0])

        dirs = [(1, 0), (0, 1), (-1, 0), (0, -1)]

        def dfs(r, c):
            if r < 0 or r >= R or c < 0 or c >= C or grid[r][c] == '0':
                return
            grid[r][c] = '0'

            for dr, dc in dirs:
                dfs(r + dr, c + dc)

        islands = 0

        for r in range(R):
            for c in range(C):
                if grid[r][c] == '1':
                    dfs(r, c)
                    islands += 1

        return islands
