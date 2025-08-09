// B. Erase First or Second Letter
// https://codeforces.com/problemset/problem/1917/B

#include <bits/stdc++.h>
using namespace std;
typedef long long ll;

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
    while (tc--)
        solve();
}

void solve() {
    int n;
    cin >> n;
    string s;
    cin >> s;

    unordered_map<char, int> freq_map;
    int count_dist_chars = 0;
    vector<int> distinct(n, 0);

    for (int i = 0; i < n; i++) {
        freq_map[s[i]]++;
        if (freq_map[s[i]] == 1) count_dist_chars++; // new char found
        distinct[i] = count_dist_chars;
    }

    ll ans = 0;
    for (int num : distinct)
        ans += num;
    cout << ans << endl;
}

/*
s = a

s = ab
    ab
   b  a

   __ = 1+2

s = abc
     abc
   bc   ac
  c b  _ a

  ___ = 1+2+3

s = abb

    abb
   bb  ab
   b   a
   ___ = 1+2+2

 */
