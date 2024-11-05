from typing import List


class Solution:
    """
    Time : O(n)
    Space: O(n)
    """

    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        answer = [0] * n

        # Next greater element
        # Decreasing mono stack
        stack = []
        for idx, num in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < num:
                top_idx = stack.pop()
                answer[top_idx] = idx - top_idx
            stack.append(idx)

        return answer


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
