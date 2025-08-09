// 134. Gas Station
// https://leetcode.com/problems/gas-station/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int canCompleteCircuit(vector<int>& gas, vector<int>& cost) {
        int n = gas.size();

        // check if it possible at all
        long long total_gas = 0, total_cost = 0;
        for (int i = 0; i < n; i++) {
            total_gas += gas[i];
            total_cost += cost[i];
        }
        if (total_gas < total_cost) return -1;

        int res = 0;
        int tank = 0;
        for (int i = 0; i < n; i++) {
            // fill gas at current station
            tank += gas[i];
            // reamining after going to next
            tank -= cost[i];
            if (tank < 0) {
                tank = 0;
                res = i + 1; // hoping the next pos is the result
            }
        }
        return res;
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
        cout << "EXPECTED: " << -1 << endl;
        cout << "RECEIVED: " << sol->canCompleteCircuit(gas, cost) << endl;
    }
    {
        gas = { 3, 1, 1 };
        cost = { 1, 2, 2 };
        cout << "EXPECTED: " << 0 << endl;
        cout << "RECEIVED: " << sol->canCompleteCircuit(gas, cost) << endl;
    }

    delete sol;
}
