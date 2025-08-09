// D. Deletive Editing
// https://codeforces.com/problemset/problem/1666/D

#include <bits/stdc++.h>
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
    string s, t;
    cin >> s >> t;

    vi freq_t(26, 0);
    for (char c : t) freq_t[c - 'A']++;

    for (int i = s.size() - 1; i >= 0; i--) {
        char c = s[i];
        if (freq_t[c - 'A'] > 0)
            freq_t[c - 'A']--;
        else
            s[i] = '.';
    }

    string final_string = "";
    loop(i, 0, s.size()) if (s[i] != '.') final_string += s[i];
    final_string == t ? cout << "YES\n" : cout << "NO\n";
}

// 5:09 - 6:43
// my solution
void solve2() {
    string s, t;
    cin >> s >> t;

    unordered_map<char, vi> hm;
    loop(i, 0, s.size()) hm[s[i]].push_back(i);

    unordered_map<char, int> t_map;
    loop(i, 0, t.size()) t_map[t[i]] += 1;

    for (auto [c, count] : t_map) {
        vi& a = hm[c];
        if (a.size() < count) {
            cout << "NO\n";
            return;
        }
        a.erase(a.begin(), a.begin() + a.size() - count);
    }
    // for (auto [k, v] : hm) cout << k << ":" << v << endl;

    int prev_idx = -1;
    loop(i, 0, t.size()) {
        char c = t[i];

        vi& a = hm[c];
        int idx = a[0];
        a.erase(a.begin());

        if (idx < prev_idx) {
            cout << "NO\n";
            return;
        }
        prev_idx = idx;
    }
    cout << "YES\n";
}
