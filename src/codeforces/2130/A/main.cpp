// A. Submission is All You Need
// https://codeforces.com/contest/2130/problem/A

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
    int n;
    cin >> n;

    vi a(n);
    ll total_sum = 0;
    loop(i, 0, n) {
        cin >> a[i];
        total_sum += a[i];
    }

    int count_0 = 0;
    for (int num : a)
        if (num == 0) count_0 += 1;

    cout << (total_sum + count_0) << endl;
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
