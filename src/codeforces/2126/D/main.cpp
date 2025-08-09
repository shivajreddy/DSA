// D. This Is the Last Time
// https://codeforces.com/contest/2126/problem/D

#include <bits/stdc++.h>
#include <unordered_set>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
#define us unordered_set

void setupIO() {
    // ios::sync_with_stdio(false);
    // cin.tie(nullptr);
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

void dfs(vector<array<int, 3>>& a, int idx, int coins, us<int>& visited,
         int* res, int hi) {
    array<int, 3> casino = a[idx];
    if (casino[0] > coins || coins > casino[1]) return; // cant enter casino
    if (*res == hi) return;      // exit early if already found the highest
    *res = max(*res, casino[2]); // udpate res
    visited.insert(idx);         // mark as visited
    loop(i, 0, a.size()) {
        if (visited.count(i) == 0) dfs(a, i, casino[2], visited, res, hi);
    }
    visited.erase(idx); // backtrack
}

#define ai3 array<int, 3>

void solve() {
    int n, k;
    cin >> n >> k;

    vector<array<int, 3>> a(n);
    loop(i, 0, n) cin >> a[i][0] >> a[i][1] >> a[i][2];

    // sort casinos based on l
    sort(a.begin(), a.end(),
         [](const ai3& x, const ai3& y) { return x[0] < y[0]; });

    int res = k;
    for (auto c : a) {
        int l = c[0], r = c[1], coins = c[2];
        if (l <= res && res <= r) res = max(res, coins);
    }
    cout << res << endl;

    /*
    int highest = 0;
    loop(i, 0, n) {
        array<int, 3> casino;
        loop(j, 0, 3) cin >> casino[j];
        highest = max(highest, casino[2]);
        a[i] = casino;
    }

    int res = k;

    loop(i, 0, n) {
        unordered_set<int> visited;
        dfs(a, i, k, visited, &res, highest);
    }

    cout << res << endl;
    */
}
