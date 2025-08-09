"""
Approach: Binary Search in Rotated Sorted Array

    - To achieve O(log n) time complexity, we'll use a modified binary search approach
      that accounts for the rotation in the array. The key idea is to identify which 
      part of the array (left or right of `mid`) is properly sorted and decide where
      to continue the search based on the target's value.

Key Steps:
    1. Initialization:
        - Set two pointers, `left` and `right`, to the start and end of the 
            array, respectively.
    2. Iterative Binary Search:
        - While `left` is less than or equal to `right`:
            - Calculate `mid` as the middle index between `left` and `right`.
            - If `nums[mid]` is the target, return `mid`.
            - Determine which side (left or right of `mid`) is properly sorted:
            - Left Side Sorted: If `nums[left] <= nums[mid]`
                - Check if the target lies within this sorted left side:
                - If `nums[left] <= target < nums[mid]`, adjust `right` to `mid - 1`.
                - Else, adjust `left` to `mid + 1`.
            - Right Side Sorted: Else, the right side must be sorted.
                - Check if the target lies within this sorted right side:
                - If `nums[mid] < target <= nums[right]`, adjust `left` to `mid + 1`.
                - Else, adjust `right` to `mid - 1`.
    3. Target Not Found:
        - If the loop ends without finding the target, return `-1`.

Time and Space Complexity:

- Time Complexity: O(log n)
  - Binary search divides the search space in half each time, leading to
    logarithmic time complexity.
  
- Space Complexity: O(1)
  - The algorithm uses a constant amount of extra space.

Edge Cases:

1. Single Element Array:
   - If `nums` has only one element, check if it's the target.
   
2. No Rotation (Properly Sorted Array):
   - The algorithm works seamlessly even if the array is not rotated.
   
3. Target Not Present:
   - If the target is not in the array, the function correctly returns `-1`.
   
4. All Elements Same Except One:
   - Although the problem guarantees all elements are unique, it's worth noting
    that similar logic can be adapted for arrays with duplicates with 
    slight modifications.

Example Walkthrough:

- Example 1:
  - `nums = [4,5,6,7,0,1,2]`, `target = 0`
  - Step 1: `left = 0`, `right = 6`, `mid = 3`, `nums[mid] = 7`
    - Left side `[4,5,6,7]` is sorted.
    - Target `0` is not in `[4,7]`, so adjust `left` to `4`.
  - Step 2: `left = 4`, `right = 6`, `mid = 5`, `nums[mid] = 1`
    - Left side `[0,1]` is sorted.
    - Target `0` is in `[0,1]`, so adjust `right` to `4`.
  - Step 3: `left = 4`, `right = 4`, `mid = 4`, `nums[mid] = 0`
    - Target found at index `4`.
  - Result: `4`

- Example 2:
  - `nums = [4,5,6,7,0,1,2]`, `target = 3`
  - Steps: Similar to Example 1, but target `3` is not found.
  - Result: `-1`
"""

from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left, right = 0, n - 1

        while left <= right:
            mid = (left + right) // 2

            # Check if the mid element is the target
            if nums[mid] == target:
                return mid

            # Determine which side is properly sorted
            if nums[left] <= nums[mid]:
                # Left side is sorted
                if nums[left] <= target < nums[mid]:
                    # Target is in the left sorted side
                    right = mid - 1
                else:
                    # Target is in the right unsorted side
                    left = mid + 1
            else:
                # Right side is sorted
                if nums[mid] < target <= nums[right]:
                    # Target is in the right sorted side
                    left = mid + 1
                else:
                    # Target is in the left unsorted side
                    right = mid - 1

        # Target not found
        return -1

