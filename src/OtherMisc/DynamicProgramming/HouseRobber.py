class Solution:

    def rob(self, nums: list[int]) -> int:
        return self.rec(nums, 0, {})

    def rec(self, nums, i, hm):

        # base case
        if i >= len(nums):
            return 0
        if i in hm:
            return hm[i]

        curr = nums[i] + self.rec(nums, i + 2, hm)
        skip_curr = self.rec(nums, i + 1, hm)
        hm[i] = max(curr, skip_curr)
        return hm[i]


s = Solution()
print(s.rob([1, 2, 3, 1]))
print(s.rob([2, 7, 9, 3, 1]))
print(s.rob([1, 2]))
print(s.rob([1, 3, 1]))
