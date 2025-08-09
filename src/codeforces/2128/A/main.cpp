// PROBLEM_NAME
// PROBLEM_LINK

// { Imports, TypeNames, Macros
#include <bits/stdc++.h>
#include <climits>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
// }

void solve() {
    int n, c;
    cin >> n >> c;

    vi a(n);
    loop(i, 0, n) cin >> a[i];

    vi res(n);
    int i = 0;
    for (int num : a) {
        int count = -1;
        // if (num < c && 2 * num < c) {
        if (num <= c) {
            double val = num / c;
            double logVal = log2(c / num);
            count = static_cast<int>(floor(logVal));
        }

        res[i] = count;
        i++;
    }

    // loop(i, 0, n) cout << res[i] << " ";
    // cout << endl;

    unordered_set<int> visited;
    loop(i, 0, n) {
        if (res[i] < 0) visited.insert(i);
    }

    while (visited.size() != n) {
        // pick the smallest & add to visited
        int small = INT_MAX;
        int small_idx;
        loop(i, 0, n) { // 30 times
            if (visited.find(i) != visited.end()) continue;
            int num = res[i];
            if (num < 0) {
                visited.insert(i);
                continue;
            }
            if (num < small) {
                small = num;
                small_idx = i;
            }
        }
        visited.insert(small_idx);

        loop(i, 0, n) {
            if (visited.find(i) != visited.end()) continue; // alread visited
            res[i]--;
        }
    }

    int total_cost = 0;
    for (int num : res) {
        if (num < 0) total_cost++;
    }

    cout << total_cost << endl;
    // loop(i, 0, n) cout << res[i] << " ";
    // cout << endl;
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
