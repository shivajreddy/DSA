"""
### Explanation:
The sliding window technique is used with two pointers, `s` (start) and `e` 
(end), both initialized to `0`.

- A dictionary `last_seen_indexes` stores the last seen index of each character.
- As we move through the string with pointer `e`, we check if the current 
  character (`curr`) was seen before:
  - If it was seen and its last seen index is inside the current window, we 
    update `s` to the next index after the last seen index of the current 
    character.
- After processing each character, we calculate the length of the current 
  substring and update the result if it's the longest found so far.
- The window is moved forward by incrementing `e`.

### Time Complexity:
- `O(n)`: Each character is processed at most twice — once when it's added 
  to the window and once when the start pointer (`s`) is moved past it. Thus, 
  the overall time complexity is linear, `O(n)`, where `n` is the length of the 
  string.

### Space Complexity:
- `O(min(n, m))`: The space complexity is dictated by the dictionary 
  `last_seen_indexes`, which holds at most the number of unique characters. 
  Therefore, it is `O(min(n, m))`, where `n` is the string's length, and `m` is 
  the size of the character set (in this case, 26 for lowercase English 
  letters).
"""


class Solution:
    def lengthOfLongestSubstring(self, word: str) -> int:
        # start & end pointers of the sliding window
        s, e = 0, 0
        result = 0

        # Dictionary to store the last seen index of each character
        last_seen_indexes = {}

        # Sliding window approach
        while e < len(word):
            # Current character at the end pointer
            curr = word[e]

            # Check if the character is already in the current window
            if curr in last_seen_indexes:
                # Shrink the start of the window to the right of the last seen index
                s = max(s, last_seen_indexes[curr] + 1)

            # Update the last seen index of the current character
            last_seen_indexes[curr] = e

            # Calculate the window size and update the result
            result = max(result, e - s + 1)

            # Move the end pointer to extend the window
            e += 1

        return result


# TESTS --------------
s = Solution()
print(s.lengthOfLongestSubstring("abcabcbb"))  # Output: 3 ("abc")
print(s.lengthOfLongestSubstring("bbbbb"))     # Output: 1 ("b")
print(s.lengthOfLongestSubstring("pwwkew"))    # Output: 3 ("wke")

