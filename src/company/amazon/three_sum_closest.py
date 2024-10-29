from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:

        nums.sort()
        n = len(nums)

        diff = float('inf')
        res = -1

        for i in range(n):

            j, k = i + 1, n - 1

            while j < k:
    
                ts = nums[i] + nums[j] + nums[k]
                curr_diff = abs(ts - target)
    
                if curr_diff == 0:
                    return ts
                
                if curr_diff < diff:
                    res = ts
                    diff = curr_diff
                
                if ts < target:
                    j += 1
                else:
                    k -= 1
        
        return res

