# https://leetcode.com/problems/add-binary/
class Solution:
    def addBinary(self, a: str, b: str) -> str:

        s = int(a, 2) + int(b, 2)
        bs = bin(s)
        return bs[2:]
