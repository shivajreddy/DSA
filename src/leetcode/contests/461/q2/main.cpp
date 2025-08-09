// Q2. Maximum Balanced Shipments
// https://leetcode.com/contest/weekly-contest-461/problems/maximum-balanced-shipments/

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int maxBalancedShipments(vector<int>& weight) {
        int n = weight.size();
        int segs = 0;
        int i = 1;
        while (i < n) {
            if (weight[i - 1] > weight[i]) {
                segs++;
                i += 2;
            } else {
                i++;
            }
        }
        return segs;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<int> weight;
    {
        weight = { 2, 5, 1, 4, 3 };
        cout << "EXPECTED: " << 2 << endl;
        cout << "RECEIVED: " << sol->maxBalancedShipments(weight) << endl;
    }
    {
        weight = { 4, 4 };
        cout << "EXPECTED: " << 0 << endl;
        cout << "RECEIVED: " << sol->maxBalancedShipments(weight) << endl;
    }
    {
        weight = { 1000, 999, 998 };
        cout << "EXPECTED: " << 1 << endl;
        cout << "RECEIVED: " << sol->maxBalancedShipments(weight) << endl;
    }
    delete sol;
}
