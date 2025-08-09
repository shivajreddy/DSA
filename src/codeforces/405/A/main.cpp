// https://codeforces.com/problemset/problem/405/A

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

void printv(vector<int> v) {
    for (int num : v)
        cout << num << " ";
}

void solve(vector<int>& v, int n, int m) {
    printv(v);
    cout << endl << n << " " << m << "\n";

    int total_sum = 0;
    for (int num : v)
        total_sum += num;

    for (int r = 0; r < m; r++) {
        int row_sum = 0;
        for (int c = 0; c < n; c++) {
            if (v[c] > 0) row_sum += 1;
            v[c] = v[c] - 1;
            if (v[c] < 0) v[c] = 0;
        }
        cout << "row: " << r << " row-sum: " << row_sum << "\n";
    }
}

int main() {
    setupIO();

    int n;
    cin >> n;

    vector<int> cols;
    int m = 0;

    int r;
    for (int c = 0; c < n; c++) {
        cin >> r;
        m = max(m, r);
        cols.push_back(r);
    }
    solve(cols, n, m);
}
