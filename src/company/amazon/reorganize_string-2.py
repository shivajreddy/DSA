import heapq
from collections import defaultdict

'''
- Track the previously added char to the result & its count
- Do the following as long as there is a heap or prev-count
    - get the most frequent char from heap, and add to result
    - if there was a previous-count, then add that prev-char-count to heap
    - update prev-char and prev-count

Time : O(n) for building heap
       O(k log k), where k is the number of unique characters.
       Overall complexity = O(n + k log k)
Space: O(n)
'''

class Solution:
    def reorganizeString(self, s: str) -> str:
        # Create a counter to track the frequency of each character
        counter = defaultdict(int)
        for char in s:
            counter[char] += 1
        
        # Build a max heap based on the frequency of characters
        max_heap = [(-count, char) for char, count in counter.items()]
        heapq.heapify(max_heap)
        
        result = []
        prev_count, prev_char = 0, ''
        
        # Process the heap
        while max_heap or prev_count:
            # Only remaining characters are the previously added characters
            if prev_count and not max_heap:
                return ""
            
            # Get the most frequent character
            count, char = heapq.heappop(max_heap)

            # Add this character to result and update count
            result.append(char)
            count = -count - 1  # convert back to +ve
            
            # If there's a previous character to reinsert, push it back into the heap
            if prev_count > 0:
                heapq.heappush(max_heap, (-prev_count, prev_char))
            
            # Update the previous character and count
            prev_count, prev_char = count, char
        
        return ''.join(result)

