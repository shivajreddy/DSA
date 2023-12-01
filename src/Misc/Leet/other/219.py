nums = [1,2,3,1]
k = 3
nums = [1,2,3,1,2,3]
k = 2


hash_map = {}
for i in range(len(nums)):
    item = nums[i]
    if item in hash_map.keys():
        print('item is in hashmap', hash_map.keys())
        j = hash_map[item]
        print('j=',j, "i=", i, "k =", k)
        if ( i-j <= k ) or ( j - i <= k ):
            # return True
            print('True')

    hash_map[item] = i
    
# return False
print('False')