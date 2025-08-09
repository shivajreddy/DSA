// https://codeforces.com/problemset/problem/1875/A

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
    // /* More optimal way
    int a, b, n;
    cin >> a >> b >> n;

    long long time = b;
    for (int i = 0, x = 0; i < n; i++) {
        cin >> x;
        time += min(a - 1, x);
    }
    cout << time << "\n";
    // */

    /* Bruteforce
    long long a, b, n;
    cin >> a >> b >> n;

    priority_queue<long long, vector<long long>, greater<long long>> minHeap;
    for (long long i = 0; i < n; i++) {
        long long x;
        cin >> x;
        minHeap.push(x);
    }

    long long time = 0;

    long long c = b; // current time
    while (c > 0) {  // if c becomes 0, boom
        // cout << "start-c: " << c << endl;
        time++;
        if (c > 2) {
            time += (c - 2);
            c = 2;
        } else if (c == 1 && !minHeap.empty()) { // must add something, or else
                                                 // next iterm boom
            // add the smallest
            c += minHeap.top();
            minHeap.pop();
        }
        c = min(c, a);
        c--; // reduce timer by 1
        // cout << "end-c: " << c << endl;
    }

    cout << time << "\n";
    // */
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
