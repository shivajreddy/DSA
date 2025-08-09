from typing import List

class Solution:
    """
    Sort the given input, find triplets going every element and using sliding 
    window over rest of the numbers, starting from the current number

    Time : O(n.log(n))
    Space: O(n)
    """
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        nums.sort()

        triplets = []

        for i in range(n):

            # Skip duplicates of i
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            # Break early, since remaining numbers are > 0
            if nums[i] > 0:
                continue

            j = i + 1
            k = n - 1

            # Sliding window to find valid j,k
            while j < k:

                # Break early, since remaining numbers are > 0
                if nums[i] + nums[j] > 0:
                    break

                three_sum = nums[i] + nums[j] + nums[k]

                if three_sum == 0:
                    triplets.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates of j
                    while j < k and nums[j] == nums[j-1]:
                        j += 1

                    # Skip duplicates of k
                    while j < k and nums[k] == nums[k+1]:
                        k -= 1

                elif three_sum < 0:
                    j += 1
                else:
                    k -= 1

        return triplets

