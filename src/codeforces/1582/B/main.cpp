// B. Luntik and Subsequences
// https://codeforces.com/problemset/problem/1582/B

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

// TERRIBLY WRONG APPROACH
void solve2() {
    int n;
    cin >> n;

    vi a(n);
    ll total_sum = 0; // sum of all elements of array
    loop(i, 0, n) {
        cin >> a[i];
        total_sum += a[i];
    }

    auto count_valid = [&](int idx) -> int {
        int ans = 0;
        ll sub = 0;
        loop(i, idx, n) {
            sub += a[i];
            if (sub == total_sum - 1) ans += 1;
        }
        return ans;
    };

    int res = total_sum == 1 ? 1 : 0;
    loop(i, 0, n) res += count_valid(i);

    cout << res << endl;
}

// WRONG APPROACH
void solve3() {
    int n;
    cin >> n;

    vi a(n);
    ll total_sum = 0; // sum of all elements of array
    loop(i, 0, n) {
        cin >> a[i];
        total_sum += a[i];
    }

    ll target_sum = total_sum - 1;
    int res = target_sum == 0 ? 1 : 0;

    map<ll, ll> hm;
    // sort(a.begin(), a.end()); // 60.log(60)
    ll seq = 0;

    loop(i, 0, n) {
        seq += a[i];
        res += hm[target_sum - seq];
        hm[seq] += 1;
    }

    cout << res << endl;
}

void solve() {
    int n;
    cin >> n;

    ll cnt0 = 0, cnt1 = 0;
    loop(i, 0, n) {
        int x;
        cin >> x;
        if (x == 0) cnt0++;
        if (x == 1) cnt1++;
    }

    // result is 2^cnt0 * cnt1

    ll res = (1LL << cnt0) * cnt1;
    cout << res << endl;
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
