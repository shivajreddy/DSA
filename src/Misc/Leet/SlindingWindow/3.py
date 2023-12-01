# s = "abcabcbb"
s = "bbbbb"
# s = "pwwkew"

# longest substring without repeating characters

def len_of_longest_unique_substring(s):
  hashmap = {}
  start = 0
  size = 0

  # for end in range(len(s)):
  #   curr = s[end]

  #   if curr not in hashmap:
  #     hashmap[curr] = 1
  #     size = max(size, end-start+1)

  #   else:
  #     start = end
  #     hashmap = {}
  #     hashmap[curr] = 1

  # return size

  for end in range(len(s)):
    curr = s[end]

    if curr in hashmap:
      start = max( start, hashmap[curr]+1 )

    hashmap[curr] = end

    size = max ( size, end-start+1 )
  
  return size

print(len_of_longest_unique_substring(s))


