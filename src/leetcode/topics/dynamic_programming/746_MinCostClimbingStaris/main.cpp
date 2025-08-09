// https://leetcode.com/problems/min-cost-climbing-stairs

#include <bits/stdc++.h>
using namespace std;

class Solution {
public:
    int minCostClimbingStairs(vector<int>& cost) {
        int n = cost.size();
        if (n == 1) return cost[0];
        if (n == 2) return min(cost[0], cost[1]);

        int res = 0;
        for (int i = 2; i < n; i++) {
            int res = min(cost[i - 1], cost[i - 2]);
            cost[i] += res;
        }
        return min(cost[n - 1], cost[n - 2]);
    }
};

/*

 after paying cost: 1 or 2

 [c1, c2, c3 ..... ]
 min(step 3) = min(c1, c2)
 min(i) = min(cost[i-1], cost[i-2])

*/

int main() {
    Solution* s = new Solution();
    vector<int> cost;

    cost = { 10, 15, 20 };
    cout << s->minCostClimbingStairs(cost) << endl;

    cost = { 1, 100, 1, 1, 1, 100, 1, 1, 100, 1 };
    cout << s->minCostClimbingStairs(cost) << endl;

    delete s;
}
