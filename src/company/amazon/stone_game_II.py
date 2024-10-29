"""
Key Insights  
    - Recursive Game with Optimal Play:  
        - Since both players play optimally, the problem can be modeled as a 
          two-player game using a recursive approach.
        - At each turn, the current player aims to maximize their score while 
          the opponent aims to minimize it.

    - Dynamic Programming with Memoization:  
        - Due to overlapping subproblems and optimal substructure, dynamic 
          programming with memoization is ideal for storing and 
          reusing computed results.
        - The states can be defined by the current index `i` and the 
          current `M` value.

    - Suffix Sum Optimization:  
        - Precomputing the suffix sums of the piles allows for quick 
          calculation of the total stones remaining from any index `i`. 
          - This optimization reduces redundant calculations of sums during 
            recursion.

    - Minimax Algorithm:  
        - We can model the game using the minimax algorithm, where the current
          player tries to maximize their gain, and the opponent 
          tries to minimize it.
        - The player's optimal strategy is to choose `X` such that they 
          maximize `total_stones - opponent's best response`.

    - Game Ending Condition:  
        - If the current player can take all the remaining stones in one 
          move (i.e., `i + 2 * M >= n`), they will do so to maximize their gain.

Detailed Plan  
    1. Define the Recursive Function:  
        - Create a recursive function `dfs(i, M)` that returns the maximum 
          number of stones the current player can obtain starting from 
          index `i` with parameter `M`.

    2. Implement Memoization:  
        - Use a memoization dictionary `memo = {}` to store results of 
          subproblems identified by the state `(i, M)`.

    3. Compute Suffix Sums:  
        - Precompute an array `suffix_sum` where `suffix_sum[i]` is the 
          total number of stones from pile `i` to the end.
        - This allows for quick calculation of the total stones remaining 
          without recalculating sums during recursion.

    4. Base Cases:  
        - If `i >= n` (where `n` is the number of piles), return 0, as there 
          are no stones left to take.
        - If the current player can take all remaining stones 
          (`i + 2 * M >= n`), return `suffix_sum[i]`.

    5. Recursive Case:  
        - For each possible `X` from 1 to `2M`, consider:
            - The total stones taken by the current player: 
              `suffix_sum[i] - suffix_sum[i + X]`.
            - The opponent's maximum stones obtained in the next state: 
              `dfs(i + X, max(M, X))`.
            - The current player's gain is 
              `total_stones_taken + (total_remaining_stones - opponent's gain)`

    6. Minimax Logic:  
        - Since the opponent aims to minimize the current player's gain, 
          consider the worst-case scenario for the opponent.
        - Calculate `max_stones = suffix_sum[i] - min(opponent's gain 
          over all X)`.

    7. Update Memoization and Return Result:  
        - Store the computed result in `memo[(i, M)]` before returning it.
        - Return the maximum stones the current player can obtain from the 
          current state.

Time and Space Complexity  
    - Time Complexity: O(n²)  
        - There are at most `n` values for `i` and up to `n` values for `M` 
          (since `M` can double each time). Thus, the total number of 
          unique states is O(n²).  
        - Each state considers up to `2M` moves, but since `M` can be at 
          most `n`, this is bounded.

    - Space Complexity: O(n²)  
        - The memoization dictionary stores results for each state `(i, M)`.
"""


from typing import List

class Solution:
    def stoneGameII(self, piles: List[int]) -> int:
        n = len(piles)
        memo = {}  # Memoization dictionary to store computed results

        # Step 1: Precompute the suffix sums
        suffix_sum = [0] * (n + 1)
        for i in range(n - 1, -1, -1):
            suffix_sum[i] = piles[i] + suffix_sum[i + 1]

        def dfs(i: int, M: int) -> int:
            if i >= n:
                return 0  # No stones left to take

            if (i, M) in memo:
                return memo[(i, M)]

            # If we can take all remaining stones
            if i + 2 * M >= n:
                memo[(i, M)] = suffix_sum[i]
                return suffix_sum[i]

            min_opponent = float('inf')
            # Try all possible X from 1 to 2M
            for X in range(1, 2 * M + 1):
                if i + X >= n:
                    break  # Can't take more stones than available

                # Opponent's best response
                opponent = dfs(i + X, max(M, X))
                min_opponent = min(min_opponent, opponent)

            # Current player's maximum stones
            memo[(i, M)] = suffix_sum[i] - min_opponent
            return memo[(i, M)]

        # Alex starts first with M=1
        max_stones_by_alex = dfs(0, 1)
        return max_stones_by_alex

