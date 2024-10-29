"""

Key Insights  
- Understanding Rotation:  
  Rotating the array to the right by k steps means that each element is shifted to the right by 
  k positions. Elements that overflow the array's end are wrapped around to the beginning.  
- Handling Large k:  
  When k is larger than the array's length, compute `k % n` (where `n` is the array's length) 
  to avoid redundant rotations.  
- In-Place Rotation:  
  To achieve O(1) space complexity, the rotation must be done without creating an extra array. 
  The Reversal Algorithm is an efficient method that reverses parts of the array to achieve 
  the desired rotation.  

### Reversal Algorithm Steps  
1. Reverse the Entire Array.  
2. Reverse the First k Elements.  
3. Reverse the Remaining n - k Elements.  
  This sequence effectively rotates the array to the right by k steps.  

### Time and Space Complexity  
- Time Complexity: O(n) since each reversal operation traverses the array.  
- Space Complexity: O(1) as the rotation is done in-place without using additional data structures.  

### Detailed Plan  
1. Compute Effective Rotations:  
   - Calculate `k = k % n` to handle cases where k exceeds the array's length.  

2. Define a Reversal Helper Function:  
   - Implement a helper function `reverse(nums, start, end)` that reverses elements in `nums` 
   from index `start` to `end` (inclusive).  

3. Apply the Reversal Algorithm:  
   - Step 1: Reverse the entire array.  
   - Step 2: Reverse the first k elements.  
   - Step 3: Reverse the remaining n - k elements.  

### Edge Case Handling  
- k == 0 or k is a multiple of n:  
  The array remains unchanged.  
- Single Element Array:  
  If the array has only one element, no rotation is needed.  

### Time and Space Complexity  
- Time Complexity: O(n)  
  Each reversal operation traverses a portion of the array, and since there are three reversals, 
  the total time is linear with respect to the array's length.  
- Space Complexity: O(1)  
  The rotation is performed in-place without using extra space proportional to the input size.

"""

from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        n = len(nums)
        if n == 0:
            return  # Empty array, nothing to rotate

        # Compute the effective number of rotations
        k = k % n
        if k == 0:
            return  # No rotation needed

        # Define the reversal helper function
        def reverse(sub_nums: List[int], start: int, end: int) -> None:
            while start < end:
                sub_nums[start], sub_nums[end] = sub_nums[end], sub_nums[start]
                start += 1
                end -= 1

        # Step 1: Reverse the entire array
        reverse(nums, 0, n - 1)

        # Step 2: Reverse the first k elements
        reverse(nums, 0, k - 1)

        # Step 3: Reverse the remaining n - k elements
        reverse(nums, k, n - 1)

