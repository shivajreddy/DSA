// B. Collecting Game
// https://codeforces.com/problemset/problem/1904/B

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
    int n;
    cin >> n;

    vector<ll> original_v(n);
    loop(i, 0, n) cin >> original_v[i];

    // copy and sort the input, (n log n)
    vector<ll> v = original_v;
    sort(v.begin(), v.end());

    vector<ll> prefix = v;
    loop(i, 1, n) prefix[i] = prefix[i] + prefix[i - 1];

    // track count of scores that each number can collect
    unordered_map<int, int> hm;
    hm[v[n - 1]] = n - 1; // last number can reach all

    for (int i = n - 2; i >= 0; i--) {
        // if current prefix is >= next number, then current number
        // can reach the same count as the next number
        if (prefix[i] >= v[i + 1]) {
            hm[v[i]] = hm[v[i + 1]];
        } else {
            hm[v[i]] = i;
        }
    }

    // output results
    for (int num : original_v)
        cout << hm[num] << " ";
    cout << "\n";
}
