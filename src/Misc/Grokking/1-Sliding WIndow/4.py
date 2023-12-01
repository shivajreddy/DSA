
#! Given a string, find the length of the longest substring in it with no more than K distinct characters.

s = "araaci"
k = 2


arr = [*s]
result = 0
start = 0
hashmap = {}

for end in range(len(arr)):

    item = arr[end]

    if item not in hashmap.keys():
        hashmap[item] = 0
    hashmap[item] += 1

    while len(hashmap) > k:
      first = arr[start]
      hashmap[first] -= 1
      if hashmap[first] == 0:
        del hashmap[first]
      start += 1


    result = max(result, end-start+1)


    # result = max(result, end-start+1)

print(result)