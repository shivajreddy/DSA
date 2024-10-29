"""
### Explanation:

#### Heap Creation:
- A max-heap is simulated using a min-heap by inserting the negative of each 
  element. In Python, `heapq` implements a min-heap, so inserting negative 
  values allows us to simulate max-heap behavior.

#### Heapify:
- The `heapq.heapify(mh)` call transforms the list `mh` into a heap, ensuring 
  that the smallest (or most negative, in this case) element is at the top.

#### K-th Largest Calculation:
- The code then repeatedly pops elements from the heap using 
  `heapq.heappop(mh)` until we reach the k-th largest element. This is done by 
  popping `k-1` elements before returning the k-th largest.

#### Returning the Correct Value:
- Since the values in the heap are negative to simulate max-heap behavior, we 
  return the negative of the top element to get the actual value.

### Time and Space Complexity:

- **Time Complexity**: 
  - `O(n + k log n)`: The heap construction (`heapify`) takes `O(n)` time. For 
    each of the `k-1` pops, it takes `O(log n)` to rebalance the heap, leading 
    to a total of `O(k log n)`.

- **Space Complexity**: 
  - `O(n)`: The space complexity is `O(n)` due to the storage of all elements 
    in the heap.

### Improvements and Suggestions for Production:

#### Handling Edge Cases:
- If `k` is greater than the length of `nums`, handle this case by throwing an 
  exception or returning a special value (e.g., `None` or `-1`).

#### Use of Built-in Functions:
- Python's `heapq.nlargest()` can also be used to simplify this, as it directly 
  provides the k-th largest elements in sorted order, which could improve 
  readability and reduce potential bugs in the code.

#### Optimizations:
- If memory constraints are an issue, we could instead maintain a min-heap of 
  size `k` by pushing elements to the heap and popping the smallest element 
  whenever the heap exceeds size `k`. This approach keeps memory usage lower by 
  maintaining a heap of fixed size `k`.
"""

from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Finds the k-th largest element in a list using a max-heap approach.

        Args:
        nums (List[int]): List of integers to search through.
        k (int): The index of the largest element to return (1-based index).

        Returns:
        int: The k-th largest element.
        """

        # Create a max heap using negative values to simulate max-heap behavior with heapq
        mh = [-num for num in nums]
        heapq.heapify(mh)

        # Pop elements from the heap until we reach the k-th largest
        for _ in range(k - 1):
            heapq.heappop(mh)

        # The k-th largest element is now the top of the heap 
        # (negative value, so return the positive)
        return -heapq.heappop(mh)

