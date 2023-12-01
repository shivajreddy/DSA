
#! Problem 3 - Smallest window containing substring (hard)

"""
Given a string and a pattern, find the smallest substring in the given string which has all the character occurrences of the given pattern.
"""

def find_substring(str1, pattern):

  arr = [*str1]
  pat = {}
  # pat_start = pattern[0]
  # pat_end = pattern[-1]
  hashmap = {}
  hashmap_count = 0
  start = 0
  # useless = 0
  # result = len(arr)

  for c in pattern:
    if c in pat.keys():
      pat[c] += 1
    else:
      pat[c] = 1
  
  pat_count = len(pat.keys())

  for end in range(len(arr)):
    item = arr[end]
    if item in hashmap.keys():
      hashmap[item] += 1
    else:
      hashmap[item] = 1
  
  if item not in pat.keys():
    # start = end+1
    hashmap.pop(item)

  elif hashmap[item] >= pat[item]:
    hashmap_count += 1

    if hashmap_count == pat_count:
      print(str1[start:end+1])
      # return str1[start:end+1]
  print(start, end, hashmap)

  
  # start_val = None
  # end_val = None
  # for i in range(len(arr)):
  #   item = arr[i]
  #   if item in hashmap.keys():
  #     hashmap[item] += 1
  #   else:
  #     hashmap[item] = 1
  #   if item not in pat.keys():
  #     useless += 1
  #     hashmap.pop(item)
  #   if start_val == None and item == pat_start:
  #     start_val = i
  #   if item == pat_end:
  #     end_val = i 

  # if len(hashmap.keys()) < len(pat.keys()):
  #   print("returning empty string")


  # # print(hashmap, pattern, arr[start_val:end_val+1])
  # start = start_val
  # end = end_val

  # while start > end:
  #   first = arr[start]
  #   if hashmap[first] > pat[first]:
  #     hashmap[first] -= 1
  #     if hashmap[first] == 0:
  #       del hashmap[first]


  #   if len(hashmap.keys()) == len(pat.keys()):
  #     result = min(result, end-start+1)
  
  # print("final result", result, )





find_substring("aabdec", "abc")
find_substring("aabdec", "abac")
find_substring("abdbca", "abc")
find_substring("adcad", "abc")
