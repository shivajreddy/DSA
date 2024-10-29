"""
Key Insights


Sliding Window Technique:
    - This problem is a classic application of the sliding window technique,
      which allows us to find the longest subarray satisfying certain conditions efficiently.
    - We maintain a window that can contain at most `k` zeros by keeping track of their positions.


Two Pointers Approach:
    - Utilize two pointers (`left` and `right`) to define the current window.
    - As we expand the window to the right, we count the number of zeros. If the count exceeds `k`,
      we shrink the window from the left until the zero count is within the allowed limit.


Optimizing for Large Inputs:
    - Given the constraints (`nums.length` up to 10^5), it's crucial to ensure the algorithm runs in
      linear time (`O(n)`) with constant space (`O(1)`), excluding the input storage.


Plan


1. Initialize Pointers and Variables:
   - `left`: Start of the window.
   - `max_len`: Maximum length of valid window found.
   - `zero_count`: Number of zeros in the current window.


2. Expand the Window:
   - Iterate through the array with the `right` pointer.
   - If `nums[right]` is `0`, increment `zero_count`.


3. Shrink the Window if Necessary:
   - If `zero_count` exceeds `k`, move the `left` pointer to the right.
   - If `nums[left]` is `0`, decrement `zero_count`.
   - Continue shrinking until `zero_count` is within `k`.


4. Update Maximum Length:
   - After each iteration, calculate the current window size (`right - left + 1`) and update `max_len` if
     it's larger than the previous maximum.


5. Return the Result:
   - After processing the entire array, `max_len` will hold the length of the longest subarray with at most `k` zeros.


Time and Space Complexity
    Time Complexity: O(n)
    - We traverse the array once with the `right` pointer and potentially once with the `left` pointer,
      resulting in linear time complexity.


    Space Complexity: O(1)
    - Only a few variables are used, regardless of the input size.


"""




from typing import List


class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Returns the maximum number of consecutive 1s in the array if you can flip at most k 0s.

        Args:
        nums (List[int]): The binary array.
        k (int): The maximum number of 0s that can be flipped.

        Returns:
        int: The length of the longest subarray with at most k 0s.
        """
        left = 0
        max_len = 0
        zero_count = 0

        for right in range(len(nums)):
            # If the current element is 0, increment the zero count
            if nums[right] == 0:
                zero_count += 1

            # If zero_count exceeds k, shrink the window from the left
            while zero_count > k:
                if nums[left] == 0:
                    zero_count -= 1
                left += 1  # Move the left pointer to the right

            # Update the maximum length if the current window is larger
            max_len = max(max_len, right - left + 1)

        return max_len




from collections import deque
from typing import List


class SolutioWithDequen:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """
        Returns the maximum number of consecutive 1s in the array if you can flip at most k 0s.
        This implementation uses a deque to keep track of the indices of 0s within the current window.


        Args:
            nums (List[int]): The binary array.
            k (int): The maximum number of 0s that can be flipped.


        Returns:
            int: The length of the longest subarray with at most k 0s.
        """
        # Initialize a deque to store the indices of 0s in the current window
        zero_indices = deque()

        # Initialize pointers for the sliding window
        left = 0  # Left boundary of the window
        max_length = 0  # Result to store the maximum length found
        # Iterate over the array using the right pointer

        for right, num in enumerate(nums):
            # If the current number is 0, add its index to the deque
            if num == 0:
                zero_indices.append(right)

            # If the number of 0s in the deque exceeds k, adjust the window
            if len(zero_indices) > k:
                # Remove the oldest 0's index from the deque
                oldest_zero_index = zero_indices.popleft()
                # Move the left boundary of the window to the right of the removed 0
                left = oldest_zero_index + 1

            # Calculate the current window size and update max_length if necessary
            current_window_length = right - left + 1
            max_length = max(max_length, current_window_length)

        return max_length

