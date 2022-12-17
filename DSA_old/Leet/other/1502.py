# 1502 Can Make Arithmetic Progression From sequence

arr = [3,5,1]
arr = [1,2,3,4]
arr = [1,100]
arr.sort()

middle_idx = int(len(arr)/2)
middle = arr[middle_idx]
left = sum(arr[:middle_idx])
right = sum(arr[middle_idx + 1:])
print('if middle =  |', middle)
print('left sum', middle-left)
print('right sum', right-middle)



if middle-left == right-middle:
    print('YES IT IS AP')
else:
    middle = arr[middle_idx-1]
    print('else middle = ', middle)
    if middle-left == right-middle:
        print('ues AP')
    else:
        print('No not DP')
# print(left,right)

# print(middle, arr[middle])
