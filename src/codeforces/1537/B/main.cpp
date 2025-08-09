// B. Bad Boy
// https://codeforces.com/problemset/problem/1537/B

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
    int ROWS, COLS, i, j;
    cin >> ROWS >> COLS >> i >> j;

    cout << "1 1 " << ROWS << " " << COLS << endl;
    return;
    queue<pair<pair<int, int>, int>> q;
    q.push({ { i - 1, j - 1 }, 0 });

    set<pair<int, int>> visited;
    visited.insert({ i - 1, j - 1 });

    int mx1 = 0, mx2 = 0;
    pair<int, int> res1, res2;

    vector<vi> dirs = { { -1, 0 }, { 1, 0 }, { 0, 1 }, { 0, -1 } };
    while (!q.empty()) {
        auto node = q.front();
        q.pop();

        int r = node.first.first, c = node.first.second, edges = node.second;
        // cout << "r:" << r << " c:" << c << " edges:" << edges << endl;

        if (2 * edges > mx1) {
            mx2 = mx1;
            res2 = res1;
            mx1 = 2 * edges;
            res1 = { r, c };
        } else if (2 * edges > mx2) {
            mx2 = 2 * edges;
            res2 = { r, c };
        }

        for (auto& d : dirs) {
            int dr = d[0], dc = d[1];
            int nr = r + dr, nc = c + dc;

            if (0 <= nr && nr < ROWS && 0 <= nc && nc < COLS &&
                visited.count({ nr, nc }) == 0) {
                visited.insert({ nr, nc });
                q.push({ { nr, nc }, edges + 1 });
            }
        }
    }
    cout << res1.first << " " << res1.second << " " << res2.first << " "
         << res2.second << endl;
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
