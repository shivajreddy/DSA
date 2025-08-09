// C. Double Perspective
// https : // codeforces.com/contest/2130/problem/C

// { Imports, TypeNames, Macros
#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
// }

void solve() {
    int n;
    cin >> n;

    vector<pii> edges(n);
    loop(i, 0, n) cin >> edges[i].first >> edges[i].second;

    if (n == 1) {
        cout << "1\n1\n";
        return;
    }
    if (n == 2) {
        cout << "2\n1 2\n";
        return;
    }

    vi space(2 * n + 1); // 2n for n pairs. +1 for 1-indexing
    vi nodes;

    loop(i, 0, n) {
        int a = edges[i].first, b = edges[i].second;

        bool did = false;
        loop(j, a, b) {
            if (space[j] == 0) {
                space[j] = 1;
                did = true;
            }
        }

        if (did) nodes.push_back(i + 1);
    }

    cout << nodes.size() << endl;
    for (int node : nodes) cout << node << " ";
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
