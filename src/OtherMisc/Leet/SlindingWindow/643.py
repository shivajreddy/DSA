
#! 643. Maximum Average Subarray I

"""
You are given an integer array nums consisting of n elements, and an integer k.
Find a contiguous subarray whose length is equal to k that has the maximum average value and return this value. Any answer with a calculation error less than 10-5 will be accepted.
"""

def findMaxAverage(nums, k):

  arr = nums
  start = 0
  total = 0
  max_avg = float('-inf')

  for end in range(len(arr)):
    total += arr[end]

    if end-start+1 == k:
      avg = total/k
      max_avg = max(max_avg,avg)

      total -= arr[start]

      start += 1
    

  return max_avg

print(findMaxAverage([4,0,4,3,3],5)) #
print(findMaxAverage([1,12,-5,-6,50,3],4)) # 12.7500
print(findMaxAverage([4,0,4,3,3],5)) #
