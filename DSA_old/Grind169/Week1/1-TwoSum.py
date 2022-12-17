class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        # O(n) -> iterate over the array, return if target, update freq map,

        freq = {}

        for i in range(len(nums)):
            curr = nums[i]
            diff = target - curr
            if diff in freq:
                return [freq[diff], i]
            freq[curr] = i
