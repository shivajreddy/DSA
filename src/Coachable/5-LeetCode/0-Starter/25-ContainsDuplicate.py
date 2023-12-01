from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:

        visited_num = set()

        for num in nums:
            if num in visited_num:
                return True
            visited_num.add(num)
        return False
