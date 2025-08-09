from typing import List


class Solution:
    """
    Brute-force : O(N^2)
    Optimized using two pointers

    This approach works because:
    - By moving the shorter line inward, we maximize the potential for a larger area,
      as increasing the shorter height is the better way for finding a larger container.

    Time: O(N)
    Space: O(1)
    """

    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0

        while left < right:
            # Calculate the current area
            current_area = min(height[left], height[right]) * (right - left)
            # Update max_area if the current area is larger
            max_area = max(max_area, current_area)

            # Move the pointer pointing to the shorter line
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
