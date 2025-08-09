"""
QuickSort.py
"""

"""
Quick Sort
Stable/unstable sorting
Time: O()
Space: O()

"""


def quick_sort(array: list[int]) -> None:
    sort(array, 0, len(array) - 1)


def sort(array, low, high):
    print("after partition")
    print(array)
    if low >= high:
        return
    partition_idx = find_partition(array, low, high)
    sort(array, low, partition_idx - 1)
    sort(array, partition_idx + 1, high)


def find_partition(array, low, high):
    pivot = array[low]
    i, j = low + 1, high

    while True:

        # 'i' goes from left to right, to find element > pivot
        while array[i] <= pivot and i < high:
            i += 1
            # if i == high:
            #     break

        # 'j' goes from right to left, to find element <= pivot
        while array[j] > pivot and j > low:
            j -= 1
            # if j == low:
            #     break

        if i >= j:
            break

        # swap the elements
        array[i], array[j] = array[j], array[i]

    # swap pivot with j
    array[low], array[j] = array[j], array[low]

    return j


# arr = [18, 0, 18, -1, -5, 10, 2, 1]
arr = [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]
quick_sort(arr)
print(arr)
