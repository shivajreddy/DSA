from typing import DefaultDict, List

class Solution:
    """
    Time : O(n)
    Space: O(n)
    """
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum_count = DefaultDict(int)

        # Most important: there are a total of 1 subarray whose sum is 0, 
        # which is an empty subarray
        prefix_sum_count[0] = 1

        current_sum = 0
        valid_subarray_count = 0

        for num in nums:
            current_sum += num  # Update the running sum

            # Check if current_sum - k exists in the hashmap
            delta_prefix = current_sum - k
            if delta_prefix in prefix_sum_count:
                valid_subarray_count += prefix_sum_count[current_sum - k]

            # Update the count of current_sum in the hashmap
            prefix_sum_count[current_sum] += 1

        return valid_subarray_count

