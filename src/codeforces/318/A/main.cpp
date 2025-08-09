// https://codeforces.com/problemset/problem/318/A

#include <iostream>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

void solve(long long n, long long k) {
    long long res = -1;

    if (n % 2 == 0) {
        // cout << "even\n";

        if (k <= n / 2) {
            // cout << "K is in LEFT\n";
            // series is 1,3,5,7,9.....
            res = 2 * k - 1;
        } else {
            // cout << "K is in RIGHT\n";
            k = k - n / 2;
            // series is 2,4,6,8,10....
            res = 2 * k;
        }

    } else {
        // cout << "odd\n";

        if (k <= n / 2 + 1) {
            // cout << "K is in LEFT\n";
            // series is 1,3,5,7,9.....
            res = 2 * k - 1;
        } else {
            // cout << "K is in RIGHT\n";
            k = k - (n / 2 + 1);
            // series is 2,4,6,8,10....
            res = 2 * k;
        }
    }
    cout << res << "\n";
}

int main() {
    setupIO();

    long long n, k;
    cin >> n >> k;

    solve(n, k);
}
