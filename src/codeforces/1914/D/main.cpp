// D. Three Activities
// https://codeforces.com/problemset/problem/1914/D

// { Imports, TypeNames, Macros
#include <bits/stdc++.h>
#include <functional>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
#define vec vector
// }

vi find_max(vi& arr) {
    int n = arr.size();
    vector<pair<int, int>> tmp(n);
    loop(i, 0, n) {
        tmp[i].first = arr[i];
        tmp[i].second = i;
    }
    sort(tmp.begin(), tmp.end(), greater<pair<int, int>>());
    vi res(3);
    loop(i, 0, 3) res[i] = tmp[i].second;
    return res;
}

void solve() {
    int n;
    cin >> n;

    vi a(n);
    loop(i, 0, n) cin >> a[i];
    vi b(n);
    loop(i, 0, n) cin >> b[i];
    vi c(n);
    loop(i, 0, n) cin >> c[i];

    vi max_a = find_max(a);
    vi max_b = find_max(b);
    vi max_c = find_max(c);

    int res = 0;
    loop(i, 0, 3) loop(j, 0, 3) loop(k, 0, 3) {
        int mxa = max_a[i], mxb = max_b[j], mxc = max_c[k];
        if ((mxa == mxb) || (mxb == mxc) || (mxc == mxa)) continue;
        res = max(res, a[mxa] + b[mxb] + c[mxc]);
    }
    cout << res << endl;
}

function<void(const vec<pii>&)> printpii = [](const vec<pii>& vp) {
    for (auto p : vp) cout << "{" << p.first << "," << p.second << "} ";
    cout << endl;
};

void helper() {
}

void solve_practise() {
    int n;
    cin >> n;

    vi a(n);
    loop(i, 0, n) cin >> a[i];
    vi b(n);
    loop(i, 0, n) cin >> b[i];
    vi c(n);
    loop(i, 0, n) cin >> c[i];

    vec<pii> pa(n);
    loop(i, 0, n) pa[i] = { a[i], i };
    printpii(pa);
    sort(pa.begin(), pa.end(), greater<pii>());
    printpii(pa);
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    int tc;
    cin >> tc;
    // while (tc--) solve();
    while (tc--) solve_practise();
}
