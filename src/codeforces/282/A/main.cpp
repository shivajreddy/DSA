// https://codeforces.com/problemset/problem/282/A

#include <iostream>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

// is there + or - in the statement
int checkStatement(const string& statement) {
    for (char c : statement) {
        if (c == '+') {
            return 1;
            break;
        } else if (c == '-') {
            return -1;
            break;
        }
    }

    return 0;
}

int main() {
    setupIO();

    int t;
    cin >> t;

    int res = 0;
    for (int i = 0; i < t; i++) {
        string statement;
        cin >> statement;
        res += checkStatement(statement);
    }

    cout << res << "\n";
}
