"""
Problem: Combination Sum III


Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.


Constraints:
- Only numbers from 1 to 9 can be used.
- Each number can be used at most once.
- All combinations should be unique.
- You may return the combinations in any order.


Approach:
    - We can solve this problem using backtracking.
    - The idea is to explore all possible combinations of numbers from 1 to 9 and
      collect those combinations that:
        - Sum up to n.
        - Contain exactly k numbers.


    - At each step, we make a choice to include a number in the current combination or not,
    moving forward with numbers greater than the current to avoid duplicates and ensure that
    each number is used at most once.


    Optimization:
    - Since the numbers are in the range 1 to 9 and we consider them in increasing order,
      we can prune the search space early. If the current sum plus the next number exceeds n,
      we can break the loop early.


Time Complexity:
    - The time complexity is O(9 choose k) since we are choosing k numbers out of 9.
    This is acceptable because k is at most 9.


Space Complexity:
    - O(k), where k is the depth of the recursion stack,
    plus the space used to store the combinations in the result list.


Edge Cases:
    - If n is less than the sum of the smallest k numbers (1 + 2 + ... + k),
      there is no valid combination.
    - If n is greater than the sum of the largest k numbers (9 + 8 + ... + (9 - k + 1)),
      there is no valid combination.


Future Improvements:
    - The current solution is efficient for the given constraints.
    - If the number range or k were larger, we might consider dynamic programming or iterative
    approaches to optimize further.


"""
from typing import List


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def backtrack(current_sum: int, combination: List[int], start: int):
            """
            Backtracking helper function to explore possible combinations.


            Args:
                current_sum (int): The sum of the current combination.
                combination (List[int]): The current combination of numbers.
                start (int): The starting number for the loop to avoid duplicates.
            """
            # If the combination is valid, add it to the result list.
            if current_sum == n and len(combination) == k:
                result.append(combination.copy())
                return
            # If the sum exceeds n or the combination size exceeds k, backtrack.
            if current_sum > n or len(combination) > k:
                return


            # Iterate over the numbers from 'start' to 9.
            for num in range(start, 10):
                # Early stopping if the next number exceeds the target sum.
                if current_sum + num > n:
                    break
                # Include the current number in the combination.
                combination.append(num)
                # Move to the next number; num + 1 ensures no repeats.
                backtrack(current_sum + num, combination, num + 1)
                # Backtrack: remove the last number added.
                combination.pop()


        result = []
        # Start backtracking with an empty combination and starting number 1.
        backtrack(0, [], 1)
        return result



