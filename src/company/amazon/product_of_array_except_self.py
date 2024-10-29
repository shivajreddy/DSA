"""
The problem **"Product of Array Except Self"** requires us to return an array 
such that each element at index `i` of the new array is the product of all the 
numbers in the original array except the one at index `i`, and it should be 
solved in `O(n)` time without using division.

### To achieve this, we use a two-pass approach:

1. **Left Prefix Product**: We compute the product of all elements to the left 
   of each index `i` and store it in an array called `left`. This means for any 
   index `i`, `left[i]` is the product of all elements from index `0` to `i-1`.

2. **Right Prefix Product**: Similarly, we compute the product of all elements 
   to the right of index `i` and store it in an array called `right`. For any 
   index `i`, `right[i]` is the product of all elements from `i+1` to the last 
   element.

Finally, the result at any index `i` will be the product of `left[i]` and 
`right[i]`.

### Explanation:

#### Left Product:
- We traverse the array from left to right. For each index `i`, we calculate 
  the product of all elements before it using an accumulator (`left_accumulator`).
- This way, by the time we reach index `i`, `result[i]` contains the product of 
  all elements to the left of `i`.

#### Right Product:
- We traverse the array from right to left. For each index `i`, we multiply 
  the current value in `result[i]` (which already holds the left product) by 
  the right product accumulator (`right_accumulator`).
- This gives us the final product of all elements except the one at index `i`.

### Time Complexity:
- `O(n)`: We make two passes through the array (one for the left product and 
  one for the right product), so the time complexity is linear.

### Space Complexity:
- `O(1)`: We do not use any extra arrays for left or right products. Instead, 
  we directly modify the result array, so the space complexity is constant (not 
  counting the output array).

"""


from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """
        Returns an array where each element is the product of all elements of the original array
        except the one at the corresponding index, without using division.

        Time Complexity: O(n), Space Complexity: O(1) (output array does not count as extra space).

        Args:
        nums (List[int]): The input list of integers.

        Returns:
        List[int]: The resulting list of products for each element.
        """
        n = len(nums)

        # Initialize the result array with 1's (this will be used as the 'left' product accumulator).
        result = [1] * n

        # Left pass to fill result with left products
        left_accumulator = 1
        for i in range(n):
            result[i] = left_accumulator
            left_accumulator *= nums[i]

        # Right pass to adjust result by multiplying with right products
        right_accumulator = 1
        for i in range(n - 1, -1, -1):
            result[i] *= right_accumulator
            right_accumulator *= nums[i]

        return result

