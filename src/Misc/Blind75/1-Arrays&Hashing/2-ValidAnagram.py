class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        if len(s) != len(t):
            return False

        hm_s = self.createFreq(s)
        hm_t = self.createFreq(t)

        if len(hm_s) != len(hm_t):
            return False

        for key in hm_s:
            if key not in hm_t:
                return False
            if hm_s[key] != hm_t[key]:
                return False

        return True

    def createFreq(self, word):
        hm = {}
        for char in word:
            hm[char] = hm.get(char, 0) + 1
        return hm


""" NOTE:

first check the lengths, cuz 2 anagrams must be of same length

you can skip the if condition for checking if the 'key' is in hm_t:
by using this

if hm_s[key] != hm_t.get(key,0):
    return False

cuz now you if a key is not in hm_t we are setting value to 0, and since all our values
in hm_s are always going to be >= 1

"""