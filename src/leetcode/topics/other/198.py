#  198 House Robber

nums = [1,2,3,1]
nums = [2,7,9,2,9,7,7,9,1,2]
nums = [2,7,9,3,1]

data = [0] * len(nums)

print(data)

# for i in range(len(nums)-2):

#     if nums[i] + nums[i+1] > nums[i] + nums[i+2]:
#         data[i] = nums[i+1]
#     else:
#         data[i] = nums[i+2]
#     print(data)

# print(data)
data = []
for i in range(len(nums)-1,-1,-2):
    item = nums[i]
    if nums[i] > nums[i-1]:
        data.append(nums[i])
    else:
        data.append(nums[i-1])
    # print(f'choose: {nums[i]} | {nums[i-1]}')

print(data)
print(sum(data))