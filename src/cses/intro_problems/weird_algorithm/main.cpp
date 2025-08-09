// Weird Algorithm
// https://cses.fi/problemset/task/1068

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve() {
    ll n;
    cin >> n;

    while (n != 1) {
        cout << n << " ";
        if (n % 2 == 0)
            n /= 2;
        else
            n = n * 3 + 1;
    }
    cout << 1 << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    solve();
    // int tc;
    // cin >> tc;
    // while (tc--) solve();
}
