// https://codeforces.com/problemset/problem/1904/A

#include <bits/stdc++.h>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

void solve() {
    int a, b, xk, yk, xq, yq;
    cin >> a >> b >> xk >> yk >> xq >> yq;
    // cout << a << b << xk << yk << xq << yq << endl;

    // Hash function for pairs
    struct PairHash {
        size_t operator()(const pair<int, int>& p) const {
            return hash<int>()(p.first) ^ (hash<int>()(p.second) << 1);
        }
    };

    unordered_set<pair<int, int>, PairHash> king_coords;
    unordered_set<pair<int, int>, PairHash> queen_coords;

    pair<int, int> dirs[] = {
        { a, b }, { a, -b }, { -a, b }, { -a, -b },
        { b, a }, { b, -a }, { -b, a }, { -b, -a },
    };

    for (auto [x, y] : dirs)
        king_coords.insert({ xk + x, yk + y });
    for (auto [x, y] : dirs)
        queen_coords.insert({ xq + x, yq + y });

    int res = 0;
    for (pair<int, int> xy : king_coords)
        queen_coords.count(xy) > 0 ? res += 1 : res += 0;

    cout << res << "\n";

    /*
    set<pair<int, int>> king_coords;
    set<pair<int, int>> queen_coords;

    pair<int, int> dirs[] = {
        { a, b }, { a, -b }, { -a, b }, { -a, -b },
        { b, a }, { b, -a }, { -b, a }, { -b, -a },
    };

    for (auto [x, y] : dirs)
        king_coords.insert({ xk + x, yk + y });
    for (auto [x, y] : dirs)
        queen_coords.insert({ xq + x, yq + y });

    int res = 0;
    for (pair<int, int> xy : king_coords)
        queen_coords.count(xy) > 0 ? res += 1 : res += 0;

    cout << res << "\n";
    */
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
