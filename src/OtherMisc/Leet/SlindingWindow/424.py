arr = "aababba"
k = 1

hashmap = {}

# start, end = 0, 0

# result = 0

# while end < len(arr):

#   curr = arr[end]

#   if curr not in hashmap:
#     hashmap[curr] = 0
#   hashmap[curr] += 1

#   # check if window is valid
#   max_char_count = max(hashmap.values())
#   if end-start+1 - max_char_count <= k:
#     result = max(result, end-start+1)
  
#   else:
#     max_char_count = max(hashmap.values())
#     while end-start+1 - max_char_count > k:

#       first = arr[start]
#       hashmap[first] -= 1
      
#       start += 1

#   end += 1

# print(result)

start = 0
result = 0

for end in range(len(arr)):

  curr = arr[end]

  hashmap[curr] = hashmap.get(curr,0) + 1

  while (end-start+1 ) - (max(hashmap.values())) > k:

    first = arr[start]
    hashmap[first] -= 1
    start += 1
  
  result = max(result, end-start+1)
  
  return result


