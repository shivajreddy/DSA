"""
### Key Insights:
- A brute-force approach would involve checking all possible subarrays, but 
  this would lead to `O(N^2)` time complexity, which is inefficient for large 
  arrays.
- A better approach is to use a prefix sum combined with a hashmap (or 
  dictionary) to track how often a prefix sum has occurred as we traverse the 
  array. This allows us to efficiently calculate the number of subarrays that 
  sum to `k` in `O(N)` time.

### Detailed Plan:
- **Prefix Sum**: The sum of elements from the start of the array to a given 
  index. For example, the prefix sum at index `i` is the sum of `nums[0]` to 
  `nums[i]`.
- **Subarray Sum using Prefix Sums**: For a subarray that ends at index `i` and 
  has a sum equal to `k`, the prefix sum at index `i` minus the prefix sum at 
  the start of this subarray must be equal to `k`. Mathematically, this means:

  `current_sum - previous_prefix_sum = k`
  
  Rearranging this:

  `previous_prefix_sum = current_sum - k`
  
- **Hashmap**: To efficiently find how many times the `previous_prefix_sum` has 
  occurred, we can use a hashmap where the key is the prefix sum and the value 
  is the count of how often that sum has occurred.
  
- **Greedy Traversal**: As we traverse the array, we calculate the running 
  prefix sum and check how many times `current_sum - k` has appeared before 
  (using the hashmap). If it has appeared, it means there's a subarray that 
  sums to `k` ending at the current index.

### Time Complexity:
- **Time**: `O(N)` where `N` is the number of elements in the array. Each 
  element is processed once.
- **Space**: `O(N)` due to the hashmap storing the prefix sums.

### Explanation:
1. **Initialize the Hashmap**: We start with `{0: 1}` in the hashmap to account 
   for subarrays that begin at the start of the array and sum to `k`. This is 
   crucial because if the prefix sum at index `i` equals `k`, we should count 
   this as a valid subarray.
   
2. **Iterate through the Array**: As we traverse each element, we:
   - Update the `current_sum` by adding the current element.
   - Check if `current_sum - k` exists in the hashmap. If it does, this means 
     there is a subarray ending at the current index that sums to `k`.
   - Update the hashmap to track how many times the `current_sum` has occurred 
     so far.
   
3. **Return the Result**: After traversing the array, `subarray_count` holds 
   the total number of subarrays that sum to `k`.

### Step-by-Step:

- **At index 0**:
  - `current_sum = 1`
  - `current_sum - k = 1 - 2 = -1`
  - `-1` is not in `prefix_sum_count`, so no subarray found yet.
  - Update `prefix_sum_count` to `{0: 1, 1: 1}`.

- **At index 1**:
  - `current_sum = 2`
  - `current_sum - k = 2 - 2 = 0`
  - `0` is in `prefix_sum_count` (it occurred once), so we found 1 subarray.
  - Update `prefix_sum_count` to `{0: 1, 1: 1, 2: 1}`.
  - `subarray_count = 1`.
"""

from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_sum_count = {0: 1}  # To account for subarrays that start from index 0
        current_sum = 0
        subarray_count = 0

        for num in nums:
            current_sum += num  # Update the running sum

            # Check if current_sum - k exists in the hashmap
            if (current_sum - k) in prefix_sum_count:
                subarray_count += prefix_sum_count[current_sum - k]

            # Update the count of current_sum in the hashmap
            if current_sum in prefix_sum_count:
                prefix_sum_count[current_sum] += 1
            else:
                prefix_sum_count[current_sum] = 1

        return subarray_count

