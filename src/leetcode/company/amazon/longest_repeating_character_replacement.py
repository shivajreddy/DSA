"""
Key Insights

Sliding Window with Optimization:
   - Use a sliding window to maintain a valid substring.
   - Expand the window while it remains valid (i.e., the number of characters to change ≤ `k`).
   - Adjust the window based on character frequencies.
   - This approach is more efficient and suitable for larger input sizes.

Algorithm Intuition:
    - The goal is to find the longest valid substring where we can change at 
      most `k` characters to make all characters the same.
    - For any given window (substring), the number of replacements needed to 
      make the substring uniform is `window_size - max_freq`, where:
        - `window_size` is the current size of the window.
        - `max_freq` is the frequency of the most common character in the window.
    - As long as `window_size - max_freq ≤ k`, the window is valid.

Why This Works:

- By considering the character that appears most frequently in the window, we 
  minimize the number of replacements needed.
- We aim to maximize the window size while ensuring the number of replacements
  doesn't exceed `k`.

---

Algorithm Design:

1. Initialize Variables:
   - Use a hashmap (`count`) to keep track of the character frequencies within 
     the current window.
   - Initialize two pointers `left` and `right` to define the window boundaries.
   - Set `max_len` to store the maximum length found.
   - Set `max_freq` to keep track of the highest frequency character in the current window.

2. Sliding Window Mechanism:

   a. Expand the Window:
      - Move the right pointer (`right`) to the right, adding the current 
        character to the `count` hashmap.
      - Update `max_freq` if the frequency of the current character exceeds 
        the previous `max_freq`.

   b. Check Window Validity:
      - If the condition `window_size - max_freq > k` is true, the window is invalid.

   c. Shrink the Window:
      - Move the left pointer (`left`) to the right to shrink the window until 
        the condition `window_size - max_freq ≤ k` is satisfied again.

   d. Update Maximum Length:
      - At each valid window, update `max_len` with the size of the current window.

3. Edge Cases:
   - Handle cases where `k` is zero, meaning no changes are allowed.
   - Handle cases where the entire string can be transformed into the same 
     character with the given `k`.

---

Time and Space Complexity:

- Time Complexity: O(n)
  - The right pointer moves `n` times (once for each character).
  - The left pointer moves at most `n` times as well, resulting in a total of `2n` operations.
- Space Complexity: O(1)
  - The `count` hashmap stores frequencies for up to 26 characters (since the 
    input consists of uppercase English letters).
  - Other variables (like `left`, `right`, `max_freq`, etc.) use constant space.

"""

from collections import defaultdict

class Solution2:
    def characterReplacement(self, s: str, k: int) -> int:
        count = defaultdict(int)
        max_len = 0
        max_freq = 0
        left = 0

        for right in range(len(s)):
            # Add the current character to the count
            count[s[right]] += 1
            # Update max frequency character count
            max_freq = max(max_freq, count[s[right]])


            ''' Dont' have to keep increasing left, we can do it once to make window valid
            # Current window size is right - left + 1
            # If replacements needed exceed k, shrink the window
            while (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                # Note: We don't update max_freq here to maintain O(n) time
            # '''

            # ''' We can just increase left pointer once
            # Calculate the number of characters that need to be replaced
            window_size = right - left + 1
            chars_to_replace = window_size - max_freq

            if chars_to_replace > k:
                count[s[left]] -= 1
                left += 1
                # Note: We don't update max_freq here to maintain O(n) time
            # '''


            # Update max_len
            max_len = max(max_len, right - left + 1)

        return max_len


"""
Finds the length of the longest substring containing the same letter 
after performing at most k character replacements.

Key Insights:
    - Sliding Window Technique: Utilize a window to keep track of the current 
      substring.
    - Frequency Tracking: Maintain the count of each character within the 
      window.
    - Max Frequency Optimization: Keep track of the count of the most frequent 
      character in the current window to determine if replacements are needed.
    - Window Adjustment: If the number of characters that need to be replaced 
      exceeds `k`, slide the window forward.

Algorithm Design:
1. Initialize Variables:
    - `left`: Left boundary of the sliding window.
    - `max_freq`: The count of the most frequent character within the current window.
    - `max_length`: The length of the longest valid substring found.
    - `char_counts`: An array to store the frequency of each uppercase 
       English letter within the window.

2. Expand the Window:
    - Iterate through the string with the right boundary `right`.
    - Update the frequency of the current character.
    - Update `max_freq` if the current character's frequency is the highest so far.

3. Check Replacement Requirement:
    - Calculate the number of characters that need to be replaced: `current_window_size - max_freq`.
    - If this number exceeds `k`, shrink the window from the left:
        - Decrease the frequency of the character at the left boundary.
        - Move the left boundary forward.

4. Update Maximum Length:
    - After each iteration, update `max_length` with the size of the current valid window.

5. Return the Result:
    - The `max_length` will be the length of the longest valid substring found.

Time Complexity: O(n)
- The algorithm traverses the string with two pointers (`left` and `right`), 
  each moving at most `n` steps, where `n` is the length of the string.

Space Complexity: O(1)
- The `char_counts` array has a fixed size of 26, corresponding to the uppercase English letters.
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        n = len(s)

        # Array to store the frequency of each character in the current window
        char_counts = [0] * 26

        max_freq = 0  # The count of the most frequent character in the current window
        max_length = 0  # The length of the longest valid substring found

        left = 0  # Left boundary of the sliding window
        for right in range(n):
            # Convert character to index (0-25)
            current_char_index = ord(s[right]) - ord('A')
            char_counts[current_char_index] += 1

            # Update the count of the most frequent character in the window
            max_freq = max(max_freq, char_counts[current_char_index])

            # Calculate the number of characters that need to be replaced
            window_size = right - left + 1
            chars_to_replace = window_size - max_freq

            # If replacements exceed k, shrink the window from the left
            if chars_to_replace > k:
                # Move the left boundary of the window forward & update counter
                left_char_index = ord(s[left]) - ord('A')
                char_counts[left_char_index] -= 1
                left += 1

            # Update the maximum length of a valid window
            max_length = max(max_length, right - left + 1)

        return max_length

