
#! 523. Continuous Subarray Sum (medium)

"""
Given an integer array nums and an integer k, return true if nums has a continuous subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.

An integer x is a multiple of k if there exists an integer n such that x = n * k. 0 is always a multiple of k."""


# nums = [23,2,4,6,7]
arr = [5,0,0,0]
k = 3

# sliding window - FAIL
# start = 0
# total = 0

# for end in range(len(arr)):
#     total += arr[end]
#     while start != end:
#         first = arr[start]
#         subtotal = total
#         if subtotal % k == 0:
#             break
#             # return True
#         else:
#             subtotal -= first
#             start += 1
    
#     start = 0

# # return False
# print("F")



# using hash table

hashmap = {}

for i in arr:

    if i in hashmap.keys():
        hashmap[i] += 1
    else:
        hashmap[i] = 1


