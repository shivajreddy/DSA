class Solution:
    def climbStairs(self, n: int) -> int:

        # Time: O(n) Space: O(n)
        # using extra space, and recursion
        """
        hm = {1 : 1, 2: 2}

        def rec(n, hm):
            if n in hm: return hm[n]
            hm[n] = rec(n-1, hm) + rec(n-2, hm)
            return hm[n]

        return rec(n, hm)
        """

        # Time: O(n) Space: O(1)
        # using no extra space
        if n < 3:
            return n

        # these are the n-1^th and n^th steps.
        # more specifically the total count that takes to reach these n-1^th step & n^th step
        fib = [1, 2]
        i = 2
        while i < n:
            x, y = fib[0], fib[1]
            fib[0], fib[1] = y, x + y
            i += 1
        return fib[1]
