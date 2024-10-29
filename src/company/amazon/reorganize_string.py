""" 
Explanation
    Problem: 
    - Given a string s, the task is to reorganize the characters such that 
      no two adjacent characters are the same. If it is impossible, return an empty string.

Approach:
    - We use a max-heap (simulated using negative counts) to always select the character
      with the highest remaining frequency, ensuring no two adjacent characters are the same.
    - After selecting the most frequent character, we then select the next most frequent
      character to alternate.
    - Each character's count is decremented after being added to the result, and if it
      still has remaining occurrences, it is pushed back into the heap.

Time Complexity:
    O(n) for building the frequency map, where n is the length of the string.
    O(k log k) for heap operations, where k is the number of unique characters.
    The overall complexity is O(n + k log k).
Space Complexity:
    O(k) for storing the frequency map and heap, where k is the number of unique characters.
"""


import heapq
from collections import defaultdict

class Solution:
    def reorganizeString(self, s: str) -> str:
        """
        Rearranges the input string such that no two adjacent characters are the same.
        If such a rearrangement is not possible, returns an empty string.

        Approach:
        - Use a max-heap to always pick the character with the highest frequency.
        - If we cannot place two consecutive characters without violating the rule,
          return an empty string.
        - Add two characters at a time to the result (if possible), decrement their count,
          and push them back into the heap.

        Time Complexity:
        - O(n + k log k): n for creating the frequency map, k log k for the heap.
        Space Complexity:
        - O(k): For storing the heap and frequency map.

        Args:
        s (str): Input string to reorganize.

        Returns:
        str: Reorganized string or an empty string if not possible.
        """
        # Step 1: Frequency map of the characters in the input string
        char_freq = defaultdict(int)
        for char in s:
            char_freq[char] += 1

        # Step 2: Create a max-heap based on frequency
        max_heap = [(-count, char) for char, count in char_freq.items()]
        heapq.heapify(max_heap)

        result = []

        while max_heap:
            # Pop the character with the highest frequency
            first_count, first_char = heapq.heappop(max_heap)

            # If this is the last character and its count is more than 1, return ""
            if not max_heap:
                if first_count == -1:
                    result.append(first_char)
                    break
                return ""

            # Pop the next most frequent character to alternate
            second_count, second_char = heapq.heappop(max_heap)

            # Append both characters to the result string
            result.append(first_char)
            result.append(second_char)

            # Decrement counts and push back if they still have remaining occurrences
            if -first_count > 1:
                heapq.heappush(max_heap, (first_count + 1, first_char))
            if -second_count > 1:
                heapq.heappush(max_heap, (second_count + 1, second_char))

        return ''.join(result)



# TESTS ------------------
import unittest

class TestReorganizeString(unittest.TestCase):

    def setUp(self):
        self.solver = Solution().reorganizeString

    def test_case_1(self):
        s = "aab"
        expected = "aba"
        self.assertEqual(self.solver(s), expected)

    def test_case_2(self):
        s = "aaab"
        expected = ""  # It's impossible to reorganize
        self.assertEqual(self.solver(s), expected)

    def test_case_3(self):
        s = "abb"
        expected = "bab"
        self.assertEqual(self.solver(s), expected)

    def test_case_4(self):
        s = "xyzxyz"
        expected = "xyzyzx"  # Already perfectly reorganized
        self.assertEqual(self.solver(s), expected)

    def test_case_5(self):
        s = "aaaabbbbcc"
        expected = "ababababcc"  # Multiple valid rearrangements possible
        result = self.solver(s)
        self.assertTrue(all(result[i] != result[i+1] for i in range(len(result) - 1)))

if __name__ == "__main__":
    unittest.main()

