// Minimize Max Distance to Gas Station
// https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findSmallestMaxDist(vector<int>& stations, int k) {
        // Code here
        int n = stations.size();

        // 3  6  12  19  33  44  67  72  89  95
        for (int i = 1; i < n; i++) {
            int d = stations[i] - stations[i - 1];
            stations[i - 1] = d;
        }
        // 3  6   7  14  11  23  5   17  6  [95] <- we just ignore the last num

        while (k) {
            // find the best spot to place, which is the largest dist
            int largest = -1, largest_idx = -1;
            for (int i = 0; i < n - 1; i++) {
                if (largest < stations[i]) {
                    largest = stations[i];
                    largest_idx = i;
                }
            }
            stations[largest_idx] = stations[largest_idx] / 2;
            k--;
        }

        int total_dist = 0;
        for (int i = 0; i < n - 1; i++) {
            total_dist += stations[i];
        }

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
