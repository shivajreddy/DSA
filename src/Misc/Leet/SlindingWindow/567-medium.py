
#! 567. Permutation in String

"""
Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.
"""


def checkInclusion(s1, s2):
  # pattern being the target string, we should compare against 
  # arr is the string we will iterate through, and keep track of char frequency
  pattern = s1
  arr = s2
  
  char_frequency = {}
  
  for c in pattern:
    if c not in char_frequency:
      char_frequency[c] = 0
    char_frequency[c] += 1
  
  start = 0
  matched = 0
  
  for end in range(len(arr)):
    item = arr[end] # item represents the current item in the iteration
    if item in char_frequency:
      char_frequency[item] -= 1
      if char_frequency[item] == 0:
        matched += 1  # Found 1 char with all repetetions
    if matched == len(char_frequency):
      return True # Found all char's with all repetetions
    
    if end >= len(pattern)-1: # shrink the window by 1, when you hit the size of s1
      first = arr[start]
      if first in char_frequency:
        if char_frequency[first] == 0:
          matched -= 1
        char_frequency[first] += 1
      start += 1
  
  return False
    

print(checkInclusion("ab", "eidbaooo")) # True
print(checkInclusion("ab", "eidboaoo")) # False