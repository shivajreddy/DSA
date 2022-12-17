# def subarraySum(nums, k):
    
#     count = 0

#     for i in range(len(nums)):

#         j = i + 1
#         sub_array = nums[i:j]
        
#         while(j <= len(nums)):
#             print(sub_array)
#             if sum(sub_array) == k:
#                 count += 1

#             j += 1
#             sub_array = nums[i:j]

#     # return count

# nums = [1,2,3]
# k = 3
# nums = [1,-1,0]
# k = 1

# print(subarraySum(nums,k))


nums = [1,2,1,2,1]
k = 3

nums = [3,4,7,2,-3,1,4,2]
k=7
# {0:1, 3:1, 7:1, 14:2, 16:1, 13:1, 18:1, 20:1}

nums = [1,-1,0]
k = 0

count = 0
m = {0:1}
s = 0
total_sum = 0

for num in nums:
    total_sum += num
    diff = total_sum - k

    if diff in m.keys():
        count += 1

    # if diff == 0 or diff == k:
    #     count += 1
    
    m[total_sum] = m.get(total_sum,0)+1


print(nums)
print(m)
# print(count)
