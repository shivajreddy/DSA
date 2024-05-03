from typing import Counter, Dict

from prompt_toolkit import HTML

nums = [3,1,4,1,5]
nums = [3,1,4,1,5]
nums = [1,2,3,4,5]
nums = [1,3,1,5,4]
nums = [1,2,4,4,3,3,0,9,2,3]
k = 3


hm = {}

for num in nums:
    hm[num] = hm.get(num,0)+1
print(hm)

for num in nums:
    r = num + k
    if r in hm.keys():
        