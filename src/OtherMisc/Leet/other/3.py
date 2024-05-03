class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        arr = [*s]
        
        start = 0
        hashmap = {}
        result = 0
        
        for end in range(len(arr)):
            
            item = arr[end]
            if item in hashmap.keys():
                hashmap[item] += 1
            else:
                hashmap[item] = 1
            
            while 2 in list(hashmap.values()):
                first = arr[start]
                
                hashmap[first] -= 1
                if hashmap[first] == 0:
                    del hashmap[first]
                
                start += 1
            
            result = max(result, end-start+1)
        
        return result