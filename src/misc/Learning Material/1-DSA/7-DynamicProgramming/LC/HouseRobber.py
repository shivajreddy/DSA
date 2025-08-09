class Solution:
    def rob(self, nums: list[int]) -> int:
        """
                1   2   3   1   X
                -   -   -   -   -

                2   7   9   3   1   X
                -   -   -   -   -   -
            i = 0   1   2   3   4   5
         dp(i)= 2   7   11  11  12


            i
            0               0
            1          2          7
            2       9     3    3     1


- if you start from beginning, the choices of next houses are to be already known.so it doesnt make sense to start
from beginning.
- We start from last house(same logic for every house), when we are at the last house we have 2 options: rob this
house + rob i-2th house, or just rob i-1 house.
- So for a house at index i, the max. amount stolen is max( dp(i-2)+nums[i], dp(i-1) ),
- i.e., the max amount that can be stolen until this point depends on these 2 situations, ie.,
e steal(current_house)+stolen until(current_house -2) or stolen(current_house-1).

- so the decision of i depends on i-1, i-2. This means that the base cases for i=0,i=1 should be defined.
- cuz starting with i = n, we go back n-1,n-2,...5,4,3,2,1. and when we reach i=2, it depends on 1,0.
-when i is at 0, we only have the option to steal that house, since each house >= 0
- when i is at 1, we chose the max(nums[0], nums[1]) bcs we start with i=1 if i=0 holds less amount, but if i=0 holds
more value, then dp(1) = nums[0] meaning at idx=1, max amount stolen is nums[0]   ex: 99, 7, ...
        """
        # Top-Down - recursion
        '''
        def dp(i, memo):
            if i == 0:
                return nums[0]
            if i == 1:
                return max(nums[0], nums[1])

            if i not in memo:
                memo[i] = max(dp(i-2, memo) + nums[i],  dp(i-1, memo))
            return memo[i]

        n = len(nums)
        memo = {}
        return dp(n - 1, memo)
        '''

        # Bottom-Up - iteration
        # edge case when nums = [0]
        n = len(nums)
        if n < 2:
            return nums[0]

        arr = [nums[0], max(nums[0], nums[1])]

        for i in range(2, n):
            # max_stolen = max(arr[i-1], arr[i-2] + nums[i])
            max_stolen = max(arr[-1], arr[-2] + nums[i])
            arr.append(max_stolen)

        return arr[-1]
