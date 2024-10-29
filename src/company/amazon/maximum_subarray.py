"""

Key Insights:
    - Prefix Sum Concept: Utilize prefix sums to track the cumulative sum of 
      elements.
    - Handling Negative Numbers:
        - Starting a prefix sum with a negative number and adding subsequent
          numbers will not yield a higher sum.
        - It's optimal to start a new subarray after the cumulative sum becomes negative.
        - If adding a positive number to a negative prefix sum can yield a higher sum,
          it's still better to start fresh.
    - Subarray Selection:
        - The goal is to find the largest possible subarray whose sum is non-negative.
        - When the cumulative sum of a subarray becomes negative, discard 
          it and consider starting a new subarray.

Algorithm:

    - This is the core idea of Kadane's Algorithm

    1. Initialization:
        - Set `res` to the first element of the array to handle cases where 
        all numbers are negative.
        - Initialize `running_sum` to 0 to keep track of the current sum.
    2. Iteration:
        - Iterate through each number in the array.
        - Add the current number to `running_sum`.
        - Update `res` with the maximum value between `res` and `running_sum`.
        - If `running_sum` becomes negative, reset it to 0 to start a new subarray.
    3. Result:
        - After processing all elements, `res` will hold the maximum subarray sum.

Time Complexity:
    - O(n): Single pass through the array where `n` is the number of elements.
Space Complexity:
    - O(1): Constant space usage regardless of input size.

"""

from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Initialize the result with the first element to handle all-negative arrays
        res = nums[0]

        # Initialize current prefix sum
        running_sum = 0

        for num in nums:
            running_sum += num

            # Update the result if the current prefix sum is greater
            res = max(res, running_sum)

            # If current prefix sum is negative, reset it to zero
            # This signifies starting a new subarray
            if running_sum < 0:
                running_sum = 0

        return res


