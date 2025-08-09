from typing import List

class Solution:
    """
    - Backtracking approach to find all unique combinations of candidates that sum up to the target.
    - Sort the candidates first to facilitate skipping duplicates and enable early termination.
    - Backtrack function recursively builds combinations, adding candidates and subtracting from the remaining target.
    - Use a 'previous' variable to skip duplicate candidates at the same recursive depth, ensuring unique combinations.
    - Prune the search space by breaking the loop when a candidate exceeds the remaining target.

    Time Complexity: O(2^n), where n is the number of candidates.
    Space Complexity: O(n)
    """
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:

        def backtrack(start_index, remaining, combination):
            # Base Case: Found a valid combination
            if remaining == 0:
                result.append(combination.copy())
                return
            # Base Case: Invalid state - exceeded the sum
            if remaining < 0:
                return

            previous = None  # Initialize previous number to an invalid number
            for i in range(start_index, len(candidates)):
                current_candidate = candidates[i]

                # Skip duplicates at the same recursive depth
                if previous and current_candidate == previous:
                    continue

                # Pruning: Further candidates will be larger (since array is sorted)
                if current_candidate > remaining:
                    break

                # Include the current candidate
                combination.append(current_candidate)
                backtrack(i + 1, remaining - current_candidate, combination)

                # Backtrack: Remove the last added candidate
                combination.pop()

                previous = current_candidate

        # Sort the candidates to help with duplicate skipping
        candidates.sort()

        result = []

        backtrack(0, target, [])

        return result

