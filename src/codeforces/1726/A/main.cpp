// A. Mainak and Array
// https://codeforces.com/problemset/problem/1726/A

#include <bits/stdc++.h>
#include <climits>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

void solve() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    int res = INT_MIN;

    // no rotations
    for (int i = 0; i < n; i++) {
        int prev_idx = i == 0 ? n - 1 : i - 1;
        res = max(res, v[prev_idx] - v[i]);
    }

    // try with all numbers in range [1..n-1] at [n-1]
    for (int i = 1; i < n; i++)
        res = max(res, v[i] - v[0]);

    // try with place all numbers in range[0..n-2] at [0]
    for (int i = 0; i < n - 1; i++)
        res = max(res, v[n - 1] - v[i]);

    cout << res << endl;
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
