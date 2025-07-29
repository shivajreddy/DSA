// 253. Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {

        function<void(vector<vector<int>>&)> print_intervals =
            [&](vector<vector<int>>& v) -> void {
            for (auto& interval : v) {
                cout << "[" << interval[0] << " " << interval[1] << "] ";
            }
            cout << endl;
        };
        // print_intervals(intervals);

        sort(intervals.begin(), intervals.end(),
             [](const vector<int>& a, const vector<int>& b) {
                 return a[0] == b[0] ? a[1] < b[1] : a[0] < b[0];
             });
        // print_intervals(intervals);

        int n = intervals.size();
        for (int i = 1; i < n; i++) {
            if (intervals[i][0] < intervals[i - 1][1]) {
                return false;
            }
        }
        return true;
    }
};

int main() {
    Solution* sol = new Solution();

    vector<vector<int>> intervals;

    {
        intervals = { { 0, 30 }, { 5, 10 }, { 15, 20 } };
        cout << sol->canAttendMeetings(intervals) << endl;
    }
    {
        intervals = { { 7, 10 }, { 2, 4 } };
        cout << sol->canAttendMeetings(intervals) << endl;
    }
    {
        intervals = { { 0, 30 }, { 0, 20 }, { 15, 20 } };
        cout << sol->canAttendMeetings(intervals) << endl;
    }

    delete sol;
}
