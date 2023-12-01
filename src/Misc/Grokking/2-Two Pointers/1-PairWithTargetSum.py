"""
 Pair with target Sum
Input: [1, 2, 3, 4, 6]
target=6
"""


def pair_with_target_sum(arr, target_sum):
    start = 0
    end = len(arr)-1

    while start < end:
        curr_sum = arr[start] + arr[end]
        if curr_sum == target_sum:
            return [start, end]
        if curr_sum < target_sum:
            start += 1
        else:
            end -= 1
    return [-1, -1]



print(pair_with_target_sum([1, 2, 3, 4, 6], 6))
print(pair_with_target_sum([2, 5, 9, 11], 11))
