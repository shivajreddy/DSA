class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # Dict to hold the pattern as key, and value as a list of words of this pattern
        # so using defaultdict there will be no keyError, bcz if there is one, it uses the
        # default value that is given, in this case its a list
        # so, for hm[pattern] if the pattern is not yet there in hm, we usually get keyerror,
        # but now hm[pattern] is an empty list, cuz we gave list in defaultdict(list)
        hm = defaultdict(list)

        for word in strs:
            # create a pattern
            pattern = [0] * 26  # [0,0,0,0...0,0,0] pattern of frequency for [a,b,c,d...x,y,z]

            for char in word:
                # ord(char) - ord('a') gives the index of char.
                # i.e., for a it will be 0, b is 1, z is 25
                pattern[ord(char) - ord('a')] += 1

            # 1.now for this pattern as key, append the word to value which is a list
            # 2. since you can't have mutable types as keys in dict in python,
            # we cant use list as the key in the dict, so we use tuple as the key,
            # since tuples are immutable, we can use them as keys for dicts
            hm[tuple(pattern)].append(word)

        return hm.values()

""" Notes:

When dealing with freq of alphabets:
1.create pattern with an empty list: l = [0] * 26
2. To deal with KeyError in dict, use hm = defaultdict(list) #where default value is list,
    default value can be anything, a 'list', 0, some string...
3. Dicts keys cant be list, but can use tuple
"""