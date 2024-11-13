from typing import List


class Solution:
    """
    Time : a
    Space: a
    """

    def lengthOfLIS(self, nums: List[int]) -> int:
        res = 0
        stack = []
        for num in nums:
            while stack and stack[-1] >= num:
                stack.pop()
            stack.append(num)
            res = max(res, len(stack))

        print(res)
        return res


# TESTS --------------
sol = Solution()
assert sol.lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]) == 4
assert sol.lengthOfLIS([0, 1, 0, 3, 2, 3]) == 4
assert sol.lengthOfLIS([7, 7, 7, 7, 7, 7, 7]) == 1
