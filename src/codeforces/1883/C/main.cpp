// C. Raspberries
// https://codeforces.com/problemset/problem/1883/C

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

    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    int count_even = 0;
    int res = 5; // max it could be is 4

    for (int num : v) {
        if (num % k == 0) {
            cout << "0\n";
            return;
        }
        if (num % 2 == 0) count_even++;
        res = min(res, k - (num % k));
    }

    if (k == 4) {
        // one liner
        res = min(res, count_even >= 2 ? 0 : 2 - count_even);

        // more clear
        // if (count_even >= 2) res = 0;
        // if (count_even == 1) res = min(res, 1);
        // if (count_even == 0) res = min(res, 2);
    }
    cout << res << "\n";
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
