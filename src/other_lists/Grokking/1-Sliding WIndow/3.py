import math
arr = [2, 1, 5, 2, 3, 2]
s = 7 

start = 0
end = 0
small = math.inf
total = 0


for end in range(len(arr)):

    total += arr[end]

    while total >= s:

        small = min(small, end-start+1)

        total -= arr[start]
        start += 1

if small == math.inf:
    return 0
return small

