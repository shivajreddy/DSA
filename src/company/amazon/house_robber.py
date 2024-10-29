"""
Problem: House Robber


You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, represented by an array `nums`. All houses are arranged in a straight line, and you cannot rob two adjacent houses (to avoid alerting the police). Determine the maximum amount of money you can rob tonight without alerting the police.


Constraints:
- 1 <= nums.length <= 100
- 0 <= nums[i] <= 400


Approach:


We solve this problem using Dynamic Programming with optimized space complexity. At each house, we have two choices:


1. **Rob the current house**: Add the current house's amount to the maximum amount robbed from all houses before the previous one.
2. **Skip the current house**: Carry forward the maximum amount robbed till the previous house.


We maintain two variables:
- `prev1`: Maximum amount robbed till the house before the previous one.
- `prev2`: Maximum amount robbed till the previous house.


For each house, we calculate:
- `current = max(nums[i] + prev1, prev2)`


Then we update:
- `prev1 = prev2`
- `prev2 = current`


This ensures we always have the maximum amounts needed for the next calculation, using only constant space.


Time Complexity: O(n), where n is the number of houses.
Space Complexity: O(1), since we use only a fixed amount of extra space.


Edge Cases:
- **No houses**: Return 0.
- **One house**: Return the amount in that house.


Future Improvements:
- Implement error handling for invalid inputs.
- Extend the solution to handle circular arrangements of houses (House Robber II problem).
- Explore recursive solutions with memoization for educational purposes.


Example:


Consider `nums = [2, 7, 9, 3, 1]`


- House 0: `current = max(2 + 0, 0) = 2`
- House 1: `current = max(7 + 0, 2) = 7`
- House 2: `current = max(9 + 2, 7) = 11`
- House 3: `current = max(3 + 7, 11) = 11`
- House 4: `current = max(1 + 11, 11) = 12`


Maximum amount that can be robbed is **12**.
"""


from typing import List


class Solution:
   def rob(self, nums: List[int]) -> int:
       """
       Calculate the maximum amount of money that can be robbed without alerting the police.


       Args:
           nums (List[int]): List of non-negative integers representing the amount of money at each house.


       Returns:
           int: The maximum amount of money that can be robbed.
       """
       # Handle edge cases where there are no houses or just one house
       if not nums:
           return 0
       if len(nums) == 1:
           return nums[0]


       # Initialize variables to store the maximum amounts
       prev1 = 0  # Max amount till the house before the previous one
       prev2 = 0  # Max amount till the previous house


       # Iterate through each house
       for num in nums:
           # Calculate the maximum amount if we rob this house
           current = max(num + prev1, prev2)
           # Update prev1 and prev2 for the next iteration
           prev1 = prev2
           prev2 = current


       # The final maximum amount is stored in prev2
       return prev2



