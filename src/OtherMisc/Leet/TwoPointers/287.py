class Solution:
    def validPalindrome(self, s: str) -> bool:
      
      def helper(sub_str):
        l = 0
        r = len(sub_str)-1
        
        while l <= r:
          if sub_str[l] != sub_str[r]:
            return False
          l += 1
          r -= 1
        return True
      
      
      start = 0
      end = len(s)-1
      
      while start <= end:
        
        if s[start] != s[end]:
          return helper(s[start+1:end]) or helper(s[start:end-1]) 
            #return True
          print(s[start], s[end])
          #return False
        
        start += 1
        end -= 1
        
      return True
