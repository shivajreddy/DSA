// B. Not Dividing
// https://codeforces.com/problemset/problem/1794/B

#include <bits/stdc++.h>
using namespace std;

void setupIO() {
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);
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

    for (int i = 0; i < n; i++)
        if (v[i] == 1) v[i] = 2;

    for (int i = 1; i < n; i++)
        if (v[i] % v[i - 1] == 0) v[i] += 1;

    /*
    for (int i = 0; i < n; i++) {
        int curr = v[i];
        int fix_left = 0, fix_right = 0;
        if (i != 0) {
            int left = v[i - 1];
            fix_left = curr % left == 0 ? 1 : 0;
            // v[i] += (curr % left == 0 ? 1 : 0);
        }
        if (i != n - 1) {
            int right = v[i + 1];
            fix_right = right % curr == 0 ? 1 : 0;
            // v[i] += (right % curr == 0 ? 1 : 0);
        }
        v[i] += (fix_left + fix_right);
    }
    // */
    for (int num : v) {
        cout << num << " ";
    }
    cout << endl;

    /*
    for (int i = n - 2; i >= 0; i--) {
        int a = v[i], b = v[i + 1];

        if (b % a != 0) continue;

        if (a == 1) {
            v[i] = b == 2 ? 3 : 2;
        } else {
            v[i] += 1;
        }

        // cout << v[i] << " ";
    }
    */
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
