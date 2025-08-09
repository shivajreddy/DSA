// https://codeforces.com/contest/2123/problem/C

#include <algorithm>
#include <iostream>
#include <string>
#include <vector>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

void solve(const vector<int>& v);

int main() {
    setupIO();

    int tc;
    cin >> tc;

    for (int i = 0; i < tc; i++) {
        // while (tc--) {
        int n;
        cin >> n;
        vector<int> v(n);
        for (int i = 0; i < n; i++)
            cin >> v[i];

        if (i == 666) {
            cout << "case num: 666: ";
            for (int x : v)
                cout << x;
            cout << endl;
        } else {
            solve(v);
        }
    }

    return 0;
}

bool all_same_to_last(const vector<int>& v, int idx) {
    int target = v[idx];
    for (int i = idx; i < v.size(); i++) {
        if (v[i] != target) return false;
    }
    return true;
}

bool all_same_from_start(const vector<int>& v, int idx) {
    int target = v[idx];
    for (int i = 0; i < idx; i++) {
        if (v[i] != target) return false;
    }
    return true;
}

void solve(const vector<int>& v) {
    string res = "";

    int min_idx = min_element(v.begin(), v.end()) - v.begin();
    int max_idx = max_element(v.begin(), v.end()) - v.begin();

    for (int idx = 0; idx < v.size(); idx++) {
        // cout << "TESTING idx: " << idx << endl;
        // current num is either min or max
        if (idx == min_idx || idx == max_idx) res += '1';
        // min (curr) max
        else if (min_idx < idx && idx < max_idx)
            res += '0';
        // max (curr) min
        else if (max_idx < idx && idx < min_idx) {
            if (max_idx == 0 || min_idx == v.size() - 1)
                res += '1';
            else
                res += '1';
        }
        // current item has min&max on one side
        else {
            if (all_same_to_last(v, idx))
                res += '1';
            else if (all_same_from_start(v, idx))
                res += '1';
            else
                res += '0';
        }
        // cout << "res:" << res << endl;
    }

    cout << res << "\n";
}
