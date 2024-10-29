"""
Constraints:
1 <= prices.length <= 3 * 104
0 <= prices[i] <= 104

Scope & Assumptions:
- at most one share
- can buy & sell on same day
- no -ve numbers in input
- can buy & sell on same day
- can sell & buy on same day
- can buy today and only sell either today or another day in future, but not any previous day.

Observations:
- for maximize profit -> sum of all maximum trades
- max profit that can be made on a trade at given day
	- buy on that day
	- which is the highest profit day after this.
- Globally optimal solution: involves choosing sub solutions that might not be totally optimal
- For more efficient solution instead of a DP approach using 2 pointers with prefix-sum
  approach, where prefix-sum is re-initialized when ever a trade’s potential profit is
  lower that current profit for the trade.

Approach & Solution:
             7     1    5     3     6     4
            se
                   s           e      

            1	5	9	10
            s	e			= 4
            s			e	= 9

            s	e			= 4
            s	e	= 6
"""

from typing import List

class Solution:
    '''
    ### Explanation
    The goal of this problem is to maximize profit by identifying potential buy and 
    sell days. The solution involves iterating over the list of prices, keeping track 
    of both the current profit and total profit as you move through the days.

    The approach taken here is a **greedy algorithm**:
    1. **Buy Pointer:** Track the day you bought the stock.
    2. **Sell Pointer:** Traverse through each day and calculate potential profit if 
    sold on that day.
    3. **Reset Conditions:** If the potential profit starts decreasing compared to 
    the previous profit, it means a local maximum has been reached (a good time 
    to sell). Add the current profit to the total and reset for the next transaction.
    4. **Final Adjustment:** After the loop finishes, any remaining profit from the 
    last ongoing transaction is added to the total profit.

    This ensures that we maximize the profit by summing up all local maximums without 
    revisiting any earlier buy-sell pair decisions.

    ### Time Complexity
    - **O(n)**: We iterate through the list of prices once, where `n` is the number 
    of days.

    ### Space Complexity
    - **O(1)**: The solution uses constant extra space, only storing variables like 
    `buy`, `curr_profit`, and `total_profit`.
    '''
    def maxProfit(self, prices: List[int]) -> int:
        """
        Calculates the maximum profit that can be made by buying and selling the stock multiple times.

        Args:
        prices (List[int]): A list of stock prices where prices[i] is the stock price on the ith day.

        Returns:
        int: The maximum profit that can be made.
        """
        n = len(prices)
        if n == 0:
            return 0

        total_profit = 0  # Tracks the total profit made from all the transactions
        curr_profit = 0   # Tracks the current profit for the ongoing transaction
        buy = 0           # Pointer to track the day we bought the stock

        # Iterate through each day to find potential selling points
        for sell in range(1, n):
            # Calculate the profit for selling on the current day
            potential_profit = prices[sell] - prices[buy]

            # If the profit starts decreasing, complete the current transaction
            if potential_profit < curr_profit:
                total_profit += curr_profit  # Add the current profit to the total
                curr_profit = 0              # Reset current profit
                buy = sell                   # Reset the buy day to the current day
            else:
                curr_profit = potential_profit  # Update the current profit

        # Add the last valid profit to the total profit
        return total_profit + curr_profit

