
def threesum(arr):

  arr.sort()
  result = []
  
  def helper(left, right, target):
    while left < right:
      curr_sum = arr[left] + arr[right]
      if curr_sum == target:
        result.append( [-target, arr[left], arr[right]] )
        left += 1
        right -= 1

        while left<right and arr[left]==arr[left-1]:
          left += 1
        while left<right and arr[right]==arr[right+1]:
          right -= 1
      
      elif curr_sum > target:
        right -= 1
      else:
        left += 1

  for i in range(len(arr)):

    if arr[i] == arr[i-1]:
      continue
    helper( left=i+1, right=len(arr)-1, target=-arr[i] )
  
  return result
