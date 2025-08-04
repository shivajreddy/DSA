// Minimize Max Distance to Gas Station
// https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findSmallestMaxDist(vector<int>& stations, int k) {
        // Code here
        return 0.0;
    }
};

int main() {
    Solution* sol = new Solution();
    vector<int> stations;
    int k;

    {
        stations = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
        k = 9;
        cout << "EXPECTED: " << 0.5 << endl;
        cout << "RECEIVED: " << sol->findSmallestMaxDist(stations, k) << endl;
    }

    {
        stations = { 3, 6, 12, 19, 33, 44, 67, 72, 89, 95 };
        k = 10;
        cout << "EXPECTED: " << 14.00 << endl;
        cout << "RECEIVED: " << sol->findSmallestMaxDist(stations, k) << endl;
    }

    delete sol;
}
