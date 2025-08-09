// https://codeforces.com/problemset/problem/50/A

#include <iostream>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

int solution(int m, int n) {
    // edge case
    if (m == 1 && n == 1) return 0;

    // even row/col  (will be fully packed, by aligning 1x2 on the even line)
    if (m % 2 == 0 || n % 2 == 0) {
        if (m % 2 == 0) return (m / 2) * n;
        return (n / 2) * m;
    }

    // odd & odd
    int even_part = ((m - 1) / 2) * (n - 1);
    return even_part + m / 2 + n / 2;
}

int main() {
    setupIO();

    int m, n;
    cin >> m >> n;

    cout << solution(m, n) << "\n";
}
