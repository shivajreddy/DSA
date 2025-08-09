"""
- This solution calculates the minimum number of key pushes required to type a given word on a keyboard
  where each key can hold multiple characters, and accessing a character requires a certain number of pushes.

Key Steps:
    1. Character Frequency Calculation: 
       - A `defaultdict` is used to count the frequency of each character in the word.
    
    2. Max Heap Creation:
       - The character frequencies are stored in a max heap (using negative values to simulate max heap behavior
         with Python's `heapq` which is a min-heap by default). This ensures that characters with higher
         frequencies are processed first.

    3. Push Count Calculation:
       - The solution simulates moving across keyboard positions (from `LOW = 2` to `HIGH = 9`).
       - For each character, the number of pushes required is determined by multiplying the character frequency
         by the current push count.
       - After processing each character, the cursor moves to the next position on the keyboard, and if the 
         position exceeds `HIGH`, it resets to `LOW`, and the push count increases by 1 to reflect the 
         increased difficulty of accessing characters further away.

    4. Return Total Pushes: 
    - The total number of key pushes required to type the word is returned.

Time Complexity: 
    O(n log n), where `n` is the number of unique characters, due to heap operations.
Space Complexity:
    O(n), where `n` is the number of unique characters.

"""

from collections import defaultdict
import heapq

class Solution:
    def minimumPushes(self, word: str) -> int:
        # Constants representing the lowest and highest index on the keyboard
        LOW = 2
        HIGH = 9
        
        # Step 1: Count the frequency of each character in the word
        char_frequency = defaultdict(int)
        for char in word:
            char_frequency[char] += 1
        
        # Step 2: Create a max heap based on character frequency (using negative values for max heap)
        max_heap = [-count for count in char_frequency.values()]
        heapq.heapify(max_heap)
        
        total_pushes = 0  # Variable to keep track of total pushes
        current_pos = LOW  # Start position on the keyboard
        push_count = 1     # Initial push count for characters at current position
        
        # Step 3: Process the heap
        while max_heap:
            # Pop the most frequent character's count from the heap
            char_count = -heapq.heappop(max_heap)
            
            # Add the required pushes for the current character frequency
            total_pushes += char_count * push_count
            
            # Move to the next position on the keyboard
            current_pos += 1
            
            # If we go past the highest key, reset the position and increase the push count
            if current_pos > HIGH:
                current_pos = LOW
                push_count += 1
        
        return total_pushes
