// https://codeforces.com/problemset/problem/

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
    for (int i = 0; i < n; i++)
        cin >> v[i];

    // Edge case: no need to do any operation
    if (v[0] == 0) {
        cout << "0\n";
        return;
    }

    vector<int> minv(n); // [min(v[0..i]), ... ]
    minv[0] = v[0];
    for (int i = 1; i < n; i++) {
        int smallest_so_far = min(minv[i - 1], v[i]);
        minv[i] = smallest_so_far;
    }

    vector<int> sumv(n); // [sum(minv[0..i]), ... ]
    sumv[0] = v[0];
    for (int i = 1; i < n; i++) {
        sumv[i] = sumv[i - 1] + minv[i];
    }

    for (int i = 1; i < n; i++) {

        int new_prev_num = v[i - 1] + v[i]; // assume adding current to previous
        int new_prev_min =
            i == 1 ? new_prev_num : min(minv[i - 2], new_prev_num);
        int new_prev_sum = i == 1 ? new_prev_num : sumv[i - 2] + new_prev_min;

        if (new_prev_sum <= sumv[i]) {
            cout << new_prev_sum << "\n";
            return;
        }
    }
    cout << sumv[n - 1] << "\n";
}

void solve2() {
    int n;
    cin >> n;
    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    // Edge case: no need to do any operation
    if (v[0] == 0) {
        cout << "0\n";
        return;
    }

    vector<int> minv(n); // [min(v[0..i]), ... ]
    minv[0] = v[0];
    for (int i = 1; i < n; i++) {
        int smallest_so_far = min(minv[i - 1], v[i]);
        minv[i] = smallest_so_far;
    }

    vector<int> sumv(n); // [sum(minv[0..i]), ... ]
    sumv[0] = v[0];
    for (int i = 1; i < n; i++) {
        sumv[i] = sumv[i - 1] + minv[i];
    }

    for (int i = 1; i < n; i++) {
        int new_prev_num = v[i - 1] + v[i]; // assume adding current to previous
        int new_prev_min;
        if (i == 1) {
            new_prev_min = new_prev_num;
        } else {
            new_prev_min = min(minv[i - 2], new_prev_num);
        }
        int new_prev_sum;
        if (i == 1) {
            new_prev_sum = new_prev_num;
        } else {
            new_prev_sum = sumv[i - 2] + new_prev_min;
        }

        if (new_prev_sum <= sumv[i]) {
            cout << new_prev_sum << "\n";
            return;
        }
    }
    cout << sumv[n - 1] << "\n";

    /*
    // Check segments
    int segs = 0;
    int prev = -1;
    int seg1_last, seg2_start;
    for (int i = 0; i < n; i++) {
        int num = minv[i];
        if (num == prev) continue;
        prev = num;
        segs++;
        if (segs > 1) {
            seg1_last = i - 1;
            seg2_start = i;
        }
    }

    // 2 segments
    if (segs == 2) {
        if (seg1_last == 0) {
            cout << minv[0] << "\n";
            return;
        } else {
            int res = minv[0] * (seg1_last + 1);
            cout << res << "\n";
            return;
        }
    }

    // 1 segment ?
    */
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
