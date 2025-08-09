from typing import List
from collections import deque

class CoinChange:
    """
    - Use a breadth-first search (BFS) approach to find the minimum number of coins needed
    - Start with the target amount and iteratively subtracts each coin value, 
      - exploring all possible combinations level by level. 
      - The level at which we reach 0 represents the minimum number of coins needed.
    """
    def min_coins(self, coins: List[int], target: int) -> int:
        coins.sort()
        queue = deque([target])
        visited = {target}
        num_coins = 0
        
        while queue:
            for _ in range(len(queue)):
                current_amount = queue.popleft()
                if current_amount == 0:
                    return num_coins
                for coin in coins:
                    remaining = current_amount - coin
                    if remaining < 0:
                        break  # No need to check larger coins
                    if remaining in visited:
                        continue
                    queue.append(remaining)
                    visited.add(remaining)
            num_coins += 1
        
        return -1  # No solution found

class PerfectSquares:
    """
    - This problem is indeed very similar to the Coin Change problem. 
    - Instead of coins, we're using perfect squares (1, 4, 9, 16, etc.) as our "denominations". 
    - The algorithm follows the same BFS approach:
        - We start with the target number n.
        - At each level, we subtract all possible perfect squares (i^2) from the current number.
        - We continue this process until we reach 0.
        - The level at which we reach 0 represents the least number of perfect squares needed to sum up to n.

    - The main difference between the two problems is that in the Coin Change problem, 
      we have a fixed set of coin denominations, while in the Perfect Squares problem, 
      we generate the "denominations" (perfect squares) on the fly up to the square root of the current number.
    - Both solutions use a queue for BFS traversal and a set to keep track of visited numbers to avoid redundant calculations. 
    - The level-by-level exploration ensures that we find the minimum number of coins or perfect squares needed.
    """
    def least_number(self, n: int) -> int:
        queue = deque([n])
        visited = {n}
        num_squares = 0
        
        while queue:
            num_squares += 1
            for _ in range(len(queue)):
                current_num = queue.popleft()
                '''
                - The possible perfect squares for current number range from [1..√current_num] inclusive
                - we can find √x in python using math.sqrt(x) or x**0.5 since x^1/2 is √x
                '''
                for i in range(1, int(current_num**0.5) + 1):
                    remaining = current_num - i**2
                    if remaining == 0:
                        return num_squares
                    if remaining < 0:
                        break  # No need to check larger squares
                    if remaining in visited:
                        continue
                    queue.append(remaining)
                    visited.add(remaining)
        
        return num_squares  # This line should never be reached for valid inputs
