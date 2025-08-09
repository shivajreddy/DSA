// B. Swap and Delete
// https://codeforces.com/problemset/problem/1913/B

#include <bits/stdc++.h>
#include <unordered_map>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

void solve() {
    string s;
    cin >> s;

    unordered_map<char, int> hm = { { '0', 0 }, { '1', 0 } };
    for (char c : s)
        hm[c] += 1;

    int last_idx = -1;
    for (int i = 0; i < s.size(); i++) {
        char needed_char = s[i] == '0' ? '1' : '0';
        if (hm[needed_char] == 0) {
            last_idx = i;
            break;
        }
        hm[needed_char] -= 1;
    }

    if (last_idx == -1) {
        cout << "0\n";
    } else {
        cout << s.size() - last_idx << endl;
    }
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
