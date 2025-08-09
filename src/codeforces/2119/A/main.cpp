// https://codeforces.com/contest/2119/problem/A

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
    int a, b, x, y;
    cin >> a >> b >> x >> y;

    int cost = 0;

    if (a == b) {
        // do nothing
    }
    // If a is larger, then it must be odd, and only 1 unit away
    else if (a > b && a % 2 == 1 && a - b == 1) {
        // operation 2: a ^ 1
        cost = y;
    } else if (a < b) {
        if (x <= y) {
            cost = x * (b - a);
        } else {
            /*
            while (a != b) {
                if (a % 2 == 0) { // operation 2: a ^ 1
                    a ^= 1;
                    cost += y;
                } else { // operation 1: a + 1
                    a += 1;
                    cost += x;
                }
            }
            // */

            // /*
            if (b - a % 2 == 0) {
                int num_add = b - a / 2;
                int num_xor = num_add;
                // cost += num_add;
                // cost += num_xor;
            } else {
                int num_add = b - a / 2;
                int num_xor = b - a / 2;
                (a % 2 == 0) ? num_xor++ : num_add++;
                cost += num_add;
                cost += num_xor;
            }
            // */
        }
    } else {
        cost = -1;
    }

    cout << cost << "\n";
}

int main() {
    setupIO();
    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
