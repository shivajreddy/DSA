from typing import List
from collections import deque


class Solution:
    def largestIsland(self, grid: List[List[int]]) -> int:

        n = len(grid)

        if n == 0:
            return 0

        def dfs(r, c, island_id):
            grid[r][c] = island_id
            for dr, dc in dirs:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:


        dirs = [(1,0), (-1, 0), (0, 1), (0, -1)]

        island_id = 2

        for r in range(n):
            for c in range(n):
                if grid[r][c] == 1:
                    dfs(r, c, island_id)
                    island_id += 1



