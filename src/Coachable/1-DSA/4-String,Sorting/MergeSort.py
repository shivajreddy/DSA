"""
MergeSort.py
"""

"""
Merge Sort

Stable/unstable sorting
Time: O(n.log n)
Space: O(n) -> Extra space for auxiliary array
"""


def merge_sort(array: list[int]) -> None:
    aux_array = [0 for _ in range(len(array))]  # auxiliary array
    divide(array, 0, len(array) - 1, aux_array)


def divide(array: list[int], left, right, aux_array):
    # base condition
    if left >= right:
        return

    mid = left + (right - left) // 2
    divide(array, left, mid, aux_array)
    divide(array, mid + 1, right, aux_array)

    merge(array, left, mid, right, aux_array)


def merge(array, low, mid, high, aux_array):
    # copy items to aux-array
    for idx, num in enumerate(array):
        aux_array[idx] = num

    i, j = low, mid + 1

    for k in range(low, high + 1):
        if i > mid:
            array[k] = aux_array[j]
            j += 1
        elif j > high:
            array[k] = aux_array[i]
            i += 1
        elif is_less(aux_array[i], aux_array[j]):
            array[k] = aux_array[i]
            i += 1
        else:
            array[k] = aux_array[j]
            j += 1


def is_less(item1, item2):
    return item1 < item2


# arr = [8, -5, 10, 2, 1]
# arr = [-2, 3, -5]
arr = [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]
merge_sort(arr)
print(arr)
