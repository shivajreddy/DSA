// https://codeforces.com/problemset/problem/231/A

#include <iostream>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

int main() {
    setupIO();

    int t;
    cin >> t;

    int res = 0;
    for (int i = 0; i < t; i++) {
        int a, b, c;
        cin >> a >> b >> c;
        if (a + b + c >= 2) {
            res++;
        }
    }
    cout << res << "\n";
}
