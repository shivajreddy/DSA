// https://codeforces.com/problemset/problem/160/A

#include <algorithm>
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

void solve(vector<int>& v) {
    // sort in descending order
    sort(v.begin(), v.end(), greater<int>());
    int total_sum = 0;
    for (int coin : v)
        total_sum += coin;

    int steal = 0;
    int res = -1;
    for (int i = 0; i < v.size(); i++) {
        int coin = v[i];
        steal += coin;
        total_sum -= coin;
        if (steal > total_sum) {
            res = i + 1;
            break;
        }
    }
    cout << res << "\n";
}

int main() {
    setupIO();

    int n;
    cin >> n;

    vector<int> v;
    int coin;
    for (int i = 0; i < n; i++) {
        cin >> coin;
        v.push_back(coin);
    }
    solve(v);
}
