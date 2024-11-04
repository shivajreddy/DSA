from typing_extensions import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        return []


# TESTS -----------------
sol = Solution()
assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert sol.maxSlidingWindow([1], 1) == [1]
