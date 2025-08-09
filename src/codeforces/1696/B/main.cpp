// B. NIT Destroys the Universe
// https://codeforces.com/problemset/problem/1696/B

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
    // cout << "current_test: " << current_test << endl;
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    // check if all 0
    int zero_count = 0;
    for (int num : v)
        zero_count += num == 0 ? 1 : 0;

    int i = 0;
    int segments = 0;
    while (i < n) {
        if (v[i] != 0) {
            while (i < n && v[i] != 0) {
                i++;
            }
            segments++;
        }
        i++;
    }

    if (zero_count == n) {
        cout << "0\n";
    } else if (zero_count == 0) {
        cout << "1\n";
    } else {
        if (segments == 1) {
            cout << "1\n";
        } else {
            cout << "2\n";
        }
    }
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
