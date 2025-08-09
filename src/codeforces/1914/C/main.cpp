// C. Quests
// https://codeforces.com/problemset/problem/1914/C

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

void solve();

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}

void solve() {
    int n, k;
    cin >> n >> k;

    vi a(n);
    loop(i, 0, n) cin >> a[i];

    vi b(n);
    loop(i, 0, n) cin >> b[i];

    int sum = 0, res = 0, mx = 0;
    loop(i, 0, min(n, k)) {
        sum += a[i];
        mx = max(mx, b[i]);
        // sum + max * remaining-turns
        res = max(res, sum + mx * (k - i - 1));
    }

    cout << res << endl;
}
