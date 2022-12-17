def minWindow(s, t):
  hash= {}
  for c in t:
    if c not in hash:
      hash[c] = 0
    hash[c] += 1
  
  start = 0
  matched = 0
  sub_start = 0
  size = len(s)+1
  
  for end in range(len(s)):
    item = s[end]
    if item in hash:
      hash[item] -= 1
      if hash[item] >= 0:
        matched += 1
    while matched == len(t):
      if size > end-start+1:
        size = end-start+1
        sub_start = start
      first = s[start]
      if first in hash:
        if hash[first] == 0:
          matched -= 1
        hash[first] += 1
      start += 1
  
  if size > len(s):
    return ""
  return s[sub_start:sub_start+size]
