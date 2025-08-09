// A. Mocha and Math
// https://codeforces.com/problemset/problem/1559/A

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve() {
    int n;
    cin >> n;
    vi a(n);
    loop(i, 0, n) cin >> a[i];

    int res = a[0];
    loop(i, 1, n) {
        res &= a[i];
    }
    cout << res << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    int tc;
    cin >> tc;
    while (tc--) solve();
}
