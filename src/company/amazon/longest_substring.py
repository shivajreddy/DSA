"""
Two pointer algorithm
Left pointer - points to the starting index of valid substring
Right pointer - ending index of valid substring

Time : O(N)
Space: O(N)
"""
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # Dictionary to store the last seen index of each character
        char_index = {}

        max_length = 0

        left = 0
        for right, char in enumerate(s):
            # If the character is already in the current substring,
            # move the left pointer to the right of its last occurrence
            if char in char_index and char_index[char] >= left:
                left = char_index[char] + 1

            # Update the last seen index of the current character
            char_index[char] = right

            # Update the max_length if the current substring is longer
            max_length = max(max_length, right - left + 1)

        return max_length
