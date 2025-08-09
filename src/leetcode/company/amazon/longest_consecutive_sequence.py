"""
### Explanation:

#### Initial Edge Case:
- If the input list `nums` is empty, return `0` since there are no sequences to 
  consider.

#### Hash Set for Efficient Lookups:
- The list is converted into a set (`num_set`) to allow `O(1)` average-time 
  lookups, which helps in checking the presence of consecutive numbers 
  efficiently.

#### Identifying the Start of a Sequence:
- The solution iterates through each number in the set. For each number, it 
  checks whether it is the beginning of a sequence by verifying that the 
  previous number (`num - 1`) is not in the set.
- If the number is the start of a sequence, it begins tracking the length of 
  this sequence.

#### Counting the Sequence:
- For each start of a sequence, the solution increments the number and checks 
  if the next consecutive number exists in the set.
- It keeps counting until the sequence breaks (i.e., there is no next 
  consecutive number).

#### Updating the Longest Streak:
- The solution keeps track of the maximum sequence length encountered 
  (`longest_streak`) and updates it whenever a longer sequence is found.

### Time and Space Complexity:
- **Time Complexity**: `O(n)`
  - Every number in the list is processed at most twice—once when it is 
    identified as the start of a sequence and then for each consecutive number 
    in that sequence.
  - Hash set operations (like checking the existence of an element) take `O(1)` 
    on average.
- **Space Complexity**: `O(n)`
  - The set stores all the numbers in the input list, which requires `O(n)` 
    space.

"""

from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Finds the length of the longest consecutive elements sequence in the array.

        Args:
        nums (List[int]): A list of integers.

        Returns:
        int: The length of the longest consecutive sequence.
        """
        if not nums:
            return 0

        # Convert the list to a set to allow O(1) lookups
        num_set = set(nums)
        longest_streak = 0

        for num in num_set:
            # Check if this number is the start of a sequence
            if num - 1 not in num_set:
                current_num = num
                current_streak = 1

                # Check for consecutive numbers following `current_num`
                while current_num + 1 in num_set:
                    current_num += 1
                    current_streak += 1

                # Update the longest streak found
                longest_streak = max(longest_streak, current_streak)

        return longest_streak


# TESTS -----------
import unittest

class TestLongestConsecutive(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case_1(self):
        self.assertEqual(self.solution.longestConsecutive([100, 4, 200, 1, 3, 2]), 4)
        # Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]

    def test_case_2(self):
        self.assertEqual(self.solution.longestConsecutive([0, -1, 1, 2, 3]), 5)
        # Explanation: The longest consecutive elements sequence is [-1, 0, 1, 2, 3]

    def test_case_3(self):
        self.assertEqual(self.solution.longestConsecutive([0]), 1)
        # Explanation: Only one element, so the sequence length is 1.

    def test_case_4(self):
        self.assertEqual(self.solution.longestConsecutive([]), 0)
        # Explanation: No elements, so the sequence length is 0.

    def test_case_5(self):
        self.assertEqual(self.solution.longestConsecutive([10, 5, 9, 11, 8, 6]), 4)
        # Explanation: The longest consecutive elements sequence is [8, 9, 10, 11]

if __name__ == "__main__":
    unittest.main()

