"""
### Explanation

The problem asks for finding all unique triplets in an array that sum to 
zero. This can be solved efficiently by using the two-pointer technique 
after sorting the array.

1. Sorting: The array is first sorted to enable the use of the 
   two-pointer technique and to easily handle duplicate numbers. Sorting 
   is done in O(n log n) time.
   
2. Iterating through the array: 
   - For each number `nums[i]`, we try to find two numbers, `nums[j]` and 
     `nums[k]`, such that their sum equals `-nums[i]`. This would satisfy 
     the condition `nums[i] + nums[j] + nums[k] = 0`.
   - To avoid duplicates, we skip any repeated values for the `i`th element.
   - Since the array is sorted, once `nums[i] > 0`, no valid triplet can be 
     found because all numbers from that point on are positive.

3. Two-pointer technique:
   - After fixing `nums[i]`, we use two pointers, `j` and `k`, where `j` 
     starts from `i + 1` and `k` starts from the end of the array (`n - 1`).
   - We calculate the sum of the triplet `nums[i] + nums[j] + nums[k]`. If 
     the sum equals zero, we have found a valid triplet and adjust both 
     pointers (`j` and `k`).
   - If the sum is less than zero, we increase `j` to try larger numbers. 
     If the sum is greater than zero, we decrease `k` to try smaller numbers.

4. Handling duplicates: 
   - To ensure uniqueness, we skip over duplicate values for both the `j` 
     and `k` pointers after a valid triplet is found.

---

### Time Complexity

- Sorting the array takes O(n log n).
- For each element in the array, we use the two-pointer approach, which 
  takes O(n) time in the worst case. 
- Hence, the overall time complexity is O(n^2), where `n` is the number 
  of elements in the input array.

---

### Space Complexity

- The space complexity is O(1), not counting the space used by the 
  result array. We only use a few integer variables and the input array is 
  sorted in place, so no additional space is used.

"""


from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
        such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
        """
        # Sort the input array for two-pointer technique
        nums.sort()
        n = len(nums)
        result = []

        # Iterate through the array, fixing one element at a time
        for i in range(n):
            # Skip duplicates for the current fixed element
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            # If i points to a number > 0, three sum is not possible, since nums are sorted
            if nums[i] > 0:
                continue

            # Two-pointer technique
            j, k = i + 1, n - 1
            while j < k:
                three_sum = nums[i] + nums[j] + nums[k]

                if three_sum == 0:
                    # Found a valid triplet
                    result.append([nums[i], nums[j], nums[k]])
                    j += 1
                    k -= 1

                    # Skip duplicates for nums[j] and nums[k]
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
                    while j < k and nums[k] == nums[k + 1]:
                        k -= 1

                elif three_sum < 0:
                    # If the sum is less than zero, move the left pointer to the right
                    j += 1
                else:
                    # If the sum is greater than zero, move the right pointer to the left
                    k -= 1

        return result


