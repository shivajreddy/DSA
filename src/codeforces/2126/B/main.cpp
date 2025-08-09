// B. No Casino in the Mountains
// https://codeforces.com/contest/2126/problem/B

#include <bits/stdc++.h>
#include <unordered_map>
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

/*
k=2
0 1 2 3 4 5
*/

int rec(int k, int idx, const vector<int>& a, unordered_map<int, int>& memo) {
    int n = a.size();
    if (memo.find(idx) != memo.end()) return memo[idx]; // already in memo
    if (idx + k - 1 > n - 1) { // not enough cells remaining
        return memo[idx] = 0;
    }
    if (a[idx] == 1) { // start itself is 1
        return memo[idx] = rec(k, idx + 1, a, memo);
    }
    bool all_zeroes = true;
    int broken_at = -1;
    loop(i, idx, idx + k) {
        if (a[i] == 1) {
            all_zeroes = false;
            broken_at = i;
            break;
        }
    }
    if (all_zeroes) {
        return memo[idx] = 1 + rec(k, idx + k + 1, a, memo);
    } else {
        return memo[idx] = rec(k, broken_at + 1, a, memo);
        // return rec(k, idx + k + 1, a);
    }
}

void solve2() {
    int n, k;
    cin >> n >> k;

    vi a(n);
    loop(i, 0, n) cin >> a[i];

    unordered_map<int, int> memo; // {start_idx : total_hikes}
    int res = rec(k, 0, a, memo);
    cout << res << endl;
}

void solve() {
    int n, k;
    cin >> n >> k;

    vi a(n);
    loop(i, 0, n) cin >> a[i];

    int hikes = 0, count = 0;
    loop(i, 0, n) {
        if (a[i] == 0)
            count++;
        else
            count = 0;
        if (count == k) {
            hikes++;
            count = 0;
            i++;
        }
    }
    cout << hikes << endl;
}
