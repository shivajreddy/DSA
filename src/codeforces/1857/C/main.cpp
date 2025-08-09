// C. Assembly via Minimums
// https://codeforces.com/problemset/problem/1857/C

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve() {
    int n;
    cin >> n;
    int size = (n * (n - 1)) / 2;

    unordered_map<int, int> hm;
    int a[size];
    loop(i, 0, size) {
        cin >> a[i];
        hm[a[i]]++;
    }

    for (auto [k, v] : hm) cout << k << ":" << v << " ";
    // loop(i, 0, size) cout << a[i] << " ";
    cout << endl;
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
