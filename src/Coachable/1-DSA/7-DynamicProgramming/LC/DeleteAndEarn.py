from collections import defaultdict


class Solution:
    """
    operation: (any # of times) -
        nums = [3, 4, 2] pick-4  earned=4   nums=[3,2]
            delete_all = 3,5 => nums=[2]
        nums = [2]  pick-2  earned=4+2  nums[2]

    nums=[2,2,3,3,3,4]  pick-3  earned=3    nums=[2,2,3,3,4]
        delete_all=2,4  nums=[3,3]
    nums=[3,3]  pick-3  earned=3+3  nums[3]
        delete_all=2,4  nums=[3]
    nums=[3]    pick-3  earned=3+3+3    nums[]

    # constraints:
    each number is an int, and >=1
    1 <= nums.length <= 2 * 10**4

                3,4,2

                    0
            3       4      2
                  2      4

                    0
            2   2   3   3   3   4
          2 4  2 4  3   3   3  2


        deleted_set = {}
        pick-4  {3,5}
        pick-2  {1,3,5}

        hm = {
            0: 0
            2: 2
            3: 3
            4: 1
        }
        range=1,2   (1-n, in hm and not in delete)
        pick=3, sum = 3*hm[3] = 3*3 = 9
        delete = {2,4}

        [2] -> 2
        [2,4]   -> 4, dont take 3 in previous step
        pick a number -> value of that number, sum(num-1), sum(num+1)
    """

    def deleteAndEarn(self, nums: list[int]) -> int:

        hm = defaultdict(int)
        n = float('-inf')
        for num in nums:
            n = max(n, num)
            hm[num] += 1

        print('hm=', hm)
        print('n=', n)

        def max_points(x, memo):
            if x == 0:
                return 0
            if x == 1:
                memo[1] = hm[1]
                return hm[1]
            if x not in memo:
                gain = hm[x] * x
                memo[x] = max(max_points(x - 2, memo) + gain, max_points(x - 1, memo))
            return memo[x]

        memo = {}
        max_points(n, memo)
        return memo[n]
