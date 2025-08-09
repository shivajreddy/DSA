class Solution:
    """
    Time : O(n), n is the no.of places in the given number
    Space: O(1)
    """
    def reverse(self, x: int) -> int:

        INT_MAX = 2**31 - 1
        # INT_MIN = -2**31

        sign = 1 if x > 0 else -1
        x = abs(x)

        result = 0
        while x:
            last_digit = x % 10
            x //= 10

            # Pre Overflow Check, for other languages
            if result > (INT_MAX - last_digit) // 10: return 0
            if result == ((INT_MAX - last_digit) // 10) - 1 and sign == -1: return 0

            # Append the digit to the reversed number
            result = (result * 10) + last_digit

            # Check Overflow Check, can do in python
            # if res == INT_MAX and sign == -1: return 0
            # if res > INT_MAX: return 0
        
        return sign * result
