from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        result = float('-inf')
        curr_sum = 0

        for num in nums:
            curr_sum += num
            result = max(result, curr_sum)

            # when dealing with -ve numbers, reset window_sum, so that next window_sum is the next -ve number
            if curr_sum < 0:
                curr_sum = 0

        return result
