// Counting Rooms
// https://cses.fi/problemset/task/1192

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void solve() {
    int rows, cols;
    cin >> rows >> cols;

    vector<string> map(rows);
    loop(r, 0, rows) cin >> map[r];

    struct pair_hash {
        size_t operator()(const pii& p) const noexcept {
            return ((size_t)p.first << 32) ^ (size_t)p.second;
        }
    };
    struct pair_equal {
        bool operator()(const pii& a, const pii& b) const noexcept {
            return a.first == b.first && a.second == b.second;
        }
    };

    unordered_set<pii, pair_hash, pair_equal> visited;

    vector<pii> dirs = { { 1, 0 }, { -1, 0 }, { 0, 1 }, { 0, -1 } };

    function<void(int r, int c)> dfs = [&](int r, int c) {
        visited.insert({ r, c }); // add to visited

        // explore all 4 directions
        for (auto d : dirs) {
            int nr = r + d.first, nc = c + d.second;
            // out of bounds
            if (nr < 0 || nr == rows || nc < 0 || nc == cols) continue;
            // already visited
            if (visited.find({ nr, nc }) != visited.end()) continue;
            if (map[nr][nc] == '#') continue;
            dfs(nr, nc);
        }
    };

    int rooms = 0;
    loop(r, 0, rows) loop(c, 0, cols) {
        if (visited.find({ r, c }) != visited.end()) continue;
        if (map[r][c] == '#') continue;
        dfs(r, c);
        rooms++;
    }
    cout << rooms << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    solve();
    // int tc;
    // cin >> tc;
    // while (tc--) solve();
}
