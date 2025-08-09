from typing import List


class Solution:

	def twoSum(self, nums: List[int], target: int) -> List[int]:

		hashmap = {}
		for i in range(0, len(nums)):
			num = nums[i]
			diff = target - num
			if diff in hashmap:
				print(hashmap[diff], i)
				return [hashmap[diff], i]
			hashmap[num] = i

		print([-1, -1])
		return [-1, -1]


s = Solution()
s.twoSum([2, 7, 11, 15], 9)
