// Q3. Minimum Time to Activate String
// https://leetcode.com/contest/weekly-contest-461/problems/minimum-time-to-activate-string/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minTime(string s, vector<int>& order, int k) {
        int res = -1;
        return res;
    }
};

int main() {
    Solution* sol = new Solution();
    string s;
    vector<int> order;
    int k;
    {
        s = "abc";
        order = { 1, 0, 2 };
        k = 2;
        cout << "EXPECTED: " << 0 << endl;
        cout << "RECEIVED: " << sol->minTime(s, order, k) << endl;
    }
    {
        s = "cat";
        order = { 0, 2, 1 };
        k = 6;
        cout << "EXPECTED: " << 2 << endl;
        cout << "RECEIVED: " << sol->minTime(s, order, k) << endl;
    }
    {
        s = "xy";
        order = { 0, 1 };
        k = k;
        cout << "EXPECTED: " << -1 << endl;
        cout << "RECEIVED: " << sol->minTime(s, order, k) << endl;
    }
    delete sol;
}
