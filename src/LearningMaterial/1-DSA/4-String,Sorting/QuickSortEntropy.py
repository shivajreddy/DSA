def quick_sort(arr, lo, hi):
    if lo >= hi: return

    lt, gt = lo, hi
    i = lo + 1
    pivot = arr[lo]

    while i <= gt:
        curr = arr[i]
        if curr < pivot:
            arr[lt], arr[i] = arr[i], arr[lt]
            i += 1
            lt += 1
        elif curr > pivot:
            arr[gt], arr[i] = arr[i], arr[gt]
            gt -= 1
        else:
            i += 1

    print("now arr=", arr)
    quick_sort(arr, lo, lt - 1)
    quick_sort(arr, gt + 1, hi)


def sort(arr):
    quick_sort(arr, 0, len(arr) - 1)
    return arr


arr = [3, 8, 2, 15, 27, 21, 17, 10, 16, 7, 24, 0, 4, 6, 18, 5]

sort(arr)
print(arr)
