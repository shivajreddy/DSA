// Missing Number
// https://cses.fi/problemset/task/1083

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

    ll sum = 0;
    int num;
    loop(i, 0, n - 1) {
        cin >> num;
        sum += num;
    }
    ll actual_sum = (static_cast<ll>(n) * (n + 1)) / 2;
    cout << actual_sum - sum << endl;
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
