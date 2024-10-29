from typing import DefaultDict

class Solution:
    """
    Create a hashmap, with key as the char-count and value as all the words of this char-count
    key: string representation of count from a..z
    Time: O(n)
    Space: O(n)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        '''
        Create an ordered character-count representation, from a..z
        Linear Time, constant space
        '''
        def create_key(word: str) -> str:
            letter_count = [0] * 26
            for char in word:
                letter_count[ord(char) - ord('a')] += 1
            return '-'.join(map(str, letter_count))     # or a tuple

        shape_words_map = DefaultDict(list)

        for word in strs:
            key = create_key(word)
            shape_words_map[key].append(word)

        return list(shape_words_map.values())

class Solution:
    """
    Create a hashmap, with key as the char-count and value as all the words of this char-count
    key: sorted word
    Time: O(n.logn)
    Space: O(n)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        shape_words_map = DefaultDict(list)

        for word in strs:
            key = str(sorted(word))
            shape_words_map[key].append(word)

        return list(shape_words_map.values())

