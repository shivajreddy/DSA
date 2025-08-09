
"""
2. Remove Duplicates
Input: [2, 3, 3, 3, 6, 9, 9]
Output: 4
Explanation: The first four elements after removing the duplicates will be [2, 3, 6, 9].
"""


def remove_duplicates(arr):
    non_duplicate_pointer = 0
    hashmap = {}

    """
    # can use this while loop also, but add i += 1
    i = 0
    while i < len(arr):
        num = arr[i]
    """
    for i, num in enumerate(arr):
        if num not in hashmap:
            hashmap[num] = i
            arr[non_duplicate_pointer] = num
            non_duplicate_pointer += 1

        i += 1

    return non_duplicate_pointer


# print(remove_duplicates([2, 3, 3, 3, 6, 9, 9]))


"""
Similar Questions

1. Given an unsorted array of numbers and a target ‘key’, remove all instances of ‘key’ in-place and return the new length of the array.
Input: [3, 2, 3, 6, 3, 10, 9, 3], Key=3
Output: 4
Explanation: The first four elements after removing every 'Key' will be [2, 6, 10, 9].
"""


def remove_element(arr, key):
    non_target_pointer = 0

    for i, num in enumerate(arr):
        if num != key:
            arr[non_target_pointer] = num
            non_target_pointer += 1

    return non_target_pointer


# remove_element([3, 2, 3, 6, 3, 10, 9, 3], 3)
# remove_element([2, 11, 2, 2, 1], 2)
