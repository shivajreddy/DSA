class Solution:
    memo = {}

    def uniquePaths(self, m: int, n: int, memo: dict) -> int:

        if str(m) + str(n) in memo:
            return memo[str(m) + str(n)]

        # base cases
        if m == 1 and n == 1:
            return 1
        if m == 0 or n == 0:
            return 0

        memo[str(m) + str(n)] = self.uniquePaths(m - 1, n, memo) + self.uniquePaths(m, n - 1, memo)

        return memo[str(m) + str(n)]


s = Solution()

print(s.uniquePaths(3, 2, {}))
