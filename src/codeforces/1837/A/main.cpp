// https://codeforces.com/problemset/problem/1837/B
// B. Comparison String

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
    int n;
    cin >> n;

    string s;
    cin >> s;

    int res = -1;

    int len = 1;
    for (int i = 1; i < n; i++) {
        if (s[i] == s[i - 1]) {
            len++;
        } else {
            len = 1; // reset
        }
        res = max(res, len);
    }

    res = res == -1 ? 2 : res + 1;

    cout << res << "\n";
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
