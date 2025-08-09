"""

all negative numbers
    k = even
    nums = [ -9  -8  -7  -5  -3 ], k = 4
    chosen: -9, -8, -7, -5  (all from left)
    nums=all-negative k=even  => pick k nums from left

    k = odd
    nums = [ -9  -8  -7  -5  -3 ], k = 3
    Result will always be -ve, so pick the lowest magnitude
    -3 -5 -7
    nums=all-negative k=odd   => pick k nums from right

mixed or +ve numbers
    k = even
    nums = [ -3  -2  0  1  2  5 ], k = 4
    chosen: 5,2,-3,-2 (pick 2 nums every turn, by comparing left & right)
    nums=mixed or all-positive k=even  => compare product 2 left, 2 right

    k = odd
    nums = [ -3  -2  0  1  2  5 ], k = 3
    chosen: 5,-3,-2 (1 from right, pick 2 nums every turn, by comparing left & right)
    nums=mixed or all-positive k=odd   => pick 1 num from right, compare product 2 left, 2 right

    nums = [ -3  -2  0  1  88  89 ], k = 3
    chosen: 89, 88, 1



all negative numbers
    k = even
    nums = [ -9  -8  -7  -5  -3 ], k = 4
    chosen: -9, -8, -7, -5

    k = odd
    nums = [ -9  -8  -7  -5  -3 ], k = 3
    Result will always be -ve, so pick the lowest magnitude
    -3 -5 -7

mixed or +ve numbers
    k = even
    nums = [ -3  -2  0  1  2  5 ], k = 4
    chosen: 5,2,-3,-2

    k = odd
    nums = [ -3  -2  0  1  2  5 ], k = 3
    chosen: 5,-3,-2

    nums = [ -3  -2  0  1  88  89 ], k = 3
    chosen: 89, 88, 1

"""

from typing import List


class Solution:
    def maximum_product(self, nums: List[int], k: int) -> int:
        nums.sort()

        n = len(nums)

        left, right = 0, n - 1
        product = 1

        # 'k' is odd
        if k % 2 == 1:
            product *= nums[right]
            right -= 1
            k -= 1  # k is now even

        # 'k' is even
        while k > 0:
            left_product = nums[left] * nums[left + 1]
            right_product = nums[right] * nums[right - 1]

            # Choose the highest product
            if left_product > right_product:
                product *= left_product
                left += 2
            else:
                product *= right_product
                right -= 2
            k -= 2

        return product


sol = Solution()
sol.maximum_product([-9, -8, -7, -5, -3], 3)
