// C. Gellyfish and Flaming Peony
// https://codeforces.com/contest/2116/problem/C

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

    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    // for (int num : v) {
    //     cout << num << " ";
    // }
    // cout << endl;

    int res = 0;

    while (true) {
        int smallest = INT_MAX;
        for (int i = 0; i < n; i++) {
            smallest = min(smallest, v[i]);
        }
        for (int i = 0; i < n; i++) {
            if (v[i] == smallest) continue;
            int rem = v[i] % smallest;
            // v[i]
        }
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
