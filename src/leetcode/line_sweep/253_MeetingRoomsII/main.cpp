// 253. Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {

        function<void(vector<vector<int>>&)> print_intervals =
            [&](vector<vector<int>>& v) -> void {
            for (auto& interval : v) {
                cout << "[" << interval[0] << " " << interval[1] << "] ";
            }
            cout << endl;
        };
        // print_intervals(intervals);

        return -1;
    }
};

int main() {
    Solution* sol = new Solution();

    vector<vector<int>> intervals;

    {
        intervals = { { 0, 30 }, { 5, 10 }, { 15, 20 } };
        cout << sol->minMeetingRooms(intervals) << endl;
    }
    {
        intervals = { { 7, 10 }, { 2, 4 } };
        cout << sol->minMeetingRooms(intervals) << endl;
    }
    {
        intervals = { { 0, 30 }, { 0, 20 }, { 15, 20 } };
        cout << sol->minMeetingRooms(intervals) << endl;
    }

    delete sol;
}
