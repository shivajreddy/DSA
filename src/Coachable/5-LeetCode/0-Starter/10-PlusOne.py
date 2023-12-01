from typing import List


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:

        result = []
        bal = 1
        for num in reversed(digits):
            total = num + bal
            bal = 0 if total < 10 else 1
            reminder = total % 10
            result.append(reminder)

        # if there is still balance to be added
        if bal:
            result.append(bal)

        return result[::-1]
