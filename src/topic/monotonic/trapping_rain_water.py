from typing_extensions import List


class Solution:
    """
    Time: O(n)
    Space: O(n)
    """

    def trap(self, height: List[int]) -> int:

        n = len(height)

        # Find left and right bounds for each index
        left_greatest = [0] * n  # highest num on right side from current index
        right_greatest = [0] * n  # highest num on left side from current index

        max_l = height[0]
        for i in range(1, n):
            left_greatest[i] = max_l
            max_l = max(max_l, height[i])

        max_r = height[-1]
        for i in range(n - 2, -1, -1):
            right_greatest[i] = max_r
            max_r = max(max_r, height[i])

        water = 0

        # Trap water at every index, based on its left & right bounds
        for i in range(n):
            if left_greatest[i] > height[i] < right_greatest[i]:
                water += min(left_greatest[i], right_greatest[i]) - height[i]

        return water

    """
    Time: O(n)
    Space: O(1)
    """

    def trap_v2(self, height: List[int]) -> int:

        left_bound = height[0]
        right_bound = height[-1]

        water = 0
        left, right = 0, len(height) - 1

        while left < right:
            if height[left] < height[right]:
                left_bound = max(left_bound, height[left])
                water += left_bound - height[left]
                left += 1
            else:
                right_bound = max(right_bound, height[right])
                water += right_bound - height[right]
                right -= 1
        return water


# TESTS --------------
sol = Solution()
assert sol.trap([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert sol.trap([4, 2, 0, 3, 2, 5]) == 9
assert sol.trap_v2([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]) == 6
assert sol.trap_v2([4, 2, 0, 3, 2, 5]) == 9
