from typing import List


class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        pass


# TESTS ---------
sol = Solution()
assert sol.dailyTemperatures([73, 74, 75, 71, 69, 72, 76, 73]) == [
    1,
    1,
    4,
    2,
    1,
    1,
    0,
    0,
]
assert sol.dailyTemperatures([30, 40, 50, 60]) == [1, 1, 1, 0]
assert sol.dailyTemperatures([30, 60, 90]) == [1, 1, 0]
