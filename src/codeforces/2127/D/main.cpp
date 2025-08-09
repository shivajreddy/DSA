// D. Root was Built by Love, Broken by Destiny
// https://codeforces.com/contest/2127/problem/D

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve() {
    int n, m;
    cin >> n >> m;

    if (n % 2 == 0) {
        cout << n - 1 << endl;
    } else {
        cout << (n + 1) / 2 + (n / 2) - 1 << endl;
    }
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
