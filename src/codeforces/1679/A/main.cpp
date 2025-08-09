// A. AvtoBus
// https://codeforces.com/problemset/problem/1679/A

#include <bits/stdc++.h>
using namespace std;

#define ll long long

void setupIO() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
#ifndef ONLINE_JUDGE
    freopen("input.txt", "r", stdin);
#endif
}
/*
x4+y6 = n

OBSERVATIONS:

x: min=0 max=n/4
y: min=0 max=n/6


while n > 0 :
    if n % 6 == 0:
        count6++
        n /= 6
    else:
        rem++
        n--
if rem % 4 != 0:

for min number of busses:
                all are 6,
                then mix with mostly 6 and other 4,
                then no 6 only 4
for max number of buses:
                all are 4
                mix of 4 and 6 - mostly 4
                no 4 all 6

*/
/*
 * Let the number of buses with two axles is x
 and the number of buses with three axles is y. Then the equality 4x+6y=n must
be true. If n is odd, there is no answer, because the left part of the equality
is always even. Now we can divide each part of the equality by two: 2x+3y=n2
.
Let's maximize the number of buses. Then we should make x
 as large as possible. So, we will get 2+…+2+2=n2 if n2 is even, and 2+…+2+3=n2
otherwise. In both cases the number of buses is ⌊n2⌋
.
Now let's minimize the number of buses. So, we should make y
 as large is possible. We will get 3+…+3+3+3=n2 if n2 is divisible by 3,
3+…+3+3+2=n2 if n≡2(mod3), and 3+…+3+2+2=n2 if n≡1(mod3). In all cases the
number of buses is ⌈n3⌉
.
Also don't forget the case n=2
 — each bus has at least four wheels, so in this case there is no answer.
Time complexity: O(1)
 */

// 1:49 -> 2:59 , still dont understand this fucking problem.
// NOTE: very useless problem to spend time on.
void solve() {
    ll n;
    cin >> n;

    // If n is odd or n < 4, no solution possible
    if (n % 2 == 1 || n < 4) {
        cout << "-1\n";
    } else {
        ll mx = n / 4;
        ll mn = (n % 6 == 0) ? n / 6 : n / 6 + 1;
        cout << mn << " " << mx << "\n";
    }
}

void solve2() {
    ll n;
    cin >> n;

    if (n % 2 == 1 || n < 4) {
        cout << "-1\n";
        return;
    }

    // /* BRUTE FORCE
    ll mn = -1, mx = -1;

    ll curr6, curr4;
    // Minmize the buses
    curr6 = n, curr4 = 0;
    // cout << "START: curr6:" << curr6 << " curr4:" << curr4 << endl;
    // cout << "curr6%6=" << curr6 % 6 << " curr4%4=" << curr4 % 4 << endl;
    while (curr6 >= 0 && curr4 >= 0 && (curr6 % 6 != 0 || curr4 % 4 != 0)) {
        curr6 -= 1;
        curr4 += 1;
        // cout << " NOW:: curr6:" << curr6 << " curr4:" << curr4 << endl;
    }
    // cout << "FINISH: curr6:" << curr6 << " curr4:" << curr4 << endl;
    if (curr6 % 6 == 0 && curr4 % 4 == 0) {
        mn = curr6 / 6 + curr4 / 4;
    }

    // Maximise the buses
    curr6 = 0, curr4 = n;
    while (curr6 >= 0 && curr4 >= 0 && (curr6 % 6 != 0 || curr4 % 4 != 0)) {
        curr6++;
        curr4--;
    }
    if (curr6 % 6 == 0 && curr4 % 4 == 0) {
        mx = curr6 / 6 + curr4 / 4;
    }

    // cout << "mn:" << mn << " mx:" << mx << endl;

    // Couldnt form x6+y4=n
    if (mn == -1 && mx == -1) {
        cout << "-1\n";
    } else if (mn != -1 && mx == -1) {
        cout << mn << " " << mn << endl;
    } else if (mx != -1 && mn == -1) {
        cout << mx << " " << mx << endl;
    } else {
        cout << mn << " " << mx << endl;
    }
    // */
}

int main() {
    setupIO();

    int tc;
    cin >> tc;
    while (tc--) solve();
}
