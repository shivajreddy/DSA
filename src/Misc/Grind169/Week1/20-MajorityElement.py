# https://leetcode.com/problems/majority-element/
class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        hm = {}
        n = len(nums)

        for num in nums:
            count = hm.get(num, 0) + 1
            hm[num] = count
            if count >= n/2:
                return num

        return -1
