
"""
Triplets with Smaller Sum
Given an array arr of unsorted numbers and a target sum, count all triplets in it 
such that arr[i] + arr[j] + arr[k] < target where i, j, and k are three 
different indices. Write a function to return the count of such triplets.

Input: [-1, 0, 2, 3], target=3 
Output: 2
Explanation: There are two triplets whose sum is less than the target: [-1, 0, 3], [-1, 0, 2]

Input: [-1, 4, 2, 1, 3], target=5 
Output: 4
Explanation: There are four triplets whose sum is less than the target: 
   [-1, 1, 4], [-1, 1, 3], [-1, 1, 2], [-1, 2, 3]
"""


def triplet_with_smaller_sum(arr, target):
    count = 0

    arr.sort()

    for i, num in enumerate(arr):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr) - 1
        while left < right:
            trip_sum = num + arr[left] + arr[right]
            if trip_sum < target:
                count += (right - left)
                left += 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1
            else:
                right -= 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1
    print(count)
    return count


triplet_with_smaller_sum([-1, 0, 2, 3], 3)
triplet_with_smaller_sum([-1, 4, 2, 1, 3], 5)


def triplet_with_smaller_sum_v2(arr, target):
    arr.sort()
    result = []
    count = 0
    for i, num in enumerate(arr):
        if i > 0 and arr[i] == arr[i-1]:
            continue

        left = i + 1
        right = len(arr)-1
        while left < right:
            total_sum = num + arr[left] + arr[right]
            if total_sum < target:
                while left < right and arr[left] != arr[left-1]:
                    result.append([num, arr[left], arr[right]])
                    count += 1
                    left += 1
            else:
                right -= 1
                while left < right and arr[right] == arr[right+1]:
                    right -= 1

    print(count, result)
    return result


triplet_with_smaller_sum_v2([-1, 0, 2, 3], 3)
triplet_with_smaller_sum_v2([-1, 4, 2, 1, 3], 5)
