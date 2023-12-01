
#! Problem 2 - String Anagrams (hard)

"""
Given a string and a pattern, find all anagrams of the pattern in the given string.
Every anagram is a permutation of a string. As we know, when we are not allowed to repeat characters while finding permutations of a string, we get N!N! permutations (or anagrams) of a string having NN characters. For example, here are the six anagrams of the string “abc”:
"""

def find_string_anagrams(str, pattern):
  result_indexes = []
  arr = [*str]
  pat = {}
  for c in pattern:
    if c in pat.keys():
      pat[c] += 1
    else:
      pat[c] = 1
  
  start = 0
  hashmap = {}

  for end in range(len(arr)):
    item = arr[end]
    if item in hashmap.keys():
      hashmap[item] += 1
    else:
      hashmap[item] = 1
    
    if item not in pat.keys():
      hashmap = {}
      start = end+1
    
    else:
      while hashmap[item] > pat[item]:
        first = arr[start]
        hashmap[first] -= 1
        if hashmap[first] == 0:
          del hashmap[first]
        start += 1

    if hashmap == pat:
      return [i for i in range(start,end+1)] 

  return -1


print(find_string_anagrams("ppqp", "pq")) # [1,2]
print(find_string_anagrams("abbcabc", "abc")) #[2,3,4]