// https://codeforces.com/problemset/problem/1883/B

#include <bits/stdc++.h>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

void solve() {
    int n, k;
    cin >> n >> k;
    string s;
    cin >> s;

    // frequency counter
    unordered_map<char, int> hm;
    for (char c : s) {
        if (hm.find(c) == hm.end()) hm[c] = 0;
        hm[c] += 1;
    }

    // palidrome: all values are even, except 1
    // remove all extra odd numbers. see if that count <= k

    int count = 0;
    for (auto [k, v] : hm) {
        // cout << k << ":" << v << endl;
        if (v % 2 != 0) count += 1;
    }

    (count <= k + 1) ? cout << "YES\n" : cout << "NO\n";
}

int main() {
    setupIO();
    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
