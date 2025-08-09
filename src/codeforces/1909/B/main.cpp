// B. Make Almost Equal With Mod
// https://codeforces.com/problemset/problem/1909/B

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve() {
    int n;
    cin >> n;

    ll a[n]; // cant use int
    // vector<ll> a(n); // using int will fail
    loop(i, 0, n) cin >> a[i];
    // EDITORIAL INSIGHT: Try k = 2^1, 2^2, ..., 2^57
    // Mathematical proof:
    // - f(k) = number of distinct values after mod k operation
    // - If f(k) = 1, then f(2k) = 2 (key relationship!)
    // - f(1) = 1, f(2^57) = n, so there exists m where f(2^m) = 1 and
    // f(2^(m+1)) = 2
    ll k;
    loop(power, 1, 58) {  // 2^1, 2^2, ... 2^57
        k = 1LL << power; // k = 2^power

        set<long long> remainders;
        loop(idx, 0, n) remainders.insert(a[idx] % k);

        if (remainders.size() == 2) break;
    }

    // loop(i, 0, n) cout << a[i] % k << " ";
    // cout << endl;
    cout << k << endl;
}

void solve2() {
    int n;
    cin >> n;

    ll a[n];
    loop(i, 0, n) cin >> a[i];

    ll k;
    loop(i, 1, 61) { // 2^1, 2^2, ... 2^60
        k = 1LL << i;

        set<ll> unique;
        loop(idx, 0, n) unique.insert(a[idx] % k);

        if (unique.size() == 2) break;
    }

    // loop(i, 0, n) cout << a[i] % k << " ";
    // cout << endl;
    cout << k << endl;
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
