// Minimize Max Distance to Gas Station
// https://www.geeksforgeeks.org/problems/minimize-max-distance-to-gas-station/1

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    double findSmallestMaxDist(vector<int>& stations, int k) {

        int n = stations.size();

        double lo = 0.0, hi = stations[n - 1] - stations[0];

        auto possible = [&](double d, vector<int>& arr) {
            int n = arr.size();
            int used = 0;
            for (int i = 1; i < n; i++) {
                // used += (int)((arr[i] - arr[i - 1]) / d);
                used += ceil((arr[i] - arr[i - 1]) / d) - 1;
            }
            return used <= k;
        };

        // Increase precision - use 1e-9 instead of 1e-6
        while (hi - lo >= 1e-9) {
            double mid = (lo + hi) / 2.0;
            if (possible(mid, stations))
                hi = mid;
            else
                lo = mid;
        }

        // Round to 2 decimal places
        // return lo;
        // return round(lo * 100.0) / 100.0;
        // return hi;
        return round(hi * 100.0) / 100.0; // Try returning hi instead of lo
    }
};

class SolutionAlternative {
public:
    double findSmallestMaxDist(vector<int>& stations, int k) {
        int n = stations.size();
        double lo = 0.0, hi = stations[n - 1] - stations[0];

        auto possible = [&](double d, vector<int>& arr) {
            int n = arr.size();
            int used = 0;
            for (int i = 1; i < n; i++) {
                used += ceil((arr[i] - arr[i - 1]) / d) - 1;
            }
            return used <= k;
        };

        // Run fixed number of iterations for better precision
        for (int i = 0; i < 100; i++) {
            double mid = (lo + hi) / 2.0;
            if (possible(mid, stations))
                hi = mid;
            else
                lo = mid;
        }

        return round(hi * 100.0) / 100.0;
    }
};

int main() {
    Solution* sol = new Solution();

    // /*
    int tc;
    cin >> tc;
    while (tc--) {

        int n;
        cin >> n;
        vector<int> stations(n);
        for (int i = 0; i < n; i++) cin >> stations[i];
        int k;
        cin >> k;

        // cout << "EXPECTED: " << 1.73 << endl;
        cout << "RECEIVED: " << sol->findSmallestMaxDist(stations, k) << endl;
    }
    // */

    /*
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
        k = 2;
        cout << "EXPECTED: " << 14.00 << endl;
        cout << "RECEIVED: " << sol->findSmallestMaxDist(stations, k) << endl;
    }
    // */

    delete sol;
}
