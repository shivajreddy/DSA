from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0

        for idx, num in enumerate(nums):
            if idx > max_reach:
                return False
            max_reach = max(max_reach, idx + num)
            if max_reach >= len(nums) - 1:
                return True

        return False


# TEST -----------------
sol = Solution()
assert sol.canJump([2, 3, 1, 1, 4])

assert not sol.canJump([3, 2, 1, 0, 4])
