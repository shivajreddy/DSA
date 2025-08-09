// https://codeforces.com/problemset/problem/339/A

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

void solve(const string& s) {
    int count1 = 0, count2 = 0, count3 = 0;

    for (int i = 0; i < s.size(); i++) {
        char c = s[i];
        if (c == '+')
            continue;
        else if (c == '1')
            count1 += 1;
        else if (c == '2')
            count2 += 1;
        else if (c == '3')
            count3 += 1;
    }

    string res = "";
    while (count1--) {
        res += "1+";
    }
    while (count2--) {
        res += "2+";
    }
    while (count3--) {
        res += "3+";
    }

    res.pop_back();
    cout << res << "\n";
}

int main() {
    setupIO();

    string s;
    cin >> s;
    solve(s);
}
