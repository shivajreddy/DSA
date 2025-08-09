// B. Maximum Sum
// https://codeforces.com/problemset/problem/1832/B

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
    int n, k;
    cin >> n >> k;

    vi a(n);
    loop(i, 0, n) cin >> a[i];

    sort(a.begin(), a.end());

    vector<ll> prefix(n);
    prefix[0] = a[0];
    loop(i, 1, n) prefix[i] = prefix[i - 1] + a[i];

    ll res = -1;

    loop(i, 0, k + 1) {

        int no_of_left_operations = i;
        int no_of_right_operations = k - i;

        // left idx will increase by 2, if chosen left operation
        int left_idx = 2 * no_of_left_operations;

        // right idx will reduce by 1, if chosen right operation
        int right_idx = n - 1 - no_of_right_operations;

        ll sum = prefix[right_idx] - (left_idx == 0 ? 0 : prefix[left_idx - 1]);
        res = max(res, sum);
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
