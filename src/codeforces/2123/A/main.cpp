// https://codeforces.com/contest/2123/problem/A

#include <iostream>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

#define a "Alice\n"
#define b "Bob\n"

void solution(int n) {
    if (n < 3) {
        cout << a;
    } else if (n % 4 == 0) {
        cout << b;
    } else {
        cout << a;
    }
}

int main() {
    setupIO();

    int t;
    cin >> t;

    int n;
    for (int i = 0; i < t; i++) {
        cin >> n;

        solution(n);
    }
}
