from __future__ import annotations

'''
There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The 
robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or 
right at any point in time.

Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the 
bottom-right corner.

Example 1:
Input: m = 3, n = 7
Output: 28

Example 2:
Input: m = 3, n = 2
Output: 3
Explanation: From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Down -> Down
2. Down -> Down -> Right
3. Down -> Right -> Down
'''

'''
Question 1. Solve the above problem using Top Down Dynamic Programming
'''


def unique_paths_top_down(m: int, n: int) -> int:
    def rec(x, y):
        if x == 1 or y == 1:
            return 1
        return rec(x - 1, y) + rec(x, y - 1)

    return rec(m, n)


'''
Question 2. Solve the above problem using Bottom Up Dynamic Programming
'''


def unique_paths_bottom_up(m: int, n: int) -> int:
    matrix = [
        [0 for _ in range(n)] for _ in range(m)
    ]
    # for idx in range(len(matrix)):
    for idx in range(m):
        matrix[idx][0] = 1
    # for idx in range(len(matrix[0])):
    for idx in range(n):
        matrix[0][idx] = 1

    for row in range(1, m):
        for col in range(1, n):
            matrix[row][col] = matrix[row - 1][col] + matrix[row][col - 1]
    print(f'matrix= {matrix}')
    return matrix[m - 1][n - 1]
