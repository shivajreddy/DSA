// C. Ski Resort
// https://codeforces.com/problemset/problem/1840/C

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
    int n, k, q;
    cin >> n >> k >> q;
    vi a(n);
    loop(i, 0, n) cin >> a[i];

    ll ans = 0, len = 0;
    loop(i, 0, n) {
        if (a[i] <= q)
            len++;
        else {
            if (len >= k) ans += (len - k + 1) * (len - k + 2) / 2;
            len = 0;
        }
    }

    if (len >= k) ans += (len - k + 1) * (len - k + 2) / 2;
    // if (len >= k) ans += ((long long)(len - k + 1) * (len - k + 2) / 2);
    cout << ans << endl;

    /*
    vi isvalid(n);
    loop(i, 0, n) a[i] <= q ? isvalid[i] = 1 : isvalid[i] = 0;

    vi segments;
    int curr_seg = 0;
    loop(i, 0, n) {
        if (isvalid[i] == 0) {
            if (curr_seg != 0) segments.push_back(curr_seg);
            curr_seg = 0;
        } else
            curr_seg += 1;
    }
    if (curr_seg != 0) segments.push_back(curr_seg);

    // for (int num : segments) cout << num << " ";
    // cout << endl;
    int res = 0;
    for (int l : segments) {
        if (l >= k) {
            int total_ways = ((l - k + 2) * (l - k + 1)) / 2;
            res += total_ways;
        }
    }
    cout << res << endl;
    */

    /*
    int l = 0, r = 0;
    int win_sum = 0;
    int res = 0;

    for (; r < k; r++) win_sum += isvalid[r];
    r--;

    while (r < n) {
        res += win_sum == (r - l + 1) ? 1 : 0;
        // keep increasing vacation duration more than k, as long as valid
        while (r + 1 < n && win_sum + isvalid[r + 1] == r + 1 - l + 1) {
            res++;
            win_sum += isvalid[r + 1];

            r++;
        }
    }

    for (; r < k; r++) win_sum += isvalid[r];

    r--; // bring it back by 2, to havel l..r = k

    while (r < n) {
        while (r < n && win_sum == k) {
            res++;
            r++;
        }
        r++;
    }

    for (; r < n; r++) {
        win_sum -= isvalid[l]; // shrink window on left by 1
        win_sum += isvalid[r]; // increase window on right by 1
        res += win_sum == k ? 1 : 0;
    }

    cout << res << endl;
    */
}
