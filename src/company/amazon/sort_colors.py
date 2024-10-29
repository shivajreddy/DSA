"""
   - Dutch National Flag algorithm, by Dijkstra
   - three pointers: low, mid, high
   - Four regions:
       [0, low-1]   : all elements are 0 (red)
       [low, mid]   : all elements are 1 (white)
       [mid, high]  : unsorted elements
       [high+1, n-1]: all elements are 2 (blue)


   1. Initialize:
        - low = 0
        - mid = 0
        - high = len(nums) - 1

       |-------------------------------------------------------------|
       |                                                             |
     low,mid                                                        high


   2. Traverse the Array:
   - While mid <= high:
        - If nums[mid] == 0:
            - Swap nums[low] and nums[mid].
            - Increment low and mid.
        - Else if nums[mid] == 1:
            - Increment mid.
        - Else if nums[mid] == 2:
            - Swap nums[mid] and nums[high]
            - Decrement high


       0 0 0 0 0 0 0 1 1 1 1 1 1 1 1 x x x x x x x x 2 2 2 2 2 2 2 2 2
       |-------------|---------------|---------------|---------------|
       |            low             mid             high             |


"""

from typing import List

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the input list nums in-place such that all 0s come first,
        followed by all 1s and then all 2s.
        """
        # Initialize pointers
        low = 0                   # Next position for 0
        mid = 0                   # Current element under consideration
        high = len(nums) - 1      # Next position for 2

        # Traverse the array
        while mid <= high:
            if nums[mid] == 0:
                # Swap nums[mid] and nums[low], increment low and mid
                nums[low], nums[mid] = nums[mid], nums[low]
                low += 1
                mid += 1
            elif nums[mid] == 1:
                # Move to the next element
                mid += 1
            else:  # nums[mid] == 2
                # Swap nums[mid] and nums[high], decrement high
                nums[mid], nums[high] = nums[high], nums[mid]
                high -= 1
                # Do not increment mid here

"""
Explanation:
    1. Initialization:
        - low and mid start at index 0.
        - high starts at the last index of the array.
        - The array is divided into four sections based on the pointers.
    2. Algorithm Steps:
        While mid <= high:
            If nums[mid] == 0:
                Swap nums[mid] with nums[low].
                Increment both low and mid.
                This moves 0s to the beginning.
            Elif nums[mid] == 1:
                Increment mid.
                1s are in the middle; no swapping needed.
            Else (nums[mid] == 2):
                Swap nums[mid] with nums[high].
                Decrement high.
                Do not increment mid because the new nums[mid] needs to be evaluated.
    3. Termination:
        The loop ends when mid > high, indicating all elements are in their correct positions.
"""

