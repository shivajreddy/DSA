// 56. Merge Intervals
// https://leetcode.com/problems/merge-intervals

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> merge(vector<vector<int>>& intervals) {

        int n = intervals.size();
        sort(intervals.begin(), intervals.end());

        int left_most, right_most;
        left_most = intervals[0][0], right_most = intervals[0][1];

        vector<vector<int>> res;

        for (int i = 1; i < n; i++) {
            if (right_most < intervals[i][0]) {
                res.push_back({ left_most, right_most });
                left_most = intervals[i][0], right_most = intervals[i][1];
            } else {
                right_most = max(right_most, intervals[i][1]);
            }
        }
        res.push_back({ left_most, right_most });

        return res;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<vector<int>> intervals;

    auto print_vvi = [&](vector<vector<int>> v) {
        int n = v.size();
        for (int i = 0; i < n; i++)
            cout << "[" << v[i][0] << " " << v[i][1] << "] ";
        cout << endl;
    };

    {
        intervals = { { 1, 3 }, { 2, 6 }, { 8, 10 }, { 15, 18 } };
        print_vvi(sol->merge(intervals));
    }
    {
        intervals = { { 1, 4 }, { 4, 5 } };
        print_vvi(sol->merge(intervals));
    }
    {
        intervals = { { 1, 4 }, { 5, 6 } };
        print_vvi(sol->merge(intervals));
    }

    delete sol;
}
