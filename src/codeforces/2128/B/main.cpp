// B. Deque Process
// https://codeforces.com/contest/2128/problem/B

// { Imports, TypeNames, Macros
#include <bits/stdc++.h>
#include <climits>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
// }

void solve() {
    int n;
    cin >> n;

    vi nums(n);
    loop(i, 0, n) cin >> nums[i];

    vi final_nums(n);
    int i = 0;

    string res = "";
    int prev_num = INT_MIN;
    char prev_op = '<';
    int l = 0, r = n - 1;
    while (res.size() != n) {
        if (prev_op == '<') {
            // try for '>'
            if (prev_num > nums[l]) {
                final_nums[i] = nums[l];
                i++;
                res += "L";
                prev_num = nums[l];
                prev_op = '>';
                l++;
            } else {
                final_nums[i] = nums[r];
                i++;
                res += "R";
                prev_num = nums[r];
                prev_op = '<';
                r--;
            }
        } else {
            // try for '<'
            if (prev_num < nums[l]) {
                final_nums[i] = nums[r];
                i++;
                res += "R";
                prev_num = nums[r];
                prev_op = '<';
                r--;
            } else {
                final_nums[i] = nums[l];
                i++;
                res += "L";
                prev_num = nums[l];
                prev_op = '>';
                l++;
            }
        }
    }

    loop(i, 0, n) cout << final_nums[i] << " ";
    cout << endl;

    cout << res << endl;
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif

    int tc;
    cin >> tc;
    while (tc--) solve();
}
