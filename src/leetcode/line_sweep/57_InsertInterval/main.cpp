// 57. Insert Interval
// https://leetcode.com/problems/insert-interval

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals,
                               vector<int>& newInterval) {
        vector<vector<int>> res;
        return res;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<vector<int>> intervals;
    vector<int> newInterval;

    auto print_vvi = [&](vector<vector<int>> v) {
        int n = v.size();
        for (int i = 0; i < n; i++)
            cout << "[" << v[i][0] << " " << v[i][1] << "] ";
        cout << endl;
    };

    {
        intervals = { { 1, 3 }, { 6, 9 } };
        newInterval = { 2, 5 };
        print_vvi(sol->insert(intervals, newInterval));
    }
    {
        intervals = { { 1, 2 }, { 3, 5 }, { 6, 7 }, { 8, 10 }, { 12, 16 } };
        newInterval = { 4, 8 };
        print_vvi(sol->insert(intervals, newInterval));
    }

    delete sol;
}
