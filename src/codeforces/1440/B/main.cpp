// B. Sum of Medians
// https://codeforces.com/problemset/problem/1440/B

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
    ll sub_arr_sizee, count;
    cin >> sub_arr_sizee >> count;
    ll n = sub_arr_sizee * count;
    // cout << "n:" << n << endl;

    vector<ll> a(n);
    loop(i, 0, n) cin >> a[i];

    int med = sub_arr_sizee / 2;
    ll res = 0;
    for (int i = n; i >= 0 && count > 0;) {
        i = i - med - 1;
        res += a[i];
        count--; // take these many medians
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
