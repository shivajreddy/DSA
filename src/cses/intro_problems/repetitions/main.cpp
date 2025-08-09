// Repetitions
// https://cses.fi/problemset/task/1069

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve() {
    string s;
    cin >> s;

    int res = 1;
    int curr = 1;

    int n = s.size();
    for (int i = 1; i < n; i++) {
        if (s[i - 1] != s[i]) curr = 0;
        curr++;
        res = max(res, curr);
    }
    cout << res << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    solve();
    // int tc;
    // cin >> tc;
    // while (tc--) solve();
}
