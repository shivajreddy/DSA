// 435. Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // Sort intervals by their END time (greedy approach)
        // This ensures we always consider keeping the interval that ends
        // earliest
        sort(intervals.begin(), intervals.end(),
             [&](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });

        int n = intervals.size();

        int last_kept_endtime =
            INT_MIN; // End time of the last interval we decided to keep
        int intervals_to_remove = 0;

        for (int i = 0; i < n; i++) {
            int curr_start = intervals[i][0], curr_end = intervals[i][1];

            // Check if current interval overlaps with the last kept interval
            if (last_kept_endtime <= curr_start) {
                // NO OVERLAP: Current interval starts after the last kept
                // interval ends We can safely keep this interval
                last_kept_endtime =
                    curr_end; // Update our tracking to this interval's end
            } else {
                // OVERLAP DETECTED: Current interval starts before the last
                // kept interval ends We must remove one of them. Since we
                // sorted by end time, the last kept interval ends earlier, so
                // we remove the current interval (greedy choice)
                intervals_to_remove++;
                // Note: We DON'T update last_kept_endtime because we're
                // removing current interval
            }
        }

        return intervals_to_remove;
    }
};

int main() {
    Solution* sol = new Solution();

    vector<vector<int>> intervals;

    {
        intervals = { { 1, 2 }, { 2, 3 }, { 3, 4 }, { 1, 3 } };
        cout << sol->eraseOverlapIntervals(intervals) << endl;
    }
    {
        intervals = { { 1, 2 }, { 1, 2 }, { 1, 2 } };
        cout << sol->eraseOverlapIntervals(intervals) << endl;
    }
    {
        intervals = { { 1, 2 }, { 2, 3 } };
        cout << sol->eraseOverlapIntervals(intervals) << endl;
    }
    {
        intervals = { { 0, 2 }, { 1, 3 }, { 2, 4 }, { 3, 5 }, { 4, 6 } };
        cout << sol->eraseOverlapIntervals(intervals) << endl;
    }

    delete sol;
}
