// B. Array Cloning Technique
// https://codeforces.com/problemset/problem/1665/B

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
    int n;
    cin >> n;

    int hi = 0;
    int rem = 0;
    // using unordered_map instead of map is causing TLE
    map<int, int> hm; // frequency map

    loop(i, 0, n) {
        int num;
        cin >> num;
        hm[num]++;
        hi = max(hi, hm[num]);
    }

    rem = n - hi;
    if (rem == 0) {
        cout << "0\n";
        return;
    }

    int res = 0;

    while (rem > 0) {
        int taken = rem - hi < 0 ? rem : hi;
        res += (1 + taken); // 1 for clone

        rem -= hi;
        hi *= 2;
    }

    cout << res << endl;
}
