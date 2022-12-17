nums = [1,1,1,2,2,3,3]

k = 0
for i in range(len(nums)):
    item = nums[i]

    if item in nums[i+1:]:
        nums[i] = "_"
        k += 1


nums[:] = (n for n in nums if n!='_')
for n in range(4):
    nums.append('_')

print(k, nums)
