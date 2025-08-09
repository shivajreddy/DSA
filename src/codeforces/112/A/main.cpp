// https://codeforces.com/problemset/problem/112/A

#include <cctype> // for tolower
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

void solve(const string& a, const string& b) {
    int res = 0;

    int n = a.size();
    for (int i = 0; i < n; i++) {
        int a_ord = tolower(a[i]) - 'a';
        int b_ord = tolower(b[i]) - 'a';
        if (a_ord == b_ord) continue; // same letter, continue
        if (a_ord < b_ord) {
            res = -1;
            break;
        } else {
            res = 1;
            break;
        }
    }

    cout << res << "\n";
}

int main() {
    setupIO();

    string a, b;
    cin >> a >> b;

    solve(a, b);
}
