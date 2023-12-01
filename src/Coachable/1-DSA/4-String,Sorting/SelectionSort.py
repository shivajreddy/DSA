"""
Selection Sort
"""

"""
Elementary Sort

Stable sorting
Time: O(n^2)
Space: O(1)
"""


class SelectionSort:

    @staticmethod
    def __init__(self):
        pass

    @staticmethod
    def sort(array):
        i, n = 1, len(array)

        for i in range(n - 1):
            curr_smallest, curr_smallest_idx = array[i], i
            for j in range(i + 1, n):
                if array[j] < curr_smallest:
                    curr_smallest, curr_smallest_idx = array[j], j
            array[i], array[curr_smallest_idx] = array[curr_smallest_idx], array[i]

        return array


arr = [8, -5, 10, 2, 1]
SelectionSort.sort(arr)
print(arr)
