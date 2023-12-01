def find_permutation(str, pattern):
  arr = [*str]
  pattern_hash = {}
  for c in pattern:
    if c in pattern_hash.keys():
      pattern_hash[c] += 1
    else:
      pattern_hash[c] = 1
  
  start = 0
  hashmap = {}

  for end in range(len(arr)):
    item = arr[end]
    if item in hashmap.keys():
      hashmap[item] += 1
    else:
      hashmap[item] = 1
    
    if item not in pattern_hash.keys():
      start = end + 1 
      hashmap = {}
    
    else:
      count = 0
      for i in hashmap.keys():
        if hashmap[i] >= pattern_hash[i]:
          count += 1
      if count == len(list(pattern_hash.keys())):
        return True

  return False

print(find_permutation('oidbcaf', 'abc'))
print(find_permutation('odicf', 'dc'))
print(find_permutation('bcdxabcdy', 'bcdyabcdx'))
print(find_permutation('aaacb', 'abc'))
