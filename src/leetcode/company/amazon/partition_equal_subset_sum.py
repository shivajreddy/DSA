"""
Key Insights:
    - Total Sum Evenness: The total sum must be even to split into two equal
      subsets. If the total sum is odd, can never split into 2 equal subsets.
    - Subset Sum Problem: The problem reduces to finding a subset 
      with sum equal to half of the total sum.
    - If there is any number that is greater than (total_sum // 2), then we can
      never form 2 valid subsets. Given that: 1 <= nums[i] <= 1000

---

Top-Down Approach Overview
    Recursive Exploration:
        - We recursively explore the possibility of including or excluding 
          each number in the subset to reach the target sum.  
        - The recursion tree represents all possible subsets.
    Memoization:  
        - To avoid redundant calculations, we store the results of subproblems 
          (i.e., whether a certain sum is achievable with a subset of the array).
        - We use a memoization table (cache) to store intermediate results.

Algorithm Steps
    1. Calculate Total Sum:
        - Compute the total sum of the array `nums`.
        - If the total sum is odd, return `False` since it's impossible to 
          partition into two equal subsets.
    2. Define Recursive Function:
        - The recursive function `dfs(index, remaining_sum)` 
    3. Base Cases:
        - If `remaining_sum` equals 0, return `True`.
        - If `remaining_sum` is less than 0 or `index` reaches the end of
          the array, return `False`.
    4. Memoization (Caching):
        - Use a cache (e.g., a dictionary) to store the result where key is
          (index, target_sum)
        - Before performing recursion, check if the result is already in the cache.
    5. Recursive Calls:
        - Include the current number: `dfs(index + 1, target_sum - nums[index])`.
        - Exclude the current number: `dfs(index + 1, target_sum)`.
    6. Return the Result:
        - If either including or excluding the current number leads to a
          valid partition, return `True`.
        - Otherwise, return `False`.

Time Complexity: O(n * target_sum)
    - Each subproblem is uniquely identified by the current index and remaining sum.
    - There are O(n * target_sum) possible subproblems.
Space Complexity: O(n * target_sum)
    - The memoization dictionary may store up to O(n * target_sum) entries.
    - The recursion stack can go as deep as O(n).

---

Bottom-Up Approach Overview
    Dynamic Programming (Subset Sum Problem):
        - This approach is similar to the 0/1 Knapsack problem.
        - Use a DP array to track which subset sums are achievable.
        - This method is efficient and suitable for the given problem constraints.

Algorithm Design
    1. Calculate Total Sum:
        - Compute the total sum of the array `nums`.
        - If `total_sum % 2 != 0`, return `False`.

    2. Initialize DP Array:
        - The data that we should hold in this array is the follows:
            - The size of the array would be (1+target_sum)
            - Each index in the array, represents the subset-sum
            - And the value at the index is boolean, where True means that we 
              are able to create 2 subsets whose total(subset-sum) is the index.
            - Example: target_sum = 4
                        dp = [ T  T  F  T  F ]
                               0  1  2  3  4
                - This implies the following, for the input of numbers,
                  they can be 2 subsets with where both will have same subset-sum
                - and possible sums are 0, 1, 3
                - we could never form a subset sum of 2 or 4
                - 0 will always be true, because the two subsets could be empty.

            - The main logic here is the same as top-down:
                - For every number in the given input, we have identify will 
                  either including or exludign this number creates a subset-sum
                  that we are looking for.
                Ex: [ 1   5   11  5 ]
                    total=22, target_sum=11
                    dp = [  T   F   F   F   F   F   F   F   F   F   F   F  ]
                            0   1   2   3   4   5   6   7   8   9   10  11
                    num=1
                        - for all the subset-sum's starting with the target_sum,
                        will including this number or exluding lead to True
                        - so for subset-sum's: 11,10,9,8,7,6,5,4,3,2,1
                          the corresponding value is either value @ [i] or [i-num]
                          in this case: 
                          [11] -> [11] or [10]
                          [10] -> [10] or [9]
                          ...
                          [1] -> [1][0]
                        dp = [True, True, False, False, False, False, False, False, False, False, False, False]

                    num=5
                        - subset-sum's: 11,10,9,8,7,6,5
                          the corresponding value is either value @ [i] or [i-num]
                          in this case: 
                          [11] -> [11][6]
                          [10] -> [10][5]
                          ...
                          [5] -> [5][0]
                        dp = [True, True, False, False, False, True, True, False, False, False, False, False]

                    num=11
                        dp = [True, True, False, False, False, True, True, False, False, False, False, True]

                    num=5
                        - subset-sum's: 11,10,9,8,7,6,5
                          [11] -> [11][6]
                          [10] -> [10][5]
                          ...
                          [5] -> [5][0]
                        dp = [True, True, False, False, False, True, True, False, False, False, True, True]


                Ex: [1 2 5]
                    total=8 target_sum=4
                    dp = [ T    F   F   F   F ]
                           0    1   2   3   4
                    num=1
                        subset-sum's : 4, 3, 2, 1
                        [4] -> [4] or [3]
                        [3] -> [3] or [2]
                        [2] -> [2] or [1]
                        [1] -> [1] or [0]
                    dp = [ T    T   F   F   F ]
                    num=2
                        subset-sum's : 4, 3, 2
                        [4] -> [4] or [2]
                        [3] -> [3] or [1]
                        [2] -> [2] or [0]
                    dp = [ T    T   T   T   F ]
                    num=5
                        no subset-sum's to exmplore
                        leaving [5] = False
                    dp = [ T   T   T   T   F ]

                - For every number in the given input
                  - we have to find all the possible sums that this number can give
                  - the 
            When can an index(i.e., sum) be marked
              as true:
              - When it's already marked as true in some previous iteration
              - If any of the 

        - Create a boolean DP array `dp` of size `(target_sum + 1)`,
          where `target_sum = total_sum // 2`.
        - `dp[i]` will be `True` if a subset sum of `i` is possible.
    3. Base Case:
        - Initialize `dp[0] = True`, as a subset sum of 0 is always possible (empty subset).
    4. Fill DP Array:
        - Iterate through each number `num` in `nums`.
        - For each `num`, update `dp` from `target_sum` down to `num`:
            - `dp[i] = dp[i] or dp[i - num]`
        - This ensures we consider each number only once (0/1 Knapsack problem logic).
    5. Check Result:
        - After filling the DP array, if `dp[target_sum]` is `True`, return `True`.
        - Otherwise, return `False`.

Time and Space Complexity
    - Time Complexity: O(n * target_sum)  
        - `n` is the number of elements in `nums`.
        - `target_sum` is at most 10,000 (since `nums[i] <= 100` and `n <= 200`).
    - Space Complexity: O(target_sum)  
        - We use a one-dimensional DP array of size `target_sum + 1`.

"""

from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        total_sum = sum(nums)

        # If total sum is odd, it's impossible to partition into equal subsets
        if total_sum % 2 != 0:
            return False

        target_sum = total_sum // 2
        n = len(nums)

        ''' DP: Top-Down using Recursion + Memoization
        # Use memoization to cache intermediate results
        memo = {}

        def dfs(index: int, remaining_sum: int) -> bool:
            # Base cases
            if remaining_sum == 0:
                return True
            if remaining_sum < 0 or index == n:
                return False

            # Check if result is already in cache
            if (index, remaining_sum) in memo:
                return memo[(index, remaining_sum)]

            # Recursive calls: Include current number & exclude current number
            include = dfs(index + 1, remaining_sum - nums[index])
            exclude = dfs(index + 1, remaining_sum)

            # Cache the result
            memo[(index, remaining_sum)] = include or exclude
            return memo[(index, remaining_sum)]

        # Start recursion from index 0 and remaining_sum is target_sum
        return dfs(0, target_sum)
        # '''

        # ''' DP: Bottom-Up using iteration
        # Initialize DP array
        dp = [False] * (target_sum + 1)
        dp[0] = True  # Base case: sum of 0 is always possible

        # Iterate through the numbers
        for num in nums:
            # Early break if there is a number in the input that is > target_sum
            if num > target_sum:
                return False
            if dp[-1] == True:
                return True

            # Update dp array from target_sum down to num
            for i in range(target_sum, num - 1, -1):
                dp[i] = dp[i] or dp[i - num]

        # The target_sum is achievable if dp[target_sum] is True
        return dp[target_sum]
        # '''

