class Solution:

    def uniquePaths(self, m: int, n: int) -> int:

        """ using top-down

        memo = {}
        count = 0

        def rec(m, n):
            nonlocal memo
            nonlocal count
            if (m,n) in memo:
                return memo[(m,n)]
            if (n,m) in memo:
                return memo[(n,m)]
            if m == 1 or n == 1:
                return 1
            count += 1
            memo[(m,n)] = rec(m-1, n) + rec(m, n-1)
            return memo[(m,n)]

        return rec(m, n)
        # return memo[(m,n)]
        # """

        # """ using bottom-up
        dp = [[None for _ in range(n)] for _ in range(m)]

        for i in range(m):
            dp[i][0] = 1
        for i in range(n):
            dp[0][i] = 1

        for row in range(1, m):
            for col in range(1, n):
                dp[row][col] = dp[row - 1][col] + dp[row][col - 1]

        return dp[m - 1][n - 1]

        # """
