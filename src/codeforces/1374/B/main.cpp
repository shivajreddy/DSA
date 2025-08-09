// B. Multiply by 2, divide by 6
// https://codeforces.com/problemset/problem/1374/B

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
    int n;
    cin >> n;

    int count3 = 0;
    while (n > 0 && n % 3 == 0) {
        count3++;
        n /= 3;
    }

    int count2 = 0;
    while (n > 0 && n % 2 == 0) {
        count2++;
        n /= 2;
    }
    if (n > 1 || count2 > count3) {
        cout << -1 << endl;
    } else {
        cout << count3 + (count3 - count2) << endl;
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
