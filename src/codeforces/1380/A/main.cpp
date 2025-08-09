// A. Three Indices
// https://codeforces.com/problemset/problem/1380/A

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
//
void solve() {
    int n;
    cin >> n;
    vi a(n);
    loop(i, 0, n) cin >> a[i];

    loop(idx, 1, n - 1) {
        int i = a[idx - 1], j = a[idx], k = a[idx + 1];
        if (i < j && j > k) {
            cout << "YES\n" << idx << " " << idx + 1 << " " << idx + 2 << endl;
            return;
        }
    }
    cout << "NO\n";
}

void solve2() {
    int n;
    cin >> n;
    vi a(n);
    loop(i, 0, n) cin >> a[i];

    bool L = false, R = false;
    int l = -1, mid = -1, r = -1;
    loop(idx, 1, n - 1) {
        l = -1, r = -1;
        L = false, R = false;
        int num = a[idx];
        loop(i, 0, idx) {
            if (a[i] < num) {
                l = i;
                L = true;
                break;
            }
        }
        loop(i, idx + 1, n) {
            if (num > a[i]) {
                r = i;
                R = true;
                break;
            }
        }
        if (L & R) {
            mid = idx;
            break;
        }
    }
    if (L & R) {
        l++;
        mid++;
        r++;
        cout << "YES\n" << l << " " << mid << " " << r << endl;
    } else {
        cout << "NO\n";
    }
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
