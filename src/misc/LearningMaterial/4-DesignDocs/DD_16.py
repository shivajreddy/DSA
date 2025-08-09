class Solution:
    def isHappy(self, n: int) -> bool:
        # get the sum of square of all digits of given number
        # this will take only O(1) space
        def sq(num):
            res = 0
            while num > 0:
                rem = num % 10
                res += rem**2
                num //= 10
            return res

        slow, fast = n, n

        while True:
            slow = sq(slow)
            fast = sq(sq(fast))
            if slow == fast:
                break

        return slow == 1 or fast == 1


def hello():
    print("hi there")
