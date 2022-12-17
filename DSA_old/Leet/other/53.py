# 53. Maximum subarray


nums = [-2,1,-3,4,-1,2,1,-5,4]


# brute force -> Time = O(n^2)
count = min(nums)
for i in range(len(nums)):

    for j in range(i+1,len(nums)+1):
        sub_arr = nums[i:j]

        if sum(sub_arr) > count :
            count = sum(sub_arr)

    