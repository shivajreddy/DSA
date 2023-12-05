"""
417. Pacific Atlantic Water Flow
https://leetcode.com/problems/pacific-atlantic-water-flow/
"""
from typing import List


def pacificAtlantic(heights: List[List[int]]) -> List[List[int]]:
    ROWS, COLS = len(heights), len(heights[0])

    def dfs(r, c, prev_height, visited):
        # base case :: shouldn't be out of bounds, should not been visited before, show have ht. < prev_height
        if r < 0 or r >= ROWS or c < 0 or c >= COLS or (r, c) in visited or heights[r][c] < prev_height:
            return

        visited.add((r, c))  # mark as visited, since working on the node

        # perform DFS on all neighbours
        dfs(r + 1, c, heights[r][c], visited)
        dfs(r - 1, c, heights[r][c], visited)
        dfs(r, c + 1, heights[r][c], visited)
        dfs(r, c - 1, heights[r][c], visited)

    pac, atl = set(), set()

    for r in range(ROWS):
        dfs(r, 0, heights[r][0], pac)
        dfs(r, COLS - 1, heights[r][COLS - 1], atl)

    for c in range(COLS):
        dfs(0, c, heights[0][c], pac)
        dfs(ROWS - 1, c, heights[ROWS - 1][c], atl)

    inter = pac.intersection(atl)
    result = []
    for tup in inter:
        result.append(list(tup))

    return result


h = [[1, 2, 2, 3, 5], [3, 2, 3, 4, 4], [2, 4, 5, 3, 1], [6, 7, 1, 4, 5], [5, 1, 1, 2, 4]]
print(pacificAtlantic(h))
