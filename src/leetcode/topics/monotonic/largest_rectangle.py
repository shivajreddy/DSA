from typing import List


class Solution2:
    def largestRectangleArea(self, heights: List[int]) -> int:
        heights.append(0)  # Append a zero to handle remaining bars
        stack = [-1]  # Initialize stack with sentinel value
        max_area = 0

        for i in range(len(heights)):
            # While the current bar is smaller than the last stacked bar
            while heights[i] < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = i - stack[-1] - 1  # Calculate the width
                max_area = max(max_area, height * width)
            stack.append(i)
        heights.pop()  # Clean up the appended zero
        return max_area


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)

        # Initialize arrays to track left and right boundaries

        # Default to -1 if no smaller element found
        left_smaller = [-1] * n

        # Default to n (out of bounds) if no smaller element found
        right_smaller = [n] * n

        # Stack to maintain monotonically increasing indices
        stack = []

        # Find left smaller
        for i in range(n):
            # Pop elements larger than current height
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            # Set left boundary
            if stack:
                left_smaller[i] = stack[-1]

            # Push current index
            stack.append(i)

        # Clear stack for right smaller computation
        stack.clear()

        # Find right smaller
        for i in range(n - 1, -1, -1):
            # Pop elements larger than current height
            while stack and heights[stack[-1]] >= heights[i]:
                stack.pop()

            # Set right boundary
            if stack:
                right_smaller[i] = stack[-1]

            # Push current index
            stack.append(i)

        # Calculate maximum rectangle
        max_area = 0
        for i in range(n):
            # Calculate width by right - left - 1
            width = right_smaller[i] - left_smaller[i] - 1
            area = width * heights[i]
            max_area = max(max_area, area)

        print("heights:", heights)
        print(
            "left_smaller : ",
            [str(heights[i]) if i != -1 else "-" for i in left_smaller],
        )
        print(
            "right_smaller: ",
            [
                (str(heights[i]) if i < len(right_smaller) else "-")
                for i in right_smaller
            ],
        )
        print("")
        return max_area


# TESTS --------
sol = Solution()
assert sol.largestRectangleArea([2, 1, 5, 6, 2, 3]) == 10
assert sol.largestRectangleArea([2, 4]) == 4
assert sol.largestRectangleArea([1]) == 1
assert sol.largestRectangleArea([9, 0]) == 9
assert sol.largestRectangleArea([1, 1]) == 2
assert sol.largestRectangleArea([2, 0, 2]) == 2
