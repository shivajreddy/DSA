"""
Key Insights
    Binary Search Application:
        - Since the array is sorted, we can use binary search to 
          achieve O(log n) runtime.
        - We need to find the first and last positions of the target.
          This can be done by modifying the standard binary search algorithm.

Finding Leftmost and Rightmost Indices:
    - Leftmost (First) Position:
        - Use binary search to find the smallest index `i` such that 
          `nums[i] == target`.
    - Rightmost (Last) Position:
        - Use binary search to find the largest index `i` such that 
          `nums[i] == target`.

---

Algorithm Outline:
    - Implement two separate binary search functions:
        - One to find the leftmost index.
        - One to find the rightmost index.
    - Both functions will have O(log n) time complexity.

---

Algorithm Design

Function to Find Leftmost Index (`findLeft`)
    1. Initialize:
        - `left = 0`
        - `right = len(nums) - 1`
    2. While left <= right:
    - Calculate `mid = left + (right - left) // 2`.
    - If `nums[mid] < target`:  
        - Move `left = mid + 1` (Search in the right half).
    - Else:  
        - Move `right = mid - 1` (Search in the left half).
    3. After Loop:
        - Check if `left` is within bounds and `nums[left] == target`.
        - If true, return `left`.
        - Else, return `-1`.

---

Function to Find Rightmost Index (`findRight`)
    1. Initialize:
        - `left = 0`
        - `right = len(nums) - 1`
    2. While left <= right:
        - Calculate `mid = left + (right - left) // 2`.
        - If `nums[mid] <= target`:  
            - Move `left = mid + 1` (Search in the right half).
        - Else:  
            - Move `right = mid - 1` (Search in the left half).
    3. After Loop:
        - Check if `right` is within bounds and `nums[right] == target`.
        - If true, return `right`.
        - Else, return `-1`.

Combine Results
    - Return `[left_index, right_index]` from the two functions.

---

Time and Space Complexity
    - Time Complexity: O(log n) for each binary search function.
        - Total time complexity: O(log n) + O(log n) = O(log n)
    - Space Complexity: O(1)
        - Only constant extra space is used.

"""

from typing import List

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findLeft(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            leftmost = -1  # Default value if target is not found
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left = mid + 1
                else:
                    if nums[mid] == target:
                        leftmost = mid
                    right = mid - 1
            return leftmost

        def findRight(nums: List[int], target: int) -> int:
            left, right = 0, len(nums) - 1
            rightmost = -1  # Default value if target is not found
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] <= target:
                    if nums[mid] == target:
                        rightmost = mid
                    left = mid + 1
                else:
                    right = mid - 1
            return rightmost

        left_index = findLeft(nums, target)
        right_index = findRight(nums, target)
        return [left_index, right_index]


