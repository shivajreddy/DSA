// A. AB Balance
// https://codeforces.com/problemset/problem/1606/A

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
    while (tc--) solve();
}

void solve() {
    string s;
    cin >> s;
    int n = s.size();

    if (s[0] != s[n - 1]) {
        s[n - 1] = s[0] == 'a' ? 'a' : 'b';
    }
    cout << s << endl;
}
