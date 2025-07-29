// 435. Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        // sort based on endings
        sort(intervals.begin(), intervals.end(),
             [&](const vector<int>& a, const vector<int>& b) {
                 return a[1] < b[1];
             });

        int n = intervals.size();

        int ans = 0;
        int k = INT_MIN;

        for (int i = 0; i < n; i++) {
            int s = intervals[i][0], e = intervals[i][1];

            if (s >= k) { // Case 1: current start is after previous end
                k = e;
            } else { // Case 2: curr start is before the previous end
                ans++;
            }
        }

        return ans;
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
