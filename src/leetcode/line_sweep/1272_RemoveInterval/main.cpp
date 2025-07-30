// 1272. Remove Interval
// https://leetcode.com/problems/remove-interval

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<vector<int>> removeInterval(vector<vector<int>>& intervals,
                                       vector<int>& toBeRemoved) {

        vector<vector<int>> result;

        for (const auto& interval : intervals) {
            // Case 1: No overlap - interval is completely before toBeRemoved
            if (interval[1] <= toBeRemoved[0]) {
                result.push_back(interval);
            }
            // Case 2: No overlap - interval is completely after toBeRemoved
            else if (interval[0] >= toBeRemoved[1]) {
                result.push_back(interval);

            }
            // Case 3: There is overlap - handle the remaining parts
            else {
                // Add left part if it exists (interval starts before
                // toBeRemoved)
                if (interval[0] < toBeRemoved[0]) {
                    result.push_back({ interval[0], toBeRemoved[0] });
                }
                // Add right part if it exists (interval ends after toBeRemoved)
                if (interval[1] > toBeRemoved[1]) {
                    result.push_back({ toBeRemoved[1], interval[1] });
                }
                // Note: If interval is completely contained in toBeRemoved,
                // both conditions above are false, so nothing gets added
            }
        }

        return result;
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
        intervals = { { 0, 2 }, { 3, 4 }, { 5, 7 } };
        toBeRemoved = { 1, 6 };
        print_vvi(sol->removeInterval(intervals, toBeRemoved));
    }

    {
        intervals = { { 0, 5 } };
        toBeRemoved = { 2, 3 };
        print_vvi(sol->removeInterval(intervals, toBeRemoved));
    }

    {
        intervals = { { -5, -4 }, { -3, -2 }, { 1, 2 }, { 3, 5 }, { 8, 9 } };
        toBeRemoved = { -1, 4 };
        print_vvi(sol->removeInterval(intervals, toBeRemoved));
    }

    delete sol;
}
