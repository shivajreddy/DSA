from typing import List

class Solution:
    """
    Sort the given input, and create a new copy merged intervals
    Time : O(n.log(n))
    Space: O(n)
    """
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        # Sort intervals by start time
        intervals.sort(key= lambda interval: interval[0])

        # Result of merged intervals
        result = [intervals[0].copy()]

        for idx in range(1, len(intervals)):
            prev_interval = result[-1]
            curr_interval = intervals[idx]

            # New interval start time in the range of previous intervals end
            if prev_interval[1] >= curr_interval[0]:
                # Update previous interval with highest end time
                prev_interval[1] = max(prev_interval[1], curr_interval[1])

            else:
                result.append(curr_interval.copy())

        return result

