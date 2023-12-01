class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # """ Using bottom-up
        memo = {}

        def rec(total):
            if total in memo:
                return memo[total]

            # base cases
            if total < 0:
                return -1
            if total == 0:
                return 0

            # track the min_costL
            min_cost = float('inf')  # min # of coins needed for this amount
            for coin in coins:
                res = rec(total - coin)  # recursive call: F(amount - coin)
                if res != -1:
                    min_cost = min(min_cost, res + 1)

            memo[total] = min_cost if min_cost != float('inf') else -1

            return memo[total]

        return rec(amount)
        # """

        '''
        sum(least # of coins) = amount

        # did not fully understand problem: kept thinking i should use given set of coins.
        # but given are denominations only and any # of these coins can be used
        # missed to ask question, will coins be -ve

        [1, 2, 5] => 11
        [1,1,1,1.... 11times]
        [2,2,2,2,2,1]
        [2,1,2,1,2,1,2]
        [5,5,1]

        # edge
        [2], 3 -> -1
        [2], 1 -> -1
        [...], 0 -> 0


        [1, 2, 5] : 11
        5 -> 1,2,5
        5,5 -> 1,2,5
        5,5,1 -> 11
        '''

        """ top-down DP
        hm = {}
        for coin in coins:
            hm[coin] = 1

        def rec(total):
            if total < 0:
                return -1

            if total in hm:
                return hm[total]

            hm[total] = min(rec(total-coin)+1 for coin in coins)
            hm[total] = hm[total]

            return hm[total]

        rec(amount)
        print(hm)

        return -1
        # """
