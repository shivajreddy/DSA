from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        return False


# TEST -----------------
sol = Solution()
assert sol.canJump([2, 3, 1, 1, 4])

assert not sol.canJump([3, 2, 1, 0, 4])
