// 134. Gas Station
// https://leetcode.com/problems/gas-station/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        return -1;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<int> gas, cost;

    {
        gas = { 1, 2, 3, 4, 5 };
        cost = { 3, 4, 5, 1, 2 };
        cout << "EXPECTED: " << 3 << endl;
        cout << "RECEIVED: " << sol->canCompleteCircuit(gas, cost) << endl;
    }
    {
        gas = { 2, 3, 4 };
        cost = { 3, 4, 3 };
        cout << "EXPECTED: " << 3 << endl;
        cout << "RECEIVED: " << sol->canCompleteCircuit(gas, cost) << endl;
    }

    delete sol;
}
