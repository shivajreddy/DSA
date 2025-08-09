"""
Key Insights  
    - Sorted Array with Pairs:  
      In a sorted array where every element appears exactly twice except one, the pairs of 
      identical elements are adjacent.  
    - Binary Search Application:  
      The requirement for an O(log n) solution indicates that a binary search approach is 
      well-suited to the problem.  
    - Index Parity Observation:  
    - Before the single element, the first occurrence of each pair is at an even index (0-based).  
    - After the single element, the first occurrence of each pair shifts to an odd index.  

Determining the Side of the Single Element  
    - By comparing the middle element with its neighbor, and depending on the parity of the 
      middle index, we can determine which side contains the single element.  

Step-by-Step Solution  
    1. Initialize Binary Search Pointers  
    - Left Pointer (left): Start at index 0.  
    - Right Pointer (right): Start at index n - 1, where n is the length of the array.  

    2. Binary Search Loop  
    - While `left < right`:
        - Calculate Midpoint:  
        `mid = left + (right - left) // 2`  
        - Ensure Mid is Even:  
        If `mid` is odd, decrement it by 1 to make it even. This ensures alignment with 
        the observation that the first occurrence of pairs before the single element is at 
        even indices.  
        - Compare `nums[mid]` with `nums[mid + 1]`:  
        - If `nums[mid] == nums[mid + 1]`:  
            The single element is after `mid + 1`. Update `left = mid + 2`.  
        - Else:  
            The single element is at or before `mid`. Update `right = mid`.  
    - Loop Continuation:  
        The loop continues until `left` meets `right`.

    3. Conclusion  
    - After the loop terminates, `left` will point to the single element.  

    4. Edge Case Handling  
    - Single Element Array: If the array contains only one element, return it directly.  
    - Single Element at the Beginning or End: The algorithm naturally handles these cases 
      through the binary search logic.  

Time and Space Complexity  
    - Time Complexity: O(log n)  
      Binary search reduces the search space by half in each iteration, resulting in 
      logarithmic time complexity.  
    - Space Complexity: O(1)  
      The solution uses constant extra space.

"""


from typing import List

class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        """ Finds the single element in a sorted array where every other element appears exactly twice. """
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            # Compare mid with the next element
            if nums[mid] == nums[mid + 1]:
                # The single element is after mid + 1
                left = mid + 2
            else:
                # The single element is at or before mid
                right = mid

        # left == right pointing to the single element
        return nums[left]

