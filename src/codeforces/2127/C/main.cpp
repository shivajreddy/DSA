// C. Trip Shopping
// https://codeforces.com/contest/2127/problem/C

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve() {
    int n, k;
    cin >> n >> k;

    vi a(n);
    loop(i, 0, n) cin >> a[i];
    vi b(n);
    loop(i, 0, n) cin >> b[i];
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
