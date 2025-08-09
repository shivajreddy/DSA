// https://codeforces.com/problemset/problem/1878/C

#include <iostream>
// #include <bits/stdc++.h>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

void solve() {
    long long n, k, x;
    cin >> n >> k >> x;

    long long min_sum = (k * (k + 1)) / 2;
    long long max_sum = (k * (2 * n - k + 1)) / 2;
    if (min_sum <= x and x <= max_sum) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}

int main() {
    setupIO();
    long long tc;
    cin >> tc;
    while (tc--)
        solve();
}
