// 57. Insert Interval
// https://leetcode.com/problems/insert-interval

#include <bits/stdc++.h>
#include <vector>
using namespace std;

class Solution {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals,
                               vector<int>& newInterval) {
        int n = intervals.size();

        vector<vector<int>> result;
        int i = 0;

        // Step 1: Add all intervals that end before newInterval starts (no
        // overlap)
        while (i < n && intervals[i][1] < newInterval[0]) {
            result.push_back(intervals[i]);
            i++;
        }

        // Step 2: Merge all overlapping intervals with newInterval
        while (i < n && intervals[i][0] <= newInterval[1]) {
            newInterval[0] = min(newInterval[0], intervals[i][0]);
            newInterval[1] = max(newInterval[1], intervals[i][1]);
            i++;
        }
        result.push_back(newInterval);

        // Step 3: Add all remaining intervals (no overlap)
        while (i < n) {
            result.push_back(intervals[i]);
            i++;
        }

        return result;
    }
};

class Solution2 {
public:
    vector<vector<int>> insert(vector<vector<int>>& intervals,
                               vector<int>& newInterval) {
        int n = intervals.size();

        intervals.push_back(newInterval);
        sort(intervals.begin(), intervals.end()); // n.log(n)

        vector<vector<int>> res;
        res.push_back(intervals[0]);

        for (int i = 1; i < n + 1; i++) { // n+1 since we added new-interal
            vector<int> prev = res.back();
            if (prev[0] <= intervals[i][0] && intervals[i][1] <= prev[1]) {
                continue;
            }
            // new interval merges with previous intnerval
            if (intervals[i][0] <= prev[1]) {
                int s = min(prev[0], intervals[i][0]); // min of both starts
                int e = max(prev[1], intervals[i][1]); // max of both ends
                res.pop_back();
                res.push_back({ s, e });
            } else { // doesnt merge, so add this interval
                res.push_back(intervals[i]);
            }
        }

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
