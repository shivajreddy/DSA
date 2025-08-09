from typing import List

'''
[ leet code ]
leetcode

[ apple pen ]
applepenapple

[abcd b bc bcd d de bcde]
abcde

                abcde_
            abcde     _
           a     bcde
                b    cde
                    c   de
                       d  e

                    fn(abcde_)
            fn(abcde)        fn(_)
        fn(a)       fn(bcde)
                fn(b)      fn(cde)
                       fn(c)     fn(de)
                             fn(d)    fn(e)

fn(abcde_)
fn(_) => True
fn(abcde) => fn(a) and fn(bcde)

 [ leet code ]
   leetcode
i->01234567

fn(i):
    # does any word in dictionary match with s[i:_]
    for word in dictionary:
        if `s[i:]` starts with word:
            if fn(i+len(word)):
                return True
    return False

'''

class Solution:

    # """ Bottom-Up
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        N = len(s)
        memo = [False] * (N + 1)
        memo[0] = True

        '''
           0 1 2 3 4 5 6 7 8
         [ T F F F F F F F F ]
                   i
             -------
        i goes from idx-1 until last, at each stage we ask 3 things
        1: Has i travelled atleast the length of the word
        2: was state in memo True, before the current word
        3: say current word is of length M, then is s[i-M:i] == word

        '''

        memo = [False] * (len(s) + 1)
        memo[0] = True
        for i in range(1, len(s) + 1):

            for word in wordDict:
                M = len(word)
                if i >= M and memo[i-M] and s[i-M:i] == word:
                    memo[i] = True
                    break

        return memo[-1]

    # """

    """ Top-Down with Memoization
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        cache = {len(s): True}
        def helper(i: int) -> bool:
            if i >= len(s): return True
            if i in cache: return cache[i]

            for word in wordDict:
                if s.startswith(word, i):
                    if helper(i+len(word)):
                        cache[i] = True
                        return True
            cache[i] = False
            return False

        res = helper(0)
        return res
    # """


s = Solution()
assert(True == s.wordBreak("leetcode", ["leet", "code"]))
assert(True == s.wordBreak("applepenapple", ["apple", "pen"]))
assert(False == s.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]))
assert(False == s.wordBreak("a", ["aa","aaa","aaaa","aaaaa","aaaaaa"]))

