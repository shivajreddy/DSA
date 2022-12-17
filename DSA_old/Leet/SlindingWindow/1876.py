
#! 1876. Substrings of Size Three with Distinct Characters

"""
A string is good if there are no repeated characters.
Given a string s​​​​​, return the number of good substrings of length three in s​​​​​​.
Note that if there are multiple occurrences of the same substring, every occurrence should be counted.
A substring is a contiguous sequence of characters in a string.

"""

def countGoodSubstrings(s):
  arr = [*s]
  start = 0
  hashmap = {}
  count = 0

  for end in range(len(arr)):
    item = arr[end]
    if item not in hashmap:
      hashmap[item] = 0
    hashmap[item] += 1

    if end-start+1 == 3:

      if len(hashmap)==3:
        count += 1
      
      first = arr[start]
      hashmap[first] -= 1
      if hashmap[first] == 0:
        del hashmap[first]
      start += 1
  
  return count


print(countGoodSubstrings("xyzzaz")) # 1
print(countGoodSubstrings("aababcabc")) # 4
