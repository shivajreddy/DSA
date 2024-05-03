
"""
Square a Sorted Array
Given a sorted array, create a new array containing squares of all the numbers of the input array in the sorted order.

Input: [-2, -1, 0, 2, 3]
Output: [0, 1, 4, 4, 9]

Input: [-3, -1, 0, 1, 2]
Output: [0, 1, 1, 4, 9]
"""


def make_squares(arr):
    left = 0
    right = len(arr)-1

    result = [0 for _ in range(len(arr))]       # create an empty array, so that you can keep prepending items to the list
    high_idx = right

    while left < right:

        left_square = arr[left] * arr[left]
        right_square = arr[right] * arr[right]

        if left_square < right_square:
            result[high_idx] = right_square
            right -= 1
        else:           # This appends the left_square even when left_square == right_square, then next iteration right_square gets appended
            result[high_idx] = left_square
            left += 1
        high_idx -= 1

    print(result)

    return result


make_squares([-2, -1, 0, 2, 3])
make_squares([-3, -1, 0, 1, 2])
