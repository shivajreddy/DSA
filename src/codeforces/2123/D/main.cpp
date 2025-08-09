// https://codeforces.com/contest/2123/problem/D

#include <iostream>
#include <vector>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
    #ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
    #endif // !ONLINE_JUDGE
}

void solve() {
    int n, k;
    cin >> n >> k;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    // play game
    while (true) {
        // alice picks best sequnce

        // bob picks best substring

        // Check if any player won
        int sum = 0;
        for (int num : v)
            sum += num;
        if (sum == 0) {
            cout << "Alice\n";
            return;
        } else {
            cout << "Bob\n";
            return;
        }
    }
}

int main() {
    setupIO();

    int tc;
    cin >> tc;

    while (tc--)
        solve();
}
