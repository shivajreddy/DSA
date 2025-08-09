class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        l = 0
        res = 0

        for r in range(1, len(prices)):

            profit = prices[r] - prices[l]

            if profit < 0:
                l = r

            else:
                res = max(res, profit)

        return res

"""Note:
1. since time moves forward, we should use 2 pointers(l,r). where l is always < r

2. We use l pointer to find the smallest in our iteration,
    so if any time arr[r] - arr[l] < 0, this means right pointer value is lower than
    the l pointer value, so move your l pointer to r i.e., l = r


"""