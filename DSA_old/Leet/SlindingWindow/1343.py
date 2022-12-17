
#! 1343. Number of Sub-arrays of Size K and Average Greater than or Equal to Threshold

def numOfSubarrays(arr, k, threshold):

  start = 0
  total = 0
  result = 0

  for end in range(len(arr)):
    total += arr[end]

    if end >= k-1:
      avg = total/k
      if avg >= threshold:
        # print(arr[start:end+1], avg)
        result += 1
      total -= arr[start]
      start += 1

    
  return result

print(numOfSubarrays([2,2,2,2,5,5,5,8], 3, 4)) #3
print(numOfSubarrays([11,13,17,23,29,31,7,5,2,3], 3, 5)) #6