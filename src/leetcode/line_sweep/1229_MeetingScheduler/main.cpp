// 1229. Meeting Scheduler
// https://leetcode.com/problems/meeting-scheduler

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    vector<int> minAvailableDuration(vector<vector<int>>& slots1,
                                     vector<vector<int>>& slots2,
                                     int duration) {
        return { -1, -1 };
    }
};

int main() {
    Solution* sol = new Solution();
    vector<vector<int>> slots1, slots2;
    int duration;

    auto print_vvi = [&](vector<vector<int>> v) {
        int n = v.size();
        for (int i = 0; i < n; i++)
            cout << "[" << v[i][0] << " " << v[i][1] << "] ";
        cout << endl;
    };
    auto printv = [&](vector<int> v) {
        for (int num : v) cout << num << " ";
    };

    {
        slots1 = { { 10, 50 }, { 60, 120 }, { 140, 210 } };
        slots2 = { { 0, 15 }, { 60, 70 } };
        duration = 8;
        printv(sol->minAvailableDuration(slots1, slots2, duration));
    }
    {
        slots1 = { { 10, 50 }, { 60, 120 }, { 140, 210 } };
        slots2 = { { 0, 15 }, { 60, 70 } };
        duration = 12;
        printv(sol->minAvailableDuration(slots1, slots2, duration));
    }

    delete sol;
}
