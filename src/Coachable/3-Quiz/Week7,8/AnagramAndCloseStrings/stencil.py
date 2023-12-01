from __future__ import annotations
from typing import *

'''
Determine if these 2 strings are anagrams in O(n) runtime

You can assume that a,b are string with only letters.
You should ignore capitalization's.

For example,
check_anagram("inTegRal, "Triangle") -> True
'''


def check_anagram(a: str, b: str) -> bool:
    hm = {}
    for char in a:
        char = char.lower()
        hm[char] = hm.get(char, 0) + 1
    for char in b:
        char = char.lower()
        if char not in hm:
            return False
        hm[char] -= 1
        if hm[char] == 0: del hm[char]
    return False if hm else True


'''
Given 2 strings determine how many full and partial matches they have.

a = BEARS
b = BEAST
-> (3,1)

3 full matches because BEA
1 partial match since S is in the remaining part of the string but incorrect index.

a = BANANA
b = ORANGE
 -> (0, 2)
0 full matches and 2 partial matches for AN.

Returns as a tuple (full matches, partial_matches)
'''


def close_strings(a: str, b: str) -> tuple:
    full_match, half_match = 0, 0
    hm_a, hm_b = {}, {}  # space O(N)
    for char in a:  # O(N)
        hm_a[char] = hm_a.get(char, 0) + 1

    n = min(len(a), len(b))  # O(1)

    def remove_char(c):
        hm_a[c] -= 1
        if hm_a[c] == 0:
            del hm_a[c]

    for idx in range(n):
        if a[idx] == b[idx]:
            full_match += 1
            remove_char(a[idx])
            continue
        char = b[idx]
        if char in hm_a:
            half_match += 1
            remove_char(char)

    for idx in range(n, len(b)):
        char = b[idx]
        print(char)
        if char in hm_a:
            half_match += 1
            remove_char(char)

    return full_match, half_match
