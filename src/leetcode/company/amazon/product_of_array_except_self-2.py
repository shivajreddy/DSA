from typing import List

class Solution:
    """
    - Create two arrays, left_products and right_products.
    - Populate left_products with the cumulative product of elements to the left of the current index.
    - Populate right_products with the cumulative product of elements to the right of the current index.
    - Multiply the corresponding values from left_products and right_products to get the final result for each index.

    Time : O(n) 
    Space: O(n)
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)

        left_products = [1] * n  # Tracks product of all elements to the left
        for i in range(1, n):
            left_products[i] = left_products[i - 1] * nums[i - 1]
        
        right_products = [1] * n  # Tracks product of all elements to the right
        for i in range(n - 2, -1, -1):
            right_products[i] = right_products[i + 1] * nums[i + 1]
        
        result = [1] * n
        for i in range(n):
            result[i] = left_products[i] * right_products[i]  # Multiply left and right products
        
        return result


class Solution2:
    """
    - Use a single array result to store the final result, avoiding extra space.
    - Calculate cumulative products from the left and update result with the left product values.
    - Calculate cumulative products from the right and multiply them directly into the result array.
    - This method avoids the use of extra arrays, making it more space-efficient with a space complexity of O(1) (ignoring output array).

    Time : O(1)
    Space: O(1) if we ignore the output array
    """
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        result = [1] * n

        left_product = 1  # Tracks the cumulative product from the left
        for i in range(n):
            result[i] = left_product
            left_product *= nums[i]
        
        right_product = 1  # Tracks the cumulative product from the right
        for i in range(n - 1, -1, -1):
            result[i] *= right_product
            right_product *= nums[i]
        
        return result

