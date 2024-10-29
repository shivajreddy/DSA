"""
"""

from typing import List

class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:

        n = len(nums)
        nums.sort()
        res = []

        for a in range(n):

            if a > 0 and nums[a] == nums[a-1]:
                continue

            '''
            - The reason we cant skip nums[a] if nums[a] > target,
              or skip if nums[a] + nums[b]] > target, is because, of -ve numbers
            - because a,b,c,d could be -ve nums, so when we want to skip nums[a]
              we cant because b could be -ve and it will bring [a]+[b] down
              - similarly just cuz [a]+[b] > target doesn't meat we shouldn't
                explore c,d cuz they could be -ve and yield to result
            '''

            for b in range(a+1, n):

                if b > a + 1 and nums[b] == nums[b-1]:
                    continue

                c, d = b + 1, n - 1
                while c < d:
                    fs = nums[a] + nums[b] + nums[c] + nums[d]
                    if fs == target:
                        res.append([nums[a], nums[b], nums[c], nums[d]])
                        c += 1
                        d -= 1
                        while c < d and nums[c] == nums[c-1]:
                            c += 1
                        while c < d and nums[d] == nums[d+1]:
                            d -= 1

                    elif fs < target:
                        c += 1
                    else:
                        d -= 1
        return res

