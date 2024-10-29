
'''
s = word
["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]

s = internationalization 
abbr = i12iz4n
Return true

s = apple
abbr = a2e
Return false

'''

class Solution:
    def valid_word_abbreviation(self, word: str, abbr: str) -> bool:
        i = 0
        j = 0

        while j < len(abbr):

            if abbr[j].isnumeric():
                curr = 0
                while j< len(abbr) and abbr[j].isnumeric():
                    curr = (curr * 10) + int(abbr[j])
                    if curr == 0: return False
                    j += 1

                i += curr
                if i > len(word):
                    return False

            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1

        return i == len(word) and j == len(abbr)



sol = Solution()
print(sol.valid_word_abbreviation("word", "word"))
print(sol.valid_word_abbreviation("word", "1ord"))
print(sol.valid_word_abbreviation("word", "w2d"))
print(sol.valid_word_abbreviation("word", "3d"))
print(sol.valid_word_abbreviation("word", "4"))
print(sol.valid_word_abbreviation("internationalization", "i12iz4n"))

print(sol.valid_word_abbreviation("a", "01"))
