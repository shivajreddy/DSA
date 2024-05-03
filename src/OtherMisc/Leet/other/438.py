
#! 438. Find All Anagrams in a String

"""
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
"""
pattern = "abac"
pattern = {'a':2, 'b':1, 'c':1} 


def findAnagrams(s, p):
    
    arr = [*s]        
    pattern = {}
    for c in p:
      if c in pattern.keys():
        pattern[c] += 1
      else:
        pattern[c] = 1
    
    start = 0
    hashmap = {}
    result = []
    
    for end in range(len(arr)):
      item = arr[end]
      if item in hashmap.keys():
        hashmap[item] += 1
      else:
        hashmap[item] = 1
      
      if item not in pattern.keys():
        start = end + 1
        hashmap ={}
   
      else:
        while hashmap[item] > pattern[item]:
          first = arr[start]
          hashmap[first] -= 1
          if hashmap[first] == 0:
            del hashmap[first]
          start += 1

      if hashmap == pattern:
        result.append(start)
    
    return result
