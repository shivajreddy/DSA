"""
### Explanation

The solution utilizes **binary search** to determine the smallest possible 
eating speed (`k`) such that Koko can finish all banana piles within `h` 
hours. The main idea is to find the **minimum speed** at which the total 
hours required to eat all the bananas is less than or equal to the given 
time limit (`h`).

1. **Binary Search Setup**:
   - The search range for `k` starts from 1 (the slowest speed) and goes up 
     to `max(piles)` (the fastest speed where Koko eats an entire pile in 
     one hour).
   
2. **Total Hours Calculation**:
   - For each mid-point (`mid`) in the binary search, the `get_total_hours` 
     function calculates the total hours required to eat all the piles with 
     the current speed `mid`. The function uses `math.ceil(pile / k)` to 
     account for Koko not being able to eat fractional piles.

3. **Binary Search Logic**:
   - If the total hours needed with the current speed (`mid`) is less than 
     or equal to `h`, we try to find a smaller eating speed by adjusting the 
     right bound (`right = mid`).
   - If the total hours exceed `h`, we increase the speed by adjusting the 
     left bound (`left = mid + 1`).

4. **Edge Case Handling**:
   - If the total hours exceed the available time (`h`) for the smallest 
     possible speed, then it's impossible to finish the piles within `h` 
     hours, though this is not possible for valid inputs.

---

### Time Complexity

The time complexity is **O(n * log(max(piles)))**, where:
- `n` is the number of piles.
- `log(max(piles))` comes from the binary search over the possible values 
  of `k`, which ranges from 1 to `max(piles)`.
- For each step of the binary search, we calculate the total hours required 
  with the given speed `k`. This requires iterating over all the piles, 
  resulting in an **O(n)** operation per binary search step.

Thus, the overall time complexity is **O(n * log(max(piles)))**.

---

### Space Complexity

The space complexity is **O(1)**, as we are only using a few integer 
variables (`left`, `right`, `mid`) and no additional data structures that 
scale with the input size. The space used is constant regardless of the size 
of the input.

This solution is efficient and scalable, handling large input sizes within 
reasonable time limits.
"""

import math
from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        """
        Calculates the minimum eating speed required to finish all piles within h hours.

        Args:
        piles (List[int]): List of piles of bananas.
        h (int): Total available hours to finish all piles.

        Returns:
        int: The minimum speed (k) required to eat all bananas in h hours.
        """

        def get_total_hours(k: int) -> int:
            """
            Helper function to calculate the total hours needed given an eating speed k.
            Args:
            k (int): Eating speed.

            Returns:
            int: Total hours required.
            """
            return sum(math.ceil(pile / k) for pile in piles)

        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if get_total_hours(mid) <= h:
                right = mid  # Try smaller speed
            else:
                left = mid + 1  # Try larger speed

        return left



# TESTS ------------
import unittest

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_case_1(self):
        piles = [30, 11, 23, 4, 20]
        h = 6
        self.assertEqual(self.s.minEatingSpeed(piles, h), 23)

    def test_case_2(self):
        piles = [3, 6, 7, 11]
        h = 8
        self.assertEqual(self.s.minEatingSpeed(piles, h), 4)

    def test_case_3(self):
        piles = [1000000000]
        h = 1000000000
        self.assertEqual(self.s.minEatingSpeed(piles, h), 1)

    def test_invalid_hours(self):
        piles = [10, 5, 7]
        h = 0
        with self.assertRaises(ValueError):
            self.s.minEatingSpeed(piles, h)

    def test_single_pile(self):
        piles = [1]
        h = 1
        self.assertEqual(self.s.minEatingSpeed(piles, h), 1)

# Run the test cases
if __name__ == '__main__':
    unittest.main()


