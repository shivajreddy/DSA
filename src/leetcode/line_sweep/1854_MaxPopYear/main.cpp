// 1854. Maximum Population Year
// https://leetcode.com/problems/maximum-population-year

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        int n = logs.size();

        vector<pair<int, char>> all(2 * n);
        for (int i = 0; i < n; i++) {
            int s = logs[i][0], e = logs[i][1];
            all[i * 2] = { s, 's' };
            all[i * 2 + 1] = { e, 'e' };
        }

        // for (int i = 0; i < 2 * n; i++)
        //     cout << "[" << all[i].first << '-' << all[i].second << "] ";
        // cout << endl;

        sort(all.begin(), all.end());

        int res;
        int max_pop = -1;
        int curr = 0;

        for (int i = 0; i < 2 * n; i++) {
            // cout << "[" << all[i].first << '-' << all[i].second << "] ";
            if (all[i].second == 's') {
                curr++;
            } else {
                curr--;
            }

            if (curr > max_pop) {
                max_pop = curr;
                res = all[i].first;
            }
        }
        return res;

        // for (int i = 0; i < 2 * n; i++)
        //     cout << "[" << all[i].first << '-' << all[i].second << "] ";
        // cout << endl;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<vector<int>> logs;

    {
        logs = { { 1993, 1999 }, { 2000, 2010 } };
        cout << sol->maximumPopulation(logs) << endl;
    }
    {
        logs = { { 1950, 1961 }, { 1960, 1971 }, { 1970, 1981 } };
        cout << sol->maximumPopulation(logs) << endl;
    }

    delete sol;
}
