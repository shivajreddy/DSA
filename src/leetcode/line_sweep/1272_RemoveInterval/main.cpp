// 1272. Remove Interval
// https://leetcode.com/problems/remove-interval/?envType=problem-list-v2&envId=mzw3cyy6

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> removeInterval(vector<vector<int>>& intervals,
                                       vector<int>& toBeRemoved) {

        return {};
    }
};

int main() {
    Solution* sol = new Solution();
    vector<vector<int>> intervals;
    vector<int> toBeRemoved;

    auto print_vvi = [&](vector<vector<int>> v) {
        int n = v.size();
        for (int i = 0; i < n; i++)
            cout << "[" << v[i][0] << " " << v[i][1] << "] ";
        cout << endl;
    };
    auto printv = [&](vector<int> v) {
        for (int num : v) cout << num << " ";
        cout << endl;
    };

    {
        cout << "TESTCASE 1\n";
        intervals = { { 10, 50 }, { 60, 120 }, { 140, 210 } };
        toBeRemoved = {};
        print_vvi(sol->removeInterval(intervals, toBeRemoved));
    }

    {
        cout << "TESTCASE 2\n";
        intervals = { { 10, 50 }, { 60, 120 }, { 140, 210 } };
        toBeRemoved = {};
        print_vvi(sol->removeInterval(intervals, toBeRemoved));
    }

    delete sol;
}
