// 435. Non-overlapping Intervals
// https://leetcode.com/problems/non-overlapping-intervals

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int eraseOverlapIntervals(vector<vector<int>>& intervals) {
        return -1;
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

    delete sol;
}
