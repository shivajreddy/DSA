// 253. Meeting Rooms II
// https://leetcode.com/problems/meeting-rooms-ii

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minMeetingRooms(vector<vector<int>>& intervals) {

        int n = intervals.size();

        vector<pair<int, char>> events(2 * n);
        for (int i = 0; i < n; i++) {
            events[i * 2] = { intervals[i][0], 's' };
            events[i * 2 + 1] = { intervals[i][1], 'e' };
        }

        sort(events.begin(), events.end()); // 2n.log(2n) => n.log(n)

        int rooms = 0, res = 0;
        for (int i = 0; i < 2 * n; i++) {
            if (events[i].second == 's') {
                rooms++;
            } else {
                rooms--;
            }
            res = max(res, rooms);
        }
        return res;
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
