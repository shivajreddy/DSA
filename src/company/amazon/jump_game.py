"""
1  1  1  1  0
2  3  1  1  _
Y  Y  Y  Y  Y

4  3  2  1  0       <- min. needed at this idx to reach end
3  2  1  0  _       <- input array
N  N  N  N  Y       <- can we reach end from this idx

Time & Space:
    Time: O(N)
    Space: O(1)
"""

from typing import List

class SolutionOld:
    def canJump(self, nums: List[int]) -> bool:
        n = len(nums)
        jumps_required = 0  # Distance needed to reach the last index

        # Traverse the array from the second-to-last index to the first
        for idx in range(n - 2, -1, -1):
            jump_dist = nums[idx]

            if jump_dist >= jumps_required + 1:
                jumps_required = 0  # Reset the distance if you can jump directly
            else:
                jumps_required += 1  # Increase the distance needed to jump

        # If we can jump to the last index from the first one, nxt should be 0
        return jumps_required == 0

"""
Key Insights  
Greedy Approach is Optimal:  
    - Greedy algorithms make the locally optimal choice at each step with the hope of finding a 
      global optimum.  
    - For this problem, at each position, we aim to maximize the range of indices we can reach, ensuring
      that we can eventually reach the end if possible.  
Track the Maximum Reachable Index:  
    - As we iterate through the array, we maintain a variable `max_reachable` that represents the 
      furthest index we can reach so far.  
    - At each index `i`, if `i` is greater than `max_reachable`, it means we cannot reach this position,
    and hence, we cannot reach the end.  
Early Termination:  
    - If at any point `max_reachable` is greater than or equal to the last index, we can immediately 
    return true, as we've confirmed that the end is reachable.  

Time and Space Efficiency:  
    - Time Complexity: O(n), where n is the length of the array. We traverse the array once.  
    - Space Complexity: O(1), as we only use a constant amount of extra space.  


Detailed Plan  
Initialize `max_reachable`:  
- Set `max_reachable` to 0 initially, representing the starting position.  

Iterate Through the Array:  
- For each index `i` in `nums`:  
  - Check Feasibility:  
    - If `i` is greater than `max_reachable`, return false as we cannot reach this index.  
  - Update `max_reachable`:  
    - Update `max_reachable` to be the maximum of its current value and `i + nums[i]`.  
  - Check for Early Termination:  
    - If `max_reachable` is greater than or equal to the last index, return true.  

Final Check:  
- After iterating through the array, check if `max_reachable` is greater than or equal to the last index.  
- Return the result accordingly.  


Time and Space Complexity  
    - Time Complexity: O(n)  
        - We traverse the array once, performing constant-time operations at each step.  
    - Space Complexity: O(1)  
        - Only a few variables are used, regardless of the input size.  
"""

from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reachable = 0  # Initialize the maximum reachable index

        for i, jump in enumerate(nums):
            if i > max_reachable:
                # If current index is beyond the maximum reachable, cannot proceed
                return False
            # Update the maximum reachable index
            max_reachable = max(max_reachable, i + jump)
            # Early termination if the end is reachable
            if max_reachable >= len(nums) - 1:
                return True

        # Final check if the last index is reachable
        return max_reachable >= len(nums) - 1


