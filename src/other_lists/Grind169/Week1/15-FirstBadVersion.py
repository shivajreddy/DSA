# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:

        l = 0
        r = n - 1

        while l < r:
            mid = l + (r-l) // 2

            if isBadVersion(mid+1):
                r = mid - 1
            else:
                l = mid + 1

        # now based on the left pointer return result
        if isBadVersion(l+1):
            return l+1
        return l+2
