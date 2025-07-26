// https://leetcode.com/problems/climbing-stairs

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int climbStairs(int n) {
        if (n < 3) return n;

        int a = 1, b = 2, num;
        for (int i = 3; i <= n; i++) {
            num = a + b;
            a = b;
            b = num;
        }
        return num;
    }
};

int main() {
    Solution* s = new Solution();
    cout << s->climbStairs(1) << endl;
    cout << s->climbStairs(2) << endl;
    cout << s->climbStairs(3) << endl;
    delete s;
}

/*
    jump: 1 or 2
   n=2 __

   1 2  _
   a[i] = a[i-1] + a[i-2]
*/
