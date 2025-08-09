class Solution:

    def isPalindrome(self, s: str) -> bool:

        l, r = 0, len(s) - 1

        while l < r:

            while l < r and not self.isAlphaNum(s[l]):
                l += 1
            while l < r and not self.isAlphaNum(s[r]):
                r -= 1

            if s[l].lower() != s[r].lower():
                print('checking', s[l].lower(), 'vs', s[r].lower())
                return False
            l, r = l + 1, r - 1
        return True

    # custom isalnum function using ASCII code
    def isAlphaNum(self, char: str) -> bool:
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))



""" NOTES:

You can make your own isAlphaNum or isAl or isNum functions, 
using the ASCII representaiton of chars. ord(char a) gives the ASCII in python

def isAlphaNum(self, char: str) -> bool:
        return (ord('A') <= ord(char) <= ord('Z') or
                ord('a') <= ord(char) <= ord('z') or
                ord('0') <= ord(char) <= ord('9'))

'A'.lower()   -> 'a'
'b'.lower()   -> 'b'
''.lower()      -> ''  # very important
'3'.lower() -> '3'  # very important, so no error if the given number cant be converted to lower case.
 which is why you can use .lower() for empty strying and strings of nums  like '3123' too.

"""