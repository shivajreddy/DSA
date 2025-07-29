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

class Solution2 {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        int n = intervals.size();

        vector<pair<int, char>> events(n * 2);
        for (int i = 0; i < n; i++) {
            events[i * 2] = { intervals[i][0], 's' };
            events[i * 2 + 1] = { intervals[i][1], 'e' };
        }
        sort(events.begin(), events.end());

        int overlaps = 0, max_overlaps = 0;

        for (int i = 0; i < 2 * n; i++) {
            if (events[i].second == 's') {
                overlaps++;
            } else {
                overlaps--;
            }
            max_overlaps = max(max_overlaps, overlaps);
        }
        // cout << max_overlaps - 1 << endl;
        return max_overlaps - 1;

        /*
        sort(intervals.begin(), intervals.end()); // n.log(n)

        vector<vector<int>> res;
        res.push_back(intervals[0]);

        for (int i = 1; i < n; i++) {
            if (res.back()[1] > intervals[i][0]) {
                int prev_d = res.back()[1] - res.back()[0] + 1;
                int curr_d = intervals[i][1] - intervals[i][0] + 1;
                if (prev_d > curr_d) {
                    res.pop_back(); // remove the previous
                    res.push_back(intervals[i]);
                }
            } else {
                res.push_back(intervals[i]);
            }
        }

        return res.size();
        */
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
