
#! 1763. Longest Nice Substring

"""
A string s is nice if, for every letter of the alphabet that s contains, it appears both in uppercase and lowercase. For example, "abABB" is nice because 'A' and 'a' appear, and 'B' and 'b' appear. However, "abA" is not because 'b' appears, but 'B' does not.

Given a string s, return the longest substring of s that is nice. If there are multiple, return the substring of the earliest occurrence. If there are none, return an empty string.
"""

def longestNiceSubstring(s):
  lower = {}
  upper = {}
  for char in s:
    if char.islower():
      if char not in lower:
        lower[char] = 0
      lower[char] += 1
    else:
      char = char.lower()
      if char not in upper:
        upper[char] = 0
      upper[char] += 1

  start = 0
  result = 0
  final = "!"
  hashmap = {}
  for end in range(len(s)):
    item = s[end]
    item = item.lower()

    if item not in hashmap:
      hashmap[item] = 0
    hashmap[item] += 1

    if item in lower and item in upper:
      print(hashmap)
      if 1 not in list(hashmap.values()):
        if end-start+1 > result:
          result = end-start+1
          final = s[start:end+1]
    else:
      start = end
  return final

print(longestNiceSubstring("YazaAay")) # "aAa"
print(longestNiceSubstring("Bb")) # "Bb"
print(longestNiceSubstring("Bab")) # ""
