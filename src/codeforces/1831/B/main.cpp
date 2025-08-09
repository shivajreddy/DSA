// B. Array merging
// https://codeforces.com/problemset/problem/1831/B

#include <bits/stdc++.h>
#include <unordered_map>
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
    int n;
    cin >> n;
    vi a(n), b(n);
    loop(i, 0, n) cin >> a[i];
    loop(i, 0, n) cin >> b[i];

    unordered_map<ll, ll> a_map;
    int i = 0;
    while (i < n) {
        ll len = 1;
        while (i + 1 < n && a[i + 1] == a[i]) {
            len++;
            i += 1;
        }
        a_map[a[i]] = max(len, a_map[a[i]]);
        i++;
    }

    unordered_map<ll, ll> b_map;
    i = 0;
    while (i < n) {
        ll len = 1;
        while (i + 1 < n && b[i + 1] == b[i]) {
            len++;
            i += 1;
        }
        b_map[b[i]] = max(len, b_map[b[i]]);
        i++;
    }

    ll res = 0;

    // Collect all unique values from both arrays
    set<ll> all_values;
    for (auto [num, count] : a_map) {
        all_values.insert(num);
    }
    for (auto [num, count] : b_map) {
        all_values.insert(num);
    }

    // Check all values, treating missing values as 0
    for (ll num : all_values) {
        ll a_count = (a_map.find(num) != a_map.end()) ? a_map[num] : 0;
        ll b_count = (b_map.find(num) != b_map.end()) ? b_map[num] : 0;
        res = max(res, a_count + b_count);
    }

    cout << res << endl;
}
