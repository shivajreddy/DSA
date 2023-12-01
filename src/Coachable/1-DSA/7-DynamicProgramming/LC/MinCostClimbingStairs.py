class Solution:
    def minCostClimbingStairs(self, cost: list[int]) -> int:
        """
               | 1    100    1    1    1    100    1    1    100    1  | 0
         i  =  | 0     1     2    3    4     5     6    7     8     9  | n
    cost(i) =  |                            [7]+{c(8),c(9)}  100    1

                c(9) = 1    # base case
                c(8) = 100  # base case
                c(7) = cost[7] + {c(8), c(9)} = 1+1 = 2
                c(6) = cost[6] + {c(7), c(8)} = 1+2 = 3
                c(5) = cost[5] + {c(6), c(7)} = 100+2 = 102
                c(4) = cost[4] + {c(5), c(6)} = 1+3 = 4
                c(3) = cost[3] + {c(4), c(5)} = 1+4 = 5
                c(2) = cost[2] + {c(3), c(4)} = 1+4 = 5
                c(1) = cost[1] + {c(2), c(3)} = 100+5 = 105
                c(0) = cost[0] + {c(1), c(2)} = 1+5 = 6
        """

        # '''
        # Bottom-Up: Iterative approach
        n = len(cost)
        arr = [cost[-1], cost[-2]]

        for i in range(n - 3, -1, -1):
            print(i, cost[i])
            c = cost[i] + min(arr[-1], arr[-2])
            arr.append(c)

        return min(arr[-1], arr[-2])
        # '''


'''
        # Top-Down: Recursive approach
        n = len(cost)
        memo = {n - 1: cost[n - 1], n - 2: cost[n - 2]}

        def dfs(i):
            nonlocal memo
            if i not in memo:
                memo[i] = cost[i] + min(dfs(i + 1), dfs(i + 2))
            return memo[i]

        dfs(0)
        return min(memo[0], memo[1])

        n = len(cost)


# '''

'''
        def minimum_cost(i):
            if i <= 1:
                return 0

            # Check if we have already calculated minimum_cost(i)
            if i in memo:
                return memo[i]

            # If not, cache the result in our hash map and return it
            down_one = cost[i - 1] + minimum_cost(i - 1)
            down_two = cost[i - 2] + minimum_cost(i - 2)
            memo[i] = min(down_one, down_two)
            return memo[i]

        memo = {}
        result = minimum_cost(len(cost))
        print(memo)
        return result
'''
