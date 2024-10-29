from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:

        def backtrack(open, close, path):
            if open < 0 or close < 0 or open > close:
                return

            if open == 0 and close == 0:
                res.append(''.join(path))
                return

            path.append('(')
            backtrack(open - 1, close, path)
            path.pop()

            path.append(')')
            backtrack(open, close - 1, path)
            path.pop()

        res = []
        backtrack(n, n, [])
        return res

