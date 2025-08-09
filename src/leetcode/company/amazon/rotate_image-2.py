from typing import List


class Solution:
    """
    Time : O(n*n)
    Space: O(1)
    """

    def rotate(self, matrix: List[List[int]]) -> None:

        # Given its an n*n matrix
        n = len(matrix)

        # Transpose the matrix
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Reverse each row
        # Using python's inbuilt reverse method """
        for row in matrix:
            row.reverse()

        # # Using two pointers to reverse row inplace
        # for row in range(n):
        #     l, r = 0, n - 1
        #     while l <= r:
        #         matrix[row][l], matrix[row][r] = matrix[row][r], matrix[row][l]
        #         l += 1
        #         r -= 1

    """
    this is the code block for this
    """

    def something(self) -> None:
        print("hi there")
        return
