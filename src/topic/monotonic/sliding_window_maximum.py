"""
    Observation: for a given window of elements, we only care about the largest
    number in that window.

    - Maintain a queue, that is in decreasing order
        - Maintain that this queue is in sync with the window of elements
        - First item in the queue will always be the largest element for that
          window of elements

    - Data Structure: Decreasing Mono Queue
        - The mono queue holds elements in decreasing order
        - The elements in the mono queue will be the range of current window

    Time : O(n), every element is accessed atmost twice
    Space: O(k)

"""

from collections import deque
from typing import List


class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:

        res = []

        # Increasing Mono Queue
        window = deque()

        # Process first 'k' elements to mono queue
        for i in range(k):
            # Maintain Increasing Mono Queue
            while window and nums[window[-1]] <= nums[i]:
                window.pop()
            window.append(i)

        # Process rest of the elements
        for i in range(k, len(nums)):

            # First element is the maximum element of window
            res.append(nums[window[0]])

            # Sync Queue with window: Remove elements outside current window
            while window and window[0] <= i - k:
                window.popleft()

            # Maintain Increasing Mono Queue
            while window and nums[window[-1]] <= nums[i]:
                window.pop()

            window.append(i)

        res.append(nums[window[0]])

        return res


sol = Solution()


assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 3, 6, 7], 3) == [3, 3, 5, 5, 6, 7]
assert sol.maxSlidingWindow([1, 3, -1, -3, 5, 7, 2, 8, 1, 4], 3) == [
    3,
    3,
    5,
    7,
    7,
    8,
    8,
    8,
]
assert sol.maxSlidingWindow([1], 1) == [1]
