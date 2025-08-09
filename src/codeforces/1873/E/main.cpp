// E. Building an Aquarium
// https://codeforces.com/problemset/problem/1873/E

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef vector<ll> vll;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve2() {
    ll n, x;
    cin >> n >> x;

    vll a(n);
    loop(i, 0, n) cin >> a[i];

    sort(a.begin(), a.end());

    vll coral_vol = a; // volume of the coral so far
    loop(i, 1, n) coral_vol[i] += coral_vol[i - 1];

    vll total_vol(n);
    loop(i, 0, n) total_vol[i] = (i + 1) * a[i];

    vll water(n);
    loop(i, 0, n) water[i] = total_vol[i] - coral_vol[i];

    int idx = 0;
    for (; idx < n; idx++) {
        // Find ht. where water overflows.
        if (water[idx] >= x) break;
    }

    int needed_ht = a[idx - 1]; // ht as of now
    int remaining_water = x - water[idx - 1];
    int remaining_ht = remaining_water / idx; // idx is the ht as of now
    int result = needed_ht + remaining_ht;
    cout << result << endl;

    /*
    cout << "heights\n";
    for (auto num : a) cout << num << " ";
    cout << endl;
    cout << "coral_vol\n";
    for (auto num : coral_vol) cout << num << " ";
    cout << endl;
    cout << "total_val\n";
    for (auto num : total_vol) cout << num << " ";
    cout << endl;
    cout << "water\n";
    for (auto num : water) cout << num << " ";
    cout << endl;
    */
}

void solve() {
    int n;
    ll x;
    cin >> n >> x;
    ll a[n];
    loop(i, 0, n) cin >> a[i];

    ll lo = 0, hi = 2'000'000'007;
    while (lo < hi) {
        ll mid = lo + (hi - lo + 1) / 2; // target-height
        ll tot = 0;
        for (int i = 0; i < n; i++) {
            tot += max(mid - a[i], 0LL);
        }
        if (tot <= x)
            lo = mid;
        else
            hi = mid - 1;
    }
    cout << lo << endl;
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
