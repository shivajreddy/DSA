""" 
Given a string s and a dictionary of strings wordDict, add spaces in s to
construct a sentence where each word is a valid dictionary word.
Return all such possible sentences in any order.

Note that the same word in the dictionary may be reused multiple times in the segmentation.

Input: s = "catsanddog", wordDict = ["cat","cats","and","sand","dog"]
Output: ["cats and dog","cat sand dog"]

Input: s = "pineapplepenapple", wordDict = ["apple","pen","applepen","pine","pineapple"]
Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
Explanation: Note that you are allowed to reuse a dictionary word.

Input: s = "catsandog", wordDict = ["cats","dog","sand","and","cat"]
Output: []

"""

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        def explore_paths(start: int, words: List[str]):
            # Base case: Reached the end of the string
            if start == len(s):
                sentence = " ".join(words)
                res.append(sentence)
                return

            # Explore all potential word endings
            for end in range(start + 1, len(s) + 1):
                if s[start:end] in d:
                    words.append(s[start:end])
                    explore_paths(
                        end, words
                    )  # Continue exploring the next part of the string
                    words.pop()  # Backtrack to explore other possibilities

        # Initialize
        d = set(wordDict)
        res = []

        # Start exploration from index 0 with an empty path
        explore_paths(0, [])

        print(res)
        return res


sol = Solution()
assert sol.wordBreak("catsanddog", ["cat", "cats", "and", "sand", "dog"]) == [
    "cat sand dog",
    "cats and dog",
]
