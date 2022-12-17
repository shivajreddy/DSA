class Solution:

    def maxArea(self, height: List[int]) -> int:

        l, r = 0, len(height) - 1
        ans = 0

        while l < r:

            h = min(height[l], height[r])
            d = r - l
            ans = max(ans, h*d)

            # this works cuz
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return ans

""" Note: 
you wont miss any possiblities by moving the smaller height pointer.
cuz every time you move the pointer you loose 1 distance.
so why would you move longer height? thats why always move smaller height
and among these combinations there exists the result
"""