from collections import deque


def pivotArray(nums, pivot):

    leftList = deque()
    midList = deque()
    rightList = deque()

    for i, num in enumerate(nums):
        if num < pivot:
            leftList.append(num)
        elif num == pivot:
            midList.append(num)
        else:
            rightList.append(num)

    idx = 0
    while len(leftList) > 0:
        nums[idx] = leftList.popleft()
        idx += 1
    while len(midList) > 0:
        nums[idx] = midList.popleft()
        idx += 1
    while len(rightList) > 0:
        nums[idx] = rightList.popleft()
        idx += 1

    print(nums)
    return nums


pivotArray([9, 12, 5, 10, 14, 3, 10], 10)
pivotArray([-3, 4, 3, 2], 2)


def pivotArrayInPlace(nums, pivot):

  pivot_idx = 0
  for i, num in enumerate(nums):
    if num == pivot:
      pivot_idx = i
      break
  

  second = 0
  for i, num in enumerate(nums):
    if num > pivot:
        second = i
    elif num < pivot:
      nums[second], nums[i] = nums[i], nums[second]
      second += 1
  nums[pivot_idx], nums[second] = nums[second], nums[pivot_idx]
  print(nums)


pivotArrayInPlace([9, 12, 5, 10, 14, 3, 10], 10)
pivotArrayInPlace([-3, 4, 3, 2], 2)
