// 1850 D.Balanced Round
// https://codeforces.com/problemset/problem/1850/D

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
    int n, k;
    cin >> n >> k;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    // edge case
    if (n == 1) {
        cout << "0\n";
        return;
    }

    sort(v.begin(), v.end());

    vector<int> ad;
    for (int i = 1; i < n; i++) {
        ad.push_back(v[i] - v[i - 1]);
    }

    int longest_seq = 0; // length of seq that has all abs <= k
    for (int i = 0, curr_len = 0; i < ad.size(); i++) {
        if (ad[i] <= k) {
            curr_len++;
            longest_seq = max(longest_seq, curr_len);
        } else {
            curr_len = 0;
        }
    }

    // say we have sequnce of 2, then there are 3 numbers. because each diffence
    // in the sequnce is the difference between 2 numbers. so if len(ad) is 2,
    // then there are 3 numbers in the array
    int total_valid_numbers = longest_seq + 1;

    int res = n - total_valid_numbers;
    cout << res << "\n";
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
