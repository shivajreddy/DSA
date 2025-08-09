// https://codeforces.com/problemset/problem/96/A

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

// find the length of the max continuous sequence
void solve(const string& s) {
    int count = 1; // NOTE: sequence length is atelast 1
    char prev = s[0];

    for (int i = 1; i < s.length(); i++) {
        char curr = s[i];
        if (curr == prev) {
            count += 1;
            if (count == 7) {
                cout << "YES\n";
                return;
            }
        } else {
            count = 1; // reset sequence length, which is the current char
        }
        prev = curr; // update prev
    }

    cout << "NO\n";
}

int main() {
    setupIO();

    string s;
    cin >> s;
    solve(s);
}
