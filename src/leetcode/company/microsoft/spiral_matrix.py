from collections import deque


class Solution:
    def spiralOrder(self, matrix):
        res = []

        # Directions for right, down, left, up
        dirs = deque([(0, 1), (1, 0), (0, -1), (-1, 0)])
        rotation_idx = 0

        min_row, max_row = 0, len(matrix) - 1
        min_col, max_col = 0, len(matrix[0]) - 1

        row, col = 0, 0
        n = len(matrix) * len(matrix[0])

        while len(res) < n:
            res.append(matrix[row][col])

            # Determine next position
            next_row = row + dirs[rotation_idx][0]
            next_col = col + dirs[rotation_idx][1]

            # Check if out of bounds
            if (
                next_row < min_row
                or next_row > max_row
                or next_col < min_col
                or next_col > max_col
            ):
                # Adjust bounds and switch direction
                if rotation_idx == 0:  # Left->Right, Shrink top
                    min_row += 1
                elif rotation_idx == 1:  # Top->Down, Shrink right
                    max_col -= 1
                elif rotation_idx == 2:  # Right->Left, Shrink bottom
                    max_row -= 1
                elif rotation_idx == 3:  # Down->Top, Shrink left
                    min_col += 1

                # Rotate direction
                rotation_idx = (rotation_idx + 1) % 4
                row += dirs[rotation_idx][0]
                col += dirs[rotation_idx][1]
            else:
                # Continue in the same direction
                row, col = next_row, next_col

        return res


def print_list(lst):
    print(" ".join(map(str, lst)))


# Test cases
solution = Solution()

matrix1 = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
result1 = [1, 2, 3, 6, 9, 8, 7, 4, 5]
print_list(solution.spiralOrder(matrix1))
print_list(result1)

matrix2 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
result2 = [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7]
print_list(solution.spiralOrder(matrix2))
print_list(result2)
