"""
- Binary search algorithm to find the minimum eating speed (k) at which Koko 
  can consume all bananas within h hours.

- slowest possible speed = 1
- fastest possible speed = max(piles)
- search range ->  [1, 2, 3, ..., max(piles)]
- In each iteration, it calculate the time needed to eat all piles at the current rate 
  using math.ceil() to round up the time for each pile.
- If the total time is less than or equal to h, it narrows the search to lower speeds;
  otherwise, it searches higher speeds.
- The algorithm continues until it finds the minimum speed that allows Koko to 
  eat all bananas within the given time constraint.

Time : O(n * log(max(piles)))
    - n is the number of piles.
    - log(max(piles)) comes from the binary search over the possible rates, 
      which ranges from 1 to max(piles)

Space : O(1)

"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        # Slowest and Fastest rate of eating
        slow = 1
        fast = max(piles)

        # Binary search the smallest rate possible, while eating under time 'h'
        while slow < fast:
            rate = (slow + fast) // 2

            # Note: Rate of eating a pile is upper bound
            all_times = [math.ceil(pile / rate) for pile in piles]
            total_time = sum(all_times)

            # Can eat at this rate, mark this highest rate until now
            if total_time <= h:
                fast = rate
            # Will get caught at this speed, increase speed
            else:
                slow = rate + 1

        return slow

