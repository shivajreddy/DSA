// B. Make it Divisible by 25
// https://codeforces.com/problemset/problem/1593/B

// { Imports & Shorthands
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
    string s;
    cin >> s;

    vector<string> seqs = { "25", "50", "75", "00" };
    const int INF = 19; // latgest number is 10^18 so 18 digits

    // Finds the right most occurrence of the given sequence
    // and returns the min number of digits to remove
    auto min_removal = [&](const string& seq) -> int {
        int count = 0; // count of the digits to remove
        int idx = s.size() - 1;
        while (idx >= 0 && s[idx] != seq[1]) {
            count++;
            idx--;
        }

        if (idx < 0) return INF; // couldn't find 2nd digit of sequence
        idx--;                   // found the second digit,

        while (idx >= 0 && s[idx] != seq[0]) {
            count++;
            idx--;
        }
        if (idx < 0) return INF; // couldn't find 1st digit of sequence
        return count;
    };

    // Calculate min removals for each sequence, and return the smallest
    int res = INF;
    for (const string& seq : seqs) res = min(res, min_removal(seq));

    cout << res << endl;
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
