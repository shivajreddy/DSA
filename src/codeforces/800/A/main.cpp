// A. Elections
// https://codeforces.com/problemset/problem/1043/A

#include <bits/stdc++.h>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;

// Macros
#define PB push_back
#define loop(i, a, b) for (int i = a; i < b; i++)

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}

int main() {
    setupIO();

    int n;
    cin >> n;
    vi v(n);
    loop(i, 0, n) cin >> v[i];

    int e_votes = accumulate(v.begin(), v.end(), 0);

    int largest_num = *max_element(v.begin(), v.end());
    double min_k = (double)(e_votes * 2) / n;
    // if min_k = 2.1, we need atleast 3, for a_votse > e_votes
    // if min_k = 2, we need atleast 3, for a_votes > e_votes
    // k cant be smaller than the largest number, because there are only k
    // votes for each person, at max they can cast all votes to e. i.e., k-ai=0
    if (floor(min_k) == min_k) {
        cout << max(largest_num, (int)ceil(min_k) + 1) << endl;
    } else {
        cout << max(largest_num, (int)ceil(min_k)) << endl;
    }

    /* O(1)
    e_votes *= 2;
    e_votes += n;
    e_votes /= n;
    cout << max(e_votes, k) << endl;
    */

    /* time: O(n*m)
    while (true) {
        ll a_votes = 0;
        for (int num : v)
            a_votes += (k - num);
        if (a_votes > e_votes) break;
        k++;
    }
    cout << k << endl;
    */
}
