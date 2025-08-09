// A. Mix Mex Max
// https://codeforces.com/contest/2127/problem/A

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

    vi a(n);
    loop(i, 0, n) cin >> a[i];

    // check for any zeros
    bool has_zero = false;
    loop(i, 0, n) {
        if (a[i] == 0) {
            has_zero = true;
            cout << "NO\n";
            return;
        }
    }

    // pick the first non -1 as the target
    int target = -1;
    loop(i, 0, n) {
        if (a[i] != -1) {
            target = a[i];
            break;
        }
    }

    // check if all numbers are same as target (target is -1 if all nums are -1)
    loop(i, 0, n) {
        if (a[i] == -1) continue;
        if (a[i] != target) {
            cout << "NO\n";
            return;
        }
    }

    cout << "YES\n";
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
