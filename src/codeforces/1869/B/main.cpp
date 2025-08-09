// B. 2D Traveling
// https://codeforces.com/problemset/problem/1869/B

// { Imports, TypeNames, Macros
#include <bits/stdc++.h>
#include <climits>
#include <queue>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
// }

void solve() {
    int n, k, s, t;
    cin >> n >> k >> s >> t;

    vector<ll> x(n + 1), y(n + 1); // x&y coordinates (1-based)
    loop(i, 1, n + 1) cin >> x[i] >> y[i];

    // Distance b/w the cities of given indexes(1-based)
    auto get_dist = [&](int idx1, int idx2) -> ll {
        return abs(x[idx1] - x[idx2]) + abs(y[idx1] - y[idx2]);
    };

    ll ans = get_dist(s, t);
    ll min_s = 1e17, min_t = 1e17;
    loop(i, 1, k + 1) {
        // smallest dist to connect to network from start
        min_s = min(min_s, get_dist(s, i));
        // smallest dist to connect to network from target
        min_t = min(min_t, get_dist(t, i));
    }
    // is it better to directly traver from s->t or using network
    ans = min(ans, min_s + min_t);
    cout << ans << endl;

    /*
    - shortest distance b/w two points is displacement
    - if you would have to use any other point, the best case scenario is if
    the point is on the line of travel, whose total distance is same as
    displacement
    - so in this case, the other case to check is, if the
    (distance from start to network) + (distance from target to network)
    is smaller than displacement.
    */
}

void solve2() {
    int n, k, a, b;
    cin >> n >> k >> a >> b;

    vector<vector<int>> mat(n, vector<int>(2));
    loop(i, 0, n) cin >> mat[i][0] >> mat[i][1];

    auto get_dist = [&](int city1_idx, int city2_idx) -> int {
        if (city1_idx < k && city2_idx < k) return 0; // both are major cities
        int ax = mat[city1_idx][0], ay = mat[city1_idx][1];
        int bx = mat[city2_idx][0], by = mat[city2_idx][1];
        return abs(bx - ax) + abs(by - ay);
    };

    // Dijkstra's Shortest Path
    int start = a - 1, target = b - 1;

    // min-heap where the smalelst pair.first comes to the top
    priority_queue<pii, vector<pii>, greater<pii>> min_heap;
    unordered_set<int> visited { start };

    loop(i, 0, n) {
        if (i == start) continue;
        auto d = get_dist(start, i);
        // cout << "d:" << d << " i:" << i << endl;
        min_heap.push({ d, i });
    }

    // test
    int prev = INT_MAX;
    while (!min_heap.empty()) {
        while (!min_heap.empty() && min_heap.top().first <= prev) {
            auto top = min_heap.top();
            cout << "picked: [" << top.first << "," << top.second << ",(";
            cout << mat[top.second][0] << "," << mat[top.second][1] << ")]\n";
            min_heap.pop();
            prev = top.first;
        }
        prev = INT_MAX;
        cout << "---" << endl;
        // Relaxation: from this node
        min_heap.pop();
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
