class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Slow and Fast pointer approach for O(n)
        Fast moves till end, starting from 1-index.
        Slow starts at 0 index.
        Slow pointer only moves if Fast pointer's value is smaller than Slow pointer's value.


        So it's like keep moving the 2nd pointer to find even bigger diff.
        but if the 2nd pointer is smaller then move first pointer there and keep finding,
        even bigger diff, so the cases that are not missing are unnecessary.

        [ 3, 5, 6] -> If left is at 3, we calculate diff of 3,5 and 3,6  and the missed 5,6
        is basically useless, cause 5 is still bigger than 3
        """

        slow = 0
        fast = 1
        max_diff = 0

        while fast < len(prices):

            diff = prices[fast] - prices[slow]

            max_diff = max(max_diff, diff)

            if diff < 0:
                slow = fast

            fast += 1

        return max_diff
