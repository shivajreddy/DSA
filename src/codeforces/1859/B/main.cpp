// B. Olya and Game with Arrays
// https://codeforces.com/problemset/problem/1859/B

#include <bits/stdc++.h>
#include <climits>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef deque<int> di;

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

    vector<vi> all_arr(n);

    int first_smallest = INT_MAX;
    int curr_n = n;
    loop(i, 0, n) {
        int m;
        cin >> m;
        vi a(m);
        loop(j, 0, m) cin >> a[j];
        sort(a.begin(), a.end()); // sort each array
        if (a[0] < first_smallest) {
            first_smallest = a[0];
        }
        all_arr[i] = a;
    }

    int second_smallest = INT_MAX;

    loop(i, 0, n) loop(j, 0, all_arr[i].size()) {
        second_smallest = min(second_smallest, all_arr[i][1]);
    }

    ll all_seconds = 0;
    loop(i, 0, n) all_seconds += all_arr[i][1];
    ll res = all_seconds + first_smallest - second_smallest;
    cout << res << endl;
}

void solve2() {
    int n;
    cin >> n;

    int global_first_smallest = INT_MAX;
    ll sum_all_second_smalls = 0;
    vi all_second_smalls;
    loop(i, 0, n) {
        int m;
        cin >> m;

        vi arr(m);
        loop(j, 0, m) cin >> arr[j];

        int first_smallest = *min_element(arr.begin(), arr.end());
        global_first_smallest = min(global_first_smallest, first_smallest);

        // remove one occurence of min_val
        auto it = find(arr.begin(), arr.end(), first_smallest);
        arr.erase(it);

        // find the second smallest (minimum of remaining)
        int second_smallest = *min_element(arr.begin(), arr.end());
        sum_all_second_smalls += second_smallest;
        all_second_smalls.push_back(second_smallest);
    }
    int min_of_second_smalls =
        *min_element(all_second_smalls.begin(), all_second_smalls.end());
    ll res =
        global_first_smallest + sum_all_second_smalls - min_of_second_smalls;
    cout << res << endl;
}
