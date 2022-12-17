def maximum_unique_subarray(arr):

  start = 0
  hashmap = {}

  total = 0
  win_sum = 0

  for end in range(len(arr)):
    curr = arr[end]
    win_sum += curr

    if curr in hashmap:
      prev_start = start
      start = max( start, hashmap[curr]+1 )
      win_sum -= sum( arr[prev_start:start] )
    
    hashmap[curr] = end

    total = max( total, win_sum)
  
  return total

nums = [4,2,4,5,6]  #17
print(maximum_unique_subarray(nums))