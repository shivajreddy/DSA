// https://codeforces.com/problemset/problem/

#include <bits/stdc++.h>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

// O(n)
bool is_derangement(vector<int>& v) {
    int n = v.size();
    vector<int> sv = v;
    sort(sv.begin(), sv.end());

    for (int i = 0; i < n; i++) {
        if (v[i] == sv[i]) {
            return false;
        }
    }
    return true;
}

void solve() {
    int n;
    cin >> n;

    vector<int> v(n);
    for (int i = 0; i < n; i++)
        cin >> v[i];

    if (n == 1) {
        cout << "NO\n";
        return;
    }

    if (is_derangement(v)) {
        cout << "YES\n";
        cout << n << "\n";
        for (int i = 0; i < n; i++) {
            cout << v[i] << " ";
        }
        cout << "\n";
        return;
    }

    // can delete 1 element
    // T: n^2, delete every element and check
    for (int i = 0; i < n; i++) {
        vector<int> new_array; // skip i'th num
        for (int j = 0; j < n; j++) {
            if (i == j) continue;
            new_array.push_back(v[j]);
        }
        if (is_derangement(new_array)) {
            cout << "YES\n";
            cout << new_array.size() << "\n";
            for (int i = 0; i < new_array.size(); i++) {
                cout << new_array[i] << " ";
            }
            cout << "\n";
            return;
        }
    }
    cout << "NO\n";
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}
