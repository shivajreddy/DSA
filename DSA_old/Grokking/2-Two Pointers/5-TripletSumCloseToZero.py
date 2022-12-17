import math

"""
Given an array of unsorted numbers and a target number, find a triplet in the array 
whose sum is as close to the target number as possible, return the sum of the triplet.
If there are more than one such triplet, return the sum of the triplet with the smallest sum

Input: [-2, 0, 1, 2], target=2
Output: 1
Explanation: The triplet [-2, 1, 2] has the closest sum to the target.

Input: [-3, -1, 1, 2], target=1
Output: 0
Explanation: The triplet [-3, 1, 2] has the closest sum to the target.

Input: [1, 0, 1, 1], target=100
Output: 3
Explanation: The triplet [1, 1, 1] has the closest sum to the target.
"""


def save_triple_sum_close_to_zero(arr, target):
    arr.sort()
    result = math.inf

    for i, num in enumerate(arr):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr) - 1
        while left < right:
            total_sum = num + arr[left] + arr[right]
            diff = target - total_sum
            if diff == 0:
                return target
            elif diff < 0:
                right -= 1
            else:
                left += 1
                result = min(result, diff)
    print(target - result)
    return target - result


def triple_sum_close_to_zero(arr, target):

    arr.sort()
    distance = math.inf

    for i, num in enumerate(arr):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr) - 1
        while left < right:
            total_sum = num + arr[left] + arr[right]
            curr_distance = target - total_sum
            if curr_distance == 0:
                return target
            elif curr_distance < 0:
                right -= 1      # this means total_sum > target, so reduce the sum => r -= 1
            else:
                left += 1       # total_sum < target, so increase sum => l += 1
                distance = min(distance, curr_distance)
    result = target - distance
    print(result)
    return result


triple_sum_close_to_zero([-2, 0, 1, 2], 2)  #1
triple_sum_close_to_zero([-3, -1, 1, 2], 1) #0
triple_sum_close_to_zero([1, 0, 1, 1], 100) #3
