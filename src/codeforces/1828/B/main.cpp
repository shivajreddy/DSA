// 1828 B. Permutation Swap
// https://codeforces.com/problemset/problem/1828/B

#include <bits/stdc++.h>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

void solve() {
    int n;
    cin >> n;

    vector<int> v(n);
    unordered_map<int, int> hm;
    for (int i = 0, num; i < n; i++) {
        cin >> num;
        v[i] = num;
        hm[num] = i;
    }

    vector<int> d(n);
    for (int i = 0; i < n; i++) {
        int num = i + 1;
        d[i] = abs(hm[num] - i);
    }

    // find the greatest common divisor in vec-d
    int res = d[0];
    for (int curr_d : d) res = gcd(res, curr_d);
    cout << res << "\n";
}

int main() {
    // setupIO();

    int tc;
    cin >> tc;
    while (tc--) solve();
}
