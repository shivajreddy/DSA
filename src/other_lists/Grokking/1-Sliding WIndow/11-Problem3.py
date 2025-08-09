arr = [*"aabdec"]
pattern = "abc"

def find_substring(str1, pattern):
  hash = {}
  for c in pattern:
    if c not in hash:
      hash[c] = 0
    hash[c] += 1
  start = 0
  matched = 0
  sub_start = 0
  size = len(str1) + 1

  for end in range(len(str1)):
    item = str1[end]
    if item in hash:
      hash[item] -= 1
      if hash[item] >= 0:   #! >= 0 because there can be more chars than required
        matched += 1
    while matched == len(pattern):    #! if total matches == size of pattern
      if size > end-start+1:
        size = end-start+1
        sub_start = start
      first = str1[start]
      if first in hash:
        if hash[first] == 0:
          matched -= 1
        hash[first] += 1
      start += 1
  if size > len(str1):
    return ""
  return str1[sub_start:sub_start+size]

print(find_substring("aabdec", "abc")) # "abdec"
print(find_substring("aabdec", "abac")) # "aabdec"
print(find_substring("abdbca", "abc")) # "bca"
print(find_substring("adcad", "abc")) # ""