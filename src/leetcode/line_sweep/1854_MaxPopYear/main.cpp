// 1854. Maximum Population Year
// https://leetcode.com/problems/maximum-population-year

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maximumPopulation(vector<vector<int>>& logs) {
        return -1;
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
