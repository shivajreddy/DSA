"""
Insertion sort
"""

"""
Elementary Sort

Stable sorting
Time: O(n^2)
Space: O(1)
"""


class InsertionSort:

    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def sort(array):

        for i in range(1, len(array)):

            j = i - 1
            while j >= 0 and array[j] > array[j + 1]:
                array[j], array[j + 1] = arr[j + 1], array[j]
                j -= 1

        return array


arr = [8, -5, 10, 2, 1]
InsertionSort.sort(arr)
print(arr)
