# https://leetcode.com/problems/valid-anagram/

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        s_map = {}
        for char in s:
            s_map[char] = s_map.get(char, 0) + 1

        t_map = {}
        for char in t:
            t_map[char] = t_map.get(char, 0) + 1

        for key in s_map.keys():
            if key not in t_map or s_map[key] != t_map[key]:
                return False

        return True
