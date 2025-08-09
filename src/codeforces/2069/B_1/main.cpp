// B. Set of Strangers
// https://codeforces.com/problemset/problem/2069/B

#include <bits/stdc++.h>
#include <vector>
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
    int n, m;
    cin >> n >> m;
    vector<vector<int>> matrix(n, vector<int>(m));
    loop(i, 0, n) loop(j, 0, m) cin >> matrix[i][j];

    loop(i, 0, n) loop(j, 0, m) {
    }
}
