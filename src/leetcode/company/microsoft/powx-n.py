"""
When power is even, base gets squared until power becomes 1
    - and power gets floor divided by 2
When power is odd, res gets multiplied with current base value
    - and power gets reduced by 1

    Note: Least value of power is going to be 1. Because 2 // 2 is 1

    Possible values of power, and the series of reduced powers:
        Power = 8  =>  8, 4, 2, 1
        Power = 16 =>  16, 8, 4, 2, 1

        power = 3   =>  3, 2, 1
        power = 10   =>  10, 5, 4, 2, 1
"""


class Solution:
    def myPow(self, x: float, n: int) -> float:

        negative_power = n < 0

        res = 1.0

        base, power = x, abs(n)

        # Reduce power to 0
        while power > 0:
            if power % 2 == 0:  # power is even => square the base
                base *= base
                power //= 2
            else:  # power is odd => multiply result with base
                res *= base
                power -= 1

        if negative_power:
            res = 1 / res

        # Rounding for precision due binary representation of decimals
        return round(res, 5)


# TESTS
sol = Solution()
assert sol.myPow(2.00000, 10) == 1024.00000
assert sol.myPow(2.10000, 3) == 9.26100
assert sol.myPow(0.25519, -6) == 3620.91299
assert sol.myPow(2.00000, -2) == 0.25000
