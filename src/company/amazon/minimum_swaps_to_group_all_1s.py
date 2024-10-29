"""
Sliding Window Approach:
    - The algorithm uses a sliding window of size `total_ones`, which represents the number of 1s in the array. 
    - The objective is to find the minimum number of 0s in any window of size `total_ones` within the array.
    - Minimizing the number of 0s in the window will minimize the number of swaps required to group all the 
      1s together.

Handling a Circular Array:
    - Since the array is circular, the algorithm effectively simulates this by looping over the
      array twice (using `2 * n` iterations) and accesses elements in a wrap-around manner using 
      the modulo operator (`% n`). This allows the sliding window to "wrap around" the end of the array, 
      ensuring that we consider all circular permutations of the window.

Counting 0s:
    - The algorithm keeps a running count of the number of 0s within the current window. For each window of 
      size `total_ones`, it compares the number of 0s in the window to the current minimum, updating the 
      minimum swaps required if the current window contains fewer 0s.

Sliding the Window:
    - The window starts with the left pointer `l` and expands the right pointer `r` forward.
    - When the window size reaches `total_ones`, the algorithm compares the number of 0s in the current window 
      with the minimum found so far.
    - As the window slides forward by incrementing the right pointer `r`, the leftmost element (`l`) is removed 
      from the window. If this element is 0, the algorithm reduces the zero count.
  
Edge Case:
    - If the array contains no 1s (`total_ones == 0`), no swaps are required, and the function 
      immediately returns 0.

Time Complexity: O(n)
    - O(n): Although the loop iterates `2 * n` times, each element is accessed only once as the window slides 
      over the array. Thus, the overall time complexity remains linear.
Space Complexity: O(1)
    - We only create fixed number of variables

"""

from typing import List

class Solution:
    def minSwaps(self, nums: List[int]) -> int:

        n = len(nums)

        # Edge case: empty list
        if n == 0:
            return 0
        
        total_ones = sum(nums)

        # Edge case: no 1's, (or) all are already 1's
        if total_ones == 0 or total_ones == n:
            return 0

        min_swaps = n  # Initialize the minimum swaps to the array length
        curr_zeroes = 0  # To count zeroes in the current window
        l = 0  # Left pointer for the sliding window

        # Sliding window over the circular array, with 2*n iterations to handle wrap-around
        for r in range(2 * n):
            if nums[r % n] == 0:  # Wrap around using modulo for the circular array
                curr_zeroes += 1

            # Once the window reaches size total_ones, start processing the window
            if r - l + 1 == total_ones:
                min_swaps = min(min_swaps, curr_zeroes)

                # Slide the window by removing the effect of the left-most element
                if nums[l % n] == 0:
                    curr_zeroes -= 1
                l += 1  # Move the left pointer right

        return min_swaps




""" Old approach - unnecessary space and confusing

Approach:
    - The problem requires grouping all 1's together in a circular array with the least number of swaps. To achieve this efficiently,
    - we can utilize the sliding window technique combined with counting the zeros within a fixed-size window (equal to the total number of 1's).
    - The minimum number of zeros in such a window corresponds to the minimum number of swaps needed.

Key Steps:
    1. Count Total Number of 1's:
        - Determine the total number of 1's (`total_ones`) in the array. This defines the size of the window we need to consider since the goal is to group all 1's together.
    2. Handle Edge Cases:
        - If there are no 1's (`total_ones == 0`), no swaps are needed, so return `0`.
        - If the total number of 1's equals the length of the array (`total_ones == n`), the array already satisfies the condition, and no swaps are needed.
    3. Sliding Window to Find Minimum Zeros:
        - Use a sliding window of size `total_ones` to track the number of zeros in the current window.
        - Since the array is circular, we need to wrap the window around the end of the array to the beginning. This can be handled by iterating through the array twice (concatenating the array with itself).
        - For each window, keep track of the number of zeros. The minimum number of zeros encountered is the number of swaps required to group all 1's together.
    4. Determine Minimum Swaps:
    - The minimum number of zeros in any valid window is equal to the minimum number of swaps required to group all 1's together.

Time and Space Complexity:
    Time Complexity: O(n)
        - We iterate through the array twice (once for counting 1's and once for applying the sliding window), resulting in a linear time complexity.
    Space Complexity: O(1)
        - The space complexity is constant since we are not using any additional arrays, just a few variables to track the number of 1's and zeros in the window.

Edge Cases:
    - No 1's: If the array contains no 1's, return `0` as no swaps are needed.
    - All 1's: If the array consists entirely of 1's, return `0` as they are already grouped.
    - Single 1: If there's only one 1, return `0` as it's trivially grouped.


Future Improvements:
    - Further Optimization: The current solution already uses O(1) space and linear time. There is little room for improvement without changing the algorithm fundamentally.
    - Handling Larger Inputs: For extremely large arrays, this approach still works efficiently due to its linear time complexity and minimal space usage.

"""


from typing import List


class SolutionOld:
    def minSwaps(self, nums: List[int]) -> int:
        """ Determines the minimum number of swaps required to group all 1's together in a circular binary array. """
        n = len(nums)
        total_ones = sum(nums)


        # Edge Cases
        if total_ones == 0:
            return 0  # No swaps needed if there are no 1's
        if total_ones == n:
            return 0  # All 1's are already grouped together


        # Calculate prefix sum of zeros
        prefix_zeros = [0] * n
        zero_count = 0
        for i in range(n):
            if nums[i] == 0:
                zero_count += 1
            prefix_zeros[i] = zero_count


        min_swaps = total_ones  # Initialize with the maximum possible zeros in a window


        # Iterate over each possible starting index of the window
        for idx in range(n):
            start = idx
            end = (start + total_ones - 1) % n  # End index of the window


            if end >= start:
                # Window does not wrap around
                zeros_in_window = prefix_zeros[end] - (prefix_zeros[start - 1] if start > 0 else 0)
            else:
                # Window wraps around the end to the beginning
                zeros_in_window = (prefix_zeros[-1] - (prefix_zeros[start - 1] if start > 0 else 0)) + prefix_zeros[end]


            min_swaps = min(min_swaps, zeros_in_window)


        return min_swaps


