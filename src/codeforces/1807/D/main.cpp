// D. Odd Queries
// https://codeforces.com/problemset/problem/1807/D

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
    int n, total_queries;
    cin >> n >> total_queries;

    vector<int> v(n);
    vector<int> prefix_sum(n + 1, 0);
    for (int i = 0, num; i < n; i++) {
        cin >> num;
        prefix_sum[i + 1] = prefix_sum[i] + num;
        v[i] = num;
    }

    /*
    cout << "v: ";
    for (int num : v) {
        cout << num << " ";
    }
    cout << endl;
    cout << "Prefixsum: ";
    for (int num : prefix_sum) {
        cout << num << " ";
    }
    cout << endl;
    // */

    for (int i = 0; i < total_queries; i++) {
        int l, r, k;
        cin >> l >> r >> k;

        // cout << "query: " << i << endl;
        int left_sum = prefix_sum[l - 1];
        int right_sum = prefix_sum[prefix_sum.size() - 1] - prefix_sum[r];
        int new_range_sum = k * (r - l + 1);
        int new_total_sum = left_sum + right_sum + new_range_sum;
        // cout << "left_sum: " << left_sum << endl;
        // cout << "right_sum: " << right_sum << endl;
        // cout << "new_range_sum: " << new_range_sum << endl;
        // cout << "new_total_sum: " << new_total_sum << endl;

        new_total_sum & 1 ? cout << "YES\n" : cout << "NO\n";
    }
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
