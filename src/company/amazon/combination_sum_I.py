"""
Key Insights:

- Backtracking:
	- The problem requires exploring all possible combinations that sum up to the
	  target.
	- Backtracking allows us to build combinations incrementally and abandon a
	  path as soon as we realize it won't lead to a valid solution.

- Handling Duplicates:
	- Since candidates can be used multiple times, we need to ensure that we
	  consider all possible counts of each candidate.
	- We avoid duplicates by always considering candidates from the current index
	  onwards, preventing permutations of the same combination.

- Efficiency Without Sorting:
	- Even without sorting, we can effectively prune paths where the sum exceeds
	  the target.
	- By not imposing an order on the candidates, we might explore some
	  unnecessary paths, but we still systematically cover all valid combinations.

Plan:
    - Backtracking Function:
        - Define a recursive function that takes the remaining target sum, the current
        combination, and the starting index.
        - At each recursive call, iterate over the candidates starting from the
        `start_index` to include each candidate multiple times if needed.
    - Decision Making:
        - Include the Candidate:
            - Add the current candidate to the combination.
            - Recursively call the function with the updated remaining sum and the same
            index (since we can reuse the same candidate).
        - Exclude the Candidate:
            - After returning from the recursive call (backtracking), remove the
            candidate from the combination.
            - Proceed to the next candidate by incrementing the index.
    - Base Cases:
        - Valid Combination Found:
            - If the remaining sum is exactly zero, add a copy of the current
            combination to the result list.
        - Invalid Path:
            - If the remaining sum becomes negative, the current path cannot lead to a
            valid combination; backtrack immediately.
    - Result Collection:
        - Collect all valid combinations in a result list that is returned after all
        recursive calls are completed.

Time and Space Complexity:
    - Time Complexity: O(N^(T/M + 1))
        - N: Number of candidates.
        - T: Target sum.
        - M: Minimum value among the candidates.
        - Explanation:
            - The maximum depth of the recursion tree is T/M, as we can include the
            smallest candidate up to T/M times.
            - At each level, we have up to N choices (since we can choose any
            candidate).
            - Without sorting, we cannot perform early termination based on candidate
            values, which may lead to exploring more paths compared to the sorted
            approach.
    - Space Complexity: O(T/M)
        - Explanation:
            - The maximum depth of the recursion tree (and thus the maximum size of the
            combination list) is proportional to T/M.
            - Additional space is used for the recursion stack and to store the current
            combination.

"""
from typing import List

class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        """
        Finds all unique combinations in candidates where the numbers sum to the target.
        Each number may be used an unlimited number of times.

        Args:
            candidates (List[int]): A list of distinct integers.
            target (int): The target sum to achieve.

        Returns:
            List[List[int]]: A list of lists, where each list is a unique combination summing up to the target.
        """
        result = []

        def backtrack(remaining: int, combination: List[int], start_index: int):
            if remaining == 0:
                # Found a valid combination
                result.append(list(combination))
                return
            elif remaining < 0:
                # Exceeded the sum, stop exploring this path
                return

            for i in range(start_index, len(candidates)):
                current_candidate = candidates[i]
                # Include the current candidate
                combination.append(current_candidate)
                # Since we can use the same candidate multiple times, we do not increment i
                backtrack(remaining - current_candidate, combination, i)
                # Backtrack: Remove the last added candidate
                combination.pop()

        # Start the backtracking with an empty combination
        backtrack(target, [], 0)
        return result



"""
Time and Space Complexity Analysis:
Let's compare the time and space complexity for both approaches: with and without sorting.

Without Sorting::
    Time Complexity:
    Worst-Case Complexity: The time complexity is O(N^(T/M)), where:
        - N is the number of candidates.
        - T is the target sum.
        - M is the minimal value among the candidates.

    Explanation:
        - The depth of the recursion tree can be up to T/M, as the smallest candidate  
	      can be used up to T/M times.
        - At each level of recursion, we have up to N choices (candidates).
        - Without sorting, we cannot perform early stopping when a candidate exceeds
        the remaining sum, so we explore more paths, including those where
        candidates are larger than the remaining sum.

    Space Complexity:
        - O(T/M) due to the maximum depth of the recursion stack.
        - The combination list can grow up to length T/M in the worst case.

With Sorting::
    Time Complexity:
        - Sorting Time: First, sorting the candidates takes O(N log N) time.
        - Recursive Calls: Similar to the unsorted case, but with optimization.
        - Optimized Complexity: Still O(N^(T/M)), but with a reduced constant factor
        due to pruning.

    Explanation:
        - By sorting the candidates, we can perform an early break when the current
        candidate exceeds the remaining sum.
        - This pruning reduces the number of unnecessary recursive calls.
        - The recursion tree is narrower because we avoid exploring paths that cannot
        possibly lead to a valid combination.

    Space Complexity:
        - O(T/M), same as the unsorted approach.

Conclusion::
    Without Sorting:
        Pros:  
            - Simpler implementation.
            - no overhead of sorting.  
        Cons:
            - Explores more unnecessary paths
            - may be less efficient for larger inputs.  
    With Sorting::
        Pros:  
            - Prunes unnecessary paths early
            - can be more efficient in practice.  
        Cons:
            - Additional time spent on sorting
            - might lead to complex code.

    When to Use Each Approach::
        Without Sorting:
            - Suitable when the input size is small, or when candidates are already
            sorted.
            - Useful if sorting is not feasible due to constraints.
        With Sorting:
            - Recommended for larger inputs to improve efficiency.
            - Beneficial when early stopping can significantly reduce the number of
            recursive calls.
"""

class SolutionWithSorting:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        # Sort the candidates to help with optimizations
        candidates.sort()
        result = []


        def backtrack(remaining, combination, start_index):
            if remaining == 0:
                # Found a valid combination
                result.append(list(combination))
                return
            elif remaining < 0:
                # Exceeded the sum, stop exploring this path
                return


            for i in range(start_index, len(candidates)):
                current_candidate = candidates[i]


                # Optimization: Early stopping if the current candidate exceeds the remaining sum
                if current_candidate > remaining:
                    break  # Since the candidates are sorted, no need to consider further
                # Include the current candidate
                combination.append(current_candidate)
                # Since we can use the same candidate multiple times, we do not increment i
                backtrack(remaining - current_candidate, combination, i)
                # Backtrack: Remove the last added candidate
                combination.pop()


        # Start the backtracking with an empty combination
        backtrack(target, [], 0)
        return result
