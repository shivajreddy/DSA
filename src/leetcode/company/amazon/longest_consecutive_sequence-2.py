from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        n = len(nums)

        if n == 0:
            return 0

        # Create a set of nums, to allow O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if this number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Check for consecutive numbers following `current_num`
                # Note: this will only run for numbers that are the starting numbers
                # so this wont run for all numbers, ensures each number is visited only once
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak found
                longest_streak = max(longest_streak, current_streak)

        return longest_streak
