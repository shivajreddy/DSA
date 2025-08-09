// B. Pathless
// https://codeforces.com/contest/2130/problem/B

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
    int n, s;
    cin >> n >> s;

    ll total_sum = 0;
    int count_0 = 0, count_1 = 0, count_2 = 0;

    vi a(n);
    loop(i, 0, n) {
        cin >> a[i];
        if (a[i] == 0) count_0++;
        if (a[i] == 1) count_1++;
        if (a[i] == 2) count_2++;
        total_sum += a[i];
    }

    // edge case
    if (total_sum == s) { // can simply walk straight
        // cout << "case1\n";
        cout << "-1\n";
        return;
    }
    // alice will have to touch all nums atleast once. sum will only increase
    // it will never decrease
    if (total_sum > s) {
        // cout << "case2\n";
        for (int num : a) cout << num << " ";
        cout << endl;
        return;
    }

    // only 0's
    if (count_0 > 0 && count_1 == 0 && count_2 == 0) {
        // cout << "case3\n";
        while (count_0 > 0) {
            cout << "0 ";
            count_0--;
        }
        cout << endl;
        return;
    }
    // only 1's
    if (count_0 == 0 && count_1 > 0 && count_2 == 0) {
        // cout << "case4\n";
        // int target = s - total_sum;
        // cout << "target:" << target << endl;
        if (s % 2 == 0) {
            cout << "-1\n";
        } else {
            while (count_1 > 0) {
                cout << "1 ";
                count_1--;
            }
            cout << endl;
        }
        return;
    }
    // only 2's
    if (count_0 == 0 && count_1 == 0 && count_2 > 0) {
        // cout << "case5\n";
        if (s % 4 == 0) {
            cout << "-1\n";
        } else {
            while (count_2 > 0) {
                cout << "2 ";
                count_2--;
            }
            cout << endl;
        }
        return;
    }
    // mix

    // 2 is not there to separate [0  1]
    if (count_2 == 0) {
        // cout << "case6\n";
        cout << "-1\n";
        return;
    }

    // alice can now only have sums in sequnce of (2, 1): 3,6,9,12,...
    //  0 0 0] [2 2 2] [1 1 1
    //  0] [2] [1       2,4,6,8   3,6,9   5,10,15,
    //  0] [1] [2
    int target = s - total_sum;
    if (target % 2 == 0 || target % 3 == 0 || target % 15 == 0) {
        // cout << "case8\n";
        cout << "-1\n";
        return;
    }

    // cout << "target is:" << target << endl;
    if (target == 1) {
        // cout << "case7\n";
        while (count_0 > 0) {
            cout << "0 ";
            count_0--;
        }
        while (count_2 > 0) {
            cout << "2 ";
            count_2--;
        }
        while (count_1 > 0) {
            cout << "1 ";
            count_1--;
        }
        cout << endl;
        return;
    }

    // cout << "case9\n";
    cout << "-1\n";
    return;
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
