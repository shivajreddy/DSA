// 252. Meeting Rooms
// https://leetcode.com/problems/meeting-rooms

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    bool canAttendMeetings(vector<vector<int>>& intervals) {
        return false;
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

    delete sol;
}
