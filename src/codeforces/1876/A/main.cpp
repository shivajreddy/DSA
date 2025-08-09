// A. Helmets in Night Light
// https://codeforces.com/problemset/problem/1876/A
#include <algorithm>
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

void solve();

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--)
        solve();
}

void solve() {
    int n, p;
    cin >> n >> p;
    vi a(n);
    loop(i, 0, n) cin >> a[i];
    vi b(n);
    loop(i, 0, n) cin >> b[i];

    vi indices(n);
    iota(indices.begin(), indices.end(), 0); // fill with 0,1,2,3..n-1
    // sort indices based on values in b
    sort(indices.begin(), indices.end(),
         [&](int i, int j) { return b[i] < b[j]; });

    // Apply the sorted order to 'a' and 'b'
    vector<int> a_sorted(n), b_sorted(n);
    loop(i, 0, n) {
        a_sorted[i] = a[indices[i]];
        b_sorted[i] = b[indices[i]];
    }
    a = std::move(a_sorted);
    b = std::move(b_sorted);

    long long cost = p; // Use long long to prevent overflow
    int count = 1;      // Number of people informed

    loop(i, 0, n) {
        if (b[i] >= p) break; // same/more cost as Pak Chanek
        int remaining = n - count;
        if (remaining <= 0) break; // everyone already informed

        int can_inform = min(a[i], remaining);
        cost += (long long)can_inform * b[i];
        count += can_inform;

        if (count >= n) break; // everyone now informed
    }

    // If residents left, Pak Chanek informs them directly
    if (count < n) {
        int remaining = n - count;
        cost += (long long)remaining * p;
    }

    cout << cost << endl;
}

void solve2() {
    int n, p;
    cin >> n >> p;
    vi a(n);
    loop(i, 0, n) cin >> a[i];

    vi b(n);
    loop(i, 0, n) cin >> b[i];

    vi indices(n);
    iota(indices.begin(), indices.end(), 0); // fill with 0,1,2,3..n-1

    // sort indices based on values in b
    sort(indices.begin(), indices.end(),
         [&](int i, int j) { return b[i] < b[j]; });

    // Appy the sorted order to 'a' and 'b'
    vector<int> a_sorted(n), b_sorted(n);
    loop(i, 0, n) {
        a_sorted[i] = a[indices[i]];
        b_sorted[i] = b[indices[i]];
    }

    a = std::move(a_sorted);
    b = std::move(b_sorted);

    int cost = p;
    int count = 1;
    loop(i, 0, n) {
        if (b[i] >= p) break; // same/more cost as pat
        int remaining = n - count;
        if (a[i] >= remaining) {
            cost += (remaining * b[i]);
            count += remaining;
            break;
        } else { // not enough use all
            cost += (a[i] * b[i]);
            count += a[i];
        }
    }
    if (count != n) { // residents left, and p is the lowest cost now
        int remaining = n - count;
        cost += (remaining * p);
    }
    cout << cost << endl;
}

/*
p=94
1   4  2  3
103 96 86 57

*/
