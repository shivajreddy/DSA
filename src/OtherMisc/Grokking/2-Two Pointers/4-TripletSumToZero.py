
"""
Triplet Sum to Zero (medium)
 Given an array of unsorted numbers, find all unique triplets in that add up to zero.

 Input: [-3, 0, 1, 2, -1, 1, -2]
Output: [-3, 1, 2], [-2, 0, 2], [-2, 1, 1], [-1, 0, 1]
Explanation: There are four unique triplets whose sum is equal to zero.

Input: [-5, 2, -1, -2, 3]
Output: [[-5, 2, 3], [-2, -1, 3]]
Explanation: There are two unique triplets whose sum is equal to zero.


"""


def search_triplets(arr):
    result = []
    arr.sort()

    for i, num in enumerate(arr):
        if i > 0 and num == arr[i-1]:
            continue

        left = i + 1
        right = len(arr) - 1

        while left < right:
            total = num + arr[left] + arr[right]

            if total == 0:
                result.append([num, arr[left], arr[right]])
                left += 1
                while left < right and arr[left] == arr[left-1]:
                    left += 1

            if total < 0:
                left += 1
            else:
                right -= 1

    print(result)
    return result


search_triplets([-3, 0, 1, 2, -1, 1, -2])
search_triplets([-1, 0, 1, 2, -1, -4])
search_triplets([0, 0, 0, 0, 0, 0, 0])
search_triplets([1, 2, -2, -1])
