// B. Line Segments
// https://codeforces.com/contest/2119/problem/B

#include <bits/stdc++.h>
#include <cmath>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

// Euclidean distance
double get_dist(double x1, double y1, double x2, double y2) {
    return sqrt(pow(abs(x1 - x2), 2) + pow(abs(y1 - y2), 2));
}

void solve() {
    int n;
    cin >> n;
    // cout << "n: " << n << endl;

    int px, py, qx, qy;
    cin >> px >> py >> qx >> qy;
    // cout << px << " " << py << " " << qx << " " << qy << " " << endl;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    double target_distance = get_dist(px, py, qx, qy);

    long long max_distance = 0; // Max. distance we can reach from S
    long long longest_d = -1;
    for (long long d : v) {
        max_distance += d;
        longest_d = max(longest_d, d);
    }
    // cout << "MAX DIST: " << max_distance << endl;
    // cout << "TARGET DIST: " << target_distance << endl;

    // Check if we can reach
    if (max_distance < target_distance) {
        cout << "NO\n";
        return;
    }
    long long remaining_dist = max_distance - longest_d;
    if (remaining_dist >= longest_d - target_distance) {
        cout << "YES\n";
        return;
    }
    cout << "NO\n";
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
