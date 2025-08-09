"""
# Problem: Rotate Image (Matrix)

## Section 1: Problem Explanation and Solution Overview
The problem asks to rotate a given `n x n` matrix by 90 degrees in place, which means modifying the matrix directly without using extra space for another matrix.

### Solution Explanation:
- The solution involves two main steps:
  1. **Transpose the Matrix**: Convert rows into columns by swapping elements such that the element at position (i, j) is swapped with the element at position (j, i).
  2. **Reverse Each Row**: After transposing, reverse each row to complete the 90-degree clockwise rotation.

- This approach ensures that the rotation is done in-place without using additional space, and the matrix is rotated efficiently in O(n²) time, where `n` is the number of rows/columns in the matrix.
"""


from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        n = len(matrix)

        # Step 1: Transpose the matrix (swap rows with columns)
        for r in range(n):
            for c in range(r + 1, n):
                matrix[r][c], matrix[c][r] = matrix[c][r], matrix[r][c]

        # Step 2: Reverse each row
        for r in range(n):
            left, right = 0, n - 1
            while left < right:
                matrix[r][left], matrix[r][right] = matrix[r][right], matrix[r][left]
                left += 1
                right -= 1

        return

"""
## Section 3: Test cases & Improvements for pushing to production

### Test Cases:

#### Test Case 1:
- Input: `matrix = [[1,2,3],[4,5,6],[7,8,9]]`
- Output: `[[7,4,1],[8,5,2],[9,6,3]]`
- Explanation: The matrix is rotated 90 degrees clockwise.

#### Test Case 2:
- Input: `matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]`
- Output: `[[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]`
- Explanation: The matrix is rotated 90 degrees clockwise.

#### Test Case 3:
- Input: `matrix = [[1]]`
- Output: `[[1]]`
- Explanation: Single element matrix remains unchanged after rotation.

### Improvements:

1. **Edge Case Handling:**
   - Handle cases where the matrix is empty or contains a single element (like `matrix = [[1]]`), ensuring no errors occur.
   
2. **Performance Optimization:**
   - The time complexity is O(n²), which is optimal for this problem. No further improvements are necessary for performance.

3. **Error Handling:**
   - Ensure the input is a valid `n x n` matrix.
   - Handle cases where the input is not a square matrix, if applicable, by throwing an appropriate error.

4. **Scalability:**
   - The current implementation scales well as it operates in-place, using O(1) extra space, making it suitable even for larger matrices.
"""
