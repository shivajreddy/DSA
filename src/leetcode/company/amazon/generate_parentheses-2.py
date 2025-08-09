
"""
- Initialize an empty list to store valid parentheses combinations.
- Define a backtracking function that takes counts of remaining open and close parentheses.
    - If counts are valid, recursively try adding an open parenthesis (decrement open count).
    - Then recursively try adding a close parenthesis (decrement close count).
    - If both counts reach zero, add the current combination to the result list.

Time : O(4^n / √n)
  - The number of valid parentheses combinations, follows the Catalan number sequence. 
    - The number of valid combinations is proportional to the `n-th` Catalan number.
    - Which asymptotically grows as O(4^n / √n)
  - While the time complexity is exponential, the algorithm is often fast enough for 
  practical use with small to moderate n, as it efficiently prunes invalid combinations early 
  in the recursion tree.

Space: O(n) Space used is proportional to the depth of the recursive call stack
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def backtrack(open_count: int, close_count: int, current_combination: List[str]):
            # Base case: invalid state
            if open_count < 0 or close_count < 0 or open_count > close_count:
                return

            # Base case: valid combination found
            if open_count == 0 and close_count == 0:
                valid_combinations.append(''.join(current_combination))
                return

            # Recursive case: try adding an open parenthesis
            current_combination.append('(')
            backtrack(open_count - 1, close_count, current_combination)
            current_combination.pop()

            # Recursive case: try adding a close parenthesis
            current_combination.append(')')
            backtrack(open_count, close_count - 1, current_combination)
            current_combination.pop()

        valid_combinations = []
        backtrack(n, n, [])
        return valid_combinations

