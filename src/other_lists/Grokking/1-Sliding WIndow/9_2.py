
#! Problem 2 - String Anagrams (hard)

"""
Given a string and a pattern, find all anagrams of the pattern in the given string.
Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:
"""

def find_string_anagrams(arr, pattern):
  start = 0
  matched = 0
  pat = {}

  for chr in pattern:
    if chr not in pat:
      pat[chr] = 0
    pat[chr] += 1

  result_indices = []
  # Our goal is to match all the characters from the 'char_frequency' with the current window
  # try to extend the range [window_start, window_end]
  for end in range(len(arr)):
    item = arr[end]
    if item in pat:
      # Decrement the frequency of matched character
      pat[item] -= 1
      if pat[item] == 0:
        matched += 1

    if matched == len(pat):  # Have we found an anagram?
      result_indices.append(start)

    # Shrink the sliding window
    if end >= len(pattern) - 1:
      first = arr[start]
      start += 1
      if first in pat:
        if pat[first] == 0:
          matched -= 1  # Before putting the character back, decrement the matched count
        pat[first] += 1  # Put the character back

  return result_indices



print(find_string_anagrams("ppqp", "pq")) # [1,2]
print(find_string_anagrams("abbcabc", "abc")) #[2,3,4]