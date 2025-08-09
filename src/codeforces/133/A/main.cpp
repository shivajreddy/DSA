// https://codeforces.com/problemset/problem/133/A

#include <iostream>
#include <string>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

#include <unordered_set>

void solve(const string s) {
    // instructions that produce an output
    unordered_set<char> set = { 'H', 'Q', '9' };
    for (char ch : s) {
        if (set.count(ch)) {
            cout << "YES\n";
            return;
        }
    }
    cout << "NO\n";
}

int main() {
    setupIO();
    string s;
    cin >> s;
    solve(s);
}
