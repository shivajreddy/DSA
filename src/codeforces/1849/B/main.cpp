// B. Monsters
// https://codeforces.com/problemset/problem/1849/B

#include <bits/stdc++.h>
#include <queue>
using namespace std;

// shorter type names
typedef long long ll;
typedef vector<int> vi;
typedef pair<int, int> pii;

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
    while (tc--) solve();
}

void solve() {
    int n, k;
    cin >> n >> k;

    vi a(n);
    loop(i, 0, n) {
        int num;
        cin >> num;
        num = num % k == 0 ? k : num % k;
        a[i] = num;
    }

    // custom comparator
    auto cmp = [](const pii& a, const pii& b) {
        if (a.first != b.first) return a.first < b.first;
        return a.second > b.second;
    };

    priority_queue<pii, vector<pii>, decltype(cmp)> minheap(cmp);
    loop(i, 0, n) minheap.push({ a[i], i });

    vi res;
    while (!minheap.empty()) {
        auto heaviest_monster = minheap.top();
        minheap.pop();

        res.push_back(heaviest_monster.second + 1);
    }

    loop(i, 0, res.size()) cout << res[i] << " ";
    cout << endl;
}
