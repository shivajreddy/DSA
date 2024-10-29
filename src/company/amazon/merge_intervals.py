"""
### Explanation

1. **Sorting**: The intervals are sorted by their starting points. This ensures 
   that we only need to compare each interval with the one right before it to 
   check for overlap.
   
2. **Merging**: For each interval, the algorithm checks if the start of the 
   current interval overlaps with the end of the previous interval. If so, the 
   intervals are merged by updating the end of the previous interval. If there 
   is no overlap, the current interval is added to the result.

3. **Edge Case**: If the input list is empty, we return an empty list 
   immediately.

---

### Time Complexity

- Sorting the intervals takes **O(n log n)**, where `n` is the number of 
  intervals.
- Merging the intervals takes **O(n)** since we only iterate through the list 
  once after sorting.
- Thus, the overall time complexity is **O(n log n)**.

---

### Space Complexity

- The space complexity is **O(n)** because we are storing the result in a 
  separate list of merged intervals.

This solution is efficient and scalable, handling cases where there are many 
intervals and merges required.

"""
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """
        Merges overlapping intervals and returns a list of non-overlapping intervals.

        Args:
        intervals (List[List[int]]): List of intervals where each interval is represented as [start, end].

        Returns:
        List[List[int]]: A list of merged intervals.
        """
        if not intervals:
            return []

        # Sort the intervals based on the starting point
        intervals.sort(key=lambda x: x[0])

        merged_intervals = [intervals[0]]

        for i in range(1, len(intervals)):
            prev_interval = merged_intervals[-1]
            curr_interval = intervals[i]

            # Check if the current interval overlaps with the previous interval
            if prev_interval[1] >= curr_interval[0]:
                # If they overlap, merge them by updating the end of the previous interval
                prev_interval[1] = max(prev_interval[1], curr_interval[1])
            else:
                # If they don't overlap, add the current interval to the result
                merged_intervals.append(curr_interval)

        return merged_intervals




# TESTS -------------
import unittest

class TestMergeIntervals(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def test_case_1(self):
        intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 6], [8, 10], [15, 18]]
        self.assertEqual(self.s.merge(intervals), expected)

    def test_case_2(self):
        intervals = [[1, 4], [4, 5]]
        expected = [[1, 5]]
        self.assertEqual(self.s.merge(intervals), expected)

    def test_case_3(self):
        intervals = []
        expected = []
        self.assertEqual(self.s.merge(intervals), expected)

    def test_case_4(self):
        intervals = [[1, 4], [2, 3]]
        expected = [[1, 4]]
        self.assertEqual(self.s.merge(intervals), expected)

    def test_case_5(self):
        intervals = [[1, 10], [2, 6], [8, 10], [15, 18]]
        expected = [[1, 10], [15, 18]]
        self.assertEqual(self.s.merge(intervals), expected)

# Run the test cases
if __name__ == '__main__':
    unittest.main()

