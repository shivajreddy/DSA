// B. Odd Grasshopper
// https://codeforces.com/problemset/problem/1607/B

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
    while (tc--) solve();
}

void solve() {
    ll x, n;
    cin >> x >> n;

    ll d; // final distance from x

    switch (n % 4) {
    case 0:
        d = 0;
        break;
    case 1:
        d = n;
        break;
    case 2:
        d = -1;
        break;
    case 3:
        d = -n - 1;
        break;
    }

    if (x % 2 == 0) {
        cout << x - d << endl;
    } else {
        cout << x + d << endl;
    }
}
