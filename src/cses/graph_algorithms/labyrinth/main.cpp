// Labyrinth
// https://cses.fi/problemset/task/1193

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;
typedef pair<ll, ll> pll;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
#define ff first
#define ss second

void solve() {
    int rows, cols;
    cin >> rows >> cols;
    vector<string> map(rows);
    loop(r, 0, rows) cin >> map[r];

    pii start, end;
    loop(r, 0, rows) loop(c, 0, cols) {
        if (map[r][c] == 'A') {
            start = { r, c };
        } else if (map[r][c] == 'B') {
            end = { r, c };
        }
    }

    // BFS with parent tracking
    queue<pii> q;
    vector<vector<pii>> parent(rows, vector<pii>(cols, { -1, -1 }));

    q.push(start);
    map[start.ff][start.ss] = '#'; // Mark visited WHEN pushing!

    typedef vector<tuple<int, int, string>> vt;
    vt dirs = { { -1, 0, "U" }, { 1, 0, "D" }, { 0, -1, "L" }, { 0, 1, "R" } };

    bool found = false;
    while (!q.empty() && !found) {
        auto [r, c] = q.front();
        q.pop();

        for (auto [dr, dc, sym] : dirs) {
            int nr = r + dr, nc = c + dc;

            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            if (map[nr][nc] == '#') continue;

            q.push({ nr, nc });
            map[nr][nc] = '#'; // Mark visited IMMEDIATELY

            parent[nr][nc] = { r, c };

            if (map[nr][nc] == 'B') {
                found = true;
                break;
            }
            if (nr == end.ff && nc == end.ss) {
                found = true;
                break;
            }
        }
    }

    if (!found) {
        cout << "NO" << endl;
        return;
    }

    // Reconstruct path
    string path = "";
    pii curr = end;
    while (curr != start) {
        pii prev = parent[curr.ff][curr.ss];
        if (prev.ff < curr.ff)
            path += 'D';
        else if (prev.ff > curr.ff)
            path += 'U';
        else if (prev.ss < curr.ss)
            path += 'R';
        else
            path += 'L';
        curr = prev;
    }

    reverse(path.begin(), path.end());

    cout << "YES" << endl;
    cout << path.length() << endl;
    cout << path << endl;
}

void solve_tle() {
    int rows, cols;
    cin >> rows >> cols;
    vector<string> map(rows);
    loop(r, 0, rows) cin >> map[r];

    pii start;
    loop(r, 0, rows) loop(c, 0, cols) {
        if (map[r][c] == 'A') {
            start = { r, c };
            break;
        }
    }
    // BFS with parent tracking
    queue<tuple<int, int, int, string>> q;

    q.push({ start.ff, start.ss, 0, "" });
    map[start.ff][start.ss] = '#'; // Mark visited WHEN pushing!

    typedef vector<tuple<int, int, string>> vt;
    vt dirs = { { -1, 0, "U" }, { 1, 0, "D" }, { 0, -1, "L" }, { 0, 1, "R" } };

    while (!q.empty()) {
        auto [r, c, d, path] = q.front();
        q.pop();

        for (auto [dr, dc, sym] : dirs) {
            int nr = r + dr, nc = c + dc;
            if (nr < 0 || nr >= rows || nc < 0 || nc >= cols) continue;
            if (map[nr][nc] == '#') continue;

            // Check if we found the destination BEFORE marking as visited
            if (map[nr][nc] == 'B') {
                cout << "YES" << endl;
                cout << d + 1 << endl;
                cout << path + sym << endl;
                return;
            }

            q.push({ nr, nc, d + 1, path + sym });
            map[nr][nc] = '#'; // Mark visited IMMEDIATELY
        }
    }
    cout << "NO" << endl;
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
