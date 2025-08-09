"""
0   1
30  0

0   5   10  15  20  30
----------------------
    ------
            ------
"""

class Solution:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        # Create a list of all start and end times marked accordingly
        events = []
        for interval in intervals:
            events.append((interval[0], 'start'))
            events.append((interval[1], 'end'))

        # Sort events by time; if times are equal, 'end' comes before 'start'
        '''
        - when comparing two items, 0'th item and 1'th item
        - choose the 0'th item(i.e., the first item) whose item[1] is 'end'
        '''
        events.sort(key=lambda event: (event[0], 0 if event[1] == 'end' else 1))

        max_rooms = 0
        current_rooms = 0

        # Sweep through the events
        for _, event_type in events:
            if event_type == 'start':
                current_rooms += 1
            else:
                current_rooms -= 1
            max_rooms = max(max_rooms, current_rooms)

        return max_rooms

import heapq

class Solution_Using_Heap:
    def minMeetingRooms(self, intervals):
        if not intervals:
            return 0

        # Sort intervals by start time
        intervals.sort(key=lambda x: x[0])

        # Initialize a heap with the end time of the first meeting
        heap = [intervals[0][1]]

        for interval in intervals[1:]:
            # If the earliest meeting ends before or at the start of the current meeting
            if heap[0] <= interval[0]:
                heapq.heappop(heap)
            heapq.heappush(heap, interval[1])

        # The size of the heap is the minimum number of rooms required
        return len(heap)



# TESTS -------------------------------------------------
import unittest

class TestMinMeetingRooms(unittest.TestCase):
    def setUp(self):
        self.solution = Solution()

    def test_case1(self):
        intervals = [[0, 30], [5, 10], [15, 20]]
        expected = 2
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case2(self):
        intervals = [[7, 10], [2, 4]]
        expected = 1
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case3(self):
        intervals = [[1, 5], [2, 6], [4, 8], [9, 10]]
        expected = 3
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case4(self):
        intervals = [[1, 4], [2, 5], [7, 9]]
        expected = 2
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case5(self):
        intervals = []
        expected = 0
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case6(self):
        intervals = [[1, 5], [5, 10], [10, 15]]
        expected = 1
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case7(self):
        intervals = [[0, 10], [10, 20], [5, 15]]
        expected = 2
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case8(self):
        intervals = [[1, 3], [3, 5], [5, 7], [7, 9]]
        expected = 1
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case9(self):
        intervals = [[1, 10], [2, 7], [3, 5], [4, 6]]
        expected = 4
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case10(self):
        intervals = [[6, 7], [2, 4], [8, 12], [5, 9]]
        expected = 2
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case11(self):
        intervals = [[13, 15], [1, 13]]
        expected = 1
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

    def test_case12(self):
        intervals = [[0, 30], [5, 10], [15, 20], [25, 35]]
        expected = 2
        result = self.solution.minMeetingRooms(intervals)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
