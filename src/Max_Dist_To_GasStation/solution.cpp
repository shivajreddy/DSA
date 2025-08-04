// https://www.geeksforgeeks.org/dsa/minimize-the-maximum-distance-between-adjacent-points-after-adding-k-points-anywhere-in-between/

#include <bits/stdc++.h>
using namespace std;

bool is_possible(double mid, int arr[], int n, int k) {
    int used = 0;
    for (int i = 1; i < n; i++) {
        used += (int)(arr[i] - arr[i - 1]) / mid;
    }
    return used <= k;
}

double minMaxDist(int stations[], int n, int k) {
    double lo = 0, hi = 1e8;
    while (hi - lo > 1e-6) {
        double mid = (lo + hi) / 2.0;
        if (is_possible(mid, stations, n, k))
            hi = mid;
        else
            lo = mid;
    }
    return lo;
}

int main() {

    int arr[] = { 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 };
    int K = 9;
    int N = sizeof(arr) / sizeof(arr[0]);

    cout << minMaxDist(arr, N, K);

    return 0;
}
