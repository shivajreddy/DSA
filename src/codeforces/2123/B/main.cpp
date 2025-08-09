// https://codeforces.com/contest/2123/problem/B

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

    int tc;
    cin >> tc;

    while (tc--) {
        int n, j, k;
        cin >> n >> j >> k;

        int num;
        int target;
        int max_num = -1;
        for (int i = 0; i < n; i++) {
            cin >> num;
            if (i == j - 1) target = num;
            max_num = max(max_num, num);
        }

        if (k > 1 || max_num == target) {
            cout << "YES\n";
        } else {
            cout << "NO\n";
        }
    }

    return 0;
}
