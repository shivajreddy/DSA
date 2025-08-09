// C. Yarik and Array
// https://codeforces.com/problemset/problem/1899/C

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

bool has_same_parity(const vector<int>& v, int idx) {
    if (idx == 0) return false;
    int prev = abs(v[idx - 1]);
    int curr = abs(v[idx]);
    // if (prev % 2 == 0 && curr % 2 == 0) return true;
    // if (prev % 2 == 1 && curr % 2 == 1) return true;
    // return false;
    return (prev % 2 == curr % 2);
}

void solve() {
    int n;
    cin >> n;
    vi v(n);
    loop(i, 0, n) cin >> v[i];

    int sum = v[0];
    int res = v[0];

    loop(i, 1, n) {
        // if (sum <= 0 || has_same_parity(v, i)) {
        if (sum <= 0 || (abs(v[i - 1]) % 2 == abs(v[i]) % 2)) {
            sum = v[i];
        } else {
            sum += v[i];
        }
        res = max(res, sum);
    }

    cout << res << endl;
}

void solve2() {
    int n;
    cin >> n;
    vi v(n);
    loop(i, 0, n) cin >> v[i];

    int sum = 0;
    int res = v[0];

    loop(i, 0, n) {
        if (sum <= 0 || has_same_parity(v, i)) {
            sum = v[i];
        } else {
            sum += v[i];
        }
        res = max(res, sum);
    }

    cout << res << endl;
}
