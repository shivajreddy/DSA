
"""Given an array containing 0s and 1s, if you are allowed to 
replace no more than ‘k’ 0s with 1s, find the length of the longest 
contiguous subarray having all 1s."""

arr = [0, 1, 1, 0, 0, 0, 1, 1, 0, 1, 1]
k=2
# arr = [0, 1, 0, 0, 1, 1, 0, 1, 1, 0, 0, 1, 1]
# k = 3 

start = 0
hashmap = {0:0,1:0}
result = 0

for end in range(len(arr)):

    item = arr[end]
    if item == 0:
        hashmap[0] += 1
    else:
        hashmap[1] += 1

    if hashmap[0] > k:
        first = arr[start]
        hashmap[first] -= 1
        start += 1
    
    result = max(result, end-start+1)

# print(hashmap, hashmap[0], hashmap[1])
print(result)
