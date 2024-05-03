

#! 1984. Minimum Difference Between Highest and Lowest of K Scores

"""
You are given a 0-indexed integer array nums, where nums[i] represents the score of the ith student. You are also given an integer k.

Pick the scores of any k students from the array so that the difference between the highest and the lowest of the k scores is minimized.

Return the minimum possible difference.
"""

def minimumDifference(nums, k):
  
  start = 0
  total = 0
  big = float('-inf')
  small = float('inf')
  result = float('inf')
  for end in range(len(nums)):
    item = nums[end]
    
    # checking for the least difference
    big = max(big, item)
    small = min(small, item)
    if start != end and nums[start] - item >= 0:
      diff = nums[start] - item
      result = min(result, diff)
    print(f'big={big}, small={small}, result={result}')
    
    # Hit the window size.
    # if end >= k-1:
    #   first = nums[start]
    #   total -= first 
    #   start += 1
  
  if result == float('inf'):
    return 0
  return result


print(minimumDifference([90], 1))  # 0
print(minimumDifference([9,4,1,7], 2))    # 2
# print(minimumDifference()) 
