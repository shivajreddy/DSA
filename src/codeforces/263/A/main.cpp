// https://codeforces.com/problemset/problem/263/A

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

    int r, c;
    int num = 0;
    for (int i = 0; i < 5; i++) {
        if (num == 1) break;
        for (int j = 0; j < 5; j++) {
            cin >> num;
            if (num == 1) {
                r = i;
                c = j;
                break;
            }
        }
    }
    // cout << r << "," << c << endl;

    int res = abs(2 - r) + abs(2 - c);
    cout << res << "\n";
}
