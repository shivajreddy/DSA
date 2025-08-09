// B. 01 Game
// https://codeforces.com/problemset/problem/1373/B

// { Imports, TypeNames, Macros
#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)
// }

void solve2() {
    string s;
    cin >> s;

    int n = s.size();

    int plays = 0;
    while (true) {

        // check if all are explored
        bool all_dots = true;
        loop(i, 0, n) {
            if (s[i] != '.') {
                all_dots = false;
                break;
            }
        }
        if (all_dots) break;

        int first = -1, second = -1;
        loop(i, 0, n) {
            if (s[i] == '.') continue;
            first = i;
            break;
        }
        loop(i, first + 1, n) {
            if (s[i] == '.') continue;
            if (s[first] != s[i]) {
                second = i;
                break;
            }
        }
        // couldn't find a match for the first index
        if (first == -1 || second == -1) {
            s[first] = '.';
        } else if (first != -1 && second != -1) {
            plays += 1;
            s[first] = '.';
            s[second] = '.';
        }
    }

    plays % 2 == 1 ? cout << "DA\n" : cout << "NET\n";
}

void solve() {
    string s;
    cin >> s;

    int n = s.size();

    int count_zeros = 0, count_ones = 0;
    loop(i, 0, n) {
        if (s[i] == '0')
            count_zeros++;
        else
            count_ones++;
    }
    int plays = min(count_zeros, count_ones);
    plays % 2 == 1 ? cout << "DA\n" : cout << "NET\n";
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
