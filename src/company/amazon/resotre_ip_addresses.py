"""
Key Insights  
    Fixed Number of ip_segments:  
        - An IP address consists of exactly four ip_segments, meaning that three dots must be placed in 
          the string to divide it into four parts.  
        - Each ip_segment must be between 1 to 3 digits long and its numerical value must lie between 0 and 255.

    Handling Leading Zeros:  
        - ip_segments cannot contain leading zeros, so while "0" is valid, "01" or "00" is not.

    Backtracking Approach:  
    - Backtracking is suitable for exploring all possible dot placements while ensuring that each ip_segment 
      conforms to IP address rules.  
    - By terminating invalid paths early, we can significantly reduce unnecessary computations.

### Step-by-Step Solution  
    1. Validate Input Length:  
        - An IP address needs a string of at least 4 digits and at most 12 digits, as each ip_segment can have up 
          to 3 digits.  
    - If the string length is outside this range, return an empty list since no valid IP addresses can be formed.

    2. Backtracking Function (backtrack):  
    - Parameters:
        - `start`: The current index in the string from where to consider the next ip_segment.
        - `ip_segments`: The current list of ip_segments formed so far.
    - Base Case:  
        - If four ip_segments have been formed and we've traversed the entire string (`start == len(s)`), 
          join the ip_segments with dots and add the IP address to the result list.
    - Recursive Case:  
        - Iterate through the next 1 to 3 digits to form a ip_segment.  
        - For each potential ip_segment, check if it's valid (i.e., no leading zeros unless it's exactly "0", 
          and the numerical value is ≤ 255).  
        - If valid, append it to the ip_segments list and recursively call `backtrack` for the next ip_segment.  
        - After recursion, backtrack by removing the last ip_segment to explore other potential placements.

    3. Helper Function (is_valid):  
    - This function checks whether a substring is a valid IP ip_segment.  
    - It returns `True` if the ip_segment does not have leading zeros (except for "0") and its integer value is 
      between 0 and 255.

    4. Initiate Backtracking:  
    - Start the backtracking process from index 0 with an empty list of ip_segments.

Time and Space Complexity  
    - Time Complexity:  
    - O(3^4) = O(81) in the worst case, as there are up to 3 possible positions for placing each of the three dots.
      The actual number of recursive calls is reduced due to constraints on ip_segment values and leading zeros.

    - Space Complexity:  
    - O(1) for the result list, since the number of possible valid IP addresses is limited.  
    - O(4) for the recursion stack, as the maximum recursion depth is 4 (one for each ip_segment).
"""



from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        # Resultant list to store all valid IP addresses
        result = []
        
        # Total length of the input string
        n = len(s)
        
        # Early termination if length is not suitable for an IP address
        if n < 4 or n > 12:
            return result
        
        # Helper function to check if a ip_segment is valid
        def is_valid(ip_segment: str) -> bool:
            # Check for leading zeros
            if len(ip_segment) > 1 and ip_segment[0] == '0':
                return False
            # Check if the ip_segment is within 0 to 255
            return 0 <= int(ip_segment) <= 255
        
        # Backtracking function to build ip_segments
        def backtrack(start: int, ip_segments: List[str]):
            # If we have four ip_segments and have traversed the entire string, add to result
            if len(ip_segments) == 4:
                if start == n:
                    ip_address = ".".join(ip_segments)
                    result.append(ip_address)
                return
            
            # Prune paths that are too long or too short
            remaining_ip_segments = 4 - len(ip_segments)
            remaining_chars = n - start
            if remaining_chars < remaining_ip_segments or remaining_chars > remaining_ip_segments * 3:
                return
            
            # Try ip_segments of length 1 to 3
            for length in range(1, 4):
                # Ensure we don't go out of bounds
                if start + length > n:
                    break
                ip_segment = s[start:start+length]
                if is_valid(ip_segment):
                    # Choose
                    ip_segments.append(ip_segment)
                    # Explore
                    backtrack(start + length, ip_segments)
                    # Un-choose (backtrack)
                    ip_segments.pop()
        
        # Initiate backtracking with starting index 0 and empty ip_segments list
        backtrack(0, [])
        
        return result

