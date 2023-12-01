# https://leetcode.com/problems/ransom-note/
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        target_map = {}
        for char in ransomNote:
            target_map[char] = target_map.get(char, 0) + 1

        matched = 0
        total = len(target_map)

        for char in magazine:
            if char in target_map:
                target_map[char] -= 1
                if target_map[char] == 0:
                    matched += 1
                    del (target_map[char])
                    if matched == total:
                        return True
        return False
