// B. Make It Increasing
// https://codeforces.com/problemset/problem/1675/B

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
    int n;
    cin >> n;

    vi a(n);
    loop(i, 0, n) cin >> a[i];

    // cout << "GIVEN ARRAY: ";
    // loop(i, 0, n) cout << a[i] << " ";
    // cout << endl;

    int res = 0;
    for (int i = n - 2; i >= 0; i--) {
        int curr = a[i], next = a[i + 1];
        if (curr < next) continue;

        // find the number that is less than next
        while (curr >= next && curr != 0) {
            curr /= 2;
            res++;
        }
        a[i] = curr;

        if (a[i] == a[i + 1]) {
            cout << "-1\n";
            return;
        }
    }
    cout << res << endl;
}
