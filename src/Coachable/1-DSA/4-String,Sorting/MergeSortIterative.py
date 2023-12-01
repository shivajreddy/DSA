"""
Merge Sort: Iterative
"""


def merge_sort(arr: list[int]) -> None:
    n = len(arr)
    p = 1

    while p <= n:
        for i in range(0, n, p):
            lo = i
            hi = i + p - 1
            mid = lo + (hi - lo) // 2
            merge(arr, lo, mid, hi)
        p *= 2

    if p // 2 < n:
        merge(arr, 0, p // 2, n - 1)


def merge(arr, lo, mid, hi):
    aux_arr = [num for num in arr]

    i, j, k = lo, mid + 1, lo

    while True:
        if aux_arr[i] <= aux_arr[j]:
            arr[i] = aux_arr[i]
            i += 1
        else:
            arr[j] = aux_arr[j]
            j += 1
        k += 1


arr = [8, 9, -7, 1, 0, 21, 17]
merge_sort(arr)
print(arr)
