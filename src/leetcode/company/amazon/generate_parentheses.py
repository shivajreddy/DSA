""" 
### Explanation:
The problem requires generating all combinations of well-formed parentheses for 
`n` pairs of parentheses. This is a classic problem that can be solved using 
backtracking.

### Steps:
- **Recursive Function**: The function `rec` takes the number of left 
  parentheses `l` and right parentheses `r` left to use, along with the current 
  path of the parentheses being generated.

#### Base Case:
- If both `l` (left parentheses) and `r` (right parentheses) are zero, it means 
  a valid combination is formed, so it is added to the result.

#### Left Parenthesis:
- You can add a left parenthesis `'('` if there are any left (`l > 0`). After 
  adding it, you reduce the count of `l` and call the function recursively.

#### Right Parenthesis:
- You can add a right parenthesis `')'` only if there are more right 
  parentheses left than left (`r > l`). This ensures the parentheses remain 
  balanced.

#### Backtracking:
- After exploring one possibility, we backtrack by removing the last added 
  parenthesis using `pop()`, ensuring that we try other valid combinations.

### Time Complexity:
- **Time Complexity**: `O(4^n / √n)`
  - This is derived from the number of valid parentheses combinations, which 
    follows the Catalan number sequence. The number of valid combinations is 
    proportional to the `n-th` Catalan number, which asymptotically grows as 
    `O(4^n / √n)`.

### Space Complexity:
- **Space Complexity**: `O(n)`
  - The space used is proportional to the depth of the recursive call stack, 
    which is at most `n` because at each level of the recursion, we add one 
    parenthesis to the current string.
"""

from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        """
        Generates all combinations of well-formed parentheses for n pairs.

        Args:
        n (int): Number of pairs of parentheses.

        Returns:
        List[str]: All valid parentheses combinations.
        """
        def rec(l, r, path):
            # Base case: If no more parentheses to add, append the current valid combination
            if l == 0 and r == 0:
                result.append(''.join(path))

            # Add left parenthesis if available
            if l > 0:
                path.append('(')
                rec(l - 1, r, path)
                path.pop()  # Backtrack

            # Add right parenthesis if valid
            if r > 0 and r > l:
                path.append(')')
                rec(l, r - 1, path)
                path.pop()  # Backtrack

        result = []
        rec(n, n, [])  # Start with n left and n right parentheses
        return result




# TEST CASES ------------

import unittest

class TestGenerateParenthesis(unittest.TestCase):
    def setUp(self):
        self.sol = Solution()

    def test_case_1(self):
        self.assertEqual(sorted(self.sol.generateParenthesis(1)), sorted(["()"]))

    def test_case_2(self):
        self.assertEqual(sorted(self.sol.generateParenthesis(2)), sorted(["()()", "(())"]))

    def test_case_3(self):
        self.assertEqual(sorted(self.sol.generateParenthesis(3)), sorted(["((()))", "(()())", "(())()", "()(())", "()()()"]))

    def test_case_4(self):
        self.assertEqual(self.sol.generateParenthesis(0), [])

if __name__ == '__main__':
    unittest.main()

