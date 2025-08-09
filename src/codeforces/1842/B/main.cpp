// B. Tenzing and Books
// https://codeforces.com/problemset/problem/1842/B

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

    vi pre[3];
    loop(i, 0, 3) {
        int s = 0;
        pre[i].push_back(s);
        loop(j, 0, n) {
            int a;
            cin >> a;
            if ((s | a) != s) {
                s |= a;
                pre[i].push_back(s);
            }
        }
    }
    bool ans = 0;
    for (int A : pre[0]) {
        for (int B : pre[1]) {
            for (int C : pre[2]) {
                if ((A | B | C) == x) ans = true;
            }
        }
    }

    cout << (ans ? "YES\n" : "NO\n");
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
