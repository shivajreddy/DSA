// B. Set of Strangers
// https://codeforces.com/problemset/problem/2069/B

#include <bits/stdc++.h>
#include <numeric>
#include <unordered_map>
#include <vector>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

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
    int n, m;
    cin >> n >> m;

    vector<vector<int>> mat(n, vector<int>(m)); // 2d matarix
    loop(i, 0, n) loop(j, 0, m) cin >> mat[i][j];

    vector<int> has_color(n * m, 0); // holds what at nums are encountered
    vector<int> has_bad(n * m, 0);

    loop(i, 0, n) loop(j, 0, m) {
        int num = mat[i][j];
        has_color[num - 1] = 1;
        // check if right & down cells have same color, if so mark as bad
        if (i + 1 < n && num == mat[i + 1][j]) has_bad[num - 1] = 1;
        if (j + 1 < m && num == mat[i][j + 1]) has_bad[num - 1] = 1;
    }
    int sum_has_color = accumulate(has_color.begin(), has_color.end(), 0);
    int sum_has_bad = accumulate(has_bad.begin(), has_bad.end(), 0);
    int max_has_bad = *max_element(has_bad.begin(), has_bad.end());
    cout << sum_has_color + sum_has_bad - 1 - max_has_bad << endl;
}

void solve2() {
    int n, m;
    cin >> n >> m;

    vector<vector<int>> mat(n, vector<int>(m)); // 2d matarix
    loop(i, 0, n) loop(j, 0, m) cin >> mat[i][j];

    int a = 0, b = 0;

    // traverse half1
    unordered_map<int, int> half1_map;
    int half1_max_freq = 0;
    int half1_max_freq_num = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i % 2 == 0 && j % 2 == 1) continue;
            if (i % 2 == 1 && j % 2 == 0) continue;
            int num = mat[i][j];
            half1_map[num] += 1;
            if (half1_map[num] > half1_max_freq) {
                half1_max_freq = half1_map[num];
                half1_max_freq_num = num;
            }
        }
    }
    int min_turns_for_half1 = (n * m / 2) - half1_max_freq;

    // traverse half1
    unordered_map<int, int> half2_map;
    int half2_max_freq = 0;
    int half2_max_freq_num = 0;
    for (int i = 0; i < n; i++) {
        for (int j = 0; j < m; j++) {
            if (i % 2 == 0 && j % 2 == 0) continue;
            if (i % 2 == 1 && j % 2 == 1) continue;
            int num = mat[i][j];
            half2_map[num] += 1;
            if (half2_map[num] > half2_max_freq) {
                half2_max_freq = half2_map[num];
                half2_max_freq_num = num;
            }
        }
    }
    int min_turns_for_half2 = (n * m / 2) - half2_max_freq;

    cout << "half1_max_freq_num:" << half1_max_freq_num << endl;
    cout << "half1_max_freq    :" << half1_max_freq << endl;
    cout << "half2_max_freq_num:" << half2_max_freq_num << endl;
    cout << "half2_max_freq    :" << half2_max_freq << endl;

    if (half1_max_freq_num == half2_max_freq_num) {
        cout << min_turns_for_half1 + min_turns_for_half2 << endl;
    } else {
        cout << min_turns_for_half1 + min_turns_for_half2 + 1 << endl;
    }
}
