// B. 250 Thousand Tons of TNT
// https://codeforces.com/problemset/problem/1899/B

#include <bits/stdc++.h>
#include <climits>
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

/*
ll get_max_diff(const vi& v, int k) {
    ll mn = 1e18, mx = -1e18;
    for (int i = 0; i < v.size(); i += k) {
        ll sum = 0;
        for (int j = i; j < i + k; j++) {
            sum += v[j];
        }
        mn = min(mn, sum);
        mx = max(mx, sum);
    }
    return mx - mn;
}

void solve() {
    int n;
    cin >> n;
    vi v(n);
    loop(i, 0, n) cin >> v[i];

    ll res = -1;
    int k = 1;
    loop(k, 1, n + 1) {
        if (n % k != 0) continue;
        res = max(res, get_max_diff(v, k));
    }

    cout << res << endl;
}
*/

ll get_max_diff(const vi& v, int k) {
    ll mn = 1e18, mx = -1e18;

    ll curr_sum = 0;
    ll curr_k = 0;
    for (int num : v) {
        curr_sum += num;
        curr_k++;
        if (curr_k == k) {
            mn = min(mn, curr_sum);
            mx = max(mx, curr_sum);
            curr_k = 0;
            curr_sum = 0;
        }
    }
    return mx - mn;
}

void solve() {
    int n;
    cin >> n;
    vi v(n);
    loop(i, 0, n) cin >> v[i];

    int k = 1;
    ll res = 0;

    loop(k, 1, n + 1) {
        if (n % k != 0) continue;
        res = max(res, get_max_diff(v, k));
    }

    cout << res << endl;
}
