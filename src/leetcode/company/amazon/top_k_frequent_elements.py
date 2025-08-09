""" 
### Explanation:

#### Step 1 - Count the frequencies:
- The `Counter` class from `collections` is used to create a frequency map 
  (`freq_map`) that counts how many times each number appears in `nums`.
- `Counter(nums)` will return a dictionary-like object where keys are the unique 
  elements and values are their frequencies.

#### Step 2 - Heapify the frequency map:
- We use a max-heap to store the numbers along with their negative frequencies. 
  Since Python's `heapq` library only provides a min-heap, using negative counts 
  allows us to simulate a max-heap.
- This way, the most frequent elements are placed at the top of the heap.

#### Step 3 - Extract the top K frequent elements:
- We extract the top `k` elements from the heap by popping the heap `k` times. 
  Each time, the most frequent element is retrieved and added to the result list.

### Time Complexity:
- Step 1 (Counting frequencies): `O(n)`, where `n` is the length of the 
  input list `nums`.
- Step 2 (Heapify the frequencies): `O(m log m)`, where `m` is the number 
  of unique elements in `nums`. Heapifying takes `O(m log m)` time.
- Step 3 (Extracting top k elements): `O(k log m)`, where `k` is the number 
  of elements to extract and `m` is the number of unique elements in `nums`.
- Overall Time Complexity: `O(n + m log m + k log m)`.

### Space Complexity:
- `O(n)` for storing the frequency map and the heap, where `n` is the number of 
  elements in `nums` and `m` is the number of unique elements.
- The result list will also take `O(k)` space.

### Improvements for Production:
- Error handling: Handle cases where `k` exceeds the number of unique 
  elements or where `nums` is an empty list.
- Efficiency: For cases where `k` is small compared to the size of the 
  input list, using a min-heap of size `k` instead of a max-heap of size `m` 
  might be more efficient, reducing the space complexity. This would require 
  pushing and popping elements as we traverse the frequency map.

### Edge Cases:
- If `nums` is empty, the result should return an empty list.
- Handle scenarios where `k = 0` by returning an empty list.

"""

from collections import Counter
import heapq
from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        # Step 1: Count the frequency of each number using a Counter
        freq_map = Counter(nums)

        # Step 2: Use a max-heap to get the k most frequent elements
        # We use -count to simulate max-heap using Python's min-heap (heapq)
        max_heap = [(-count, num) for num, count in freq_map.items()]
        heapq.heapify(max_heap)

        # Step 3: Extract the top k frequent elements
        result = []
        for _ in range(k):
            _, num = heapq.heappop(max_heap)
            result.append(num)

        return result

