// A. Strange Partition
// https://codeforces.com/problemset/problem/1471/A

// { Imports, TypeNames, Macros
#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
// }

void solve() {
    int n, x;
    cin >> n >> x;

    vi a(n);
    loop(i, 0, n) cin >> a[i];

    ll mn = 0, mx = 0;

    ll total_sum = 0;
    for (int num : a) {

        // can do this or just directly do ceiling division
        // int count = num / x;
        // int rem = num % x;
        // mx += rem == 0 ? count : count + 1;

        mx += (num + x - 1) / x; // ceiling division

        total_sum += num;
    }
    mn += (total_sum + x - 1) / x; // ceiling division

    cout << mn << " " << mx << endl;
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
