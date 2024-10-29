"""

Approach: Backtracking with Duplicate Handling
    - To generate all unique subsets from an array that may contain duplicates, we employ a backtracking
      approach combined with sorting to efficiently handle and skip over duplicate elements.

1. Sort the Input Array:
   - Sorting `nums` ensures that duplicate elements are adjacent. This property is crucial for 
     identifying and skipping duplicates during the backtracking process.
   - Example:
     - Original `nums = [1, 2, 2]`
     - Sorted `nums = [1, 2, 2]`
2. Backtracking Function:
   - We define a recursive helper function `backtrack(start, combo)` where:
     - `start` is the current index in `nums` from which we consider elements to include in the 
       current subset.
     - `combo` is the current subset being constructed.
   - At each recursive call:
     - Add the Current Combination:
       - We add a copy of `combo` to the result list `res` to include the current subset.
     - Iterate Through Candidates:
       - We iterate over `nums` starting from the `start` index to explore all possible elements that 
         can be included in the subset.
     - Skip Duplicates:
       - If the current element is the same as the previous one (`nums[i] == nums[i - 1]`) and `i` is
         greater than `start`, we skip this element to avoid generating duplicate subsets.
     - Include the Current Element:
       - We include `nums[i]` in `combo` and make a recursive call to `backtrack(i + 1, combo)` to
         continue building the subset.
     - Backtrack:
       - After exploring subsets that include `nums[i]`, we remove it from `combo` to backtrack and
         explore subsets that exclude `nums[i]`.
3. Collecting Results:
   - We initialize an empty list `res` to store all unique subsets.
   - We start the backtracking process with `backtrack(0, [])`, indicating that we begin from index `0`
     with an empty subset.
   - After the backtracking completes, `res` contains all unique subsets of `nums`.
4. Time and Space Complexity:
   - Time Complexity: O(2^n), where `n` is the number of elements in `nums`. Each element can either 
     be included or excluded from a subset.
   - Space Complexity: O(n), due to the recursion stack and the space required to store the current 
     subset `combo`.
5. Edge Cases:
   - All Elements Identical: The algorithm correctly handles cases where all elements are duplicates 
     by ensuring only one subset is generated for each unique element count.
   - Single Element: The algorithm generates both the empty subset and the subset containing the 
     single element.
   - Empty Array: Although the constraints specify `1 <= nums.length`, handling an empty array 
     gracefully ensures robustness.

"""

from typing import List

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """ Generates all possible unique subsets from a list of integers that may contain duplicates. """
        # Sort the array to ensure that duplicates are adjacent
        nums.sort()
        res = []
        n = len(nums)

        def backtrack(start: int, combo: List[int]):
            """ Recursively builds subsets by including or excluding each element. """
            # Append a copy of the current subset to the result
            res.append(combo.copy())

            # Iterate through the array starting from the 'start' index
            for i in range(start, n):
                # If the current element is the same as the previous one and not at the start index,
                # skip it to avoid duplicate subsets
                if i > start and nums[i] == nums[i - 1]:
                    continue

                # Include nums[i] in the current subset
                combo.append(nums[i])

                # Move to the next element
                backtrack(i + 1, combo)

                # Backtrack: remove the last element before the next iteration
                combo.pop()

        # Start backtracking with an empty subset and starting index 0
        backtrack(0, [])
        return res

