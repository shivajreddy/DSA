# https://leetcode.com/problems/maximum-subarray/submissions/

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        s = 0
        max_sum = float('-inf')

        for num in nums:
            s += num
            max_sum = max(max_sum, s)
            # if it -ve then reset to 0, cause
            # we are looking for larger sum
            if s < 0:
                s = 0

        return max_sum
