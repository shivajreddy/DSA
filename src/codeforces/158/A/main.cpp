// https://codeforces.com/problemset/problem/158/A

#include <iostream>
using namespace std;

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);

#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif // !ONLINE_JUDGE
}

int main() {
    setupIO();

    int n, k;
    cin >> n >> k;

    int res = 0;
    int cutoff, score;
    for (int i = 0; i < n; i++) {
        cin >> score;
        if (score == 0) break; // all scores after here are 0

        if (i <= k - 1) {
            res++;
            cutoff = score; // update cutoff
        } else {
            if (score < cutoff) break; // scores from here are < cutoff
            res++;
        }
    }

    cout << res << "\n";
}
