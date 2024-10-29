"""
### Explanation

This problem requires grouping words that are anagrams of each other. An **anagram** is 
a word or phrase formed by rearranging the letters of another, using all the original 
letters exactly once.

1. **Approach**:
   - Each word can be described by its **character frequency signature** (the count 
     of each letter).
   - For example, "eat", "tea", and "ate" all have the same character counts 
     (one 'e', one 'a', one 't').
   - By converting each word into its signature (a tuple representing letter 
     counts for each of the 26 lowercase English letters), we can group words 
     that are anagrams.
   - A **dictionary** is used to store these character signatures as keys and lists 
     of words as values.

2. **Detailed Steps**:
   - For each word in the input list:
     1. Initialize an array of size 26 (for each letter of the alphabet).
     2. Count how many times each letter appears in the word.
     3. Convert this count array into a tuple and use it as a key in a dictionary.
     4. Group words with the same signature in the dictionary.
   - Finally, return the values of the dictionary as a list of lists, where each 
     sublist contains words that are anagrams of each other.

---

### Time Complexity

- **O(n*m)**: where `n` is the number of words in the input list, and `m` is 
  the maximum length of a word. For each word, we create a character frequency 
  array in **O(m)** time, and since there are `n` words, the overall time complexity 
  is **O(n*m)**.

### Space Complexity

- **O(n)**: Although we create a character frequency array of size 26 for each word, 
  these arrays are stored as tuples in a dictionary. Thus, the space complexity is 
  **O(n)**, where `n` is the number of words, as each word contributes one key 
  to the dictionary.

"""

from typing import List
from collections import defaultdict

class Solution:
    '''
    n -> no.of words in the ‘strs’ input
    m -> max. size of word among all the words in the ‘strs’ input
    Time : O(n * m)
    Space: O(n*26) => since each word will create a ‘shape’ either tuple/string of size 26
           Big.O => O(n)
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Groups a list of strings into anagrams.

        Args:
        strs (List[str]): A list of strings.

        Returns:
        List[List[str]]: A list of lists, where each sublist contains anagrams.
        """
        # Dictionary to group words by their "character frequency signature"
        anagrams_map = defaultdict(list)

        for word in strs:
            # Create a tuple representing the character frequency of the word
            char_count = [0] * 26  # Array to store the count of each letter

            for char in word:
                char_count[ord(char) - ord('a')] += 1
            
            # Convert the word into a char_count shape, that is hashable
            # shape = '-'.join(map(str, char_count))    # shape of a string
            shape = tuple(char_count)                   # shape of a tuple

            # Use the char_count shape as a unique key for anagram groups
            anagrams_map[shape].append(word)

        # Return all grouped anagrams
        return list(anagrams_map.values())


