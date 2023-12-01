from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        '''
        using 2 pointers
        j goes from beginning to end
        i moves to j, when profit is <= 0
        '''
        i, j = 0, 0
        profit = 0
        for j in range(len(prices)):
            diff = prices[j] - prices[i]
            if diff <= 0:
                i = j
            else:
                profit = max(profit, diff)

        return profit
        # """

        '''
        prices =  7     1     5       3       6       4
    min_price  =  7     1     1       1       1       1

        dp[idx] = max(dp[idx-1], prices[idx]-min_price)
        dp     =  0    0,0   0,4     2,4     4,5    3,5
               =  0     0     4       4       5      5

        max_profit = dp[-1]

        '''

        n = len(prices)

        min_price = prices[0]  # track the minimum price encountered so far

        dp = [0] * n  # this list tracks the profit_so_far

        for idx in range(1, n):
            min_price = min(min_price, prices[idx])
            curr_profit = prices[idx] - min_price
            dp[idx] = max(dp[idx - 1], curr_profit)

        return dp[-1]
