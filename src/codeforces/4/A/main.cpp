// https://codeforces.com/problemset/problem/4/A
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

    int weight;
    cin >> weight;

    if (weight > 2 && weight % 2 == 0) {
        cout << "YES\n";
    } else {
        cout << "NO\n";
    }
}
