# https://leetcode.com/problems/longest-palindrome/

from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:

        result = 0

        hm = Counter(s)

        for val in hm.values():
            # add all the even sized chars
            # if val = 7,  6 of them can be used
            # the symbol // is the floor division. how many times will denominator goes in numerator
            # % is the remaining number
            # 10 // 3 is 3, 3 goes 3 times in 10. reminder will be 1, so 10 % 3 is 1
            result += val // 2 * 2

            if result % 2 == 0 and val % 2 != 0:
                result += 1

        return result
