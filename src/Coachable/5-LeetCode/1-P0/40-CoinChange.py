class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        # """ Top-down
        """Approach
        coins = [1, 2, 5], amount = 11

        # IMPORTANT
        f(0) = 0
        f(-1) = -1, f(-20) = -1
        So, for any number less than 0, we return -1 because that means that amount can't be formed
        with the denominations we have

        memo = {11: f(11), 10 : f(10)}


        f(11) -> returns the min_coins needed to make up an amount of 11

                                f(11)                       ->
                f(10)           f(9)            f(6)        -> min(f(10), f(9), f(6))
          f(9)  f(8) f(5)

        """

        memo = {}  # memoization

        def rec(total):
            if total in memo: return memo[total]  # memoization

            # base cases
            if total < 0:
                return -1
            if total == 0:
                return 0

            min_coins = float('inf')
            for coin in coins:
                curr_total = rec(total - coin)  # f(coin_1), f(coin_2), f(coin_3)
                if curr_total != -1:  # this path either is >0 or is ==0, but not a -ve number
                    min_coins = min(min_coins, curr_total + 1)
            memo[total] = min_coins if min_coins != float('inf') else -1  # for failed paths, use -1
            return memo[total]

        return rec(amount)

        # """
