// A. Only One Digit
// https://codeforces.com/contest/2126/problem/A

#include <bits/stdc++.h>
#include <unordered_set>
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
    int x;
    cin >> x;

    unordered_set<int> s;
    vi a;
    while (x > 0) {
        int digit = x % 10;
        s.insert(digit);
        x /= 10;
    }

    // loop(i, 0, a.size()) cout << a[i] << " ";
    // cout << endl;
    int smallest = 10;
    for (int digit : s) smallest = min(smallest, digit);

    cout << smallest << endl;
}
